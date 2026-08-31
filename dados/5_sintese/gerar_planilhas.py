#!/usr/bin/env python3
"""Gera as planilhas de síntese da RSL a partir das fontes primárias.

Nada aqui é digitado de memória: cada planilha é uma reprojeção tabular de um
arquivo que já existe no repositório. As fontes são

  ../4_extracao/categorizacao_c3_c5.md   codificação C3, C4, C5, C-RQ1, C-RQ3, C-RQ5
  ../3_qualidade/pt1/incluidos.csv       notas QA1–QA8 por estudo (40 x 8 linhas)
  ../3_qualidade/pt2_pt3/resultado.csv   somas e status dos 40 avaliados
  ../4_extracao/referencias_28.bib       metadados bibliográficos dos 28
  ../4_extracao/status_rq_por_estudo.csv status por questão de pesquisa (campo 10)

e, para o funil e a base de recuperação de cada estudo, os números conciliados
em ../NOTAS_METODOLOGICAS.md (§1 e §2), que são a fonte canônica do repositório
e a mesma usada nas figuras do relatório.

Ao final o script confere os agregados contra os números publicados no artigo e
falha se algum divergir. Rodar sempre que a categorização mudar:

    python3 gerar_planilhas.py
"""
import csv
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
CATEG = RAIZ / "dados/4_extracao/categorizacao_c3_c5.md"
QA_ITENS = RAIZ / "dados/3_qualidade/pt1/incluidos.csv"
QA_SOMAS = RAIZ / "dados/3_qualidade/pt2_pt3/resultado.csv"
BIB = RAIZ / "dados/4_extracao/referencias_28.bib"
STATUS_RQ = RAIZ / "dados/4_extracao/status_rq_por_estudo.csv"

# Base de recuperação por estudo: NOTAS_METODOLOGICAS.md, §2 (15 IEEE, 13 ACM).
# E02 é co-publicado IEEE/ACM e foi recuperado via IEEE; E46 é publicado pela
# IEEE Press mas só consta do export da ACM. Ver a justificativa na §2.
BASE_IEEE = "E01 E02 E12 E25 E27 E29 E40 E51 E58 E63 E64 E70 E72 E75 E79".split()
BASE_ACM = "E09 E21 E23 E32 E36 E38 E43 E45 E46 E47 E57 E67 E74".split()

# Funil conciliado: NOTAS_METODOLOGICAS.md, §1 (mesma narrativa da Figura 1).
FUNIL = [
    ("Busca (v2, 08/05/2026)", "", 235, 0, 235,
     "163 na IEEE Xplore e 72 na ACM DL"),
    ("Remoção antes da triagem", "CE1, CE2", 235, 11, 224,
     "4 contêineres de anais (CE1) e 7 duplicatas (CE2)"),
    ("Triagem por título e resumo", "CE3, CI1, CE7, CE1, CE6", 224, 144, 80,
     "razão primária por registro; ver exclusoes_por_criterio.csv"),
    ("Elegibilidade em texto completo", "CE7, CE3, CE5, CE4, CE1, CE6, CI3", 80, 40, 40,
     "razão primária por registro; ver exclusoes_por_criterio.csv"),
    ("Avaliação de qualidade", "corte 6,5", 40, 8, 32,
     "nenhum estudo pontuou entre 6,0 e 6,5"),
    ("Extração (reaplicação dos critérios)", "CE7, CE4", 32, 4, 28,
     "3 short papers (CE7) e 1 fora de escopo (CE4), somas 7,0 a 7,5"),
]

# Razões de exclusão por fase, com as multi-marcações resolvidas pela razão
# primária de cada registro (NOTAS_METODOLOGICAS.md §1; é o que a Figura 2 publica).
EXCLUSOES = [
    ("Triagem por título e resumo", "CE3", 95),
    ("Triagem por título e resumo", "¬CI1", 26),
    ("Triagem por título e resumo", "CE7", 15),
    ("Triagem por título e resumo", "CE1", 4),
    ("Triagem por título e resumo", "CE6", 4),
    ("Elegibilidade em texto completo", "CE7", 17),
    ("Elegibilidade em texto completo", "CE3", 8),
    ("Elegibilidade em texto completo", "CE5", 5),
    ("Elegibilidade em texto completo", "CE4", 4),
    ("Elegibilidade em texto completo", "CE1", 3),
    ("Elegibilidade em texto completo", "CE6", 2),
    ("Elegibilidade em texto completo", "¬CI3", 1),
]

