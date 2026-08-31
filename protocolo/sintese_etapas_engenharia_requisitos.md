# Síntese das Etapas da Engenharia de Requisitos

Documento de fundamentação conceitual — base para o esquema de codificação de "Atividades de ER"

---

## 1. Fontes adotadas e por que estas três

As três referências operam em níveis distintos e se complementam, o que é justamente o que permite sustentar um esquema de codificação sem depender de um autor isolado.

**ISO/IEC/IEEE 29148:2018** é a fonte **normativa**. Não descreve "etapas" como fases sequenciais, mas define *processos de ciclo de vida* — principalmente o processo de Definição de Requisitos de Stakeholders e o processo de Definição de Requisitos de Sistema/Software — cada um com atividades e tarefas prescritas. É a referência mais forte para afirmar o que a ER deve produzir e com quais características.

**SWEBOK Guide (v3.0, 2014), KA 1 — Software Requirements** é a fonte de **consenso da área**. Organiza o conhecimento em subáreas que funcionam como a taxonomia mais citada em Engenharia de Software: *Requirements Elicitation*, *Requirements Analysis*, *Requirements Specification*, *Requirements Validation*, além de *Requirements Process* e *Practical Considerations*. É a taxonomia mais próxima do vocabulário usado na literatura primária que será triada na RSL.

**POHL (2010)** é a fonte **conceitual**. É o único dos três que oferece uma teoria explicativa do *porquê* das atividades, e não apenas sua enumeração. Fundamenta o corpo de conhecimento do IREB e é a base mais adequada para justificar decisões de categorização.

---

## 2. O enquadramento conceitual de Pohl: as três dimensões

Antes de listar etapas, é útil entender o modelo que Pohl propõe, porque ele explica por que as atividades existem. Segundo o autor, todo processo de ER busca reduzir a opacidade em **três dimensões** simultâneas:

| Dimensão | Estado inicial | Estado desejado | Atividade que a endereça |
|---|---|---|---|
| **Conteúdo** (*content*) | Não se sabe quais são os requisitos | Requisitos conhecidos e compreendidos | Elicitação |
| **Documentação** (*documentation*) | Requisitos não registrados ou registrados de forma inadequada | Requisitos documentados conforme regras e formatos definidos | Documentação / Especificação |
| **Acordo** (*agreement*) | Stakeholders divergem sobre os requisitos | Consenso estabelecido entre as partes | Negociação |

A **validação** atravessa as três dimensões — verifica se cada uma atingiu o estado desejado. A **gestão** é transversal ao processo inteiro. Esse modelo explica um ponto importante para a RSL: *documentar não é registrar o que foi elicitado*. São dimensões independentes, e um projeto pode avançar em uma sem avançar nas outras.

---

## 3. As etapas

### 3.1 Elicitação

**O que é.** A atividade de identificar fontes de requisitos e delas extrair, descobrir e desenvolver os requisitos do sistema. O termo "elicitar" é preferido a "coletar" ou "levantar" precisamente porque requisitos raramente estão prontos esperando para serem apanhados: em boa parte dos casos precisam ser construídos em conjunto com os stakeholders, que frequentemente não sabem articular o que precisam.

**O que se faz.** Identificação e caracterização de stakeholders; identificação de fontes de requisitos além de pessoas (documentos, legislação, sistemas legados, o próprio domínio); definição do contexto e das fronteiras do sistema; aplicação de técnicas de elicitação. Pohl classifica as técnicas em quatro grupos: de levantamento (entrevistas, questionários), de apoio criativo (brainstorming, analogias), de apoio à documentação (análise de sistemas existentes, perspective-based reading) e de observação (etnografia, apprenticing).

**Ancoragem.** SWEBOK trata como subárea própria e enfatiza fontes de requisitos e técnicas. ISO 29148 corresponde à tarefa de *definir as necessidades dos stakeholders*, que inclui a elaboração do conceito de operação (ConOps) e dos cenários de uso. Pohl a associa à dimensão de conteúdo.

**Erro comum a observar na literatura.** Tratar elicitação como sinônimo de "conversar com o cliente". A norma e Pohl são explícitos em que stakeholders são apenas uma das classes de fonte.

