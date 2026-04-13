import socket
import platform
from datetime import datetime

def verificar_portas(ip, portas):
    print(f"[*] Iniciando varredura de segurança local em {ip}...")
    portas_abertas = []
    
    for porta in portas:
        # Cria a conexão de rede para testar a porta
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # Espera no máximo 1 segundo por porta
        resultado = sock.connect_ex((ip, porta))
        
        if resultado == 0:
            portas_abertas.append(porta)
        sock.close()
        
    return portas_abertas

def gerar_relatorio():
    # Lista de portas críticas: FTP (21), SSH (22), Telnet (23), SMB (445), RDP (3389)
    portas_alvo = [21, 22, 23, 445, 3389]
    ip_alvo = "127.0.0.1" # Testa a própria máquina localmente (seguro)
    
    print("="*50)
    print("   AUDITORIA BÁSICA DE CIBERSEGURANÇA PARA PMEs   ")
    print("="*50)
    print(f"Responsável: Alexandre Machia Araujo (RU: 5436041)")
    print(f"Local: Cerquilho, SP | Foco: ODS 9")
    print(f"Sistema Operacional: {platform.system()} {platform.release()}")
    print(f"Data da Auditoria: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("-" * 50)
    
    portas_abertas = verificar_portas(ip_alvo, portas_alvo)
    
    print("\n" + "-" * 50)
    print("                 RESULTADO FINAL                 ")
    print("-" * 50)
    
    if len(portas_abertas) == 0:
        print("[+] EXCELENTE! Nenhuma porta crítica de teste está exposta.")
        print("[+] A infraestrutura básica está protegida contra ataques diretos comuns.")
    else:
        print("[-] ATENÇÃO: Encontramos portas abertas que exigem cuidado:")
        for porta in portas_abertas:
            if porta == 21:
                print(" -> Porta 21 (FTP): Risco de interceptação de arquivos não criptografados.")
            elif porta == 23:
                print(" -> Porta 23 (Telnet): Protocolo antigo e inseguro. Evite usar.")
            elif porta == 445:
                print(" -> Porta 445 (SMB): Risco ALTO de Ransomware se o sistema não estiver atualizado.")
            elif porta == 3389:
                print(" -> Porta 3389 (RDP): Risco de invasão remota. Certifique-se de usar senhas muito fortes.")
            else:
                print(f" -> Porta {porta} aberta.")
                
    print("\n[!] Recomendação: Mantenha sempre o Windows e o Antivírus atualizados.")
    print("="*50)

if __name__ == "__main__":
    gerar_relatorio()
    
    # Esta linha garante que a janela do terminal permaneça aberta após a execução
    print("\n")
    input("[!] Auditoria finalizada. Pressione ENTER para sair...")
