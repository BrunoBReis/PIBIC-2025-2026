# RSL: Engenharia de Requisitos × abordagens de design

Revisão sistemática da literatura sobre as interações entre a Engenharia de
Requisitos (ER) e as abordagens de design de serviços e produtos no
desenvolvimento de software e soluções digitais. Iniciação Científica
(ProIC/UnB, 2025/2026), Faculdade de Ciências e Tecnologias em Engenharia,
Universidade de Brasília.

Autor: Bruno Bragança dos Reis · Orientador: Prof. Dr. George Marsicano Correa

A revisão está concluída: 28 estudos primários, recuperados na IEEE Xplore e na
ACM Digital Library, sintetizados em cinco questões de pesquisa. Este
repositório guarda a evidência que sustenta o relatório, de modo que cada número
do texto possa ser conferido na sua fonte.

## O que está aqui

```txt
.
├── protocolo/   o protocolo predefinido (PICOC, RQs, CI/CE, QA) e a síntese das atividades de ER
└── dados/       a evidência, uma pasta por fase da RSL, com as planilhas em dados/5_sintese/
```

Comece por [`dados/README.md`](dados/README.md): ele lista as planilhas e mapeia
cada tabela e figura do relatório à fonte de onde os números saíram. As decisões
que a leitura direta dos arquivos não explica sozinha, a conciliação do funil, a
base de recuperação de cada estudo estão em
[`dados/NOTAS_METODOLOGICAS.md`](dados/NOTAS_METODOLOGICAS.md).

## O que não está aqui

O relatório final, o resumo submetido ao Congresso de Iniciação Científica e o
material de escrita que os produziu não são publicados. Os PDFs dos 28 estudos
também não, por direito autoral e `dados/4_extracao/referencias_28.bib` traz o
DOI de cada um.

Isso não impede a conferência: as planilhas de `dados/5_sintese/` reproduzem
todas as tabelas e figuras do relatório, as fichas de
`dados/4_extracao/extraction/` ancoram cada afirmação em seção e página, e o
script que gera as planilhas roda a partir deste repositório.

## O funil

Busca final em 08/05/2026, **235 registros** (163 na IEEE Xplore, 72 na ACM DL).

| Etapa | Saem | Restam |
| --- | ---: | ---: |
| Remoção antes da triagem (4 contêineres de anais, 7 duplicatas) | 11 | 224 |
| Triagem por título e resumo | 144 | 80 |
| Elegibilidade em texto completo | 40 | 40 |
| Avaliação de qualidade (corte 6,5 de 8,0) | 8 | 32 |
| Reaplicação dos critérios durante a extração | 4 | **28** |

Não houve estudo não recuperado: todos os textos completos foram obtidos.
Os 28 finais são 15 recuperados via IEEE Xplore e 13 via ACM DL, publicados
entre 2010 e 2025. O detalhamento por critério está em
`dados/5_sintese/exclusoes_por_criterio.csv`, e a conciliação do funil, na §1 de
`dados/NOTAS_METODOLOGICAS.md`.

## Registro das iterações de seleção

Triagem por título e resumo, em duas passagens sobre os 235 registros. A
segunda corrigiu três decisões da primeira: *An Introduction to Experience
Requirements* (CE7, short paper), *SecondLook: Participatory Design Process to
Create a Phone App that Detects Digital Dating Abuse* (CE3, foco no produto) e
*Visual Requirements Specification and Automated Test Generation for Digital
Applications* (CE3, foco em geração de testes). Resultado: 80 estudos para
leitura em texto completo.

Elegibilidade e qualidade, em três passagens. A primeira levou 80 a 40. A
segunda aplicou o corte de qualidade de **6,5**, acordado com o orientador, e
excluiu oito (E08, E19, E22, E26, E30, E48, E53, E54; ver
`dados/3_qualidade/pt2_pt3/resultado.csv`). A terceira, já durante a extração,
removeu quatro que a leitura integral revelou inelegíveis: três short papers
(CE7) e um fora do escopo de software (CE4), todos com nota entre 7,0 e 7,5.
A Tabela V do relatório nomeia os doze avaliados que não entraram na síntese.

## Condução

Revisão de revisor único, com apoio de um modelo de linguagem (Claude,
Anthropic) na triagem, na avaliação de qualidade e na extração, sempre por
prompts padronizados e arquivados (`dados/3_qualidade/prompt.md` e
`dados/4_extracao/prompt.md`). Todas as decisões foram revisadas pelo autor. A
limitação está declarada nas ameaças à validade do relatório, junto com o
recorte a duas bases e o *snowballing* previsto e não executado.

## Regerar as planilhas

As planilhas de `dados/5_sintese/` são derivadas; nenhuma é editada à mão.
Depois de qualquer mudança na codificação:

```sh
python3 dados/5_sintese/gerar_planilhas.py
```

O script confere os agregados contra os números publicados no relatório e falha
se algum divergir, de modo que uma planilha desatualizada não passa em silêncio.
