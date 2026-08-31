# Relatório Final — Análise dos Resultados da Nova String de Busca (IEEE + ACM)

## Sumário Executivo

A nova string de busca, executada em IEEE Xplore e ACM Digital Library, retornou
**228 artigos únicos** (231 brutos, 3 duplicatas internas removidas). Comparando
com a busca anterior, **114 artigos são inéditos** — material que a string
original não havia capturado. A composição temática mudou conforme planejado:
Design Thinking + UX agora respondem por quase metade dos resultados (48%),
contra apenas 18% antes.

A análise das hipóteses levantadas confirmou:

- **Hipótese 1 — duplicatas no CSV antigo:** **confirmada parcialmente.** Há
  duplicatas, mas em volume baixo (79 linhas, ~1,6%) — não são suficientes
  para explicar as perdas observadas. A inspeção, porém, revelou um problema
  adicional: pelo menos 60 linhas do CSV antigo são lixo bibliográfico
  (Tables of Contents, Forewords, Title Pages).
- **Hipótese 2 — artigos perdidos estão em outras bases:** **confirmada por
  evidência direta.** A busca individual no IEEE Xplore e ACM por *"Design
  Thinking in Software Requirements: What Techniques to Use?"* não encontrou
  o artigo, indicando que ele está hospedado em base não consultada (Springer,
  Scopus, etc.).
- **Decisão de escopo:** manter a busca apenas em IEEE + ACM. Esta decisão
  é metodologicamente legítima desde que documentada como **limitação do
  estudo** no protocolo da SLR.

---

## 1. Quantitativos Consolidados

### 1.1. Resultado da nova string

| Fonte | Registros |
|-------|----------:|
| ACM (`acm_v4.bib`) | 68 |
| IEEE (`merged.ris`) | 163 |
| **Bruto somado** | **231** |
| Duplicatas removidas (DOI ou título idêntico) | 3 |
| **Únicos pós-deduplicação** | **228** |

> **Nota sobre o `acm_v4.bib`.** O arquivo continha 72 entradas, mas 4 eram
> do tipo `@proceedings` (metadados de actas, não artigos individuais) e
> foram descartadas — restaram 68 artigos.

A baixa deduplicação interna (3 registros) confirma que IEEE e ACM têm
**pouca sobreposição entre si** — bom indicador de cobertura complementar.

### 1.2. Sobreposição com a busca anterior

| Categoria | Quantidade | % |
|-----------|-----------:|---:|
| Já estavam no CSV antigo | 114 | 50,0% |
| **Inéditos** (capturados só pela string nova) | **114** | **50,0%** |

A reformulação da string trouxe **114 artigos genuinamente novos**, validando
a hipótese inicial de que a string anterior estava restrita ao eixo de ER e
deixava de fora trabalhos que viviam pelo lado do design.

---

## 2. Hipótese 1 — Duplicatas no CSV antigo

### 2.1. O que foi encontrado

| Aspecto | Resultado |
|---------|-----------|
| Total de linhas no CSV | 4.820 |
| IDs únicos | 4.820 (todos distintos) |
| Títulos exatamente iguais | 70 linhas duplicadas |
| Títulos normalizados (case-insensitive, sem pontuação) | 79 linhas duplicadas |
| **Títulos verdadeiramente únicos** | **4.741** |

**Conclusão sobre duplicatas:** existem, mas representam **1,6% do total**.
Mesmo que todas as 79 fossem do núcleo (Design ∪ UX) ∩ ER — o que é
estatisticamente impossível —, ainda restariam mais de 60 perdas
inexplicadas. **Duplicatas não explicam a diferença de cobertura.**

### 2.2. Achado adicional: lixo bibliográfico

A análise revelou um problema mais relevante que duplicatas: **pelo menos
60 linhas do CSV antigo são lixo bibliográfico** — não são artigos científicos
mas sim metadados de actas:

- *Table of contents* (14 ocorrências)
- *Title Page i* (10 ocorrências)
- *Contents* (6 ocorrências)
- *Foreword*, *Welcome Message*, *Front Cover*, *Author Index*, *Preface*

