Faça a avaliação de qualidade (AQ) do artigo anexado, seguindo o protocolo_rsl_er_design.pdf. ID do estudo: [Exx]

REGRA DE SAÍDA (defina antes de tudo):
- Se o artigo cair de forma AMBÍGUA em qualquer critério de inclusão (CI1–CI4) ou exclusão (CE1–CE8): PARE a execução. Não gere o CSV. Responda apenas com um parágrafo curto (2–4 linhas) dizendo qual critério foi acionado e o motivo objetivo da flag, para eu decidir.
- Se NÃO houver flag: gere APENAS o bloco CSV (8 linhas), sem texto antes ou depois.

Aplique as 8 questões com pontuação 1 = Sim, 0,5 = Parcial, 0 = Não:
AQ1: O objetivo do estudo está claramente definido?
AQ2: O contexto de desenvolvimento de software/digital está descrito?
AQ3: A abordagem de ER é explicitada?
AQ4: A abordagem de design é explicitada?
AQ5: A forma de integração entre ER e design é descrita com detalhes suficientes?
AQ6: Há evidências empíricas, relato de aplicação ou avaliação da abordagem?
AQ7: Benefícios, limitações ou desafios são relatados?
AQ8: As ameaças à validade, limitações ou condições de aplicabilidade são discutidas?

Regras de calibração:
- "Parcial" = a informação existe, mas é implícita, incompleta ou superficial.
- AQ6: argumentação ou exemplos ilustrativos NÃO contam como evidência empírica; exija aplicação real, estudo de caso, experimento ou avaliação. Só proposta conceitual sem validação = Parcial ou Não.
- AQ8: distinga limitações DO MÉTODO/PROPOSTA das ameaças à validade DA EVIDÊNCIA empírica. Se o estudo só discute um dos dois, tende a Parcial (0,5).
- Toda nota deve vir amarrada a um trecho/seção/página rastreável; se não houver evidência localizável, a nota cai.
- Avaliação de qualidade NÃO é triagem de elegibilidade — não exclua o artigo aqui.

Formato da referência: padrão ABNT — Sobrenome, Iniciais.; Sobrenome, Iniciais. (Ano). Título. Veículo.

Encapsulamento de campos no CSV: qualquer campo que contenha vírgula ou ponto e vírgula internos deve ser envolvido em aspas duplas, para não conflitar com o ponto e vírgula que delimita as colunas. Isso vale obrigatoriamente para o campo Referencia e para campos Justificativa ou Evidencia_secao_pagina que contenham vírgulas.

Saída (caso SEM flag): gere 8 linhas no MESMO formato do avaliacao_qualidade_RSL.csv (delimitado por ponto e vírgula, vírgula decimal em 0,5), colunas:
ID_estudo;Referencia;Questao;Descricao_da_questao;Pontuacao;Justificativa;Evidencia_secao_pagina;Revisor