GRUPOS_RQ4 = {
    "A": "Modelo, framework ou processo de integração proposto",
    "B": "Técnica ou artefato específico proposto",
    "C": "Catálogo ou apoio à seleção de técnicas",
    "D": "Aplicação de abordagem existente, sem proposta nova",
}
GRAUS = {"EE": "Empírico", "RP": "Participantes", "SA": "Sem evidência"}
ABREV_ABORD = {"DT": "Design Thinking", "UCD": "UCD/HCD", "PD": "Participatory Design",
               "CoD": "Co-Design", "UX": "UX Design"}


# --------------------------------------------------------------------- leitura
def tabelas_markdown(texto):
    """Devolve toda tabela markdown do arquivo como lista de listas de células."""
    tabelas, atual = [], []
    for linha in texto.splitlines():
        if linha.lstrip().startswith("|"):
            celulas = [c.strip() for c in linha.strip().strip("|").split("|")]
            if not all(re.fullmatch(r":?-{2,}:?", c) for c in celulas):
                atual.append(celulas)
        elif atual:
            tabelas.append(atual)
            atual = []
    if atual:
        tabelas.append(atual)
    return tabelas


def tabela_com_cabecalho(tabelas, *inicio):
    """Escolhe a tabela cujo cabeçalho começa com as células dadas."""
    for t in tabelas:
        cab = [c.strip() for c in t[0]]
        if len(cab) >= len(inicio) and all(a == b for a, b in zip(cab, inicio)):
            return t
    raise SystemExit(f"tabela com cabeçalho {inicio} não encontrada em {CATEG}")


def limpa(c):
    """Remove ênfase markdown e as marcas de inferência († ‡)."""
    return re.sub(r"[*`†‡]", "", c).strip()


def marcado(c):
    return limpa(c).lower() == "x"


def ids_do_texto(s):
    return re.findall(r"\bE\d{2}\b", s)


texto = CATEG.read_text(encoding="utf-8")
tabelas = tabelas_markdown(texto)

# ------------------------------------------------------------------ mestra
mestra = tabela_com_cabecalho(tabelas, "ID", "Abordagens", "Atividades ER", "Tipo")
estudos = {}
for linha in mestra[1:]:
    eid = limpa(linha[0])
    if not re.fullmatch(r"E\d{2}", eid):
        continue
    brutas = [a.strip() for a in limpa(linha[2]).split(",") if a.strip()]
    # Recodificação de 2026-08-20: priorização é absorvida na análise (Aná = Aná ∪ Pri).
    cinco = [a for a in brutas if a != "Pri"]
    if "Pri" in brutas and "Aná" not in cinco:
        cinco.insert(1, "Aná")
    estudos[eid] = {
        "id": eid,
        "abordagens": ", ".join(ABREV_ABORD[a.strip()] for a in limpa(linha[1]).split(",")),
        "atividades_er_brutas": ", ".join(brutas),
        "atividades_er": ", ".join(cinco),
        "grupo_rq4": limpa(linha[3]),
        "proposta_central": limpa(linha[4]),
        "avaliacao_empirica": limpa(linha[5]),
        "dominio": limpa(linha[6]),
        "contexto": limpa(linha[7]),
    }
assert len(estudos) == 28, f"tabela mestra com {len(estudos)} estudos, esperados 28"

# ----------------------------------------------------- eixos da RQ1 e papéis
dim = tabela_com_cabecalho(tabelas, "ID", "(a) Temporal", "(b) Participação", "(c) Mediação")
for linha in dim[1:]:
    eid = limpa(linha[0])
    if eid in estudos:
        estudos[eid].update(temporal=limpa(linha[1]).replace("Não explic.", "Não explicitada"),
                            participacao=limpa(linha[2]).replace("Não explic.", "Não explicitada"),
                            mediacao=limpa(linha[3]))

crq1 = tabela_com_cabecalho(tabelas, "ID", "Seq", "Ite", "Col", "Art")
for linha in crq1[1:]:
    eid = limpa(linha[0])
    if eid in estudos:
        estudos[eid].update(
            seq=int(marcado(linha[1])), ite=int(marcado(linha[2])),
            col=int(marcado(linha[3])), art=int(marcado(linha[4])),
            trecho_campo5=limpa(linha[5]))