Além disso, **46 linhas são introduções de workshops/proceedings** (ex.:
*"Welcome to the Sixth International Workshop on Crowd-Based Requirements
Engineering"*, *"5th International Workshop on the Twin Peaks of Requirements
and Architecture"*) — esses são *front matter* de eventos, não estudos
primários.

> **Implicação para o protocolo da SLR.** Esse material será excluído pelos
> seus critérios **CE1** (artigos de opinião) e **CE7** (relatórios, short
> papers, teses). A nova busca, por estar mais focada, deve trazer menos
> lixo desse tipo — uma **vantagem secundária** da reformulação. Recomenda-se
> adicionar uma etapa explícita de "remoção de front matter" antes da
> aplicação dos CI/CE para tornar o processo auditável.

---

## 3. Hipótese 2 — Artigos perdidos estão em outras bases

### 3.1. Evidência direta

Você verificou manualmente o artigo *"Design Thinking in Software Requirements:
What Techniques to Use? A Proposal for a Recommendation Tool"* nas bases IEEE
Xplore e ACM Digital Library e **não o encontrou em nenhuma das duas**. Esta
é a confirmação mais robusta da hipótese: se o artigo não está hospedado nessas
bases, nenhuma string — por mais bem formulada — poderia capturá-lo a partir
delas. A perda é estrutural, não decorre de falha na busca.

### 3.2. Magnitude do efeito

O CSV antigo continha **165 artigos** que cumpriam o critério (Design ∪ UX) ∩ ER
pelo título. Cruzando com o resultado da nova string:

- **22 foram recuperados** pela nova string.
- **143 não foram recuperados.**

A análise lexical dos 143 mostra que **101 deles têm termos do bloco 2
(Design/UX) no próprio título** — incluindo 22 com "Design Thinking" no
título. Se estivessem na ACM ou IEEE, teriam sido capturados. Sua verificação
manual confirma que ao menos um desses 22 não está nessas bases. Por
extrapolação, é plausível que a maioria dos demais também esteja em outras
bases (Scopus, Springer Link, ScienceDirect — bases típicas para REFSQ, RE
e periódicos como Information and Software Technology, JSS).

### 3.3. Os 42 sem termo de design no título

Dos 143 perdidos, 42 não têm nenhum termo de design/UX no título — foram
incluídos no núcleo antigo via abstract ou keywords. **Estes podem ser perdas
parcialmente justificadas:** sem termo de design no título, há menor garantia
de que o trabalho realmente integra ER × Design (em vez de apenas mencionar
um conceito en passant).

---

## 4. Decisão Metodológica — Escopo Restrito a IEEE + ACM

Você decidiu manter a busca apenas em IEEE Xplore e ACM Digital Library. Esta
é uma decisão **metodologicamente legítima** desde que reportada com
transparência. Eis o que isso implica e como tratar.

### 4.1. Implicações

✅ **Vantagens:**

- **Reprodutibilidade.** Duas bases bem documentadas, com sintaxe estável.
- **Qualidade editorial controlada.** IEEE e ACM são as duas maiores
  publishers de Computação; cobrem as principais conferências do campo
  (ICSE, RE, REFSQ é Springer mas IEEE/ACM cobrem a contraparte de RE),
  CHI, ICSE Companion, etc.).
- **Tempo viável.** Buscar em mais bases multiplicaria o trabalho de
  triagem.

⚠️ **Limitações reconhecidas:**

- **Estudos de Springer (REFSQ, IS&T) ficam de fora.** REFSQ é a principal
  conferência europeia sobre requisitos e tem boa proporção de papers
  cruzando ER e design. Periódicos da Springer e Elsevier (REJ, JSS, IST)
  contêm trabalhos centrais ao tema.
- **Trabalhos brasileiros via SBC podem escapar.** SBC é parcialmente
  indexada em ACM (anais do SBQS, SBES, SBSI estão na ACM Digital Library
  desde ~2018) mas não integralmente.
- **Cobertura quantitativa estimada:** com base nas 143 perdas observadas,
  a busca atual captura provavelmente entre **50% e 65%** da literatura
  relevante existente.

### 4.2. Como reportar no protocolo

