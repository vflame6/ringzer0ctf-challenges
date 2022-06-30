import base64
import requests
from bs4 import BeautifulSoup

url = 'http://challenges.ringzer0team.com:10016/'
answer_url = 'http://challenges.ringzer0team.com:10016/?r=%s'


def main():
    r = requests.get(url)
    r = BeautifulSoup(r.text, 'html.parser')
    data = r.findAll('div', class_='message')
    key_pool, encoded_message = (msg.text.split()[5].encode() for msg in data)
    key_length = 10

    message = base64.b64decode(encoded_message)

    for i in range(len(key_pool) - key_length):
        key = key_pool[i:i+key_length]
        res = ''

        for index, char in enumerate(message):
            res += chr(char ^ key[index % key_length])

        if res.isalnum():
            answer = res
            break
    
    r = requests.get(answer_url % answer)
    r = BeautifulSoup(r.text, 'html.parser')
    flag = r.findAll('div', class_='alert alert-info')[0].text
    print(f'[*] Flag: {flag}')


if __name__ == '__main__':
    main()
