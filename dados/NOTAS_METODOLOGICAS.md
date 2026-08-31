# Notas metodológicas

Quatro pontos em que a leitura direta dos arquivos não chega sozinha ao número
publicado. Cada um registra a decisão tomada e o que a sustenta, para que a
conferência possa refazer o caminho em vez de aceitar o resultado.

## 1. Conciliação do funil PRISMA

`2_triagem/pt2.csv` tem 235 linhas, mas contar exclusões diretamente nele não
reproduz a Figura 1 do relatório. Duas razões:

- **Vários registros têm mais de um critério marcado.** O funil publicado
  resolve cada registro pela sua **razão primária**, uma só por registro. É isso
  que `5_sintese/exclusoes_por_criterio.csv` reproduz, e por isso as somas por
  critério fecham com o total de excluídos da fase.
- **Quatro contêineres de anais saem antes da triagem, não nela.** São entradas
  `@proceedings` do export da ACM — o volume inteiro, não um artigo. Junto com
  as duplicatas, são removidos na etapa anterior à leitura de títulos.

A narrativa oficial, conferida em 16/08/2026 contra os exports
(`1_busca/exports/artigos_ieee.bib` = 163, `artigos_acm.bib` = 72) e contra as
235 linhas do `pt2.csv`:

| Etapa | Saem | Restam | Razão primária |
|---|---:|---:|---|
| Busca (v2, 08/05/2026) | — | 235 | 163 IEEE + 72 ACM |
| Remoção antes da triagem | 11 | 224 | 4 contêineres de anais (CE1) + 7 duplicatas (CE2) |
| Triagem por título e resumo | 144 | 80 | CE3 95, ¬CI1 26, CE7 15, CE1 4, CE6 4 |
| Elegibilidade em texto completo | 40 | 40 | CE7 17, CE3 8, CE5 5, CE4 4, CE1 3, CE6 2, ¬CI3 1 |
| Avaliação de qualidade (corte 6,5) | 8 | 32 | nenhum estudo pontuou entre 6,0 e 6,5 |
| Reaplicação dos critérios na extração | 4 | **28** | 3 short papers (CE7) + 1 fora de escopo (CE4) |

As 7 duplicatas são 1 intra-IEEE e 6 entre ACM e IEEE, confirmadas por título
nos dois exports. Não houve estudo não recuperado: todos os textos completos
foram obtidos, e por isso a caixa "relatórios não recuperados" do PRISMA é zero.
CE8 não tem nenhuma ocorrência em `pt2.csv`, `3_qualidade/pt1/excluidos.csv`,
`3_qualidade/pt1/incluidos.csv` ou `3_qualidade/pt2_pt3/resultado.csv`.

**Dois números que aparecem na cronologia das strings e não são o funil.** Em
`1_busca/strings/3_1_sintese_cronologica_strings.md` lê-se 231 e 196. O primeiro
é 68 + 163, isto é, a contagem da ACM já descontando os 4 `@proceedings`. O
segundo é 224 − 28: os 28 registros anteriores a 2010 marcados com CI1 no CSV
(dois deles contêineres). Nenhum dos dois corresponde a uma etapa do funil.

## 2. Base de recuperação dos 28

Atribuída por **presença nos exports**, não pela editora do veículo: **15 IEEE**
(E01, E02, E12, E25, E27, E29, E40, E51, E58, E63, E64, E70, E72, E75, E79) e
**13 ACM** (E09, E21, E23, E32, E36, E38, E43, E45, E46, E47, E57, E67, E74).
É a coluna `base` de `5_sintese/estudos.csv`.

Dois casos são espelhados e precisaram de decisão explícita:

- **E02** — o SEHS'16 é workshop co-patrocinado IEEE/ACM e está indexado nas duas
  bases (é uma das 6 duplicatas entre bases). Recuperado via IEEE → contado como
  IEEE.
- **E46** — a ficha diz "IEEE Xplore" porque é o que o carimbo do PDF traz
  (DISE'17 é workshop do ICSE publicado pela IEEE Press), mas o registro só
  existe em `artigos_acm.bib` → contado como ACM.

## 3. 219 não é 235

A bibliometria em `evidentia/bibliometria/` cobre **219 obras** do OpenAlex; 16
dos 235 registros exportados não têm correspondência lá. São recortes
diferentes, e qualquer uso dos dados bibliométricos precisa declarar isso — no
relatório, em nota de rodapé. Os números do funil e da síntese saem sempre das
fichas e dos CSVs das fases, nunca da bibliometria.

## 4. Os rótulos AQ e QA

`3_qualidade/pt1/incluidos.csv` rotula as oito questões de qualidade ora
`AQ1..AQ8` (36 estudos), ora `QA1..QA8` (4 estudos, os primeiros extraídos). São
as mesmas oito questões, com as mesmas descrições; a diferença é só de
digitação. O relatório padronizou **QA1–QA8**, e `5_sintese/gerar_planilhas.py`
normaliza `AQ` → `QA` na leitura, de modo que
`5_sintese/qualidade_por_estudo.csv` sai com um rótulo só.