---

### 3.2 Análise

**O que é.** O exame dos requisitos elicitados — que chegam em forma bruta, incompletos, ambíguos, conflitantes e sobrepostos — para estruturá-los, classificá-los, detectar problemas e resolvê-los. É onde a matéria-prima da elicitação se torna algo tratável.

**O que se faz.** Classificação de requisitos (funcionais e não funcionais, de produto e de processo, por prioridade, por escopo, por volatilidade); modelagem conceitual para compreender o problema; alocação de requisitos a componentes de arquitetura; detecção e resolução de conflitos; negociação e priorização.

**Ancoragem — e uma divergência relevante.** SWEBOK trata *Requirements Analysis* como subárea única, que absorve modelagem conceitual, negociação e priorização. Pohl, em contraste, **separa a negociação como atividade central autônoma**, argumentando que resolver conflitos entre stakeholders é qualitativamente distinto de analisar a consistência lógica de um conjunto de requisitos: a primeira é uma atividade de construção de acordo, a segunda é técnica. ISO 29148 posiciona a análise como tarefa de *analisar requisitos* dentro dos dois processos de definição.

**Implicação para a RSL.** Se um estudo primário descreve workshops colaborativos de resolução de divergências, ele pode ser codificado como "análise" segundo o SWEBOK ou como "negociação" segundo Pohl. Vale registrar essa decisão de codificação explicitamente.

---

### 3.3 Especificação / Documentação

**O que é.** O registro sistemático dos requisitos em artefatos, de modo que possam ser comunicados, consultados, verificados e mantidos ao longo do tempo. SWEBOK usa "especificação"; Pohl prefere "documentação", termo mais amplo por não pressupor um documento formal único.

**O que se faz.** Escolha do formato e do nível de formalização (linguagem natural livre, linguagem natural estruturada por templates, modelos semiformais como UML e BPMN, notações formais); redação dos requisitos conforme critérios de qualidade; organização e estruturação do conjunto documentado; atribuição de identificadores e atributos.

**Ancoragem.** É aqui que a ISO 29148 é mais prescritiva e mais útil como referência citável. A norma define **características de requisitos individuais** — necessário, apropriado, não ambíguo, completo, singular, viável, verificável, correto, conforme — e **características do conjunto de requisitos** — completo, consistente, factível, compreensível, capaz de ser validado. Define também estruturas de documentos: StRS (Stakeholder Requirements Specification), SyRS (System Requirements Specification) e SRS (Software Requirements Specification).

**Observação.** A norma não exige documentação pesada. Especificação e formalismo são dimensões independentes: um backlog de produto com histórias de usuário é documentação de requisitos tanto quanto um SRS de trezentas páginas — o que muda é o nível de formalização, não a existência da atividade.

---

### 3.4 Validação (e verificação)

**O que é.** A confirmação de que os requisitos estão corretos e adequados. A distinção clássica se aplica: **verificação** pergunta se os requisitos foram construídos corretamente (qualidade interna — consistência, conformidade com regras de documentação); **validação** pergunta se são os requisitos corretos (qualidade externa — correspondência com as necessidades reais dos stakeholders).

**O que se faz.** Revisões e inspeções; prototipação; validação de modelos; derivação de critérios de aceitação e casos de teste a partir dos requisitos; verificação de conformidade com os critérios de qualidade.

**Ancoragem.** SWEBOK trata como subárea própria, listando revisões, prototipação, validação de modelos e testes de aceitação. Pohl estrutura a validação segundo as três dimensões — valida-se conteúdo, documentação e acordo separadamente — e propõe seis princípios de validação, entre eles o envolvimento dos stakeholders certos e a separação entre identificação e correção de erros. ISO 29148 exige validação como tarefa em ambos os processos de definição de requisitos.

**Por que importa metodologicamente.** É a atividade em que os requisitos deixam de ser um artefato interno da equipe e passam a ser um compromisso acordado. Estudos que discutem envolvimento do usuário na aprovação de requisitos tipicamente estão falando de validação, ainda que não usem o termo.

---

