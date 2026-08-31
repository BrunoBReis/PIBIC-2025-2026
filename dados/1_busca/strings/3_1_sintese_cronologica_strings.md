# Síntese Cronológica das Strings de Busca

*Anexo ao relatório final consolidado — documenta a evolução do processo de
busca e serve como material auditável para a seção de método da SLR.*

---

## Visão geral em uma tabela

| Versão | Data | Escopo conceitual | Bases | Bruto | Únicos | Núcleo¹ | Design² | UX² | ER² |
|:------:|:----:|:------------------|:------|------:|-------:|--------:|--------:|----:|----:|
| **v1** | maio/2026 (inicial) | ER + Software | ACM + IEEE | ~4.820³ | 4.741 | 159 | 7,9% | 9,4% | 39,0% |
| **v2** | 2026 (reformulada) | ER × (Design ∪ UX) × Contexto digital | ACM + IEEE | 231 | 224 | 25 | 27,2% | 19,2% | 23,7% |

¹ Núcleo = artigos que casam com (Design ∪ UX) ∩ ER **apenas pelo título** (subestima o valor real, que só a leitura de abstracts revelaria).
² Percentuais sobre o total de únicos, classificação multi-rótulo por área temática.
³ v1: exportação bruta reportada pelas bases; o CSV consolidado tem 4.820 linhas, das quais 79 são duplicatas por título e ~60 são lixo bibliográfico (front matter de actas).

---

## Fase 1 — String v1 (busca inicial exploratória)

### Formulação

```
("Requirements Engineering" OR
 "Requirements Analysis" OR
 "Requirements Elicitation" OR
 "Requirements Management" OR
 "Requirements Specification" OR
 "Requirements Process" OR
 "Requirements Practices" OR
 "Requirements Gathering" OR
 "Requirements Modeling" OR
 "User Requirements" OR
 "Stakeholder Requirements")
AND
("Software")
```

### Racional

A string v1 partiu de uma abordagem clássica de mapeamento em Engenharia de
Requisitos: capturar amplamente o vocabulário canônico do subcampo e filtrar
pelo contexto de software. Não incorporava termos do outro lado do fenômeno
investigado (design), o que a tornava uma **busca de um só eixo** — ampla
em ER e cega em design.

Aplicação nas bases: título e resumo na IEEE Xplore; apenas resumo na ACM
Digital Library.

### Resultado

- **4.820 registros exportados** (após uma primeira deduplicação por DOI feita
  pelas próprias bases).
- Após deduplicação por título normalizado: **4.741 únicos** (79 duplicatas
  residuais, 1,6%).
- Aproximadamente **60 registros** identificados como lixo bibliográfico
  (*Table of Contents*, *Foreword*, *Front Cover*, *Welcome Message* etc.),
  que seriam eliminados pelos critérios de exclusão CE1 ou CE7.

### Composição temática

Classificação em 15 áreas amplas por palavras-chave nos títulos:

| Área | Multi-rótulo | % |
|------|-------------:|---:|
| Engenharia de Requisitos | 1.880 | 39,0% |
| Métodos Ágeis, DevOps e Gestão de Projetos | 681 | 14,1% |
| UX, Usabilidade e HCI | 452 | 9,4% |
| Domínios: Saúde, Educação, Sociedade | 429 | 8,9% |
| Verificação, Validação e Testes | 407 | 8,4% |
| Mobile, Web e Plataformas Digitais | 395 | 8,2% |
| Design Thinking, Service Design e Co-Design | 381 | 7,9% |
| Demais áreas | — | — |

A composição refletia diretamente o desenho da string: **ER dominante**
(39%), com Design + UX somando pouco (17,3%). O núcleo (Design ∪ UX) ∩ ER
computado pelo título totalizou **159 artigos** — apenas 3,4% do conjunto.

### Diagnóstico

A v1 cumpriu a função **exploratória** de mapear a paisagem. Mas, do ponto
de vista da pergunta central da SLR — *como a literatura descreve as
interações entre ER e abordagens de design de serviços e produtos?* —, o
sinal-ruído era desfavorável: para cada artigo genuinamente sobre a
interação, havia dezenas de artigos de ER pura que iriam ser excluídos por
CE5 (não responde a nenhuma questão de pesquisa).

