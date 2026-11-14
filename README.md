# Sistema de Alertas de Vencimento de Contratos

Automação desenvolvida em Python para monitorar prazos de vigência de contratos administrativos, identificar vencimentos próximos e enviar notificações automáticas por e-mail aos responsáveis pelo acompanhamento contratual.

## Sobre o projeto

O projeto surgiu da necessidade de facilitar o acompanhamento de contratos administrativos no contexto de licitações e gestão pública.

A solução automatiza a leitura de uma planilha Excel, verifica as datas de vigência dos contratos e identifica aqueles que estão próximos do vencimento. Quando são encontrados contratos dentro do período de alerta, o sistema organiza as informações e encaminha uma notificação por e-mail.

Com isso, busca-se reduzir verificações manuais, melhorar o controle de prazos e otimizar atividades administrativas.

## Funcionalidades

- Leitura automatizada de planilhas Excel.
- Identificação de contratos próximos do vencimento.
- Cálculo automático dos dias restantes de vigência.
- Período de alerta configurável, definido inicialmente em 60 dias.
- Geração de mensagens com os contratos identificados.
- Envio automático de notificações por e-mail utilizando SMTP.
- Verificação da existência de contratos dentro do período de alerta.

## Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Desenvolvimento da automação |
| Pandas | Leitura e manipulação dos dados |
| Excel (.xlsx) | Fonte dos dados contratuais |
| SMTP / Gmail | Envio de notificações |
| GitHub Actions | Automação de execução |

## Fluxo de funcionamento

1. O sistema carrega a planilha com os registros contratuais.
2. Realiza a leitura das informações e das datas de vigência.
3. Calcula quantos dias faltam para o vencimento de cada contrato.
4. Identifica os contratos que vencerão nos próximos 60 dias.
5. Organiza os contratos encontrados em uma mensagem.
6. Envia um e-mail de alerta ao destinatário configurado.

Caso nenhum contrato esteja próximo do vencimento, o sistema informa que não existem alertas para o período.

## Estrutura dos dados

A planilha utilizada deve conter, entre outras informações, as seguintes colunas:

- `Contrato`: identificação do contrato.
- `Data Vigência`: data de encerramento da vigência contratual.

## Configuração

Para executar o projeto localmente:

**1. Clone o repositório**

```bash
git clone https://github.com/Luis01101101/alertas-contratos.git
```

**2. Acesse a pasta**

```bash
cd alertas-contratos
```

**3. Instale as dependências**

```bash
pip install pandas openpyxl
```

**4. Configure as credenciais de e-mail**

Configure o endereço de origem, o destinatário e a autenticação SMTP do Gmail. Recomenda-se utilizar variáveis de ambiente para armazenar credenciais, evitando sua exposição no código.

**5. Execute a aplicação**

```bash
python verificar_contratos.py
```

## Objetivo e aprendizado

Este projeto representa a aplicação prática de conhecimentos em programação, manipulação de dados e automação de processos para solucionar uma necessidade operacional real.

Durante seu desenvolvimento, foram explorados conceitos como:

- Manipulação e processamento de dados.
- Trabalhos com datas e intervalos de tempo.
- Integração com serviços de e-mail.
- Automação de tarefas repetitivas.
- Organização e execução de scripts Python.

## Autor

**Luis Henrique Matos**

Estudante de Engenharia de Software, interessado em desenvolvimento de sistemas, automação e inteligência artificial.

- GitHub: [Luis01101101](https://github.com/Luis01101101)
- LinkedIn: [Luis Matos](https://www.linkedin.com/in/luis-matos-65bb47267/)

---

*Projeto desenvolvido com foco na aplicação da tecnologia para otimização de processos administrativos.*