crq3 = tabela_com_cabecalho(tabelas, "ID", "Dst", "Est", "Org", "Dis")
PAPEIS = {"dst": "Destinatária", "est": "Estruturadora",
          "org": "Organizadora", "dis": "Prática coletiva distribuída"}
for linha in crq3[1:]:
    eid = limpa(linha[0])
    if eid in estudos:
        marcas = {k: int(marcado(linha[i])) for i, k in enumerate(PAPEIS, start=1)}
        estudos[eid].update(marcas)
        estudos[eid]["papeis"] = ", ".join(v for k, v in PAPEIS.items() if marcas[k]) or "—"
        estudos[eid]["trecho_campo10"] = limpa(linha[5])

# ------------------------------------------------------------ lacunas (RQ5)
temas_l = tabela_com_cabecalho(tabelas, "Tema", "Descrição", "n", "Estudos")
lacunas_temas = [(limpa(l[0]), limpa(l[1]), int(limpa(l[2])), ids_do_texto(l[3]))
                 for l in temas_l[1:] if limpa(l[0]).startswith("L")]
lac_por_estudo = tabela_com_cabecalho(tabelas, "ID", "Temas", "Trecho do campo 9")
for linha in lac_por_estudo[1:]:
    eid = limpa(linha[0])
    if eid in estudos:
        estudos[eid]["lacunas"] = " ".join(re.findall(r"\bL\d\b", linha[1])) or "—"
        estudos[eid]["trecho_campo9"] = limpa(linha[2])

# ------------------------------------------------- benefícios e limitações
benef = tabela_com_cabecalho(tabelas, "Tema", "EE", "RP", "SA")
beneficios = [(limpa(l[0]), eid, GRAUS[sigla])
              for l in benef[1:]
              for sigla, col in zip(("EE", "RP", "SA"), l[1:4])
              for eid in ids_do_texto(col)]

lim = tabela_com_cabecalho(tabelas, "Tema", "Estudos")
limitacoes = [(limpa(l[0]), eid) for l in lim[1:] for eid in ids_do_texto(l[1])]

# ------------------------------------------------- abordagens x atividades
c3 = tabela_com_cabecalho(tabelas, "Abordagem", "Estudos", "n", "Eli")
abordagens = [[limpa(c) for c in l] for l in c3[1:]]

# ------------------------------------------- caracterização (grupos e veículo)
def mapa_de_bullet(rotulo):
    bloco = re.search(rf"\*\*{rotulo}:?\*\*(.+?)(?=\n- \*\*|\Z)", texto, re.S).group(1)
    mapa = {}
    for grupo, ids in re.findall(r"([^;:]+?)\s*\d+\s*\(([^)]*)\)", bloco):
        nome = re.sub(r"\s+", " ", grupo).strip().lstrip(";").strip()
        for eid in ids_do_texto(ids):
            mapa[eid] = nome
    return mapa

dominio_g = mapa_de_bullet("Domínio de aplicação")
contexto_g = mapa_de_bullet("Contexto de condução")
veiculo_g = mapa_de_bullet("Veículo")
for eid, e in estudos.items():
    e["dominio_agrupado"] = dominio_g.get(eid, "")
    e["contexto_agrupado"] = contexto_g.get(eid, "")
    # "conferência 21 (demais)": o bullet lista só periódicos e workshops.
    e["tipo_veiculo"] = veiculo_g.get(eid, "conferência")
    e["base"] = "IEEE Xplore" if eid in BASE_IEEE else "ACM DL"

# --------------------------------------------------------------- qualidade
qa_por_estudo = {}
for r in csv.DictReader(QA_ITENS.open(encoding="utf-8")):
    # A planilha original rotula as oito questões ora "AQ1..AQ8" (36 estudos),
    # ora "QA1..QA8" (4 estudos, os primeiros extraídos). São as mesmas questões,
    # com a mesma descrição; o relatório padronizou QA1–QA8.
    questao = re.sub(r"^AQ", "QA", r["Questao"].strip())
    qa_por_estudo.setdefault(r["ID_estudo"], {})[questao] = r["Pontuacao"].replace(".", ",")
somas = {r["ID_estudo"]: (r["Soma de Pontos"].replace(".", ","), r["Status"])
         for r in csv.DictReader(QA_SOMAS.open(encoding="utf-8"))}
for eid, e in estudos.items():
    e["nota_qa"] = somas[eid][0]

