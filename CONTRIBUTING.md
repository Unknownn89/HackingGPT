# Contribuindo para o HackingGPT

Obrigado por querer contribuir para o HackingGPT! Sua colaboração é essencial para melhorar e expandir este projeto. Abaixo estão as diretrizes e o fluxo para enviar suas contribuições.

## Como posso contribuir?

Você pode ajudar de várias maneiras:

- **Reportar problemas:**  
  Encontre um bug, comportamento inesperado ou tem uma sugestão de melhoria? Abra uma _issue_ neste repositório. Por favor, descreva detalhadamente o problema, incluindo passos para reproduzi-lo (se aplicável).

- **Enviar pull requests:**  
  Corrija um bug, adicione uma funcionalidade ou melhore a documentação. Para isso, siga o fluxo abaixo para garantir que sua contribuição será bem integrada ao projeto.

- **Testar e sugerir melhorias:**  
  Teste novas funcionalidades e sugira melhorias ou otimizações baseadas na experiência de uso.

## Fluxo para envio de pull requests

1. **Fork do repositório:**  
   Clique no botão "Fork" no repositório do HackingGPT para criar uma cópia do projeto na sua conta.

2. **Clone o seu fork localmente:**  
   No terminal, execute:
   ```bash
   git clone https://github.com/seu-usuario/HackingGPT.git
   ```

Substitua `seu-usuario` pelo seu nome de usuário no GitHub.

3. **Crie uma branch para a sua contribuição:**  
    Escolha um nome descritivo para a sua branch:
    
    ```bash
    git checkout -b feature/nome-da-sua-alteracao
    ```
    
4. **Realize suas alterações:**  
    Faça as modificações necessárias no código ou na documentação.
    
5. **Testes:**  
    Certifique-se de que suas alterações não quebram a funcionalidade existente. Execute o script e valide o comportamento.
    
6. **Commit das alterações:**  
    Faça commits com mensagens claras e descritivas, utilizando o imperativo. Por exemplo:
    
    ```bash
    git commit -m "Adiciona suporte ao DeepSeek API"
    ```
    
7. **Envie sua branch para o seu fork:**
    
    ```bash
    git push origin feature/nome-da-sua-alteracao
    ```
    
8. **Abra um pull request:**  
    No GitHub, acesse o repositório do HackingGPT e clique em "New Pull Request". Selecione a sua branch e envie o pull request com uma descrição detalhada das alterações e dos motivos para a mudança.
    
## Diretrizes de código e estilo

- **Clareza e consistência:**  
    Mantenha o estilo de código claro e consistente. Utilize as convenções de nomenclatura e formatação já existentes no projeto.
    
- **Mensagens de commit:**  
    Escreva mensagens de commit concisas e descritivas, utilizando o imperativo (ex.: "Adiciona", "Remove", "Corrige").
    
- **Documentação:**  
    Mantenha o código bem comentado e atualize a documentação sempre que modificar ou adicionar funcionalidades.
    
- **Segurança das chaves de API:**  
    Certifique-se de que as chaves de API usadas no código sejam carregadas via variáveis de ambiente e que nenhuma chave seja exposta no código ou no histórico de commits.
    
## Código de conduta

Este projeto adota um [Código de Conduta](CODE_OF_CONDUCT.md) para garantir um ambiente colaborativo, respeitoso e inclusivo. Espera-se que todos os colaboradores mantenham um comportamento profissional e respeitem os demais membros da comunidade. Problemas de conduta serão tratados com seriedade.

## Dúvidas

Se tiver dúvidas sobre como contribuir ou sobre o projeto, abra uma _issue_ no repositório para que possamos ajudar.

## Agradecimento

Agradecemos sua contribuição e interesse em fazer parte do desenvolvimento do HackingGPT!
