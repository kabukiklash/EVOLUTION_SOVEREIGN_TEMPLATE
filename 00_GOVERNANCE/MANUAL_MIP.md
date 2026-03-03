# Manual do Protocolo Militar de Instalação (MIP) 🏛️🛡️

Este guia descreve como utilizar o **Gabarito de Ouro** (`ANTIGRAVITY_SOVEREIGN_TEMPLATE`) para implantar uma nova instância do Antigravity em qualquer ambiente Windows, garantindo conformidade com as normas ISO e integridade soberana.

## 🚀 1. Preparação (Clone Nomádico)
Para iniciar uma nova célula, você não deve "forkar" o repositório, mas sim clonar a estrutura física para manter a pureza original.

1.  Copie a pasta `ANTIGRAVITY_SOVEREIGN_TEMPLATE` para o destino final.
2.  Mantenha a árvore `[00-04]` intacta.
3.  Garanta que não existam arquivos `.env` ou `.log` prévios na cópia (verifique via `ls -R`).

## 🛠️ 2. Execução da Fundação (Apply)
O script `Apply.ps1` realiza a "Linha de Chegada" do ambiente operacional.

1.  Abra o PowerShell como Administrador.
2.  Navegue até a raiz da nova instância.
3.  Execute:
    ```powershell
    .\Apply.ps1
    ```
4.  **O que acontece:** O sistema cria um Ponto de Restauração, valida a topologia das zonas e gera o marcador `deployment.ok`.

## 🔬 3. Auditoria Sobrenatural (SAR V2)
Nenhuma instalação é considerada "Soberana" sem o selo SAR.

1.  Execute o auditor hardened:
    ```bash
    python 00_GOVERNANCE/audit_installation.py
    ```
2.  **Verificação:** Abra o arquivo `00_GOVERNANCE/FIRST_SAR_REPORT.md`.
3.  **Integridade:** O `Merkle Root` deve ser idêntico ao valor de referência do Gabarito de Ouro. Se os valores divergirem, a instalação foi adulterada ou existem restos de arquivos (Slag).

## ⚠️ 4. Gestão de Crises (Revert)
Se o `Apply.ps1` falhar ou se o SAR acusar erros de integridade:

1.  Execute o script de reversão:
    ```powershell
    .\Revert.ps1
    ```
2.  O sistema removerá marcadores de operação e limpará o lixo temporário.
3.  Se persistirem erros no sistema operacional, utilize o Ponto de Restauração `Antigravity-MIP-Gold` via Windows System Restore.

## ⚖️ 5. Manutenção de Soberania
- **Mudanças no Core:** Qualquer alteração na zona `01_KINETIC_CORE` exige a regeneração do manifesto e uma nova rodada de auditoria SAR.
- **Auditoria Independente:** Periodicamente, submeta o SAR atual ao Concílio de uma instância mestre para validação de drift (desvio).

---
**Protocolo Antimanchas:** Nunca edite arquivos diretamente na zona 01 enquanto o sistema estiver em `MISSION_CERTIFIED`.
