# IA na prática

Curso em português para estudar inteligência artificial do primeiro contato à construção de agentes e automações. Site estático, sem instalação de dependências para navegar e preparado para GitHub Pages.

## Conteúdo

- 16 módulos e 48 aulas autorais, com explicação, passo a passo, exercício, resposta comentada e questão de revisão.
- ChatGPT, Claude, Gemini, NotebookLM, Copilot, Perplexity e modelos locais.
- Prompts, multimodalidade, pesquisa, escrita, dados e programação.
- APIs, RAG, agentes, ferramentas, plugins, skills e MCP.
- n8n: instalação, workflow por regras, webhooks, IA, revisão humana e operação.
- Quatro projetos guiados, glossário e fontes oficiais.
- Nove materiais para baixar, incluindo dois workflows n8n, três scripts Python e conjuntos de dados.

Edição editorial: **17/09/2026**. As durações são estimativas de leitura e prática, não carga horária certificada. Recursos e limites de serviços externos podem mudar.

## Abrir no computador

Abra `index.html` no navegador. O curso usa arquivos locais e não exige uma API para leitura.

Para testar com um endereço local consistente e melhor compatibilidade de armazenamento:

```powershell
cd C:\git\estudos\curso-ia-na-pratica
python -m http.server 8937 --bind 127.0.0.1
```

Abra `http://127.0.0.1:8937`. Se a porta estiver ocupada, escolha outra. O site também pode ser servido por qualquer servidor estático. Não há backend de IA embutido.

## Publicar no GitHub Pages

1. Crie um repositório vazio chamado `curso-ia` na conta desejada. Para publicação gratuita comum, use um repositório público, após revisar os arquivos. Não inicialize outro README no remoto se já houver commits locais.
2. Na pasta do projeto, confira `git status` e `git log --oneline`. Se ainda não houver commit, revise e faça `git add .` e `git commit -m "Cria o curso IA na prática"`.
3. Cadastre o remoto com `git remote add origin https://github.com/SEU_USUARIO/curso-ia.git`, substituindo o usuário. Se já houver remoto, confira antes de alterá-lo.
4. Envie a branch: `git push -u origin main`.
5. No GitHub, abra **Settings → Pages → Build and deployment**. Escolha **Deploy from a branch**, branch **main**, pasta **/(root)** e salve.
6. Aguarde a publicação e abra o endereço exibido pelo GitHub. Para um repositório de projeto, costuma ser `https://SEU_USUARIO.github.io/curso-ia/`.
7. Teste uma aula, um download e uma recarga em um link interno. O site usa caminhos relativos e rotas por hash para funcionar sob a subpasta do repositório.

Não é necessário um workflow de Actions personalizado. O arquivo `.nojekyll` mantém os arquivos estáticos como foram preparados. Documentação: [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).

## Progresso e privacidade

Conclusões, respostas e anotações ficam em `localStorage` no navegador. Não há login, sincronização, anúncios nem rastreadores. Fontes e recursos visuais do site não dependem de CDN.

Use **Meu caderno → Exportar backup** antes de limpar o navegador ou mudar de dispositivo/endereço. O armazenamento de `file://`, localhost e GitHub Pages é separado. Na importação, conclusões são somadas; conflitos de anotações pedem confirmação. O backup pode conter texto pessoal que você escreveu.

## Editar o conteúdo

Os originais ficam em `conteudo/`. `catalogo.json` define módulos, fontes, projetos, glossário e downloads. Cada módulo tem um Markdown com marcadores de aula e blocos de exercício/gabarito/revisão.

```powershell
python scripts/build_content.py
python scripts/validate.py
```

O primeiro comando atualiza `data/course.js`, que deve entrar no commit junto com os originais. O navegador não compila Markdown: lê o arquivo JavaScript gerado. Não altere ids de aulas existentes sem planejar migração do progresso.

Para regenerar os workflows após alterar seu gerador:

```powershell
python scripts/build_workflows.py
```

Para verificar sintaxe e lógica de laboratório com Node.js:

```powershell
node --check app.js
node scripts/check_workflows.cjs
```

## Estrutura

```text
index.html              Estrutura e navegação
styles.css              Aparência e adaptação à tela
app.js                  Rotas, busca, caderno, quiz e progresso
data/course.js          Conteúdo compilado, pronto para o navegador
conteudo/               Conteúdo autoral editável
downloads/              Materiais utilizados nas aulas
scripts/                Compilação e validação local
VALIDACAO.md            Evidências de testes e limites da validação
```

## Laboratórios externos

- A leitura do curso é independente de serviços pagos.
- `chamada_api.py --dry-run` não faz rede. A execução real exige sua chave, modelo compatível e pode gerar cobrança.
- `recuperacao_local.py` é busca lexical educativa, não uma implementação com embeddings ou um chatbot.
- `servidor_mcp.py` requer `mcp[cli]>=1.28,<2`. É um exemplo local de leitura com dados fictícios.
- Os workflows n8n usam dados fictícios e não enviam mensagens. A versão com “IA” simula respostas para ensinar validação; a aula explica como conectar um provedor.
- Não coloque chaves em HTML, JavaScript público, prompts ou commits. GitHub Pages não executa Python nem protege segredos de API.

## Escopo pedagógico

A formação é prática: uso de ferramentas, construção de protótipos e avaliação. Não substitui uma graduação em aprendizado de máquina nem cobre treinamento de grandes modelos do zero. As fontes oficiais estão associadas aos módulos para aprofundamento e atualização.
