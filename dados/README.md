# `dados/` — evidência da revisão sistemática

Uma pasta por fase da RSL, na ordem em que foram executadas. Tudo o que o
relatório afirma sobre os estudos sai daqui.

```txt
dados/
├── 1_busca/        strings de busca e exports brutos das bases
├── 2_triagem/      decisão de título e resumo, registro a registro
├── 3_qualidade/    notas QA1–QA8, somas e elegibilidade em texto completo
├── 4_extracao/     fichas dos 28 estudos e a codificação da análise
├── 5_sintese/      planilhas derivadas (geradas por script) ← comece aqui
├── evidentia/      as mesmas etapas vistas pela ferramenta Evidentia
└── NOTAS_METODOLOGICAS.md   o que a leitura direta dos arquivos não explica
```

O protocolo que fixou tudo isso antes da triagem está em `../protocolo/`.

## As fases

| Pasta | Conteúdo | Papel |
| --- | --- | --- |
| `1_busca/strings/` | evolução da string, v1 (27/04/2026) → v2 (08/05/2026), com a análise exploratória que motivou o refinamento | fonte da Tabela III |
| `1_busca/exports/` | `artigos_ieee.bib` (163) e `artigos_acm.bib` (72) exportados em 08/05/2026 | os 235 registros do topo do funil |
| `2_triagem/` | `pt2.csv`: 235 registros com decisão e critério (`pt1.csv` é a 1ª iteração) | fonte da triagem por título e resumo |
| `3_qualidade/pt1/` | `incluidos.csv`: 320 linhas (40 estudos × 8 questões) com nota, justificativa e âncora de seção e página; `excluidos.csv`: os 40 barrados na elegibilidade | fonte da Tabela IV |
| `3_qualidade/pt2_pt3/` | `resultado.csv`: soma e status dos 40 avaliados | fonte da Tabela V |
| `4_extracao/extraction/` | as 28 fichas `E*.md`, 13 campos cada, com âncora por afirmação | fonte de tudo na Seção 4 |
| `4_extracao/categorizacao_c3_c5.md` | a codificação da análise (C3, C4, C5, C-RQ1, C-RQ3, C-RQ5) | **fonte única** das planilhas de síntese |
| `4_extracao/referencias_28.bib` | autores, ano, título, veículo e DOI dos 28 | identificação bibliográfica |
| `4_extracao/status_rq_por_estudo.csv` | o status de cada estudo em RQ1–RQ5, do campo 10 das fichas | fonte da Tabela VII |
| `5_sintese/` | as planilhas em CSV, geradas do arquivo acima | o que se abre para conferir números |
| `evidentia/` | exportações da ferramenta usada na condução, incluindo a bibliometria OpenAlex (219 obras) | visão paralela, não substitui as pastas acima |

Os PDFs dos 28 estudos não são redistribuídos aqui, por direito autoral.
`4_extracao/referencias_28.bib` traz o DOI de cada um, e as fichas de
`4_extracao/extraction/` ancoram cada afirmação em seção e página, de modo que a
conferência não depende de ter o PDF em mãos.

Os prompts usados com a LLM estão em `3_qualidade/prompt.md` e
`4_extracao/prompt.md`, citados na Declaração de Utilização de LLMs do relatório.

A conciliação dos números do funil e a atribuição da base de recuperação de cada
estudo estão em `NOTAS_METODOLOGICAS.md`.

## As planilhas de `5_sintese/`

Todas são reprojeções tabulares de `4_extracao/categorizacao_c3_c5.md`, do
`.bib` e dos CSVs das fases anteriores. Regenerar depois de qualquer mudança na
codificação:

```sh
python3 5_sintese/gerar_planilhas.py
```

O script confere os agregados contra os números publicados no relatório e falha se
algum divergir, de modo que uma planilha desatualizada não passa em silêncio.