# ------------------------------------------------------ status por questão
SIMBOLO = {"R": "Responde", "P": "Responde parcialmente", "N": "Não responde"}
status_rq = {}
for r in csv.DictReader(STATUS_RQ.open(encoding="utf-8")):
    marcas = [r[f"rq{n}"].strip() for n in range(1, 6)]
    assert all(x in SIMBOLO for x in marcas), f"{r['id']}: marcas inválidas {marcas}"
    status_rq[r["id"].strip()] = [SIMBOLO[x] for x in marcas]
assert len(status_rq) == 28, (
    f"{len(status_rq)} linhas em status_rq_por_estudo.csv, esperadas 28")

# ------------------------------------------------------------- bibliografia
bib = BIB.read_text(encoding="utf-8")
def campo(entrada, nome):
    m = re.search(rf"{nome}\s*=\s*\{{(.+?)\}},?\s*(?:\n|$)", entrada, re.S)
    if not m:
        return ""
    v = re.sub(r"\s+", " ", m.group(1)).strip()
    for tex_, uni in [("{\\'i}", "í"), ("{\\'e}", "é"), ("{\\'a}", "á"), ("{\\'o}", "ó"),
                      ("{\\'u}", "ú"), ("{\\~a}", "ã"), ("{\\~o}", "õ"), ("{\\c c}", "ç"),
                      ("{\\^a}", "â"), ("{\\^e}", "ê"), ("{\\^o}", "ô"), ("{\\`a}", "à")]:
        v = v.replace(tex_, uni)
    return v.replace("{", "").replace("}", "")

for bloco in re.findall(r"@\w+\{(E\d{2}),(.*?)\n\}", bib, re.S):
    eid, corpo = bloco
    if eid not in estudos:
        continue
    estudos[eid].update(
        autores=campo(corpo, "author"), ano=campo(corpo, "year"),
        titulo=campo(corpo, "title"), doi=campo(corpo, "doi"),
        veiculo=campo(corpo, "journal") or campo(corpo, "booktitle"))

faltando = [e for e in estudos.values() if not e.get("titulo")]
assert not faltando, f"sem metadados no .bib: {[e['id'] for e in faltando]}"

ORDEM = sorted(estudos)


# ---------------------------------------------------------------- escrita
def escrever(nome, cabecalho, linhas):
    caminho = AQUI / nome
    with caminho.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(cabecalho)
        w.writerows(linhas)
    print(f"  {nome:<34} {len(linhas):>3} linhas")


print(f"Gerando planilhas em {AQUI.relative_to(RAIZ)}/")

escrever("estudos.csv",
         ["id", "autores", "ano", "titulo", "veiculo", "tipo_veiculo", "doi", "base",
          "dominio", "dominio_agrupado", "contexto", "contexto_agrupado",
          "nota_qa", "grupo_rq4"],
         [[e[k] for k in ("id", "autores", "ano", "titulo", "veiculo", "tipo_veiculo",
                          "doi", "base", "dominio", "dominio_agrupado", "contexto",
                          "contexto_agrupado", "nota_qa", "grupo_rq4")]
          for e in (estudos[i] for i in ORDEM)])

escrever("matriz_evidencias.csv",
         ["id", "grupo_rq4", "proposta_central", "abordagens", "atividades_er",
          "temporal", "participacao", "mediacao", "papeis", "avaliacao_empirica"],
         [[e[k] for k in ("id", "grupo_rq4", "proposta_central", "abordagens",
                          "atividades_er", "temporal", "participacao", "mediacao",
                          "papeis", "avaliacao_empirica")]
          for e in (estudos[i] for i in ORDEM)])

escrever("estudo_x_rq.csv", ["id", "rq1", "rq2", "rq3", "rq4", "rq5"],
         [[i] + status_rq[i] for i in ORDEM])

escrever("rq1_eixos.csv",
         ["id", "temporal", "participacao", "mediacao", "seq", "ite", "col", "art",
          "trecho_campo5"],
         [[e[k] for k in ("id", "temporal", "participacao", "mediacao",
                          "seq", "ite", "col", "art", "trecho_campo5")]
          for e in (estudos[i] for i in ORDEM)])

escrever("rq2_abordagem_x_atividade.csv",
         ["abordagem", "estudos", "n", "eli", "ana", "esp", "val", "ges"], abordagens)

