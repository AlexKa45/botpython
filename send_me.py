import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/test')
def get_test_data():
    print('\nrequest:')
    print(request)
    print('request.data:')
    print(request.data)

url='http://i-tek.000webhostapp.com/bot_mail.php?message=Hello&mail=kasperskiialex@gmail.com&head=Test'
s = requests.get(url)

