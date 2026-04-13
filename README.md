# auditoria-seguranca-pme
Projeto de Extensão - Gestão de TI - Auditoria de Segurança para PMEs.


# Auditoria de Cibersegurança para PMEs (ODS 9)

Este projeto foi desenvolvido como parte da **Atividade Extensionista II** do curso de **Gestão de Tecnologia da Informação**. O objetivo é promover a inclusão digital e a segurança da informação para pequenas e médias empresas (PMEs) no município de Cerquilho/SP.

## 🎯 Objetivo
O projeto visa auxiliar pequenos comerciantes a identificarem vulnerabilidades críticas em suas infraestruturas de rede, focando no **Objetivo de Desenvolvimento Sustentável 9 (Indústria, Inovação e Infraestrutura)** da ONU.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.13
* **Bibliotecas:** Socket, Platform, Datetime (nativas)

## 🔍 Funcionalidades
O script realiza uma varredura local segura para identificar se portas críticas (frequentemente usadas em ataques de Ransomware ou invasões remotas) estão expostas:
* **Porta 445 (SMB):** Alvo comum de vírus sequestradores de dados.
* **Porta 3389 (RDP):** Porta de acesso remoto.
* **Portas 21, 22 e 23:** Protocolos de transferência de arquivos e acesso.

## 🚀 Como Executar
1. Certifique-se de ter o Python instalado.
2. Baixe o arquivo `auditoria_pme.py`.
3. Execute o comando no terminal:
   ```bash
   python auditoria_pme.py
