# Categorização C3–C5 — abordagens, frameworks, benefícios e limitações

> Arquivo de rastreabilidade entre as fichas de extração (`extraction/E*.md`) e as
> tabelas C3, C4, C5 e de caracterização do corpus do relatório.
> Cada classificação abaixo deriva dos campos 2, 4–9 e 12 das fichas
> (leitura integral em 2026-08-16). Toda mudança nas tabelas do relatório deve
> passar por aqui primeiro.

## Convenções de categorização

**Abordagens de design** (multi-rótulo; segue a nomenclatura entre colchetes das
próprias fichas): DT = Design Thinking; UCD = UCD/HCD (inclui activity-centered
design e Agile-UCD); PD = Participatory Design (inclui design semioparticipativo,
Design Socialmente Consciente/DSC, SAwD e participatory sensing); CoD =
Co-Design; UX = UX Design (inclui proto-persona/Lean UX e ER orientada a
emoções).  *Rótulos revistos em 2026-08-23 — ver justificativa abaixo.*

**Atividades de ER** (multi-rótulo, códigos brutos da 1ª codificação): Eli =
elicitação/descoberta; Aná = análise/refinamento; Esp =
especificação/documentação/modelagem; Val = validação/verificação; Pri =
priorização; Ges = gestão/rastreamento.

> **Recodificação em 5 etapas (2026-08-20).** Por decisão do autor (feedback
> do orientador), o relatório adota a nomenclatura de **5 etapas de ER** do
> documento `../../protocolo/sintese_etapas_engenharia_requisitos.md`
> (SWEBOK v3.0 + ISO/IEC/IEEE 29148:2018 + Pohl 2010): **Elicitação,
> Análise, Especificação/Documentação, Validação e Gestão (transversal)**.
> Regra de mapeamento: `Pri` é absorvida em `Aná` (no SWEBOK, análise inclui
> negociação e priorização), calculada por estudo como Aná′ = Aná ∪ Pri.
> A tabela mestra abaixo preserva os códigos brutos; as tabelas do relatório
> (C3/Tabela VI e C4/Tabela VII) usam as 5 etapas.

> **Justificativa dos rótulos compostos (registrada em 2026-08-23, a pedido do
> autor).** Os três agrupamentos eram declarados sem argumento. Varredura das 28
> fichas:
> - **UCD/HCD.** Nenhum estudo do corpus define, contrasta ou declara equivalência
>   entre *user-centred* e *human-centred*, e **nenhum cita a ISO 9241-210** (a
>   única norma citada no corpus é a ISO/IEC/IEEE 29148, em E21). Cada estudo
>   adota um só rótulo: HCD em E01, E09, E45; UCD em E12, E27, E38, E51, E75
>   (E46 alterna entre "UCD" e "design thinking activity" sem distinguir os
>   conceitos, campo 11). Só E45 nomeia os dois, e como itens paralelos de uma
>   lista. **A fusão é, portanto, decisão de codificação do revisor**, adotada
>   para preservar a comparabilidade — não um achado dos estudos. Deve ser
>   declarada como tal no relatório e nas ameaças à validade de construto.
> - **Co-Design.** O rótulo era "Co-Design/Co-Creation", mas **"co-creation" não é
>   termo de nenhum autor do corpus**: aparece só como rótulo do extrator sobre o
>   "co-production" de E02, e como fala de participante em E74. "Co-design" é
>   termo de autor em E43, E51 e E63. Nenhuma ficha cita Sanders & Stappers nem
>   distingue os dois conceitos. **Rótulo reduzido para "Co-Design" em
>   2026-08-23.**
> - **UX Design.** O rótulo era "UX/Lean UX (incl. emoções)". Lean UX aparece
>   **só em E67**, e ali como filiação bibliográfica do template de proto-persona
>   (Gothelf & Seiden), não como método do estudo; E72, o outro membro da
>   categoria, **não declara filiação a abordagem de design alguma** (a própria
>   ficha alerta para isso no campo 11). Nenhuma ficha compara UX e Lean UX.
>   **Rótulo reduzido para "UX Design" em 2026-08-23.**

**Tipo de proposta (RQ4)**: A = modelo/framework/processo de integração proposto;
B = técnica/artefato específico proposto; C = catálogo/apoio à seleção de
técnicas; D = aplicação/avaliação de abordagem existente (sem proposta nova).

**Grau de evidência dos benefícios** (campo 7): EE = evidenciado empiricamente;
RP = relatado por participantes; SA = afirmado sem evidência.

## Tabela mestra (28 estudos)

