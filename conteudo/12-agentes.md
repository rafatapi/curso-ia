@lesson {"id":"agente-versus-workflow","title":"Quando você precisa de um agente?","minutes":40,"summary":"Diferencie conversa, automação previsível e decisão orientada por modelo."}
## Não use autonomia sem necessidade
Um workflow segue etapas definidas. Um agente usa um modelo para escolher próximos passos dentro de um ambiente e de limites. As duas abordagens podem se combinar: um processo fixo pode conter uma etapa de decisão por IA.

Se a tarefa é enviar um lembrete em uma data, uma automação determinística pode bastar. Se a tarefa exige descobrir quais documentos consultar e adaptar a busca conforme resultados, um agente pode ser útil. Quanto mais autonomia, maior a necessidade de observar, limitar e testar o processo.

## As peças de um agente
Um projeto mínimo tem objetivo, modelo, ferramentas, estado, política de execução e critérios de parada. O estado guarda informações da tarefa; memória persistente é uma decisão adicional. Ferramentas oferecem operações específicas. A política determina o que pode ser executado e quando é necessária revisão.

```text
Receber objetivo
→ observar estado
→ decidir próxima ação
→ validar ação e argumentos
→ executar ferramenta permitida
→ devolver resultado ao modelo
→ finalizar ou repetir dentro dos limites
```

## Desenhe antes de implementar
1. Defina uma tarefa pequena: responder uma dúvida de política com fonte.
2. Liste ferramentas indispensáveis, como buscar política e consultar trecho.
3. Defina um máximo de passos e tempo de execução.
4. Estabeleça sucesso: resposta sustentada ou ausência de evidência reconhecida.
5. Estabeleça falha: ferramenta indisponível, limite atingido ou conflito de fontes.
6. Defina o que será registrado para revisão.

O modelo não deve ganhar acesso genérico a qualquer comando só para facilitar a implementação. Uma ferramenta `consultar_politica(topico)` com valores limitados é mais controlável que uma ferramenta que executa texto arbitrário.

“Autônomo” não significa sem responsabilidade humana. O sistema precisa de um dono, uma forma de interromper a execução e um procedimento para quando algo foge do esperado.
@exercise
Classifique três tarefas: ordenar um CSV, pesquisar uma resposta em vários documentos e enviar um e-mail já aprovado em um horário fixo. Em qual delas a decisão por modelo pode ser mais útil?
@answer
Ordenar um CSV tem procedimento conhecido. Enviar um e-mail aprovado em horário fixo também pode ser um workflow. Pesquisar em documentos pode se beneficiar de decisões adaptativas, como reformular uma busca após resultado insuficiente. Ainda assim, um pipeline simples de RAG pode bastar: um agente deve justificar sua complexidade.
@quiz {"question":"O que caracteriza melhor um agente neste curso?","options":["Uso de um modelo para decidir próximos passos com ferramentas e limites definidos.","Qualquer tarefa agendada.","Um chatbot com nome e avatar."],"correct":0,"explanation":"A característica central é a decisão de ações no ambiente, não a aparência ou o nome do sistema."}

@lesson {"id":"ferramentas-e-contratos","title":"Ferramentas são contratos, não comandos livres","minutes":45,"summary":"Defina argumentos, permissões e resultados para cada ação do agente."}
## O modelo propõe; a aplicação controla
Em function calling, o modelo solicita uma ferramenta e fornece argumentos. A aplicação verifica o pedido, executa a função permitida e devolve o resultado. Em sistemas com ferramentas hospedadas, parte dessa execução é gerenciada pelo provedor, mas as permissões e efeitos ainda precisam ser entendidos.

O contrato deve descrever o nome, a finalidade, os parâmetros e a saída. Diferencie leitura de escrita. Consultar um pedido e cancelar um pedido não devem parecer a mesma operação. Uma descrição clara ajuda o modelo, mas o código precisa impor as restrições.

## Um contrato pequeno
```json
{
  "name": "consultar_politica",
  "description": "Consulta uma política fictícia; somente leitura.",
  "parameters": {
    "type": "object",
    "properties": {
      "topico": {"type":"string","enum":["acesso","suporte","certificado"]}
    },
    "required": ["topico"],
    "additionalProperties": false
  }
}
```

Esse é um contrato conceitual; cada API tem seu formato de envelope. Na execução, valide que o nome está na lista de ferramentas e que `topico` pertence aos valores aceitos. Não transforme o argumento em comando de terminal nem em caminho de arquivo sem controle.

