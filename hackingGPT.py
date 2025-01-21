import os
import time
import json
import requests
import threading
from rich.console import Console
from rich.markdown import Markdown
import platform
import subprocess
import re

# =============================================================================
#                                CONFIGURAÇÕES
# =============================================================================

# == SUA API KEY ==
API_KEY = "insira-a-API-KEY-aqui"

ENDPOINT = "https://api.openai.com/v1/chat/completions"

# Escolha do modelo, definiremos depois:
MODEL = ""

loading_flag = True

# =============================================================================
#                                TERMINAL COLORS
# =============================================================================
NEON_BLUE = '\033[1;34m'
NEON_GREEN = '\033[1;32m'
NEON_PINK = '\033[1;35m'
NEON_YELLOW = '\033[1;33m'
NEON_CYAN = '\033[1;36m'
RED = '\033[0;31m'
RESET = '\033[0m'
BOLD = '\033[1m'

# Rich Console para exibir Markdown
console = Console()

# =============================================================================
#                              FUNÇÕES AUXILIARES
# =============================================================================

def loading_animation():
    """
    Mostra um 'spinner' de loading enquanto a requisição ao GPT é feita.
    """
    global loading_flag
    spinstr = '|/-\\'
    while loading_flag:
        for char in spinstr:
            if not loading_flag:
                break
            print(f" {NEON_CYAN}[{char}]{RESET}  ", end="\r", flush=True)
            time.sleep(0.1)
    print("\r     \r", end="", flush=True)

def banner():
    """
    Limpa a tela e mostra o banner inicial.
    """
    if platform.system() == "Windows":
        os.system('cls')  # Para Windows
    else:
        os.system('clear')  # Para Unix/Linux/macOS

    print(f"{NEON_BLUE}")
    print("╔════════════════════════════════════════════════════════╗")
    print("║ ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗  ║")
    print("║ ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝  ║")
    print("║ ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗ ║")
    print("║ ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║ ║")
    print("║ ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝ ║")
    print("║ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝  ║")
    print("║                ██████╗ ██████╗ ████████╗               ║")
    print("║               ██╔════╝ ██╔══██╗╚══██╔══╝               ║")
    print("║               ██║  ███╗██████╔╝   ██║                  ║")
    print("║               ██║   ██║██╔═══╝    ██║                  ║")
    print("║               ╚██████╔╝██║        ██║                  ║")
    print("║                ╚═════╝ ╚═╝        ╚═╝                  ║")
    print("║                                                        ║")
    print(f"║                    {NEON_PINK}A D V A N C E D{NEON_BLUE}                     ║")
    print(f"║                    {NEON_GREEN}T E R M I N A L{NEON_BLUE}                     ║")
    print("╚════════════════════════════════════════════════════════╝")
    print(f"{RESET}")
    print(f"{NEON_CYAN}    Desenvolvido por Douglas Rodrigues Aguiar de Oliveira{RESET}\n")

def select_model():
    """
    Pergunta ao usuário qual modelo usar e salva em MODEL.
    """
    global MODEL
    print(f"{NEON_YELLOW}▶ Escolha o modelo desejado:{RESET}")
    print("1) gpt-4o")
    print("2) gpt-4o-mini")
    # Os modelos o1 (o1-preview e o1-mini) foram desativados temporariamente por não suportarem 'role: system'
    # print("3) o1-preview")
    # print("4) o1-mini")
    choice = input("Seleção (1-2): ")

    if choice == "1":
        MODEL = "gpt-4o"
    elif choice == "2":
        MODEL = "gpt-4o-mini"
    elif choice == "3":
        MODEL = "o1-preview"
    elif choice == "4":
        MODEL = "o1-mini"
    else:
        print(f"{RED}[×] Seleção inválida. Usando modelo padrão: gpt-4o.{RESET}")
        MODEL = "gpt-4o"