| ID | Abordagens | Atividades ER | Tipo | Proposta/prática central | Avaliação empírica | Domínio | Contexto |
|----|-----------|---------------|------|--------------------------|--------------------|---------|----------|
| E01 | UCD | Eli, Aná, Esp, Val, Pri | A | Modelo activity-centered de 4 estágios + extensão do nested model | Retrospectiva comparativa (75 projetos) | Visualização científica | Acadêmico |
| E02 | DT, CoD | Eli, Aná, Esp, Val, Ges | A | Connected Health Innovation Framework (DT como pré-fase da ER) | Caso único, sem medição | Saúde | Industrial |
| E09 | UCD | Eli, Esp, Val, Ges | D | ER ágil em 5 etapas com prototipação HCD | Caso industrial com indicadores | Governo/e-gov | Industrial |
| E12 | UCD | Aná, Esp | A | Método de análise por padrões de usabilidade (UML estendida) | Avaliação exploratória (10 especialistas) | Genérico (móvel) | Acadêmico |
| E21 | DT | Eli, Aná | B | Técnicas IoThinking e Mind IoT | Experimento controlado (crossover, 59 estudantes) | IoT | Acadêmico |
| E23 | DT | Eli | D | 5 técnicas de DT na elicitação IoT | Estudo experimental (23 participantes) | IoT/Smart Home | Acadêmico |
| E25 | PD | Eli, Aná, Pri, Val | D | Participatory design (3 estágios de Spinuzzi) + RITE | Caso com 19 clínicos + SUS | Saúde | Campo |
| E27 | UCD | Eli, Aná | A | Framework DSR de requisitos orientado a usabilidade | Caso de campo com medições | Agricultura | Campo |
| E29 | DT | Eli, Esp | A | PRO-RE-DT (empatia interna/externa; Vision Canvas + Empathy Map) | Quase-experimento (33 equipes, 23–28 analisadas) | Serviços (adoção de animais) | Acadêmico |
| E32 | PD | Eli, Esp | A | DSC semioparticipativo + árvore metodológica | Caso único (oficinas) | Educação (jogo) | Acadêmico |
| E36 | DT | Eli | C | Universo de Seleção × DTA4RE (seleção de técnicas) | Experimento (acurácia) | Genérico | Acadêmico |
| E38 | UCD | Aná, Esp, Val, Pri | A | User Objectives + diagramas (ágil-UCD) | Sem avaliação | Genérico (web/móvel) | Acadêmico |
| E40 | DT | Eli, Esp | D | DT (4 imersões) em programa de intraempreendedorismo | Pesquisa-ação (2 ciclos) | Indústria de software | Industrial |
| E43 | PD, CoD | Eli, Esp, Val | A | Conflict Sensitive Design (6 fases, workshops separados) | Caso real (workshops) | Segurança pública | Campo |
| E45 | UCD | Eli, Aná, Pri, Ges | C | Catálogo de 41 padrões de ER ágil (agileRE.org) | RSL + painel Delphi (padrões não avaliados) | Genérico ágil | Industrial |
| E46 | UCD, DT | Eli, Pri, Val | B | Triangulação RSL + survey crowdsourcing + atividade de design | Caso único | Energia residencial | Acadêmico |
| E47 | DT | Eli, Aná, Esp, Val, Pri, Ges | A | Framework DT–Scrum para gestão da ER | Sem avaliação | Genérico ágil | Acadêmico |
| E51 | CoD, UCD | Eli, Esp, Val, Pri | D | Co-design + DSR multipaís (protótipo como especificação) | Validação de campo (4 países, 36 participantes) | Saúde (mHealth) | Campo |
| E57 | DT | Eli | C | Tabelas comparativas SADT de 27 técnicas de DT | Estudo de viabilidade | Genérico | Misto |
| E58 | PD | Eli, Esp | B | Grupos focais em díade + storytelling → casos de uso | Aplicação (2 grupos focais) | Saúde (demência) | Campo |
| E63 | PD | Eli, Esp | A | Arquitetura PD–PS em camadas + ciclo 4Co-Ds | Sem avaliação | Smart city/e-gov | Campo |
| E64 | PD | Eli, Esp | A | Processo de workshop SAwD (Stakeholder Diagram → Escada Semiótica) | Caso único (workshop) | Educação (RPG) | Acadêmico |
| E67 | UX | Eli, Esp | B | Template de proto-persona adaptado (Lean UX) | Experimento (13 participantes) | Educação (m-learning) | Acadêmico |
| E70 | DT, PD | Eli, Aná, Ges | A | DivingBoard (DT físico) no framework ágil Speedplay | Estudo de caso único (9 meses, comunidade real) | Energia/sustentabilidade | Campo |
| E72 | UX | Eli, Aná, Esp | B | Metamodelo de requisitos emocionais + mapeamento GRL | Demonstração (5 usuários) | Saúde (clínicas virtuais) | Industrial |
| E74 | DT | Eli, Esp | D | Percepções de DT na ER (survey 158 + 39 em grupos focais) | Survey (158) + grupos focais (39) | Genérico ágil | Industrial |
| E75 | UCD | Eli, Aná, Esp, Val | A | Ciclo UCD de 5 fases com cenários encenados (casa de bonecas) | Protótipo avaliado por 5 geriatras (cenários validados por cuidadores) | Saúde (smart home) | Acadêmico |
| E79 | DT | Eli, Aná, Esp, Pri | A | Parallel micro-crowd RE (DT em quadros online) | Execução única (Jam week, 700 alunos) | Social (solidão) | Acadêmico |

Notas de classificação:
- E01: "activity-centered design" tratado pela ficha como família HCD → UCD.
- E32/E64: DSC e SAwD classificados como PD (design semioparticipativo, conforme
  campo 12 das fichas).
- E43: ficha aponta base em VSD + participatory design + design justice → PD, CoD.
- E45: aborda HCD como componente da ER ágil; DT/PD/Co-Design aparecem apenas
  como itens do catálogo → só UCD.
- E72: ER orientada a emoções com think-aloud/modelo circumplexo — a ficha marca
  RQ2 como "responde parcialmente"; classificado em UX (interface com experiência
  do usuário).
- E12/E38 sem "Eli": os métodos partem de insumos já elicitados (user stories,
  desejos do usuário) e atuam da análise em diante.
