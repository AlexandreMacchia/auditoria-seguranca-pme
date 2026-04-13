import socket
import platform
from datetime import datetime

def verificar_portas(ip, portas):
    print(f"[*] Iniciando varredura no IP: {ip}...")
    portas_abertas = []
    
    for porta in portas:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        resultado = sock.connect_ex((ip, porta))
        
        if resultado == 0:
            portas_abertas.append(porta)
        sock.close()
        
    return portas_abertas

def obter_dados_rede():
    # Coleta o nome real do PC e o IP na rede Wi-Fi/Cabo
    nome_pc = socket.gethostname()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_local = s.getsockname()[0]
        s.close()
    except:
        ip_local = "127.0.0.1"
    return nome_pc, ip_local

def gerar_relatorio():
    # Portas que PMEs precisam tomar cuidado
    portas_alvo = [21, 22, 23, 445, 3389]
    nome_maquina, ip_alvo = obter_dados_rede()
    
    print("="*65)
    print("         AUDITORIA BÁSICA DE CIBERSEGURANÇA PARA PMEs         ")
    print("="*65)
    print(f"Responsável: Alexandre Machia Araujo (RU: 5436041)")
    print(f"Local: Cerquilho, SP | Foco: ODS 9")
    print("-" * 65)
    
    # Exibe os dados exclusivos de quem está rodando o script
    print(f"Máquina Auditada: {nome_maquina}")
    print(f"IP da Máquina na Rede: {ip_alvo}")
    print(f"Sistema Operacional: {platform.system()} {platform.release()}")
    print(f"Data da Auditoria: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("-" * 65)
    
    portas_abertas = verificar_portas(ip_alvo, portas_alvo)
    
    print("\n" + "-" * 65)
    print("                       RESULTADO FINAL                       ")
    print("-" * 65)
    
    if len(portas_abertas) == 0:
        print("[+] EXCELENTE! Nenhuma porta crítica de teste está exposta.")
        print("[+] A infraestrutura básica está protegida contra ataques diretos comuns.")
    else:
        print("[-] ATENÇÃO: Encontramos portas abertas que exigem cuidado:")
        for porta in portas_abertas:
            if porta == 21:
                print(" -> Porta 21 (FTP): Risco de interceptação de arquivos.")
            elif porta == 23:
                print(" -> Porta 23 (Telnet): Protocolo antigo e inseguro.")
            elif porta == 445:
                print(" -> Porta 445 (SMB): Risco ALTO de Ransomware (vírus de resgate).")
            elif porta == 3389:
                print(" -> Porta 3389 (RDP): Risco de invasão remota. Use senhas muito fortes.")
            else:
                print(f" -> Porta {porta} aberta.")
                
    print("\n[!] Recomendação: Mantenha sempre o Windows Update e o Antivírus em dia.")
    print("="*65)

if __name__ == "__main__":
    gerar_relatorio()
    
    # Trava para a janela não fechar
    print("\n")
    input("[!] Auditoria finalizada. Pressione ENTER para sair...")