### 3.5 Gestão de requisitos (transversal)

**O que é.** Não é uma etapa no mesmo sentido das anteriores, e nenhuma das três fontes a trata como fase. É o conjunto de atividades que atravessa todo o processo e garante que os requisitos permaneçam organizados, rastreáveis e atualizados ao longo do ciclo de vida.

**O que se faz.** Rastreabilidade (pré e pós-especificação, vertical e horizontal); gestão de mudanças e controle de versões; priorização continuada; gestão de atributos dos requisitos; medição e acompanhamento; gestão da linha de base.

**Ancoragem.** SWEBOK aloca esses temas em *Requirements Process* e em *Practical Considerations* — notadamente rastreabilidade, natureza iterativa do processo e gestão de mudanças. ISO 29148 define rastreabilidade e atributos de requisitos de forma detalhada e prescreve a manutenção da rastreabilidade bidirecional. Pohl a define explicitamente como atividade transversal, ao lado das quatro centrais.

---

## 4. Quadro comparativo

| Etapa | SWEBOK v3.0 | ISO/IEC/IEEE 29148:2018 | Pohl (2010) |
|---|---|---|---|
| Elicitação | Requirements Elicitation | Definir necessidades dos stakeholders; ConOps | Elicitação (dimensão: conteúdo) |
| Análise | Requirements Analysis (inclui negociação e priorização) | Analisar requisitos | Análise + **Negociação como atividade autônoma** (dimensão: acordo) |
| Especificação | Requirements Specification (StRS, SyRS, SRS) | Transformar necessidades em requisitos; estruturas documentais e critérios de qualidade | Documentação (dimensão: documentação) |
| Validação | Requirements Validation | Validar requisitos (em ambos os processos) | Validação (atravessa as três dimensões) |
| Gestão | Requirements Process + Practical Considerations | Gerenciar requisitos; rastreabilidade e atributos | Gerenciamento (transversal) |

---

## 5. Três advertências sobre "etapas"

**Não são fases sequenciais.** Nenhuma das três fontes descreve a ER como uma sequência linear. SWEBOK afirma explicitamente que o processo é iterativo e concorrente com o desenvolvimento. ISO 29148 usa deliberadamente o vocabulário de *processos* e *atividades*, não de fases. Pohl trata as quatro atividades centrais como intercaladas. A representação sequencial é uma conveniência didática, e a literatura que a apresenta como cronologia costuma estar simplificando.

**A granularidade varia com a fonte.** Modelagem, priorização e negociação aparecem ora como atividades próprias, ora absorvidas em análise. Ao codificar estudos primários, o critério deve ser o que o estudo descreve, não o rótulo que ele usa.

**Verificação e validação nem sempre são distinguidas.** Boa parte da literatura primária usa "validação" de forma abrangente. A distinção deve ser inferida do que o estudo descreve, não presumida a partir do termo empregado.

---

## Referências

INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION; INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **ISO/IEC/IEEE 29148:2018** — Systems and software engineering — Life cycle processes — Requirements engineering. Geneva: ISO, 2018.

BOURQUE, P.; FAIRLEY, R. E. (Eds.). **Guide to the Software Engineering Body of Knowledge (SWEBOK)**: Version 3.0. Los Alamitos: IEEE Computer Society, 2014. Cap. 1: Software Requirements.

POHL, K. **Requirements Engineering**: Fundamentals, Principles, and Techniques. Berlin: Springer, 2010.

### Complementares (para triangulação, se necessário)

KOTONYA, G.; SOMMERVILLE, I. **Requirements Engineering**: Processes and Techniques. Chichester: John Wiley & Sons, 1998.

NUSEIBEH, B.; EASTERBROOK, S. Requirements Engineering: A Roadmap. In: **Proceedings of the Conference on the Future of Software Engineering (ICSE '00)**. New York: ACM, 2000. p. 35-46.

POHL, K.; RUPP, C. **Requirements Engineering Fundamentals**: A Study Guide for the Certified Professional for Requirements Engineering Exam — Foundation Level — IREB compliant. 2. ed. Santa Barbara: Rocky Nook, 2015.
