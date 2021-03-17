import requests

def count_words_at_url(url):
    print("Count words inside the page : %s"%url)
    resp = requests.get(url)
    print('Internet conn is OK')
    return len(resp.text.split())