| Planilha | Linhas | Conteúdo |
| --- | ---: | --- |
| `estudos.csv` | 28 | um estudo por linha: metadados do `.bib`, base de recuperação, domínio, contexto, veículo, nota de qualidade, grupo da RQ4 |
| `matriz_evidencias.csv` | 28 | a Tabela IX do relatório: proposta central, abordagem, atividades de ER, os três eixos da RQ1, papel da ER e avaliação relatada |
| `estudo_x_rq.csv` | 28 | status de cada estudo em RQ1–RQ5 (Responde / Responde parcialmente / Não responde) |
| `rq1_eixos.csv` | 28 | os três eixos mais os rótulos brutos Seq/Ite/Col/Art e o trecho literal do campo 5 que sustenta a classificação |
| `rq2_abordagem_x_atividade.csv` | 6 | cruzamento abordagem × atividade de ER, com a lista de estudos de cada abordagem |
| `rq3_papeis.csv` | 28 | os quatro papéis atribuídos à ER, com o trecho literal do campo 10 ou 12 |
| `rq4_propostas.csv` | 28 | grupo (A–D), proposta central e avaliação empírica relatada |
| `rq5_lacunas_temas.csv` | 6 | os seis temas de lacuna (L1–L6), com contagem e estudos |
| `rq5_lacunas_por_estudo.csv` | 28 | os temas de cada estudo e o trecho literal do campo 9 |
| `beneficios.csv` | 43 | formato longo: tema × estudo × grau de evidência (Empírico, Participantes, Sem evidência) |
| `limitacoes.csv` | 46 | formato longo: tema × estudo |
| `qualidade_por_estudo.csv` | 40 | QA1–QA8 por estudo, soma e status |
| `funil_prisma.csv` | 6 | as etapas do funil, com quantos entram, saem e restam |
| `exclusoes_por_criterio.csv` | 12 | razão primária de exclusão por fase |

## Onde cada tabela e figura do relatório foi buscar seus números

O relatório em si não é publicado neste repositório, mas cada número que ele
afirma pode ser conferido pela linha correspondente abaixo.

| No relatório | Planilha | Fonte primária |
| --- | --- | --- |
| Tabela I (PICOC) | — | `../protocolo/protocolo_rsl_er_design.pdf` |
| Tabela II (critérios CI/CE) | — | `../protocolo/protocolo_rsl_er_design.pdf` |
| Tabela III (string de busca) | — | `1_busca/strings/4_string_de_busca_final.md` |
| Figura 1 (fluxo PRISMA) | `funil_prisma.csv` | `2_triagem/pt2.csv` + `3_qualidade/` |
| Figura 2 (exclusões por critério) | `exclusoes_por_criterio.csv` | `2_triagem/pt2.csv`, `3_qualidade/pt1/excluidos.csv` |
| Tabela IV (qualidade) | `qualidade_por_estudo.csv` | `3_qualidade/pt1/incluidos.csv` |
| Tabela V (avaliados e não incluídos) | `qualidade_por_estudo.csv` | `3_qualidade/pt2_pt3/resultado.csv` |
| Figura 3 (distribuição por ano) | `estudos.csv` | `4_extracao/referencias_28.bib` |
| Tabela VI (caracterização do corpus) | `estudos.csv` | `4_extracao/categorizacao_c3_c5.md` |
| Tabela VII (estudo × RQ) | `estudo_x_rq.csv` | `4_extracao/status_rq_por_estudo.csv` (campo 10 das fichas) |
| Tabela VIII (abordagens × atividades) | `rq2_abordagem_x_atividade.csv` | seção C3 da categorização |
| Tabela IX (matriz de evidências) | `matriz_evidencias.csv` | tabela mestra + C-RQ1 + C-RQ3 |
| Tabela X (benefícios, limitações, lacunas) | `beneficios.csv`, `limitacoes.csv`, `rq5_lacunas_temas.csv` | seções C5 e C-RQ5 |
| Figura 4 (três eixos da RQ1) | `rq1_eixos.csv` | seção C-RQ1 (dimensional) |

## Três coisas que confundem quem chega agora

**O funil não sai de uma contagem direta do `pt2.csv`.** Vários registros têm
mais de um critério marcado; o funil publicado resolve cada um pela razão
primária, e quatro contêineres de anais saem antes da triagem, não nela. A
conciliação está registrada na §1 de `NOTAS_METODOLOGICAS.md` e é o que
`exclusoes_por_criterio.csv` reproduz.

**As oito questões de qualidade aparecem com dois rótulos.**
`3_qualidade/pt1/incluidos.csv` usa `AQ1..AQ8` em 36 estudos e `QA1..QA8` em 4,
com as mesmas descrições. O relatório padronizou QA1–QA8, e o gerador normaliza
(§4 de `NOTAS_METODOLOGICAS.md`).

**219 não é 235.** A bibliometria em `evidentia/bibliometria/` cobre 219 obras
do OpenAlex; 16 dos 235 registros não têm correspondência lá. São recortes
diferentes, e qualquer uso dos dados bibliométricos precisa dizer isso
(§3 de `NOTAS_METODOLOGICAS.md`).