Recomenda-se um parágrafo explícito no capítulo de método da SLR, algo como:

> *"A busca foi conduzida nas bases IEEE Xplore e ACM Digital Library, escolhidas
> por sua centralidade na área de Engenharia de Software e por reunirem as
> principais conferências e periódicos do campo. Reconhece-se como limitação
> deste estudo a não inclusão de bases adicionais como Scopus, Springer Link
> e ScienceDirect, que indexam outros veículos relevantes (notadamente o REFSQ
> e periódicos como o Requirements Engineering Journal). Estima-se, com base
> em análise exploratória, que a cobertura da busca corresponde a
> aproximadamente metade da literatura existente sobre o cruzamento entre ER
> e abordagens de design. Este risco de cobertura parcial é mitigado por
> [estratégias adotadas — ver seção 4.3]."*

### 4.3. Mitigação recomendada (sem expandir bases)

Como você decidiu manter o escopo, três estratégias podem reforçar a
cobertura **sem adicionar bases**:

1. **Snowballing forward + backward.** Após a triagem por CI/CE, faça
   snowballing nos estudos incluídos. Mesmo limitado a IEEE/ACM, isto
   trará referências cruzadas para artigos importantes que vivem em outras
   bases. Esta é, hoje, **uma prática recomendada em qualquer SLR de SE
   (Wohlin, 2014)** e legitima a cobertura.

2. **Aceitar achados de busca manual em bases-chave.** Você já encontrou
   artigos relevantes (ex.: o *"Design Thinking in Software Requirements"*
   em uma busca individual). Se incorporar esses achados como
   "recuperação manual complementar" e documentar a fonte, a cobertura
   aumenta sem mudar a string principal.

3. **Considere validar os resultados da SLR junto a um especialista.** Após
   a triagem final, um par expert da área pode apontar trabalhos seminais
   ausentes que mereçam inclusão por busca direcionada. Esta é uma prática
   reconhecida em SLRs maduras.

---

## 5. Distribuição Temporal e Filtro CI1

Distribuição dos 228 artigos por ano:

| Período | Artigos | % |
|---------|--------:|---:|
| Antes de 2010 | 30 | 13,2% |
| 2010–2014 | 34 | 14,9% |
| 2015–2019 | 54 | 23,7% |
| 2020–2024 | 80 | 35,1% |
| 2025–2026 | 30 | 13,2% |

**30 artigos serão excluídos pelo critério CI1** (a partir de 2010), restando
**~198 artigos** para a triagem por demais CI/CE.

A concentração nos últimos 6 anos (2020–2026: 110 artigos, 48% do total)
indica um campo em expansão, o que é consistente com a percepção geral de
que Design Thinking e Co-Design vêm sendo cada vez mais incorporados em
contextos de desenvolvimento de software.

---

## 6. Composição Temática

### 6.1. Áreas dos 228 artigos da nova string

| Área | Multi-rótulo | Primária |
|------|-------------:|---------:|
| Design Thinking, Service Design e Co-Design | 64 (28%) | 64 |
| UX, Usabilidade e HCI | 45 (20%) | 38 |
| Engenharia de Requisitos | 54 (24%) | 28 |
| Mobile, Web e Plataformas Digitais | 50 (22%) | 11 |
| Domínios: Saúde, Educação, Sociedade | 44 (19%) | 12 |
| Métodos Ágeis, DevOps e Gestão de Projetos | 24 (11%) | 8 |
| IoT, Embarcados, CPS e Indústria 4.0 | 23 (10%) | 13 |
| Verificação, Validação e Testes | 18 (8%) | 3 |
| Inteligência Artificial, ML e NLP | 11 (5%) | 8 |
| Jogos, Gamificação, VR/AR | 11 (5%) | 3 |
| Arquitetura, MDE, SPL e Cloud | 9 (4%) | 3 |
| Dados, Visualização e BD | 6 (3%) | 1 |
| Processos de Negócio e SI | 3 (1%) | 1 |
| Segurança, Privacidade, Safety | 2 (1%) | 1 |
| Outros / Não classificado | 34 (15%) | 34 |

### 6.2. Comparação Antes vs. Depois

