# Create your views here.
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import requests


TELEGRAM_TOKEN = '6681514810:AAH5Ai1bgNjJQUF44o_Xdz0PXcmGqY9BojY'
TELEGRAM_CHAT_ID = '-1001993149936'

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
    requests.post(url, data=data)

@csrf_exempt
def home(request: HttpRequest):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        print(data["action"])
        if data.get('action') == 'opened' and 'pull_request' in data:
            pr_user_login = data['pull_request']['user']['login']
            pr_title = data['pull_request']['title']
            pr_url = data['pull_request']['html_url']
            message = f'New PR opened: {pr_title}\nURL: {pr_url}\nCreated By:{pr_user_login}'
            send_telegram_message(message)
            
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'not found'} )