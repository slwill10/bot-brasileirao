from functions import *
import requests
import time
from datetime import datetime

TELEGRAM_TOKEN = ''

# Configurações do Telegram
#ID grupo Telegram de Produção
telegram_chat_id = 'SEU ID'
telegram_token = 'SEU TOKEN'


urls = {
   "https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/": uol,
   "https://www.terra.com.br/esportes/futebol/brasileiro-serie-a/tabela/": terra,
   "https://www.revistacolorada.com.br/?s=brasileir%C3%A3o+serie+a": revistaColorada,
   "https://esportenewsmundo.com.br/?s=Brasileir%C3%A3o+serie+a": esportesnewmundo
}

def send_telegram_notification(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    while True:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Notificação enviada com sucesso.")
            break
        elif response.status_code == 429:
            print("Erro 429: Too Many Requests. Aguardando 25 segundos...")
            time.sleep(25)
        else:
            print(f"Erro ao enviar notificação: {response.status_code} - {response.text}")
            break

def main():
    for url, func in urls.items():
        try:
            headlines = func(url)
            batch_size = 10

            for i in range(0, len(headlines), batch_size):
                batch_headlines = headlines[i:i + batch_size]
                now = datetime.now()
                date_time = now.strftime("%d/%m às %H:%M:%S")

                message_lines = [f'''🏅 {headline['texto']}\nFonte: {headline['fonte']}\n\n''' for headline in batch_headlines]
                message = f'''🏆📢 Últimas notícias do brasileirão 2024!\nAqui estão as manchetes mais recentes de {urls[url]}\nData de extração: {date_time}\n\n''' + "\n".join(message_lines)

                send_telegram_notification(telegram_token, telegram_chat_id, message)

        except Exception as e:
            print(f"Erro ao extrair manchetes de {url}: {e}")

# Executar a função principal
if __name__ == "__main__":
    main()

main()