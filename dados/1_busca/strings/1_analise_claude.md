# Análise das Áreas dos Artigos Retornados pela String de Busca

## Sumário Executivo

A string de busca retornou **4.820 artigos**. Para entender a paisagem temática
desse conjunto e identificar quais áreas dialogam com o objetivo da SLR
— investigar as interações entre **Engenharia de Requisitos (ER)** e **abordagens
de design de serviços e produtos** (Design Thinking, Service Design, Lean Inception,
Co-Design) —, os artigos foram classificados por palavras-chave em seus títulos.

A análise gerou **15 áreas amplas**. Como muitos artigos são interdisciplinares
por natureza (ex.: um artigo sobre "Design Thinking aplicado à elicitação de
requisitos em um sistema de saúde"), adotou-se um esquema **multi-rótulo**: um
artigo pode pertencer a mais de uma área. Para cada área, são reportadas duas
contagens:

- **Contagem total (multi-rótulo):** número de artigos que tocam a área (somas
  excedem 4.820 porque um artigo pode estar em várias áreas).
- **Área primária:** cada artigo conta uma única vez, atribuído à primeira área
  que casou segundo a ordem de prioridade (que prioriza o tema central da SLR).

- **Nota metodológica.** A classificação se baseia somente em palavras dos títulos
- (o CSV não inclui abstract, keywords ou venue). Isso é suficiente para um
- mapeamento exploratório, mas pode subestimar áreas cujos títulos são genéricos.
- Cerca de **18,4%** dos artigos não casaram com nenhuma palavra-chave e foram
- agrupados em "Outros / Não classificado" — em geral títulos curtos, abstratos
- ou de domínios muito específicos.

---

## 1. Visão Geral: Distribuição das 15 Áreas

| # | Área | Total (multi-rótulo) | % | Área primária | % |
|---|------|---------------------:|---:|--------------:|---:|
| 1 | Design Thinking, Service Design e Co-Design | 416 | 8,6% | 416 | 8,6% |
| 2 | UX, Usabilidade e Interação Humano-Computador | 460 | 9,5% | 401 | 8,3% |
| 3 | Engenharia de Requisitos: Elicitação, Especificação e Modelagem | 1.880 | 39,0% | 1.715 | 35,6% |
| 4 | Métodos Ágeis, DevOps e Gestão de Projetos de Software | 681 | 14,1% | 310 | 6,4% |
| 5 | Inteligência Artificial, Machine Learning e NLP | 357 | 7,4% | 118 | 2,4% |
| 6 | Segurança, Privacidade, Safety e Compliance | 240 | 5,0% | 80 | 1,7% |
| 7 | IoT, Sistemas Embarcados, Cyber-Physical e Indústria 4.0 | 348 | 7,2% | 167 | 3,5% |
| 8 | Domínios de Aplicação: Saúde, Educação e Sociedade | 429 | 8,9% | 148 | 3,1% |
| 9 | Arquitetura de Software, MDE, SPL e Cloud | 316 | 6,6% | 150 | 3,1% |
| 10 | Mobile, Web e Plataformas Digitais | 395 | 8,2% | 157 | 3,3% |
| 11 | Processos de Negócio e Sistemas de Informação | 170 | 3,5% | 59 | 1,2% |
| 12 | Verificação, Validação, Testes e Qualidade de Software | 407 | 8,4% | 119 | 2,5% |
| 13 | Linguagens, Ontologias e Métodos Formais | 218 | 4,5% | 42 | 0,9% |
| 14 | Dados, Visualização e Banco de Dados | 82 | 1,7% | 22 | 0,5% |
| 15 | Jogos Digitais, Gamificação e Realidade Virtual/Aumentada | 102 | 2,1% | 29 | 0,6% |
| — | Outros / Não classificado | 887 | 18,4% | 887 | 18,4% |

**Distribuição multi-rótulo:**

- 1.957 artigos (40,6%) foram atribuídos a **uma só** área
- 1.465 artigos (30,4%) a **duas** áreas
- 441 artigos (9,1%) a **três** áreas
- 70 artigos a **quatro ou cinco** áreas
- 887 artigos (18,4%) a **nenhuma** (Outros)

---

## 2. Detalhamento das Áreas

A seguir, cada área é descrita com seus principais termos, o tamanho da fatia e
exemplos representativos.

### 2.1. Design Thinking, Service Design e Co-Design — 416 artigos (8,6%)

Termos: *design thinking, service design, co-design, design sprint, lean inception,
participatory design, co-creation, human-centred design, user-centred design, UCD,
HCD, design science, product design, design workshop*.

Esta é uma das três áreas-núcleo da SLR. Concentra estudos que aplicam, propõem
ou avaliam abordagens de design no desenvolvimento de soluções.

Exemplos:
- *Design Thinking in Software Requirements: What Techniques to Use? A Proposal for a Recommendation Tool.*
- *The Use of Design Thinking for Requirements Engineering: An Ongoing Case Study in the Field of Innovative Software-Intensive Systems*
- *Promoting the Elicitation of Usability and Accessibility Requirements in Design Thinking: Using a Designed Object as a Boundary Object*
- *Co-designing interactive content: developing a traffic safety game concept for adolescents*
- *Requirement Analysis and Problem Finding Using Design Thinking Concepts in Students' Information System Projects*

### 2.2. UX, Usabilidade e Interação Humano-Computador — 460 artigos (9,5%)

Termos: *user experience, UX, usability, HCI, persona, scenario, prototype,
mockup, wireframe, interactive, accessibility, user involvement, GUI, end-user, HMI*.

Família de práticas adjacente ao design — voltada para qualidade de interação,
representação do usuário e validação experiencial.

Exemplos:
- *Lessons Learned from Using Personas and Scenarios for Requirements Specification of Next-Generation Industrial Robots*
- *Integrating requirements engineering and user experience design in Product Life Cycle Management*
- *From workshop to prototype: A project about the development of a conference application based on the use of UIM*

### 2.3. Engenharia de Requisitos: Elicitação, Especificação e Modelagem — 1.880 artigos (39,0%)

Termos: *requirements engineering, elicitation, specification, modeling, analysis,
management, prioritization, validation, goal-oriented, KAOS, i\*, use case,
user story, functional/non-functional requirement*.

Esta é a área **majoritária** do conjunto, o que é coerente com o objeto da SLR.
Inclui tanto trabalhos puramente técnicos de ER quanto trabalhos que cruzam ER
com outras áreas.

Exemplos:
- *Customer focused requirement engineering and system design for plug-in hybrid electric vehicles (PHEV)*
- *WERT technique in requirements elicitation for web applications*
- *Web-based Stakeholder Participation in Distributed Requirements Elicitation*

### 2.4. Métodos Ágeis, DevOps e Gestão de Projetos de Software — 681 artigos (14,1%)

Termos: *agile, scrum, kanban, DevOps, lean, sprint, continuous integration,
project management, distributed/global software development, GSD, outsourcing,
collaborative, team, software project, hackathon, innovation, creativity*.

Inclui contextos ágeis e colaborativos — que estão no escopo declarado da SLR
("cenários ágeis, colaborativos e centrados no usuário").

Exemplos:
- *Dual-Track Agile in Software Engineering Education*
- *The Impact of Agile Software Development Process on the Quality of Software Product*
- *A Collaborative Approach to Requirements Elicitation*

### 2.5. Inteligência Artificial, Machine Learning e NLP — 357 artigos (7,4%)

Termos: *machine learning, deep learning, AI, neural network, NLP, natural language
processing, LLM, chatbot, generative AI, text mining, classification, recommender,
automated requirement*.

Inclui aplicações de IA/ML à própria ER (ex.: classificação automática de
requisitos, geração com LLMs) e softwares onde o produto é IA.

Exemplos:
- *AIRE 2022: 9th International Workshop on Artificial Intelligence and Requirements Engineering*
- *Automated Glossary Extraction from Collaborative Requirements Models*
- *Cartoon Extraction Mechanism via UML Model Based on Natural Language Requirement Specs*

### 2.6. Segurança, Privacidade, Safety e Compliance — 240 artigos (5,0%)

Termos: *security, privacy, safety, compliance, GDPR, regulatory, threat model,
risk, vulnerability, cybersecurity, attack*.

Domínio próprio da ER de Segurança/Privacidade.

Exemplos:
- *CIA-level driven secure SDLC framework for integrating security into SDLC process*
- *A risk management ontology for Quality-by-Design based on a new development approach*
- *Design Principles for Interactive Dashboards in Drug Safety Surveillance: Design Science Research*

### 2.7. IoT, Sistemas Embarcados, Cyber-Physical e Indústria 4.0 — 348 artigos (7,2%)

Termos: *IoT, internet of things, embedded, cyber-physical, CPS, automotive,
Industry 4, smart, manufacturing, robot, drone, sensor, monitoring, wearable,
automation, hardware*.

Domínio com forte presença porque ER em sistemas físicos é tópico clássico
em conferências como REFSQ e RE.

Exemplos:
- *Lessons Learned from Using Personas and Scenarios for Requirements Specification of Next-Generation Industrial Robots*
- *Trends in the Use of Design Thinking for Embedded Systems*
- *Digital Transformation Process of a Mechanical Parts Production Workshop to Fulfil the Requirements of Industry 4.0*

### 2.8. Domínios de Aplicação: Saúde, Educação e Sociedade — 429 artigos (8,9%)

Termos: *health, healthcare, medical, clinic, patient, hospital, e-health, m-health,
education, teaching, student, classroom, accessibility, elderly, disability,
government, public sector, sustainability, rehabilitation, autism, parkinson, stroke*.

Domínios de aplicação em que ER e design centrado no usuário costumam ser
estudados em conjunto (saúde, em particular, é fortíssimo nesse cruzamento).

Exemplos:
- *Welcome to the Fifth International Workshop on Requirements Engineering for Well-Being, Aging, and Health*
- *Promoting the Elicitation of Usability and Accessibility Requirements in Design Thinking: Using a Designed Object as a Boundary Object*
- *Recruiting Medical Professionals for Visualization Studies: Challenges and Practical Lessons from Clinical Contexts*

### 2.9. Arquitetura de Software, MDE, SPL e Cloud — 316 artigos (6,6%)

Termos: *architecture, microservice, model-driven, MDE, MDD, MDA, product line,
SPL, software reuse, cloud, edge computing, service-oriented, SOA, API*.

Inclui o tópico clássico "Twin Peaks" (requisitos × arquitetura).

Exemplos:
- *MoDRE 2025: 15th International Model-Driven Requirements Engineering Workshop*
- *5th International Workshop on the Twin Peaks of Requirements and Architecture (TwinPeaks 2015)*
- *Early Aspects at ICSE 2007: Workshop on Aspect-Oriented Requirements Engineering and Architecture Design*

### 2.10. Mobile, Web e Plataformas Digitais — 395 artigos (8,2%)

Termos: *mobile, smartphone, Android, iOS, web, website, web-based, platform,
digital platform, social media, e-commerce, digital, online, digital
transformation, digital product/service*.

Plataformas em que a maior parte do desenvolvimento de "soluções digitais"
acontece — alinha-se ao Context do PICOC.

Exemplos:
- *Design and Development of the Ez Claim Mobile Application Through Human-Centered Design Thinking*
- *MOBILE PROBING KIT: User centered development of personal networks services and applications*
- *Web-based Stakeholder Participation in Distributed Requirements Elicitation*

### 2.11. Processos de Negócio e Sistemas de Informação — 170 artigos (3,5%)

Termos: *business process, BPM, BPMN, workflow, enterprise, ERP, information
system, domain model, conceptual model*.

Exemplos:
- *Using Design Thinking in Information System Development: A Survey*
- *Design Thinking in a Nutshell for Eliciting Requirements of a Business Process: A Case Study of a Design Thinking Workshop*
- *Query-based requirements engineering for health care information systems: Examples and prospects*

### 2.12. Verificação, Validação, Testes e Qualidade de Software — 407 artigos (8,4%)

Termos: *test, testing, verification, validation, quality assurance, software
quality, defect, bug, metric, measurement, evaluation, empirical*.

Inclui principalmente trabalhos empíricos e de avaliação. Note que muitos
títulos de avaliação ("evaluation", "empirical") foram captados aqui — esta
área é menos focada em "testes funcionais" do que o nome sugere isoladamente.

Exemplos:
- *Effects of Early User-Testing on Software Quality – Experiences from a Case Study*
- *2nd International Workshop on Requirements Engineering and Testing (RET 2015)*
- *User-centred design and evaluation of support management system*

### 2.13. Linguagens, Ontologias e Métodos Formais — 218 artigos (4,5%)

Termos: *ontology, semantic, formal, specification language, DSL, modeling
language, logic, grammar, UML, SysML*.

Exemplos:
- *SysML Modeling for Hardware Test Requirements*
- *Cartoon Extraction Mechanism via UML Model Based on Natural Language Requirement Specs*
- *Constructing A Creative Service Software with Semantic Web*

### 2.14. Dados, Visualização e Banco de Dados — 82 artigos (1,7%)

Termos: *database, data model, big data, data mining, data warehouse,
visualization, dashboard, analytics*.

Pequena, mas presente.

Exemplos:
- *A novel database model for gravel road maintenance*
- *Peculiarities of fall prevention database development that support big data and analytics*
- *Design Principles for Interactive Dashboards in Drug Safety Surveillance: Design Science Research*

### 2.15. Jogos Digitais, Gamificação e Realidade Virtual/Aumentada — 102 artigos (2,1%)

Termos: *game, gaming, gamification, serious game, game design, virtual reality,
augmented reality, mixed reality, VR, AR*.

Exemplos:
- *Teaching Multidisciplinary Teams Requirements for Undergraduate Students: an Approach to Augmented Reality Software in Design Thinking Context*
- *ViTAWiN - Developing Multiprofessional Medical Emergency Training with Mixed Reality*
- *Game On: Using Serious Tabletop Games to Enhance User Engagement and Optimize Requirements Engineering for Smart City Urban Mobility Solutions*

### 2.16. Outros / Não Classificado — 887 artigos (18,4%)

Títulos que não casaram com nenhuma palavra-chave. Inspeção amostral indica
três perfis típicos:

- Títulos muito **genéricos ou abstratos** (ex.: *"Blurring Boundaries"*,
  *"Aging, Mind and Brain"*, *"Interviews Transcripts"*).
- Títulos sobre **subdomínios muito específicos** que não foram cobertos por
  palavras-chave (ex.: design de mobiliário, sensores específicos, processos
  de certificação industrial).
- Títulos focados em **conceitos teóricos / metodológicos gerais** (ex.: *"The
  Prevalence of Code Over Models"*, *"Participatory analysis of flexibility"*).

Estes artigos podem ser inspecionados manualmente em uma etapa posterior, ou
reclassificados após leitura de abstracts.

---

## 3. Quais Áreas Conversam com o Tema da Pesquisa?

A SLR foca na **interação entre ER e abordagens de design**. A pergunta-chave
desta seção é: **quais áreas, além das três centrais (Design, UX, ER), aparecem
junto delas e portanto formam contextos de aplicação relevantes?**

### 3.1. O núcleo: ER × (Design ∪ UX)

|  | Total |
|---|------:|
| Artigos em **Design Thinking/Co-Design** ∩ **ER** | 72 |
| Artigos em **UX/HCI** ∩ **ER** | 98 |
| **Artigos em (Design ∪ UX) ∩ ER** (núcleo da SLR) | **165** |
| Artigos em Design sem ER | 344 |
| Artigos em UX sem ER | 362 |
| Artigos em ER sem Design/UX | 1.715 |

A interseção direta entre ER e abordagens de design soma **165 artigos** —
este é o conjunto que **mais provavelmente atende às questões de pesquisa
R1–R5** após aplicação dos critérios de inclusão/exclusão. Os 706 artigos
de Design ou UX que **não** casaram com a área de ER são candidatos secundários:
podem citar requisitos sem usar a terminologia "requirement", e a leitura do
abstract dirá se devem ser incluídos ou excluídos pelo critério **CE3** (fora
do escopo de ER).

### 3.2. Áreas que mais co-ocorrem com o núcleo

Para cada área, foi calculada a fração dos 165 artigos do núcleo que também
tocam aquela área:

| Área | Co-ocorrência com o núcleo | % |
|------|---------------------------:|---:|
| Métodos Ágeis, DevOps e Gestão de Projetos | 22 | 13,3% |
| Domínios de Aplicação: Saúde, Educação e Sociedade | 22 | 13,3% |
| Mobile, Web e Plataformas Digitais | 19 | 11,5% |
| IoT, Sistemas Embarcados, Cyber-Physical e Indústria 4.0 | 16 | 9,7% |
| Verificação, Validação, Testes e Qualidade | 10 | 6,1% |
| Linguagens, Ontologias e Métodos Formais | 9 | 5,5% |
| Inteligência Artificial, Machine Learning e NLP | 7 | 4,2% |
| Segurança, Privacidade, Safety e Compliance | 5 | 3,0% |
| Arquitetura de Software, MDE, SPL e Cloud | 3 | 1,8% |
| Processos de Negócio e Sistemas de Informação | 2 | 1,2% |
| Jogos Digitais, Gamificação e VR/AR | 2 | 1,2% |
| Dados, Visualização e Banco de Dados | 1 | 0,6% |

### 3.3. Leitura: que áreas dialogam com a sua pesquisa?

**Áreas com diálogo direto** (são o objeto ou o contexto declarado da SLR):

1. **Design Thinking, Service Design e Co-Design** — é uma das duas pernas
   centrais. Os 416 artigos desta área são candidatos prioritários.
2. **UX, Usabilidade e HCI** — tradição adjacente que precisa ser tratada
   junto: muitos trabalhos sobre Design Thinking usam personas/cenários
   (instrumentos clássicos de UX) e vice-versa. Vale decidir explicitamente
   no protocolo se UX/HCI entra ou não no escopo da SLR.
3. **Engenharia de Requisitos** — a outra perna central. Os 1.715 artigos só
   de ER (sem cruzamento com Design/UX) mostram como o conjunto traz muito
   "ruído" de ER pura, que será excluído por **CE5** (não responde a nenhuma
   QP) na maioria dos casos.

**Áreas com diálogo expressivo** (contextos onde a integração ER × Design
aparece com mais frequência):

4. **Métodos Ágeis, DevOps e Gestão de Projetos (13,3% do núcleo)** —
   diretamente alinhada ao Context do PICOC ("cenários ágeis, colaborativos").
   Provável fonte de respostas para R3 (papéis da ER em design colaborativo)
   e R4 (frameworks integradores: Dual-Track Agile, Design Sprint em times
   ágeis, etc.).
5. **Saúde, Educação e Sociedade (13,3% do núcleo)** — domínio de aplicação
   onde a literatura cruza ER com co-design e design participativo com
   muita força (acessibilidade, e-health, m-health). Provável fonte de
   estudos empíricos para R1 e R5.
6. **Mobile, Web e Plataformas Digitais (11,5% do núcleo)** — alinhada ao
   Context "soluções digitais" do PICOC. Plataforma típica onde ER e Design
   se encontram na prática.
7. **IoT / Sistemas Embarcados / CPS (9,7% do núcleo)** — domínio mais
   tradicional de ER que vem incorporando design. Pode trazer evidência
   contrastante: como a integração funciona em sistemas onde requisitos
   técnicos pesados convivem com necessidades de usuário?

**Áreas com diálogo lateral** (aparecem mas em menor proporção):

8. **Verificação, Validação, Testes e Qualidade (6,1%)** — interseção sobretudo
   por trabalhos sobre avaliação empírica de práticas de design para ER.
9. **Linguagens, Ontologias e Métodos Formais (5,5%)** — trabalhos pontuais
   tentando formalizar artefatos de design (personas, cenários) como modelos.
10. **IA / ML / NLP (4,2%)** — emergente: ferramentas automáticas para apoiar
    Design Thinking em ER, recomendadores de técnicas. Tendência interessante
    para discussão de lacunas (R5).
11. **Segurança / Privacidade (3,0%)** — diálogo discreto: privacy-by-design,
    safety-critical co-design.

**Áreas com diálogo marginal** (aparecem mas raramente cruzam o núcleo):

12. **Arquitetura, MDE, SPL e Cloud (1,8%)** — apesar do tópico "Twin Peaks"
    (requisitos × arquitetura), pouca interseção com abordagens de design
    centradas em humano.
13. **Processos de Negócio e Sistemas de Informação (1,2%)** — surpreendentemente
    baixa, dado o protagonismo histórico de Design Thinking em SI; a diferença
    vem provavelmente do fato de muitos desses trabalhos serem capturados
    primeiro pelas áreas de ER, Design ou Mobile/Web.
14. **Jogos / Gamificação / VR-AR (1,2%)** — nicho específico.
15. **Dados / Visualização / BD (0,6%)** — praticamente ausente do núcleo.

---

## 4. Implicações para a Condução da SLR

1. **Foco prioritário (após aplicar critérios de inclusão/exclusão).**
   Os ~165 artigos do núcleo (Design ∪ UX) ∩ ER são o ponto de partida natural
   para leitura completa. Adicionando os 706 artigos de Design ou UX sem ER
   (candidatos secundários), o conjunto a triar por leitura de
   título+abstract fica em torno de 870 artigos — número viável para uma SLR.

2. **Decisão a tomar no protocolo: tratar UX/HCI como parte da Intervenção?**
   O PICOC menciona "Design Thinking, Service Design, Lean Inception, Co-Design".
   Trabalhos de UX/HCI clássicos (que usam personas/cenários sem invocar
   Design Thinking) podem estar dentro ou fora do escopo dependendo dessa
   decisão. Recomenda-se tornar isso explícito (CI/CE), pois a área 2 é grande
   (460 artigos) e a fronteira é tênue.

3. **Áreas-contexto a destacar nas R2 e R4.**
   Métodos Ágeis (DevOps incluso), Saúde e Mobile/Web são os contextos onde a
   integração ER×Design mais aparece. Em R4 (modelos/frameworks), procurar
   especificamente: Dual-Track Agile, Twin Peaks com Design, Design Thinking
   em equipes Scrum, Design Sprint adaptado a ER.

4. **Possível lacuna a destacar em R5.**
   A baixa interseção com Arquitetura (1,8%) e Sistemas de Informação (1,2%)
   sugere que a integração de design com decisões arquiteturais e com
   modelagem conceitual de SI ainda é pouco explorada — candidata a "lacuna
   apontada na literatura" se confirmada por leitura aprofundada.

5. **Limitações da classificação por palavras-chave.**
   18,4% dos artigos não foram classificados; alguns deles podem pertencer
   ao núcleo da SLR. Recomenda-se uma triagem manual leve do bucket "Outros"
   antes de descartá-lo. A classificação aqui é exploratória — serve para
   mapear, não para substituir os critérios CI/CE da seleção.

---

## 5. Anexo: Resumo dos Critérios de Classificação

Cada artigo foi classificado por casamento de regex em seu título com listas
de termos. Em resumo:

- **Design Thinking, Service Design e Co-Design:** termos sobre as abordagens
  de design citadas no PICOC (Design Thinking, Service Design, Co-Design,
  Design Sprint, Lean Inception, Participatory Design) e suas variantes
  (HCD, UCD, Design Science, Product Design, etc.).
- **UX, Usabilidade e HCI:** termos sobre experiência do usuário, usabilidade,
  HCI, instrumentos clássicos (personas, cenários, protótipos, mockups,
  wireframes), acessibilidade e interfaces.
- **Engenharia de Requisitos:** termos sobre RE, suas atividades (elicitação,
  especificação, modelagem, validação, gestão), formalismos (KAOS, i*),
  artefatos (use case, user story) e qualidades (NFR, FR).
- Demais áreas: termos amplamente reconhecidos como vocabulário do subcampo.

A ordem das áreas na lista define a prioridade quando um artigo casa com mais
de uma área e precisa-se atribuir uma "área primária".
