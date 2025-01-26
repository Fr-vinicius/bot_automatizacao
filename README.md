# Bot de Automação de Tarefas

Um projeto desenvolvido em **Python** para automatizar ações repetitivas, como acessar um site, ler uma base de dados e realizar o cadastro dessas informações de forma automática. Este bot reduz a necessidade de intervenção humana em tarefas repetitivas.

---

## Índice

1. [Descrição](#descrição)  
2. [Pré-requisitos](#pré-requisitos)  
3. [Instalação](#instalação)  
4. [Uso](#uso)  
5. [Funcionalidades](#funcionalidades)  
6. [Contato](#contato)

---

## Descrição

O **Bot de Automação de Tarefas** é uma aplicação que utiliza a biblioteca **PyAutoGUI** para interagir com a interface gráfica e automatizar processos. Ele lê dados de um arquivo CSV e realiza o cadastro de informações em um sistema online, substituindo o esforço manual por uma solução automatizada.

### Funcionalidades principais
- Acesso automático a sites.  
- Leitura de dados de arquivos CSV.  
- Preenchimento automático de formulários online.  

---

## Pré-requisitos

Para executar o projeto, você precisa ter:  
- Python 3.8 ou superior instalado.  
- As seguintes bibliotecas Python:  
  - pyautogui  
  - pandas  

---

## Instalação

1. Clone o repositório:  
   
   `git clone https://github.com/Fr-vinicius/bot-automacao.git`
   
2. Navegue até o diretório do projeto:
  - `cd bot-automacao`

3. Instale as dependências:
  -  `pip install -r requirements.txt`

## Uso

1. Configuração do ambiente:

- Insira as informações do site, e-mail e senha diretamente no código ou em um arquivo de configuração.

2. Execução do bot:

 - Execute o script principal
   
`python bot_automacao.py`

 
3. Acompanhamento do processo:

- O bot abrirá o navegador, acessará o site especificado e começará a cadastrar os dados encontrados no arquivo produtos.csv.

4. Ajuste de coordenadas:

- Caso necessário, utilize o script de localização para ajustar as coordenadas de cliques e rolagens:

`python localizar_posicao.py`

## Funcionalidades

1. Acesso automático a sites:
- O bot abre o navegador e acessa o site desejado com as credenciais fornecidas.

2. Preenchimento de formulários:
- Lê os dados de um arquivo CSV e os insere automaticamente no formulário online.

3. Automação de tarefas repetitivas:
- Reduz significativamente o tempo necessário para ações manuais repetitivas.

4. Localização de coordenadas:
- Utilize a função de localização para ajustar os cliques e rolagens conforme necessário no ambiente.

## Contato

Se você tiver dúvidas ou sugestões, entre em contato:

Autor: Ederson Vinicius

LinkedIn: https://www.linkedin.com/in/ederson-vinicius-ferreira-rosa-b97550239

Email: evfr.trabalho@gmail.com
