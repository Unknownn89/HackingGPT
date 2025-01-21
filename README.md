# HackingGPT

**HackingGPT** é uma ferramenta de terminal avançada para pentest e bug bounty que integra a API do ChatGPT para auxiliar pesquisadores de segurança na execução e análise de comandos – tudo diretamente pelo terminal.

## Funcionalidades

- **Assistência dinâmica:**  
  Utiliza a API do ChatGPT para orientar suas operações de pentest, sugerindo comandos personalizados com base nas suas consultas.

- **Execução interativa de comandos:**  
  O código detecta comandos na resposta do ChatGPT (por meio de blocos de código ou linhas que iniciam com `$`) e permite que o usuário:
  - Execute o comando;
  - Edite o comando antes da execução;
  - Ou o pule.

- **Integração de resultados:**  
  Os resultados dos comandos executados são agregados e enviados de volta ao ChatGPT para nova análise, permitindo um fluxo contínuo de orientação.

- **Interface colorida:**  
  Utiliza a biblioteca [Rich](https://github.com/willmcgugan/rich) para exibir mensagens formatadas e renderizar Markdown com cores no terminal.

- **Seleção de modelos:**  
  Permite a escolha entre diferentes modelos, como **gpt-4o** e **gpt-4o-mini**.  
  As opções referentes aos modelos **o1-preview** e **o1-mini** estão desativadas (comentadas).

## Requisitos

- **Python 3.6+**
- **Dependências externas:**
  - `requests`
  - `rich`

Para instalar as dependências, execute:

  ```bash
  pip install -r requirements.txt
  ```

- **Chave de API:**  
  É necessário possuir uma chave de API válida do OpenAI. O local da chave já está definido no código.

- **Terminal compatível:**  
  Utilize um terminal que suporte cores ANSI (a maioria dos terminais modernos em Linux, macOS e Windows).

## Instalação

1. **Clone o repositório**

   ```bash
   git clone https://github.com/DouglasRao/hackingGPT.git
   ```

2. **Acesse o diretório do projeto**

   ```bash
   cd hackingGPT
   ```

3. **(Opcional) Crie e ative um ambiente virtual**

   ```bash
   python -m venv venv
   ```
   
   - No Linux/macOS:
     ```bash
     source venv/bin/activate
     ```
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Instale as dependências**

   Execute o arquivo `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. **Execute o script**

   No diretório do projeto, execute:

   ```bash
   python hackingGPT.py
   ```

2. **Siga as instruções na tela**

   - **Seleção do modelo:**  
     Escolha entre as opções disponíveis (por exemplo, digite `1` para *gpt-4o* ou `2` para *gpt-4o-mini*).

   - **Entrada de consulta:**  
     Digite sua consulta de pentest ou bug bounty (por exemplo: "Quero fazer um pentest básico em bancocn.com") ou digite `desconectar` para sair.

   - **Fluxo interativo:**  
     O script enviará sua consulta para a API e exibirá a resposta. Se forem detectados comandos na resposta, um menu interativo permitirá:
     
     1. Fazer nova pergunta (voltando ao prompt principal);
     2. Verificar/Executar os comandos apresentados na resposta;
     3. Desconectar (sair do script).

   - **Execução de comandos:**  
     Ao escolher a opção para verificar/rodar comandos, você poderá decidir para cada comando se deseja:
       - Executá-lo (com a opção de editá-lo antes);
       - Ou pular o comando.
     
     Os resultados dos comandos serão exibidos e enviados para nova análise.

3. **Itere ou saia**

   Utilize o menu interativo para continuar fazendo novas perguntas ou processando comandos adicionais conforme necessário.

## Contribuição

Contribuições são bem-vindas! Consulte o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para obter diretrizes sobre como reportar bugs, sugerir melhorias ou enviar novas funcionalidades.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

**Desenvolvido por Douglas Rodrigues Aguiar de Oliveira**