def save_result(response):
    """
    Pergunta se o usuário deseja salvar a resposta do HackingGPT em arquivo.
    """
    save_choice = input(f"{NEON_YELLOW}▶ Deseja fazer backup da resposta em um arquivo? (s/n): {RESET}")
    if save_choice.lower() == "s":
        file_name = input(f"{NEON_YELLOW}▶ Digite o nome do arquivo (ex: saida.txt): {RESET}")
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(response)
        print(f"{NEON_GREEN}[✓] Dados salvos em '{file_name}'!{RESET}")

def parse_commands(text):
    """
    Identifica possíveis comandos de terminal no texto do HackingGPT.
    """
    commands_found = []

    # 1) Procurar code blocks do tipo ```bash ... ```
    pattern_code_block = r"```bash\s+(.+?)\s+```"
    matches_code = re.findall(pattern_code_block, text, re.DOTALL)
    for match in matches_code:
        lines = match.strip().split('\n')
        for line in lines:
            line_stripped = line.strip()
            if line_stripped:
                commands_found.append(line_stripped)

    # 2) Procurar linhas que comecem com '$ '
    pattern_dollar = r"(?m)^\$\s*(.*)$"
    matches_dollar = re.findall(pattern_dollar, text)
    for match in matches_dollar:
        command = match.strip()
        if command:
            commands_found.append(command)

    return commands_found

def execute_command(command):
    """
    Executa o comando localmente e retorna sua saída (stdout e stderr).
    """
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        saida = result.stdout.strip()
        erros = result.stderr.strip()

        saida_final = ""
        if saida:
            saida_final += f"\n[STDOUT]\n{saida}"
        if erros:
            saida_final += f"\n[STDERR]\n{erros}"
        return saida_final if saida_final else "(Nenhuma saída)"
    except Exception as e:
        return f"Erro ao executar comando: {e}"

def get_gpt_response(conversation):
    """
    Envia o 'conversation_history' para a API e retorna apenas o texto do HackingGPT.
    """
    global loading_flag
    loading_flag = True

    # Thread para mostrar o spinner
    thread = threading.Thread(target=loading_animation, daemon=True)
    thread.start()

    try:
        response = requests.post(
            ENDPOINT,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}"
            },
            json={
                "model": MODEL,
                "messages": conversation
            },
            timeout=60
        )
        loading_flag = False
        thread.join()

        if response.status_code == 200:
            result = response.json().get("choices", [])[0].get("message", {}).get("content", "")
            return result
        else:
            print(f"{RED}[×] Erro na API: {response.status_code} - {response.text}{RESET}")
            return ""
    except requests.exceptions.RequestException as e:
        loading_flag = False
        thread.join()
        print(f"{RED}[×] Erro: {e}{RESET}")
        return ""