## Estruture os resultados
1. Retorne `ok`, dados e identificador da fonte quando houver sucesso.
2. Retorne um erro explícito quando não houver dados.
3. Não exponha chave, pilha interna completa ou informação de outro usuário.
4. Devolva o resultado ligado à chamada que o originou.
5. Exija nova decisão após a observação, dentro do limite de passos.

Para uma ferramenta de escrita, inclua identificação da operação, validação de autorização e idempotência. Antes de confirmar uma ação importante, mostre exatamente o efeito a aprovar. A aprovação de um rascunho não autoriza uma versão diferente depois.
@exercise
Desenhe duas ferramentas: consultar pedido e preparar cancelamento. Defina uma diferença essencial em entrada, saída e permissão. Não implemente o cancelamento real.
@answer
Consultar pedido recebe id e retorna dados autorizados. Preparar cancelamento recebe id e motivo, retorna uma proposta com efeitos previstos, sem executar. A execução real seria outra operação, com autorização e confirmação vinculadas à proposta. Separar preparação de execução torna a revisão concreta e auditável.
@quiz {"question":"O modelo solicitou uma ferramenta com argumentos. O que vem antes da execução?","options":["Executar imediatamente qualquer nome recebido.","Validar nome, argumentos, autorização e regras de negócio.","Transformar os argumentos em comandos livres."],"correct":1,"explanation":"A aplicação deve impor o contrato e as permissões; a saída do modelo não é autorização suficiente."}

@lesson {"id":"limites-memoria-multiagentes","title":"Limites, memória e múltiplos agentes","minutes":45,"summary":"Evite ciclos sem fim e entenda quando dividir trabalho realmente ajuda."}
## Um ciclo precisa de saídas
Defina limites de passos, tempo, custo e tamanho de resultados. Se uma busca falhar duas vezes, o agente pode pedir esclarecimento ou encerrar com limitação. Repetir a mesma ação indefinidamente não é persistência útil.

O pseudocódigo abaixo mostra a estrutura, não uma biblioteca pronta. As funções representam componentes que você implementará com o provedor e as ferramentas escolhidos.

```text
para passo de 1 até 5:
    decisão = modelo(estado, ferramentas_permitidas)
    se decisão é resposta_final:
        validar_e_encerrar(decisão)
    se ferramenta ou argumentos são inválidos:
        encerrar_com_revisão()
    resultado = executar_com_timeout(decisão)
    registrar_evento_sem_segredos(resultado)
    adicionar_observação_ao_estado(resultado)
ao atingir o limite: encerrar_com_revisão()
```

## Memória tem finalidade e prazo
Estado da execução guarda o que aconteceu nesta tarefa. Memória durável pode guardar preferências ou fatos aprovados, mas precisa de origem, atualização e exclusão. Não armazene automaticamente tudo que o modelo produziu como verdade para o futuro.

Uma política recuperada deve continuar identificada como fonte externa. Não permita que um texto de documento vire uma instrução permanente só porque apareceu no histórico. Injeções de prompt exploram exatamente essa confusão de autoridade.

## Divida somente o que pode ser coordenado
Múltiplos agentes podem pesquisar subtópicos independentes ou revisar uma entrega. Também podem duplicar trabalho, discordar e aumentar custos. Comece com um agente e ferramentas simples. Ao dividir, defina responsabilidade, entrada, saída e quem consolida o resultado.

1. Separe pesquisa e revisão em tarefas delimitadas.
2. Dê a cada agente apenas dados e ferramentas necessários.
3. Exija evidências e formatos compatíveis.
4. Resolva conflitos com critérios, não por votação de respostas semelhantes.
5. Meça se o ganho de qualidade compensa latência e custo.
@exercise
Um agente faz três vezes a mesma busca sem encontrar resposta e pede uma quarta tentativa. Defina uma regra de parada e uma mensagem final útil. Depois diga quando uma nova tentativa seria justificável.
@answer
Após o limite, encerre dizendo qual informação foi buscada, quais fontes foram consultadas e o que falta para continuar. Uma nova tentativa pode ser útil se houver uma consulta diferente, nova fonte ou esclarecimento do usuário. Repetir a mesma ação sem nova evidência tende a desperdiçar recursos.
@quiz {"question":"Adicionar mais agentes garante um resultado melhor?","options":["Sim, porque concordância sempre prova verdade.","Sim, qualquer tarefa deve usar vários agentes.","Não. É preciso considerar independência das tarefas, coordenação, qualidade e custo."],"correct":2,"explanation":"A divisão de trabalho é uma decisão de arquitetura que precisa ser medida e justificada."}