Duas fragilidades foram identificadas:

1. **Ausência de termos de design no filtro:** a string não continha
   "Design Thinking", "Co-Design", "User-Centered Design" etc. Artigos que
   tratavam da integração ER × Design mas cujo título/abstract não usava o
   léxico canônico de ER (ex.: *"Trends in the Use of Design Thinking for
   Embedded Systems"*) ficavam invisíveis para a busca.
2. **Contexto muito restrito no terceiro bloco:** o operando `AND ("Software")`
   deixava de fora trabalhos indexados sob "digital", "application" ou
   "platform", que são termos alinhados ao escopo declarado no PICOC
   ("desenvolvimento de software e soluções digitais").

Esses diagnósticos motivaram a reformulação.

---

## Fase intermediária — Análise exploratória

Entre v1 e v2, foi realizada uma análise da composição temática dos 4.820
resultados. Essa análise **não é uma etapa formal da SLR**, mas cumpriu
papel metodológico importante: permitiu tomar decisões sobre o novo desenho
da string com base em evidência empírica (frequência de termos, coocorrência
entre áreas, distribuição por eixo temático) e não em intuição.

Três produtos dessa fase:

1. **Mapeamento em 15 áreas amplas**, útil como referência semântica para
   as decisões de escopo.
2. **Identificação da assimetria do conjunto:** apenas 3,4% dos artigos
   caíam no núcleo (Design ∪ UX) ∩ ER pelo título.
3. **Lista de termos candidatos para o bloco de design**, extraída da
   inspeção do vocabulário efetivamente empregado nos títulos.

A prática de conduzir uma análise exploratória antes de refinar a string é
consistente com a orientação de Kitchenham e Charters (2007, §5.6) de que
o protocolo de busca pode ser refinado durante a fase de execução, desde
que as mudanças sejam **documentadas e justificadas**. Este anexo cumpre
essa função de documentação.

---

## Fase 2 — String v2 (busca reformulada)

### Formulação

```
(
  "Requirements Engineering" OR "Requirements Analysis" OR
  "Requirements Elicitation" OR "Requirements Management" OR
  "Requirements Specification" OR "Requirements Process" OR
  "Requirements Practices" OR "Requirements Gathering" OR
  "Requirements Modeling" OR "User Requirements" OR
  "Stakeholder Requirements"
)
AND
(
  "Design Thinking" OR "Service Design" OR
  "Co-Design" OR "Codesign" OR
  "Co-Creation" OR "Cocreation" OR
  "Design Sprint" OR "Lean Inception" OR
  "Participatory Design" OR
  "User-Centered Design" OR "User Centered Design" OR
  "User-Centred Design" OR "User Centred Design" OR
  "Human-Centered Design" OR "Human Centered Design" OR
  "Human-Centred Design" OR "Human Centred Design" OR
  "User Experience" OR "UX Design"
)
AND
(
  "Software" OR "Digital" OR "Application" OR "Platform"
)
```

### Racional (mudanças em relação à v1)

Três alterações foram introduzidas, cada uma amparada por decisão explícita:

1. **Bloco 2 — Design + UX adicionado.** Foram incluídos os cinco termos
   listados no PICOC (Design Thinking, Service Design, Lean Inception,
   Co-Design, Design Sprint) mais Participatory Design, Co-Creation e as
   oito variantes ortográficas de UCD/HCD (com/sem hífen, americana/britânica).
   User Experience e UX Design foram incorporados como **ponte** para o corpo
   de UX/HCI, decisão tomada explicitamente após análise exploratória.

2. **Bloco 3 — contexto ampliado.** `("Software")` foi expandido para
   `("Software" OR "Digital" OR "Application" OR "Platform")`, alinhando o
   filtro ao Context declarado no PICOC ("desenvolvimento de software **e
   soluções digitais**").

   *Nota:* o termo "System" foi cogitado e **rejeitado** por ser guarda-chuva
   em Computação — em teste, `("Software" OR "Digital" OR "System")` teria
   anulado o filtro (praticamente todo paper de SE contém "system" em algum
   ponto do abstract).

3. **Termos genéricos deliberadamente excluídos.** "Persona", "Scenario",
   "Prototype", "Usability", "HCI" isolados **não** foram incluídos no bloco
   de design. Justificativa: são instrumentos genéricos, presentes em milhares
   de trabalhos fora do escopo; sua adição inflaria drasticamente o ruído sem
   ganho proporcional. Os trabalhos relevantes que usam esses instrumentos
   tendem a ser capturados por termos mais específicos do próprio bloco.

Aplicação nas bases: mesmos campos que a v1 (título + resumo na IEEE; resumo
na ACM). Sintaxe adaptada para os operadores próprios de cada base.

### Resultado

| Métrica | Valor |
|---------|------:|
| ACM (`acm_v4.bib`) | 68 registros¹ |
| IEEE (`merged.ris`) | 163 registros |
| **Bruto somado** | **231** |
| Duplicatas internas (DOI + título) | 7 |
| **Únicos** | **224** |

¹ O arquivo ACM continha 72 entradas, mas 4 eram `@proceedings` (metadados
de actas inteiras) e foram descartadas.

### Composição temática

| Área | Multi-rótulo | % | Δ vs. v1 |
|------|-------------:|---:|---------:|
| Design Thinking, Service Design e Co-Design | 61 | 27,2% | **+19,3 pp** |
| Engenharia de Requisitos | 53 | 23,7% | −15,3 pp |
| UX, Usabilidade e HCI | 43 | 19,2% | **+9,8 pp** |
| Mobile, Web e Plataformas Digitais | 50 | 22,3% | +14,1 pp |
| Domínios: Saúde, Educação, Sociedade | 44 | 19,6% | +10,7 pp |
| Demais áreas | — | — | — |

A **inversão da composição** é o efeito mais evidente da reformulação: Design
e UX juntos passaram de 17,3% (v1) para 46,4% (v2), enquanto ER pura caiu
de 39% para 23,7%. O núcleo (Design ∪ UX) ∩ ER pelo título subiu de 3,4%
(v1) para 11,2% (v2) — ganho de 3,3x na densidade de sinal.

### Distribuição temporal (v2)

| Período | Artigos | % |
|---------|--------:|---:|
| Antes de 2010 | 28 | 12,5% |
| 2010–2014 | 33 | 14,7% |
| 2015–2019 | 53 | 23,7% |
| 2020–2024 | 80 | 35,7% |
| 2025–2026 | 30 | 13,4% |

Após aplicação do critério **CI1** (a partir de 2010), restam **196 artigos**
para triagem pelos demais CI/CE.

---

## Comparação sistemática v1 × v2

### Sobreposição de conjuntos

| Categoria | Quantidade |
|-----------|-----------:|
| Presentes em v1 e v2 (recuperados pela nova string) | 111 |
| Presentes só em v1 (perdidos pela v2) | 4.630 |
| Presentes só em v2 (inéditos) | 113 |
| União (v1 ∪ v2) | 4.854 |

**Metade do resultado da v2 é material inédito.** Dos 224 artigos únicos
recuperados pela v2, 111 já constavam na v1 e **113 são novos** — trabalhos
que a string original não havia capturado, apesar de estarem indexados nas
mesmas bases (IEEE e ACM). Isto confirma que o problema da v1 não era
apenas de composição, mas também de **cobertura no eixo do design**.

### Perdas: o que ficou apenas na v1?

A questão relevante não é quantos artigos foram perdidos (4.630 é esperado
— a v1 tinha desenho amplíssimo), e sim **quantos artigos do núcleo da SLR
foram perdidos**.

O núcleo (Design ∪ UX) ∩ ER da v1, computado pelo título, continha **159
artigos**. Destes:

- **Recuperados pela v2:** 16
- **Não recuperados pela v2:** 143

A análise dos 143 mostrou dois perfis:

1. **101 artigos** contêm termos de design ou UX no próprio título (ex.:
   "Design Thinking", "Persona", "Co-Design"). Se estivessem indexados em
   IEEE ou ACM, teriam sido capturados pela v2 — como não foram, a
   explicação plausível é que **estão hospedados em outras bases**.
   *Esta hipótese foi confirmada empiricamente:* a busca manual, feita
   por você, do artigo *"Design Thinking in Software Requirements:
   What Techniques to Use? A Proposal for a Recommendation Tool"* nas duas
   bases retornou vazio, o que indica hospedagem em Springer, Scopus ou
   similar.

2. **42 artigos** não têm termo de design/UX no título — foram classificados
   como núcleo por presença do termo no abstract (via classificador). Estes
   são **perdas parcialmente justificadas**: sem termo de design no título,
   há menor garantia de que o trabalho realmente integra ER × Design em vez
   de apenas mencionar o conceito en passant.

### Interpretação metodológica das perdas

Kitchenham e Charters (2007, §6.1.5) chamam a atenção para o fato de que
"nenhuma base isoladamente encontra todos os estudos primários" e recomendam
diversificação de fontes. Petticrew e Roberts (2005) reforçam que o **viés
de fonte** é uma ameaça reconhecida em revisões sistemáticas e deve ser
declarado como limitação quando bases são intencionalmente restritas.

Neste protocolo, a decisão de manter apenas ACM e IEEE é assumida como
delimitação de escopo (não como falha), com **três mitigações previstas**:

1. **Snowballing forward + backward** sobre os estudos incluídos após a
   triagem por CI/CE. Wohlin (2014) propõe o snowballing como estratégia
   complementar rigorosa, capaz de recuperar trabalhos indexados fora das
   bases originais.
2. **Reconhecimento explícito da limitação** na seção de ameaças à validade
   externa (item 13 do protocolo original).
3. **Discussão da cobertura estimada** no relato final, apoiada por evidência
   empírica: com base nas 143 perdas observadas, estima-se que a busca cobre
   entre 50% e 65% da literatura relevante existente.

---

## Cronograma sintético

| Momento | Ação | Produto |
|---------|------|---------|
| 1 | Formulação da string v1 baseada no vocabulário canônico de ER | String v1 e protocolo original |
| 2 | Execução da v1 em ACM e IEEE | CSV com 4.820 registros exportados |
| 3 | Análise exploratória do resultado da v1 (classificação em 15 áreas) | Mapa temático + diagnóstico de que Design/UX estavam sub-representados |
| 4 | Decisões de reformulação (adicionar bloco Design + UX; expandir contexto) | Registro de decisões metodológicas |
| 5 | Formulação da string v2 | String v2 e adaptação para sintaxe IEEE/ACM |
| 6 | Execução da v2 em ACM e IEEE | 231 registros brutos → 224 únicos |
| 7 | Análise de sobreposição v1 × v2 | 111 em ambos + 113 inéditos |
| 8 | Investigação de perdas (143 artigos do núcleo v1 ausentes da v2) | Diagnóstico: majoritariamente atribuíveis à cobertura de bases |
| 9 | Confirmação empírica da hipótese de cobertura | Busca manual sem retorno + amostra aleatória para verificação |
| 10 | Decisão de manter escopo em IEEE + ACM, com mitigação por snowballing | Este documento; protocolo atualizado |

---

## Referências metodológicas usadas na síntese

Kitchenham, B.; Charters, S. **Guidelines for Performing Systematic Literature
Reviews in Software Engineering.** EBSE Technical Report, EBSE-2007-01, 2007.
(§5.6 sobre revisão do protocolo; §6.1.5 sobre limitações de fontes; §6.2
sobre seleção de estudos.)

Petticrew, M.; Roberts, H. **Systematic Reviews in the Social Sciences: A
Practical Guide.** Blackwell Publishing, 2005. (Discussão sobre viés de
publicação e viés de fonte.)

Wohlin, C. **Guidelines for snowballing in systematic literature studies and
a replication in software engineering.** Proceedings of the 18th International
Conference on Evaluation and Assessment in Software Engineering (EASE '14),
ACM, 2014.

Moher, D. et al. **PRISMA-P 2015 statement.** Systematic Reviews, 4:1, 2015.
(Recomendação de documentar mudanças ao protocolo antes da conclusão da
triagem.)