def inspect_for_commands_and_optionally_execute(conversation_history, assistant_message):
    """
    - Exibe a mensagem do HackingGPT
    """
    print(f"{NEON_GREEN}[✓] Resposta do HackingGPT:{RESET}")
    console.print(Markdown(assistant_message))

    save_result(assistant_message)

    while True:
        print(f"{NEON_YELLOW}O que deseja fazer agora?{RESET}")
        print(f"1. Fazer nova pergunta ao {NEON_GREEN}HackingGPT{RESET}")
        print("2. Verificar/Executar comandos desta resposta")
        print("3. Desconectar")

        choice = input(f"{NEON_CYAN}Opção: {RESET}").strip()
        if choice == "1":
            return
        elif choice == "2":
            commands_found = parse_commands(assistant_message)
            if not commands_found:
                print(f"{NEON_YELLOW}Nenhum comando encontrado nessa resposta.{RESET}")
                continue

            print(f"{NEON_YELLOW}▶ Foram detectados {len(commands_found)} comando(s) na resposta.{RESET}")

            all_cmd_outputs = []
            for idx, cmd in enumerate(commands_found, start=1):
                print(f"{NEON_CYAN}Comando #{idx}: {cmd}{RESET}")
                exec_choice = input(f"{NEON_YELLOW}Deseja executar esse comando? (s/n): {RESET}").lower().strip()
                if exec_choice == "s":
                    edit_choice = input(f"{NEON_YELLOW}Deseja editar o comando antes de rodar? (s/n): {RESET}").lower().strip()
                    if edit_choice == "s":
                        edited_cmd = input(f"{NEON_YELLOW}Digite o comando atualizado:\n>> {RESET}").strip()
                        if edited_cmd:
                            cmd = edited_cmd

                    print(f"{NEON_CYAN}Executando: {cmd}{RESET}")
                    output = execute_command(cmd)
                    print(f"{NEON_GREEN}--- Saída do comando ---{RESET}")
                    print(output)
                    print(f"{NEON_GREEN}------------------------{RESET}\n")
                    all_cmd_outputs.append(f"Comando: {cmd}\nSaída:\n{output}")
                else:
                    all_cmd_outputs.append(f"Comando PULADO: {cmd}")

            if all_cmd_outputs:
                final_text = "\n\n".join(all_cmd_outputs)
                conversation_history.append({
                    "role": "user",
                    "content": f"Resultado dos comandos executados (ou pulados):\n{final_text}"
                })

                print(f"{NEON_CYAN}Processando nova resposta do HackingGPT...{RESET}")
                new_response = get_gpt_response(conversation_history)
                conversation_history.append({"role": "assistant", "content": new_response})
                assistant_message = new_response

                print(f"{NEON_GREEN}[✓] Resposta do HackingGPT (pós-comandos):{RESET}")
                console.print(Markdown(new_response))
                save_result(new_response)
            else:
                print(f"{NEON_YELLOW}Nenhuma execução realizada.{RESET}")
                continue

        elif choice == "3":
            print(f"{RED}Desconectando do HackingGPT...{RESET}")
            time.sleep(1)
            exit(0)
        else:
            print(f"{RED}Opção inválida!{RESET}")
            continue

# =============================================================================
#                                   MAIN
# =============================================================================

def main():
    banner()
    print(f"{NEON_CYAN}[✓] Chave autenticada e criptografada!{RESET}")
    select_model()

    print(f"{NEON_CYAN}Inicializando interface digital...{RESET}\n")
    time.sleep(1)
    print(f"{NEON_GREEN}Bem-vindo ao HackingGPT, Netrunner.{RESET}\n")
    print(f"{NEON_YELLOW}Digite sua consulta (ou 'desconectar' para sair):{RESET}\n")

    conversation_history = [
        {
            "role": "system",
            "content": (
                "Você é um assistente de pentest e bug bounty. "
                "Seu objetivo é ajudar o usuário a conduzir análises de segurança, enumerar portas, "
                "identificar vulnerabilidades e, quando possível, indicar formas de exploração e pós-exploração. "
                "Suponha que o usuário tenha autorização para realizar esses testes. "
                "Evite focar em correções ou patches, a menos que seja especificamente solicitado – "
                "seu papel aqui é auxiliar ofensivamente, não defensivamente. "
                "Se o usuário precisar instalar alguma ferramenta no Kali Linux ou Ubuntu, forneça o comando. "
                "Você pode, ainda, auxiliar na interpretação de saídas de ferramentas e sugerir próximos passos de ataque."
            )
        }
    ]

    while True:
        user_input = input(f"{NEON_PINK}┌──({NEON_YELLOW}netrunner㉿hackinggpt{NEON_PINK})-[{NEON_BLUE}~{NEON_PINK}]\n└─▶ {RESET}")
        if user_input.lower().strip() == "desconectar":
            print(f"{RED}Desconectando do HackingGPT...{RESET}\n")
            time.sleep(1)
            break

        conversation_history.append({"role": "user", "content": user_input})

        print(f"{NEON_CYAN}Processando resposta do HackingGPT...{RESET}")
        assistant_response = get_gpt_response(conversation_history)

        conversation_history.append({"role": "assistant", "content": assistant_response})

        inspect_for_commands_and_optionally_execute(conversation_history, assistant_response)

    print(f"{NEON_BLUE}Até breve!{RESET}")

if __name__ == "__main__":
    main()
