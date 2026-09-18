# Validação da primeira edição

Preparação do conteúdo: 17/09/2026. Conferência final: 18/09/2026.

## Verificações concluídas

- Catálogo com 16 módulos, 48 aulas e identificadores únicos.
- Todas as aulas têm conteúdo, exercício, resposta comentada e questão com explicação.
- Fontes dos módulos referenciam entradas válidas no catálogo.
- Nove downloads presentes; links locais e arquivos de entrada verificados.
- Sintaxe de JavaScript e Python verificada.
- Gabarito do CSV recalculado: 8 pedidos válidos, 3 exceções e R$ 2.960,00.
- Cliente de API testado em dry-run para OpenAI, Claude e Gemini, sem rede ou credenciais.
- Leitores de resposta testados com exemplos de JSON e resposta vazia.
- Recuperação lexical testada com pergunta conhecida, entrada vazia e assunto ausente.
- Dois workflows n8n: conexões, sintaxe e lógica dos nós Code verificadas em isolamento com Node.js.
- Classificação: casos financeiro, acesso, desconhecido, vazio e múltiplas intenções.
- Validação de IA: objeto correto, JSON malformado, categoria inválida, tipo incorreto, campos extras e revisão obrigatória.
- Navegador: primeira aula, questão de revisão, anotações, conclusão e persistência após recarregar.
- Busca textual, cópia de exemplo, filtro de nível, biblioteca, glossário sem depender de acentos e navegação a aula avançada.
- Layout visual em 1440 × 1000 e 390 × 844; menu móvel abre e fecha ao navegar; sem transbordamento horizontal nos cenários inspecionados.
- Nenhum erro de console observado nos percursos verificados.

## Limites desta verificação

- Não foram feitas chamadas pagas ou autenticadas a modelos. Disponibilidade de modelo, cobrança e autorização devem ser conferidas na conta do aluno.
- Os workflows foram verificados estruturalmente e sua lógica Code foi executada; não foram importados/executados numa instância real do n8n nesta entrega.
- O exemplo MCP foi conferido contra a documentação da linha 1.x e validado sintaticamente; não houve instalação do SDK nem teste de protocolo com um cliente real.
- O botão de exportação de backup foi acionado sem erro de console; o navegador integrado não confirmou o evento de download. A gravação do arquivo não foi comprovada nesse ambiente.
- A importação de backup pela interface não foi executada: a revisão automática de permissões bloqueou o teste por poder substituir o estado do navegador. Não foi feita tentativa de contornar o bloqueio.
- O site não foi publicado nesta etapa. O teste do endereço público deve ser feito após habilitar GitHub Pages.

## Como repetir os testes locais

Na raiz do projeto, com Python 3.11+ e Node.js:

```text
python scripts/build_content.py
python scripts/validate.py
node --check app.js
node scripts/check_workflows.cjs
```

Para a interface, abra o site, acesse uma aula, faça uma anotação de teste, marque a conclusão e recarregue. Para validar um backup, use um perfil de navegador exclusivo de testes e confira o conteúdo exportado antes de importar. Não substitua anotações reais sem revisar o arquivo.