- **E43 e E63 (nota acrescentada em 2026-08-23).** O campo 10 (RQ2) de E43 nomeia
  também *design thinking*, e o de E63 nomeia também *human centred design*. A
  regra aplicada conta as abordagens que **estruturam** o trabalho, conforme o
  campo 12 ("a combinação de VSD, participatory design e design justice como base
  de uma proposta de co-design", em E43; "a combinação participatory design com
  participatory sensing", em E63), e não as citadas de passagem no referencial.
  Se a regra fosse "toda abordagem nomeada", os totais passariam a DT 13, UCD 10
  e 35 atribuições.
- **E67 (nota acrescentada em 2026-08-23).** O rótulo da ficha é
  `[UCD/UX Design, com filiação declarada ao Lean UX]` — o único do corpus que
  cruza duas famílias. Classificado só em UX porque o objeto do estudo é a
  proto-persona como técnica de UX, e não um ciclo UCD; o componente UCD do
  rótulo é herança da linhagem da técnica, não da metodologia aplicada.

## C3 — Frequência das abordagens × etapas de ER (derivada da tabela mestra)

**Versão em 5 etapas (2026-08-20, usada na Tabela VI do relatório).**
Aná′ = Aná ∪ Pri por estudo. Conferência da fusão: estudos com Pri e sem
Aná = E46 (DT e UCD), E51 (CoD e UCD); os demais estudos com Pri (E01, E25,
E38, E45, E47, E79) já tinham Aná.

| Abordagem | Estudos | n | Eli | Aná′ | Esp | Val | Ges |
|-----------|---------|---|-----|------|-----|-----|-----|
| Design Thinking | E02 E21 E23 E29 E36 E40 E46 E47 E57 E70 E74 E79 | 12 | 12 | 6 | 6 | 3 | 3 |
| UCD/HCD | E01 E09 E12 E27 E38 E45 E46 E51 E75 | 9 | 7 | 8 | 6 | 6 | 2 |
| Participatory Design | E25 E32 E43 E58 E63 E64 E70 | 7 | 7 | 2 | 5 | 2 | 1 |
| Co-Design | E02 E43 E51 | 3 | 3 | 2 | 3 | 3 | 1 |
| UX Design | E67 E72 | 2 | 2 | 1 | 2 | 0 | 0 |
| **Estudos únicos com a etapa** | — | 28 | 26 | 15 | 19 | 10 | 5 |

(multi-rótulo: 33 atribuições de abordagem para 28 estudos)

Detalhe da fusão por abordagem: DT Aná 5 (E02 E21 E47 E70 E79) ∪ Pri 3
(E46 E47 E79) → 6; UCD Aná 6 (E01 E12 E27 E38 E45 E75) ∪ Pri 5 (E01 E38
E45 E46 E51) → 8; PD Aná 2 (E25 E70) ∪ Pri 1 (E25) → 2; CoD Aná 1 (E02) ∪
Pri 1 (E51) → 2; UX Aná 1 (E72) ∪ Pri 0 → 1. Agregado Aná′: 13 + E46 +
E51 = 15.

<details><summary>Versão anterior (6 atividades, histórico)</summary>

| Abordagem | n | Eli | Aná | Esp | Val | Pri | Ges |
|-----------|---|-----|-----|-----|-----|-----|-----|
| Design Thinking | 12 | 12 | 5 | 6 | 3 | 3 | 3 |
| UCD/HCD | 9 | 7 | 6 | 6 | 6 | 5 | 2 |
| Participatory Design | 7 | 7 | 2 | 5 | 2 | 1 | 1 |
| Co-Design | 3 | 3 | 1 | 3 | 3 | 1 | 1 |
| UX Design | 2 | 2 | 1 | 2 | 0 | 0 | 0 |
| **Total** | 28 | 26 | 13 | 19 | 10 | 8 | 5 |

</details>

## C4 — Grupos da matriz de propostas (RQ4)

- **A — Modelos/frameworks/processos propostos (14):** E01, E02, E12, E27, E29,
  E32, E38, E43, E47, E63, E64, E70, E75, E79.
- **B — Técnicas/artefatos específicos (5):** E21, E46, E58, E67, E72.
- **C — Catálogos/apoio à seleção (3):** E36, E45, E57.
- **D — Aplicações de abordagens existentes (6):** E09, E23, E25, E40, E51, E74.
- Propostas **sem avaliação empírica**: E38, E47, E63 (três dos 14 do grupo A).
- **Avaliação da proposta no grupo A (revisto em 2026-08-23):** dez dos 14 relatam
  avaliação empírica da proposta; **E02** relata o caso que originou o framework
  *sem avaliá-lo* (campo 3: *"o framework é apresentado como produto do caso, sem
  avaliação empírica própria"*); três (E38, E47, E63) não relatam avaliação
  alguma. Não usar mais a contagem "11 de 14".

## C5 — Benefícios por tema e grau de evidência (campo 7)

| Tema | EE | RP | SA |
|------|----|----|----|
| Descoberta de necessidades latentes e compreensão do problema | E25 E72 | E02 E27 E40 E43 E46 E58 E63 E70 E74 | E47 |
| Colaboração, engajamento e comunicação | — | E09 E32 E43 E70 E74 | E02 E12 E45 |
| Produtividade da elicitação (requisitos, stakeholders, ideias) | E23 E29 E64 | E21 E36 E57 | E46 |
| Qualidade do produto, redução de risco e retrabalho | E01 E09 E25 E51 | — | E12 E38 E45 E47 |
| Inclusão de não especialistas e usuários vulneráveis | E67 | E32 E51 | E58 E75 E79 |
| Rastreabilidade e documentação do racional | E79 | — | E38 |

## C5 — Limitações e desafios por tema (campo 8)

| Tema | Estudos |
|------|---------|
| Custo, tempo e esforço de aplicação | E29 E40 E43 E47 E64 E74 E79 |
| Dependência de especialistas/expertise multidisciplinar | E09 E27 E40 E74 |
| Engajamento e disponibilidade de stakeholders | E27 E32 E43 E47 E64 E70 E74 |
| Resistência e cultura organizacional | E40 E74 |
| Inadequação de técnicas genéricas ao domínio | E21 E23 E36 E57 E72 |
| Formalismo, curva de aprendizado e artefatos não lidos | E01 E12 E32 E38 E46 E67 |
| Restrições contextuais (privacidade, regulação, vulnerabilidade) | E25 E43 E51 E58 E63 E70 E75 |
| Evidência empírica limitada das propostas (campo 8/9, transversal) | E02 E38 E45 E46 E47 E63 E67 E79 |

Lacunas recorrentes (campo 9): validação empírica ausente ou insuficiente e
necessidade de estudos comparativos (maioria do corpus); transferência
academia→indústria (E21, E23, E29, E36, E57, E75); escalabilidade e adaptação a
outros domínios (E27, E43, E46, E63, E72).

## C-RQ1 — Configurações de interação ER–design (RQ1)

> Criada em 2026-08-23. **Motivo:** até esta data a RQ1 era a única categorização
> do relatório sem camada de rastreabilidade. A Figura 4 do relatório declarava
> no cabeçalho `estudos exemplares = os citados na prosa da RQ1`, e a prosa havia
> sido montada a partir da linha "Participatory Design" da C3 — isto é, pela
> **abordagem de design**, e não pela **forma de articulação** (campo 5), que é o
> critério declarado da RQ1. Três dos seis estudos da configuração colaborativa
> estavam classificados errado (E25, E58, E64) e dois que pertencem a ela estavam
> ausentes (E70, E79).

**Regra de codificação.** A configuração é a que a **primeira frase do campo 5**
declara ("O padrão é…", "A integração é…", "A articulação é…"); os rótulos
secundários da mesma frase valem como atribuições adicionais. As configurações
**não são mutuamente exclusivas**: a maioria dos estudos recebe duas ou três.
Atribuições marcadas com † são inferência do revisor (não há rótulo literal na
ficha); as marcadas com ‡ são inferência já registrada como `[INFERÊNCIA]` pela
própria ficha.

**Configurações:** Seq = sequencial (o design opera como fase anterior à ER,
alimentando-a); Ite = iterativa (design e ER intercalados em ciclos, sem
precedência fixa); Col = colaborativa (a ER acontece dentro da atividade
participativa; requisitos emergem da interação direta com usuários e
comunidades); Art = por artefatos compartilhados (um artefato acumula função de
design e de especificação).

| ID | Seq | Ite | Col | Art | Trecho literal do campo 5 (primeira frase) |
|----|:---:|:---:|:---:|:---:|--------------------------------------------|
| E01 |   | x |   |   | "A articulação é **simultânea e iterativa**, com a ER embutida no processo de design" |
| E02 | x |   |   |   | "A integração é **sequencial e a montante da ER**: o Design Thinking é adotado como um novo estágio de pré-levantamento de requisitos" |
| E09 |   | x | x | x | "A integração é **iterativa e colaborativa por artefatos compartilhados**, com o protótipo operando como artefato-ponte" |
| E12 | x |   |   | x | "A integração se dá **por artefatos compartilhados** […] O padrão é **sequencial** em duas atividades encadeadas" |
| E21 | x |   |   | x | "O padrão de integração é **sequencial e por artefato compartilhado**" |
| E23 | x‡ |   |   | x‡ | "[INFERÊNCIA] O padrão é **sequencial e mediado por artefatos compartilhados**" |
| E25 |   | x | | x† | "O padrão é **simultâneo e iterativo por prototipação**: a análise de requisitos não antecede o design, mas é executada dentro dele" |
| E27 |   | x |   | x | "A integração é **iterativa e cíclica, mediada por artefatos compartilhados**" |
| E29 | x |   |   | x | "A articulação é **sequencial e por artefatos encadeados**" |
| E32 |   |   | x | x | "A integração é **colaborativa e mediada por artefatos compartilhados** […] a elicitação de requisitos não é etapa separada, mas produto das oficinas de design" |
| E36 |   |   |   | x‡ | "[INFERÊNCIA] O padrão é de **integração por artefato compartilhado** de apoio à decisão" |
| E38 |   | x‡ |   | x‡ | "[INFERÊNCIA] O padrão é **iterativo e por artefato compartilhado**" |
| E40 | x‡ | x‡ |   | x‡ | "[INFERÊNCIA] O padrão é **sequencial por fases, com iteração** entre os dois ciclos de pesquisa-ação e **ancoragem em artefatos compartilhados**" |
| E43 |   | x | x | x | "O padrão é **iterativo e colaborativo por artefatos compartilhados**, com colaboração deliberadamente não colocada" |
| E45 |   | x‡ | x‡ | x‡ | "[INFERÊNCIA] O padrão de integração é **colaborativo e por artefatos compartilhados, com caráter iterativo**" |
| E46 | x |   |   |   | "A integração é **sequencial e cumulativa**, em cadeia de três etapas cujas saídas alimentam a etapa seguinte" |
| E47 | x | x |   |   | "A integração é **sequencial-iterativa** por posicionamento de fase […] e depois retorna ciclicamente a cada Sprint" |
| E51 |   | x | x | x | "O padrão é **iterativo e colaborativo**, com o protótipo funcionando como **artefato compartilhado** de elicitação" |
| E57 |   |   |   | x | "A integração é **por artefatos compartilhados** e ocorre em nível meta" |
| E58 | x‡ |   |   | x‡ | "[INFERÊNCIA] O padrão é **sequencial e por artefatos compartilhados** […] sem retorno documentado dos casos de uso aos participantes" |
| E63 |   | x | x |   | "A integração é **colaborativa e iterativa** por ciclos de co-design" |
| E64 | x |   |   | x | "A integração é **sequencial e por artefatos encadeados** dentro de um único workshop semiparticipativo" |
| E67 |   |   |   | x | "A integração é **por artefato compartilhado**: a proto-persona […] opera como instrumento de elicitação e registro de requisitos" |
| E70 |   | x | x | x | "O padrão é **iterativo e colaborativo, com integração por artefatos compartilhados**" |
| E72 | x‡ |   |   | x‡ | "A articulação é **sequencial e mediada por artefatos compartilhados** [INFERÊNCIA, com base na ordem descrita em *goal modeling is the next step after eliciting*]" |
| E74 |   |   | x |   | "O padrão descrito é **colaborativo** e de suporte: o Design Thinking […] opera como camada de compreensão do problema que alimenta as atividades de ER" |
| E75 | x | x |   |   | "O padrão é **sequencial em fases com validação iterativa** nos estágios iniciais" |
| E79 |   |   | x | x | "A integração é **colaborativa e mediada por artefatos compartilhados**: o DT não antecede a ER, ele é o próprio veículo em que a ER acontece" |
| **Total** | **12** | **13** | **9** | **21** | 55 atribuições para 28 estudos |

**Composição por configuração:**

- **Sequencial (12):** E02, E12, E21, E23, E29, E40, E46, E47, E58, E64, E72, E75.
- **Iterativa (13):** E01, E09, E25, E27, E38, E40, E43, E45, E47, E51, E63, E70, E75.
- **Colaborativa (9):** E09, E32, E43, E45, E51, E63, E70, E74, E79.
- **Por artefatos compartilhados (21):** E09, E12, E21, E23, E25, E27, E29, E32,
  E36, E38, E40, E43, E45, E51, E57, E58, E64, E67, E70, E72, E79 (E25 por
  inferência do revisor; os demais com rótulo literal na ficha).

**Estudos exemplares usados na Figura 4 do relatório** (a figura ilustra, não
enumera; a classificação completa é a tabela acima):

- (a) Sequencial: E02, E29, E40, E46.
- (b) Iterativa: E01, E09, E25, E27, E47.
- (c) Colaborativa: E32, E43, E63, E70, E79.
- (d) Por artefatos compartilhados: E51, E58, E67, E72 (cada um com um tipo
  distinto de artefato: protótipo, narrativa, proto-persona, metamodelo).

**Notas de codificação:**

- **E25 (correção de 2026-08-23).** Estava em "colaborativa" por ser Participatory
  Design. O campo 5 o classifica como **iterativo por prototipação**, e o campo 8
  registra que *"a imersão no trabalho prevista pelo participatory design foi
  inviabilizada pelo sigilo médico-paciente, e a observação de visitas
  domiciliares reais teve de ser substituída por entrevistas no consultório"* —
  não houve workshop no estudo. A atribuição a Art é inferência do revisor: o
  campo 5 diz "por prototipação" e o campo 6 confirma o protótipo como veículo do
  ciclo de feedback, mas a ficha não usa o rótulo "artefato compartilhado".
- **E58 (correção).** Estava em "colaborativa"; o campo 5 o classifica como
  sequencial + por artefatos ("fluxo unidirecional […] sem retorno documentado
  dos casos de uso aos participantes"). Permanece em (d), onde já estava.
- **E64 (correção).** Estava em "colaborativa"; o campo 5 diz "sequencial e por
  artefatos encadeados". Atenuante registrado: ocorre dentro de um workshop
  semiparticipativo real, mas o padrão de articulação declarado não é
  colaborativo.
- **E43.** Recebe Col porque o campo 5 usa o rótulo literal, mas com ressalva: a
  colaboração é *deliberadamente não colocada* — "os pesquisadores atuam como
  mediadores e transportam os desenhos entre grupos que nunca se encontram".
  É por isso que a legenda do painel (c) não pode prometer "workshops".
- **E74.** Recebe apenas Col, sem Art: a ficha registra que "o artigo não descreve
  quem faz o quê nem em que ordem"; a articulação aparece só pela voz dos
  profissionais nos grupos focais.
- Art é o rótulo mais frequente do corpus (21/28) — é o achado que sustenta a
  frase da 4.2 de que a integração se concentra nos pontos de contato em que
  artefatos de design podem ser convertidos em insumos de requisitos.

### C-RQ1 (dimensional) — reprojeção em três eixos · 2026-08-29

> **Motivo.** Feedback do orientador (rev. 26/08/2026, p. 8): *"Sequencial e
> iterativa descrevem organização temporal; colaborativa descreve participação; e
> artefatos compartilhados descrevem mecanismo de mediação. Esses elementos não
> pertencem ao mesmo eixo classificatório. Chamá-los de quatro configurações
> equivalentes gera sobreposição conceitual e explica por que um estudo recebe
> duas ou três categorias."* A crítica procede: as 55 atribuições para 28 estudos
> da tabela acima são efeito de mistura de eixos, não de riqueza do fenômeno.
>
> **A tabela original acima permanece intocada como histórico e como fonte.** Esta
> seção é uma *reprojeção determinística* dela — nenhuma ficha foi relida, nenhuma
> atribuição foi revista. Toda mudança de codificação continua devendo ser feita na
> tabela mestra acima, e esta seção, recalculada a partir dela.

**Regra de projeção** (aplicada estudo a estudo sobre as colunas Seq/Ite/Col/Art):

| Eixo | Valores | Derivação |
|---|---|---|
| (a) Temporal | Sequencial / Iterativa / Híbrida / Não explicitada | `Seq ∧ ¬Ite` → Sequencial; `Ite ∧ ¬Seq` → Iterativa; `Seq ∧ Ite` → Híbrida; nenhum → Não explicitada |
| (b) Participação | Colaborativa / Não explicitada | `Col` |
| (c) Mediação | Por artefatos compartilhados / Interação direta | `Art` |

Cada estudo recebe **exatamente um valor por eixo**; cada eixo soma **28**. Acabou a
dupla contagem.

| ID | (a) Temporal | (b) Participação | (c) Mediação |
|----|--------------|------------------|--------------|
| E01 | Iterativa | Não explic. | Interação direta |
| E02 | Sequencial | Não explic. | Interação direta |
| E09 | Iterativa | Colaborativa | Por artefatos |
| E12 | Sequencial | Não explic. | Por artefatos |
| E21 | Sequencial | Não explic. | Por artefatos |
| E23 | Sequencial | Não explic. | Por artefatos |
| E25 | Iterativa | Não explic. | Por artefatos |
| E27 | Iterativa | Não explic. | Por artefatos |
| E29 | Sequencial | Não explic. | Por artefatos |
| E32 | Não explic. | Colaborativa | Por artefatos |
| E36 | Não explic. | Não explic. | Por artefatos |
| E38 | Iterativa | Não explic. | Por artefatos |
| E40 | Híbrida | Não explic. | Por artefatos |
| E43 | Iterativa | Colaborativa | Por artefatos |
| E45 | Iterativa | Colaborativa | Por artefatos |
| E46 | Sequencial | Não explic. | Interação direta |
| E47 | Híbrida | Não explic. | Interação direta |
| E51 | Iterativa | Colaborativa | Por artefatos |
| E57 | Não explic. | Não explic. | Por artefatos |
| E58 | Sequencial | Não explic. | Por artefatos |
| E63 | Iterativa | Colaborativa | Interação direta |
| E64 | Sequencial | Não explic. | Por artefatos |
| E67 | Não explic. | Não explic. | Por artefatos |
| E70 | Iterativa | Colaborativa | Por artefatos |
| E72 | Sequencial | Não explic. | Por artefatos |
| E74 | Não explic. | Colaborativa | Interação direta |
| E75 | Híbrida | Não explic. | Interação direta |
| E79 | Não explic. | Colaborativa | Por artefatos |

**Composição por eixo**

- **(a) Temporal** — Iterativa **10**: E01, E09, E25, E27, E38, E43, E45, E51, E63, E70. Sequencial **9**: E02, E12, E21, E23, E29, E46, E58, E64, E72. Não explicitada **6**: E32, E36, E57, E67, E74, E79. Híbrida **3**: E40, E47, E75.
- **(b) Participação** — Colaborativa **9**: E09, E32, E43, E45, E51, E63, E70, E74, E79. Não explicitada **19**: E01, E02, E12, E21, E23, E25, E27, E29, E36, E38, E40, E46, E47, E57, E58, E64, E67, E72, E75.
- **(c) Mediação** — Por artefatos **21**: E09, E12, E21, E23, E25, E27, E29, E32, E36, E38, E40, E43, E45, E51, E57, E58, E64, E67, E70, E72, E79. Interação direta **7**: E01, E02, E46, E47, E63, E74, E75.

**Achados que a projeção revela e a classificação anterior escondia**

1. **Seis estudos não declaram organização temporal alguma** (E32, E36, E57, E67, E74, E79).
   Na classificação de quatro configurações eles apareciam só em "colaborativa" ou
   "por artefatos", e a ausência de precedência declarada ficava invisível. É um achado
   sobre o relato dos estudos, não sobre o fenômeno: eles descrevem *com quem* e *por
   meio de quê*, mas não *em que ordem*.
2. **Três estudos são híbridos no tempo** (E40, E47, E75): declaram fase sequencial
   com retorno iterativo. Antes contavam duas vezes, uma em cada configuração.
3. **A mediação por artefatos é quase universal** (21/28) e
   **atravessa os três valores temporais** — é o eixo mais estável do corpus e sustenta
   a leitura da 4.2 de que a integração se concentra nos pontos de conversão de
   artefato em requisito.
4. A colaboração (9/28) **não coincide** com a iteratividade:
   dos 10 iterativos, 6 são
   colaborativos (E09, E43, E45, E51, E63, E70); iterar não implica
   participar.

**Reflexo no relatório:** Figura 4 (três painéis) e a coluna `Config.` da Tabela
IX, matriz de evidências (vira três colunas).


## C-RQ3 — Papéis atribuídos à ER nos processos de design colaborativo

> Criada em 2026-08-24, pelo mesmo motivo da C-RQ1: a RQ3 apresentava três
> papéis com dois ou três estudos citados cada, **sem contagem e sem matriz**,
> de modo que o achado não era verificável por um revisor.

**Regra de codificação.** O papel é o que o **campo 10 (RQ3)** declara; quando o
campo 10 apenas registra o status, usa-se o **campo 12** ("Contribuição para as
RQs"). Multi-rótulo: um estudo pode atribuir mais de um papel à ER.

**Papéis:** **Dst** destinatária (a ER recebe os resultados do design como
insumo, ou é absorvida pelo processo de design); **Est** estruturadora (a ER
formaliza ou traduz o material gerado em especificações, modelos e artefatos de
requisitos); **Org** organizadora (a ER ordena o processo, com o design acoplado
aos seus objetivos, fases ou gestão); **Dis** prática coletiva distribuída (a ER
deixa de ser atividade de um analista e passa a ser exercida coletivamente).

| ID | Dst | Est | Org | Dis | Trecho literal (campo 10, salvo indicação) |
|----|:---:|:---:|:---:|:---:|---------------------------------------------|
| E01 |   | x | x |   | "atribui à ER papéis de **estruturadora**, **gate de prototipação**, tradutora de vocabulário e validação antecipada" |
| E02 | x | x |   |   | "a ER aparece como **receptora e tradutora** das necessidades levantadas e como instância de verificação e validação" |
| E09 |   | x |   |   | "a ER aparece como **estruturadora** e como base contratual da comunicação com a contratada" |
| E12 |   | x |   |   | "atribui à análise de requisitos o papel de **tradutora e formalizadora** das tarefas de usuário em funcionalidades" |
| E21 | x |   |   |   | "atribui à ER o papel de **destino do trabalho de design**, com a elicitação recebendo os artefatos" |
| E23 |   |   |   |   | "**RQ3: Não responde.**" — único estudo sem papel discernível |
| E25 | x |   |   |   | "a análise de requisitos aparece como **produto do processo colaborativo**" |
| E27 | x |   |   |   | c.12: "mostrar a ER **distribuída ao longo dos ciclos, realimentada** pela análise de usabilidade" |
| E29 | x | x |   |   | "a ER aparece como **atividade receptora que converte** insights de empatia em histórias de usuário" |
| E32 | x |   |   |   | c.12: "posicionar a ER como **saída do processo de design colaborativo**, e não como disciplina autônoma que o antecede ou governa" |
| E36 | x |   | x |   | "a ER aparece como **atividade demandante que consome** as técnicas de DT" |
| E38 |   | x | x |   | "atribui à especificação de requisitos o papel de **atividade estruturante e de origem dos testes de aceitação**" |
| E40 |   |   |   | x | c.12: "documentar a **transição do papel dos profissionais de receptores de requisitos para descobridores e críticos** das necessidades dos usuários" |
| E43 |   |   | x |   | c.12: "posicionar a coleta de requisitos como **fase estruturante que condiciona a formação de times e o formato dos workshops**" |
| E45 |   |   | x | x | c.12: "**distribuir responsabilidades de requisitos entre papéis ágeis** catalogados como padrões" |
| E46 |   |   | x |   | c.12: "posicionar a ER como **processo guarda-chuva que ordena e absorve as atividades de design**" |
| E47 |   |   | x |   | c.12: "propor um **mapeamento explícito das cinco atividades de ER sobre as etapas do modelo de design**" |
| E51 | x |   |   |   | c.12: "situar a definição de requisitos como **etapa interna do ciclo de design science research**" |
| E57 |   |   | x |   | c.12: "posicionar os **objetivos da ER como critério de classificação das técnicas de design**" |
| E58 | x | x |   |   | "a ER aparece como **destino do material participativo, formalizado em casos de uso**" |
| E63 | x |   |   |   | c.12: "situando a ER como **atividade absorvida pelo co-design**" |
| E64 | x | x |   |   | c.12: "posicionar a ER como **produto terminal da cadeia de artefatos, formalizada** pela Escada Semiótica e pela lista de requisitos" |
| E67 | x | x |   |   | c.12: "posicionar a ER como **consumidora e estruturadora** do conhecimento externo ao time" |
| E70 |   | x |   |   | c.12: "a ER operando como **tradutora** de temas comunitários e feedback informal em mudanças rastreáveis de versão" |
| E72 |   | x |   |   | "a ER aparece como **estruturadora e tradutora**, convertendo relatos emocionais em soft goals" |
| E74 | x |   |   |   | c.12: "situar a ER como **destino do entendimento produzido no DT**" |
| E75 |   | x |   |   | "a ER aparece como **estruturadora**, convertendo cenários e feedback em requisitos funcionais e não funcionais" |
| E79 |   |   |   | x | c.12: "**deslocar a ER de atividade de analista para prática coletiva distribuída** entre desenvolvedores multidisciplinares" |
| **Total** | **13** | **12** | **8** | **3** | 36 atribuições; 27 dos 28 estudos |

**Composição:**

- **Destinatária (13):** E02, E21, E25, E27, E29, E32, E36, E51, E58, E63, E64, E67, E74.
- **Estruturadora (12):** E01, E02, E09, E12, E29, E38, E58, E64, E67, E70, E72, E75.
- **Organizadora (8):** E01, E36, E38, E43, E45, E46, E47, E57.
- **Prática coletiva distribuída (3):** E40, E45, E79.
- **Sem papel discernível (1):** E23 (campo 10: "Não responde").

**Notas:**

- O papel **Dis** não constava da prosa original da 4.2, que falava em "papéis de
  mediação ou liderança" aparecendo "apenas pontualmente". A codificação mostra
  que o que aparece pontualmente é algo mais específico: a ER **deixando de ser
  atividade de um analista** para virar prática coletiva (E40, E45, E79).
- **Dst é o papel mais frequente (13/28)**, o que sustenta quantitativamente a
  observação de que a maioria dos estudos parte da perspectiva do design e trata
  a ER como consequência. **Org**, o papel em que a ER governa o processo,
  aparece em apenas 8 e concentra-se nos estudos que propõem catálogos ou
  frameworks de processo (E43, E45, E46, E47, E57).
- E40 e E79 descrevem um **deslocamento** de papel, não um papel estático; ambos
  foram codificados por onde o deslocamento chega, não por onde parte.

## C-RQ5 — Lacunas declaradas pelos autores (campo 9) · 2026-08-29

> **Motivo.** Feedback do orientador (rev. 26/08/2026, p. 8): *"A pergunta
> reúne lacunas, desafios e limitações, mas a tabela apresenta somente limitações e
> desafios. As lacunas aparecem em um parágrafo, sem estudos de origem, frequência ou
> definição operacional equivalente."* Até aqui as lacunas viviam num parágrafo solto
> ("maioria do corpus", sem IDs). Esta seção lhes dá o mesmo tratamento das demais
> categorizações: tema, contagem e âncora literal por estudo.

**Definição operacional — o que distingue lacuna de limitação.** As duas categorias vêm
de campos diferentes da ficha e têm sujeitos diferentes:

- **Limitação/desafio (campo 8)** — obstáculo *encontrado na execução* do próprio
  estudo ou reconhecido como fraqueza do que foi feito. Sujeito: o trabalho realizado.
- **Lacuna (campo 9)** — o que os autores declaram *faltar e ficar para depois*, seja
  no próprio trabalho, seja no estado da arte. Sujeito: a agenda futura.

Um mesmo tópico pode aparecer nos dois campos com papéis distintos: "evidência empírica
limitada" é limitação quando o estudo admite não ter avaliado sua proposta, e lacuna
quando ele enuncia a avaliação como trabalho futuro.

**Codificação multirrótulo:** 50 atribuições para 26 dos 28 estudos.
**2 estudos não declaram agenda de pesquisa alguma** (E58, E70) — em ambos
a ficha registra a ausência explicitamente, o que é, em si, um dado sobre o relato.

| Tema | Descrição | n | Estudos |
|---|---|---:|---|
| **L1** | Validação empírica da própria proposta ainda pendente | **17** | E02, E09, E12, E25, E27, E29, E36, E45, E46, E47, E51, E57, E63, E64, E67, E74, E75 |
| **L4** | Escalabilidade e adaptação a outros domínios | **10** | E23, E25, E27, E29, E32, E43, E63, E67, E72, E79 |
| **L3** | Transferência para a indústria e para contexto real | **8** | E12, E21, E29, E36, E45, E74, E75, E79 |
| **L6** | Ferramental de apoio ainda por construir | **6** | E09, E36, E38, E45, E47, E57 |
| **L2** | Ausência de estudos comparativos com alternativas | **5** | E09, E32, E40, E47, E64 |
| **L5** | Cobertura incompleta do ciclo de ER | **4** | E01, E02, E38, E72 |

**Atribuição por estudo, com âncora literal do campo 9**

| ID | Temas | Trecho do campo 9 |
|----|-------|-------------------|
| E01 | L5 | "técnicas alternativas como focus groups, questionários e estudo de documentação não são cobertas e permanecem em aberto" |
| E02 | L1 L5 | "planejam testar e validar o framework em outras soluções"; "elicitação, análise, especificação e gestão de requisitos são explicitamente deixadas para pesquisa e desenvolvimento futuros" |
| E09 | L1 L2 L6 | "ampliar a amostra de projetos"; "análise comparativa com projetos que não utilizaram prototipação"; "explorar ferramentas de inteligência artificial" |
| E12 | L1 L3 | "investigar a confiabilidade do método e aplicar verificações e validações pós-implementação em projetos reais" |
| E21 | L3 | "realizar a transferência das técnicas para a indústria" |
| E23 | L4 | "adaptar técnicas baseadas em conceitos de DT às particularidades dos sistemas IoT" |
| E25 | L1 L4 | "estudo de acompanhamento com os clínicos […] para verificar se o design funciona na prática"; "confirmar a aplicabilidade fora da Bélgica" |
| E27 | L1 L4 | "argumentam que o método deveria aumentar o sucesso […] sem apresentar essa verificação"; "outros domínios, como saúde e pesca" |
| E29 | L1 L3 L4 | "validar os achados com amostras maiores"; "em contextos organizacionais diversos"; "adaptar as técnicas a diferentes escalas de projeto e domínios" |
| E32 | L2 L4 | "o projeto pode servir de objeto de comparação com pesquisas futuras"; "aplicar os conceitos e artefatos do DSC na elaboração de outros jogos educacionais" |
| E36 | L1 L3 L6 | "novos estudos experimentais para garantir a qualidade da abordagem"; "visando sua transferência para a indústria"; "concluir a versão web" |
| E38 | L5 L6 | "não há acordo na literatura sobre quando e como incluir práticas de UCD no ciclo de vida ágil"; "construindo uma ferramenta para elaborar automaticamente os diagramas" |
| E40 | L2 | "comparar o DT com outras abordagens […] lean start-up, lean inception e customer development" |
| E43 | L4 | "investigar a escalabilidade e a adaptabilidade do CSD em diferentes contextos sociais, culturais e econômicos" |
| E45 | L1 L3 L6 | "avaliação empírica adicional na indústria"; "integrar ferramentas que apoiem a análise semiautomática de requisitos" |
| E46 | L1 | "avaliá-la a cada estágio com pelo menos 20 a 25 participantes" |
| E47 | L1 L2 L6 | "validar o framework integrado localizando um estudo de caso"; "estudo comparativo de efetividade"; "desenvolver uma Prioritization Tool" |
| E51 | L1 | "as validações das iterações subsequentes informarão a especificação final da plataforma" |
| E57 | L1 L6 | "experimento online em que participantes agrupariam e nomeariam as categorias […] para validar o agrupamento proposto"; "uso de métodos de tomada de decisão multicritério como PROMETHEE" |
| E58 | — | "Nenhuma agenda de pesquisa adicional é apresentada" |
| E63 | L1 L4 | "implementação e validação dos frameworks propostos"; "em cidades urbanas e periurbanas" |
| E64 | L1 L2 | "avaliar e apresentar os resultados do jogo criado"; "identificar vantagens e desvantagens do SAwD em comparação com outros processos" |
| E67 | L1 L4 | "avaliar o uso do artefato e seus efeitos"; "explorar o uso dos resultados em outros domínios de e-learning" |
| E70 | — | "Não relatado; o artigo encerra […] sem enunciar agenda de pesquisa futura" |
| E72 | L4 L5 | "taxonomia de emoções que cubra todas as emoções"; "aprofundar a investigação do vínculo entre requisitos emocionais e os demais tipos de requisitos" |
| E74 | L1 L3 | "investigar a adoção de DT visando avaliar o potencial da abordagem"; "replicar o estudo em outros países e contextos e com número maior de profissionais" |
| E75 | L1 L3 | "instalação do sistema em ambiente real, já que alguns desafios só aparecerão com o sistema implantado" |
| E79 | L3 L4 | "contextos adicionais, tanto educacionais quanto empresariais" |

**Leitura.** O tema dominante é **L1** (17/28): a maioria dos estudos
declara, por conta própria, que sua proposta ainda não foi suficientemente avaliada —
o que converge com a limitação "evidência empírica limitada das propostas" (campo 8, 8
estudos) e com a contagem de sustentação empírica dos benefícios (11 de 43). São três
medidas independentes apontando para o mesmo diagnóstico de campo em fase propositiva.
Em contraste, **L2** (5/28) é raro: poucos autores enunciam a
comparação com alternativas como agenda, ainda que a ausência de comparação seja
justamente o que impede escolher entre propostas concorrentes.

**Reflexo no relatório:** bloco (c) da Tabela X (benefícios, limitações e
lacunas) e prosa da RQ5 na Seção 4.2.

## Pontos discutíveis — fechados em 2026-08-23 (2ª rodada)

A auditoria havia registrado dez pontos como "juízos de codificação, mantidos
como estão". Reexaminados um a um contra as fichas, **sete eram erros**: a ficha
contradiz a tabela. Os três restantes eram juízos de fato, decididos pelo autor.
Todos foram aplicados; nada permanece pendente aqui.

### Erros corrigidos (a ficha contradiz a tabela)

| # | Onde | Estava | Passou a ser | Trecho da ficha |
|---|------|--------|--------------|-----------------|
| 1 | Aval. E12 | "Experimento (10 especialistas)" | "Avaliação exploratória (10 especialistas)" | c.3: *"Proposta de método seguida de exemplo ilustrativo e **avaliação exploratória**"* — sem tratamento, controle nem aleatorização |
| 2 | Aval. E29 | "Quase-experimento (28 equipes)" | "(33 equipes, 23–28 analisadas)" | c.3: *"33 equipes iniciais reduzidas a 23 e 28 conforme a variável"* |
| 3 | Aval. E79 | "Execução única (workshop)" | "Execução única (Jam week, 700 alunos)" | c.3: *"a 'Jam week' de 2021, hackathon-like de quatro dias, com 700 estudantes"* |
| 4 | Aval. E45 | "RSL + painel Delphi + caso" | "RSL + painel Delphi (padrões não avaliados)" | c.3: *"o artigo **não relata avaliação empírica nova dos 41 padrões**"* |
| 5 | E21 em Rastreabilidade · EE | presente | **removido do tema** | O c.7 de E21 **não tem item de rastreabilidade**; ela aparece no c.5 como critério de pontuação do experimento, não como benefício |
| 6 | E21 e E36 em Produtividade · EE | Empírico | **Participantes** | E21 c.7: *"desempenho equivalente […] **sem diferença estatisticamente significativa** (p = 0,379)"* — evidência de equivalência entre dois tratamentos, não de ganho. E36 c.7 mede **acurácia na seleção de técnicas** (75% / 65,56%, p = 0,283) e diz que a conclusão sobre requisitos é *"afirmado sem evidência, pois **nenhum requisito foi de fato elicitado ou avaliado**"*. Os itens RP dos dois são percepção de utilidade |
| 7 | E46 em Produtividade · EE | Empírico | **Sem evidência** | c.7: *"A conclusão de que a combinação de técnicas ajudou efetivamente a identificar os requisitos também é **afirmada sem medição própria**"* |
| 8 | E12 em Qualidade do produto · EE | Empírico | **Sem evidência** | Os itens EE de E12 são de **tempo de modelagem** (2,90 min/tarefa; −45% na reaplicação), que não é qualidade do produto; o item do tema é *"antecipação da gestão de riscos de usabilidade […] **afirmado sem evidência**"* |

> Observação sobre o item 8: o achado de tempo de modelagem de E12 é real e
> empírico, mas não cabe em nenhum dos seis temas — "Produtividade da
> elicitação" não serve porque E12 não atua na elicitação (é um dos dois
> estudos sem `Eli`). Fica registrado aqui e não entra na tabela.

### Juízos decididos pelo autor

- **Graus por "observação dos autores" → alinhados à legenda.** A legenda da
  Tabela IX define *Empírico* como benefício sustentado por medição, comparação
  ou instrumento, e *Participantes* como relatado por participantes **ou
  observado pelos autores, sem medição**. Aplicando-a: **E70** sai de Empírico
  para Participantes (c.7: *"evidenciado empiricamente **por observação dos
  autores**"*) e **E02** sai de Sem evidência para Participantes (c.7:
  *"**relatado pelos autores a partir do caso, sem medição**"*, formulação que a
  própria ficha distingue do *"afirmado sem evidência"* usado nos demais itens
  de E02). **E27** já estava em Participantes e permanece.
- **E58 movido do grupo D para o grupo B.** O c.10 (RQ4) diz que o estudo
  *"**propõe** a prática do grupo focal em díade com storytelling prévio à
  tecnologia, sem formalizá-la como modelo ou framework"* — o que contradiz a
  definição de D ("sem proposta nova") e não chega a A justamente por não ser
  formalizado. Grupos passam a **A 14, B 5, C 3, D 6**.
- **E46, base de recuperação:** sem alteração. O c.1 diz "IEEE Xplore" (carimbo
  do PDF), mas o registro só existe em `artigos_acm.bib`; contado como ACM
  conforme a §2 de `../NOTAS_METODOLOGICAS.md`, que já documenta o caso.

### Efeito agregado na Tabela IX(a)

| Tema | n | Antes (EE/RP/SA) | Depois (EE/RP/SA) |
|------|--:|------------------|-------------------|
| Descoberta de necessidades latentes | 12 | 3 / 7 / 2 | **2 / 9 / 1** |
| Colaboração, engajamento e comunicação | 8 | 0 / 5 / 3 | 0 / 5 / 3 |
| Produtividade da elicitação | 7 | 6 / 1 / 0 | **3 / 3 / 1** |
| Qualidade do produto e redução de risco | 8 | 5 / 0 / 3 | **4 / 0 / 4** |
| Inclusão de não especialistas | 6 | 1 / 2 / 3 | 1 / 2 / 3 |
| Rastreabilidade do racional | 3 → **2** | 2 / 0 / 1 | **1 / 0 / 1** |
| **Total de atribuições** | | **44, 17 empíricas (39%)** | **43, 11 empíricas (26%)** |

Consequências para o relatório: (a) "produtividade da elicitação" **deixa de ser
o tema com maior proporção de evidência empírica** (43%, atrás de qualidade do
produto, 50%) — a frase da Seção 4.1 foi substituída pelo número agregado
(11 de 43); (b) na Seção 4.2, o único experimento com grupo de controle entre os
14 do grupo A passa a ser **E29** (E12 é avaliação exploratória); (c) o achado
reforça, e não enfraquece, a tese do campo em fase propositiva.

## Log de correções de 2026-08-23

Auditoria sistemática das Tabelas IV–IX e das cinco RQs contra as 28 fichas.
Tabelas IV, V, VI, VII e IX(b) recontadas célula a célula **sem divergências**.
Corrigidos:

1. **E74** (tabela mestra): survey com **158** respondentes e **39** nos grupos
   focais; 197 era a soma dos dois métodos (campo 3: *"envio a 466 profissionais
   e 158 respondentes, taxa de 33,9%"*).
2. **E75** (tabela mestra): o protótipo foi avaliado por **cinco geriatras**; os
   cuidadores validaram os *cenários*, etapa anterior (campo 3).
3. **E70** (tabela mestra): **estudo de caso único** de nove meses, não
   pesquisa-ação (o campo 3 não usa o termo; quem é pesquisa-ação é E40).
4. **E21** (tabela mestra): **experimento controlado** com desenho crossover e 59
   estudantes, não quase-experimento (campo 3).
5. **C5 benefícios, "Inclusão"**: E58 estava contado em RP **e** em SA; o campo 7
   registra os dois benefícios de inclusão como *afirmado sem evidência* → fica
   só em SA. E75 movido de RP para SA (campo 7: *"melhor participação e feedback
   mais rico dos cuidadores […] afirmado sem evidência: não há medida ou
   comparação"*).
6. **C5 benefícios**: E45 era o único dos 28 ausente de todo tema de benefício;
   codificado em "Colaboração" (SA, *"tornar a conversa da equipe mais efetiva"*)
   e "Qualidade do produto" (SA, *"melhorar a UX geral"* e *"melhorar seus
   modelos de processo de ER ágil"*).
7. **C5 limitações**: E46, E67 e E70 eram ausentes de todo tema, apesar do campo 8
   substantivo. E46 → Formalismo (*"os paper designs confundiram participantes
   […] exigindo piloto intenso prévio"*) e Evidência limitada (*"o número de
   participantes foi baixo […] impedindo conclusões efetivas"*). E67 → Formalismo
   (*"engenheiros de software relataram dificuldade em usar a técnica"*) e
   Evidência limitada (*"a proto-persona pressupõe validação posterior […] não
   executada"*). E70 → Engajamento (*"a confiança é um obstáculo em comunidades
   pequenas […] risco de não articularem necessidades reais"*) e Restrições
   contextuais (*"banda larga ruim ou ausente criou dificuldades de
   comunicação"*).
8. **Nova seção C-RQ1** (acima): classificação das quatro configurações de
   interação pelo campo 5, que não existia — ver o motivo no cabeçalho da seção.
9. **E02 e a contagem do grupo A**: o campo 3 diz que *"o framework é apresentado
   como produto do caso, **sem avaliação empírica própria**"*. Logo, dos 14 do
   grupo A, **dez** relatam avaliação empírica da proposta, E02 relata o caso sem
   avaliá-la e três (E38, E47, E63) não relatam avaliação alguma. O relatório
   dizia "11 dos 14".

## Caracterização do corpus

- **Domínio de aplicação:** Saúde 6 (E02 E25 E51 E58 E72 E75); Genérico/indústria
  de software 8 (E12 E36 E38 E40 E45 E47 E57 E74); Educação 3 (E32 E64 E67);
  Cidades/governo digital 3 (E09 E43 E63); IoT/Smart Home 2 (E21 E23);
  Energia/sustentabilidade 2 (E46 E70); Agricultura 1 (E27); Visualização
  científica 1 (E01); Social 1 (E79); Serviços 1 (E29).
- **Contexto de condução:** Acadêmico 14 (E01 E12 E21 E23 E29 E32 E36 E38 E46
  E47 E64 E67 E75 E79); Campo/comunidade 7 (E25 E27 E43 E51 E58 E63 E70);
  Industrial 6 (E02 E09 E40 E45 E72 E74); Misto 1 (E57).
- **Base de recuperação:** IEEE 15; ACM 13 (ver §2 de `../NOTAS_METODOLOGICAS.md`).
- **Veículo:** periódico 2 (E01 TVCG; E40 IEEE Software); workshop 5 (E02 E27
  E46 E72 E79); conferência 21 (demais).
