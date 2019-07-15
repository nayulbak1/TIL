import requests
from decouple import config

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
token = '813870714:AAFlzviLiVZyLNOR6gnyegcm70xORJxwnXM'
chat_id = config('CHAT_ID')
text = '안녕하세요'

send_message = requests.get('https://api.telegram.org/bot813870714:AAFlzviLiVZyLNOR6gnyegcm70xORJxwnXM/sendMessage?chat_id=779293675&text=안녕하세요')


send_message = requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

print(send_message.text)