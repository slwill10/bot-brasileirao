# Bot de Telegram - Notícias do Brasileirão

Este projeto é um bot do Telegram que realiza web scraping para extrair as últimas notícias do Campeonato Brasileiro (Brasileirão) e as envia para um grupo do Telegram automaticamente. Utiliza as bibliotecas Requests e BeautifulSoup para extrair as informações de sites de notícias e a API do Telegram para enviar as atualizações.

# Funcionalidades
- Scraping das últimas notícias sobre o Brasileirão de fontes confiáveis.
- Envio automático das notícias para um grupo de Telegram.

## Clonar o Repositório

git clone https://github.com/slwill10/bot-brasileirao.git

cd bot-brasileirao

# Instalação das Dependências

Após criar e ativar o ambiente virtual, instala as bibliotecas necessárias com o seguinte comando:
## pip install -r requirements.txt

# Como Usar
1. Criar um Bot no Telegram
2. Vai ao Telegram e pesquisa por @BotFather.
3. Cria um novo bot com o comando /newbot.
4. https://api.telegram.org/botXXX:YYYY/getUpdates
Anota o Token que o BotFather te dá, pois vais precisar dele para o código.