escrever("rq3_papeis.csv",
         ["id", "destinataria", "estruturadora", "organizadora",
          "pratica_coletiva_distribuida", "papeis", "trecho_campo10"],
         [[e[k] for k in ("id", "dst", "est", "org", "dis", "papeis", "trecho_campo10")]
          for e in (estudos[i] for i in ORDEM)])

escrever("rq4_propostas.csv",
         ["id", "grupo", "grupo_descricao", "proposta_central", "avaliacao_empirica"],
         [[e["id"], e["grupo_rq4"], GRUPOS_RQ4[e["grupo_rq4"]],
           e["proposta_central"], e["avaliacao_empirica"]]
          for e in (estudos[i] for i in ORDEM)])

escrever("rq5_lacunas_temas.csv", ["codigo", "descricao", "n", "estudos"],
         [[c, d, n, " ".join(ids)] for c, d, n, ids in lacunas_temas])

escrever("rq5_lacunas_por_estudo.csv", ["id", "temas", "trecho_campo9"],
         [[e["id"], e.get("lacunas", "—"), e.get("trecho_campo9", "")]
          for e in (estudos[i] for i in ORDEM)])

escrever("beneficios.csv", ["tema", "id", "grau_de_evidencia"], sorted(beneficios))
escrever("limitacoes.csv", ["tema", "id"], sorted(limitacoes))

escrever("qualidade_por_estudo.csv",
         ["id", "qa1", "qa2", "qa3", "qa4", "qa5", "qa6", "qa7", "qa8", "soma", "status"],
         [[eid] + [qa_por_estudo[eid][f"QA{n}"] for n in range(1, 9)] + list(somas[eid])
          for eid in sorted(somas)])

escrever("funil_prisma.csv",
         ["etapa", "criterios", "entram", "saem", "restam", "observacao"], FUNIL)

escrever("exclusoes_por_criterio.csv", ["fase", "criterio", "n"], EXCLUSOES)


# ------------------------------------------------------------- verificação
def conta(chave, valor):
    return sum(1 for e in estudos.values() if e[chave] == valor)


esperado = {
    "eixo temporal": ({conta("temporal", v) for v in ["Iterativa"]}, {10}),
    "mediação por artefatos": (sum(e["art"] for e in estudos.values()), 21),
    "participação colaborativa": (sum(e["col"] for e in estudos.values()), 9),
    "papel destinatária": (sum(e["dst"] for e in estudos.values()), 13),
    "papel estruturadora": (sum(e["est"] for e in estudos.values()), 12),
    "papel organizadora": (sum(e["org"] for e in estudos.values()), 8),
    "papel distribuída": (sum(e["dis"] for e in estudos.values()), 3),
    "grupo A (RQ4)": (conta("grupo_rq4", "A"), 14),
    "grupo B (RQ4)": (conta("grupo_rq4", "B"), 5),
    "grupo C (RQ4)": (conta("grupo_rq4", "C"), 3),
    "grupo D (RQ4)": (conta("grupo_rq4", "D"), 6),
    "atribuições de benefício": (len(beneficios), 43),
    "benefícios com evidência empírica": (
        sum(1 for _, _, g in beneficios if g == "Empírico"), 11),
    "estudos recuperados na IEEE": (conta("base", "IEEE Xplore"), 15),
    "estudos recuperados na ACM": (conta("base", "ACM DL"), 13),
    "lacuna L1 (validação pendente)": (
        next(n for c, _, n, _ in lacunas_temas if c == "L1"), 17),
    "atribuições de lacuna": (sum(n for _, _, n, _ in lacunas_temas), 50),
}
esperado["eixo temporal"] = (conta("temporal", "Iterativa"), 10)

print("\nConferência contra os números publicados no artigo:")
falhas = []
for nome, (obtido, alvo) in esperado.items():
    ok = obtido == alvo
    print(f"  {'ok ' if ok else 'ERRO'} {nome:<38} {obtido} (esperado {alvo})")
    if not ok:
        falhas.append(nome)

for eixo in ("temporal", "participacao", "mediacao"):
    total = sum(1 for e in estudos.values() if e.get(eixo))
    ok = total == 28
    print(f"  {'ok ' if ok else 'ERRO'} eixo {eixo} classifica os 28{'':<17} {total}")
    if not ok:
        falhas.append(f"eixo {eixo}")

if falhas:
    print(f"\n{len(falhas)} divergência(s): {', '.join(falhas)}", file=sys.stderr)
    sys.exit(1)
print("\nTodas as planilhas conferem com o relatório.")