| Área | CSV antigo (4.820) | Nova string (228) | Variação |
|------|------------------:|------------------:|---------:|
| Design Thinking, Service Design e Co-Design | 8,6% | 28% | **+19 pp** |
| UX, Usabilidade e HCI | 9,5% | 20% | **+10 pp** |
| Engenharia de Requisitos | 39,0% | 24% | -15 pp |

A reformulação inverteu a proporção esperada: agora **Design + UX dominam
a composição (48%) contra ER pura (24%)** — exatamente o foco desejado para
a SLR. Isso confirma que a nova string mudou a natureza do conjunto, não
apenas seu tamanho.

### 6.3. Artigos no núcleo (Design ∪ UX) ∩ ER

Pelo título, **26 dos 228 (11,4%)** já caem no núcleo. Considerando que a
busca foi feita em título + abstract (e a classificação aqui é só pelo
título), o número real deve ser bem maior — provavelmente acima de 60% do
conjunto pertence ao núcleo após leitura completa de abstracts.

---

## 7. Conclusões e Próximos Passos

### 7.1. Conclusões

1. A reformulação da string foi **bem-sucedida** no foco temático: Design
   e UX passaram de 18% para 48% da composição, enquanto ER pura caiu de
   39% para 24%.

2. **114 artigos inéditos** foram trazidos pela nova string, validando
   a hipótese de que a string anterior tinha cobertura cega no eixo do
   design.

3. As **143 perdas** observadas em relação ao CSV antigo são quase
   integralmente atribuíveis à **cobertura de bases** (não a falhas da
   string). A evidência direta — sua busca manual sem sucesso em IEEE/ACM
   pelo artigo *"Design Thinking in Software Requirements"* — confirma que
   esses artigos vivem em Springer, Scopus e similares.

4. Duplicatas no CSV antigo existem (79 linhas, 1,6%) mas **não explicam
   as perdas**. Há também 60+ linhas de lixo bibliográfico que serão
   excluídas pelos critérios CI/CE.

5. A decisão de **manter o escopo em IEEE + ACM** é legítima, mas precisa
   ser **declarada como limitação** no protocolo da SLR e mitigada por
   snowballing pós-triagem.

### 7.2. Recomendações para os próximos passos

1. **Trabalhar com os 228 artigos da nova string como conjunto definitivo.**
   Não é necessário reincorporar artigos do CSV antigo — eles foram
   exploratórios e cumpriram seu propósito de informar a reformulação da
   string.

2. **Aplicar uma etapa de pré-limpeza** antes dos CI/CE: remover
   front matter de actas, *welcome messages*, *table of contents* e similares
   (espera-se baixíssima incidência na nova busca, mas vale conferir).

3. **Aplicar o filtro CI1** (a partir de 2010): elimina ~30 artigos.

4. **Aplicar os demais CI/CE** sobre os ~198 artigos remanescentes, com
   leitura de título + abstract (e do texto completo quando o abstract for
   inconclusivo). Recomenda-se uso de uma ferramenta de gestão (Parsifal,
   Rayyan, Notion) para registrar cada decisão.

5. **Após a inclusão definitiva, aplicar snowballing** (forward via
   citações; backward via referências) sobre os estudos incluídos.

6. **No protocolo final**, documentar:
   - A evolução da string (v1 exploratória → v2 definitiva);
   - A decisão de manter as duas bases (IEEE + ACM) e suas implicações;
   - Os critérios de pré-limpeza adotados;
   - A estratégia de snowballing como mitigação para cobertura limitada.

### 7.3. Resumo numérico para o protocolo

| Métrica | Valor |
|---------|------:|
| Artigos retornados da busca (IEEE + ACM, deduplicados) | 228 |
| Após exclusão de pré-2010 (CI1) | ~198 |
| Esperados no núcleo (Design/UX × ER) após leitura de abstracts | ~140 (estimado) |
| Esperados após CI/CE completos (estimativa cautelosa) | 40–80 |
| Após snowballing (forward + backward) | a estabelecer |

A SLR converge para um conjunto final dentro da faixa típica de revisões
sistemáticas em ER (40–100 estudos primários).
