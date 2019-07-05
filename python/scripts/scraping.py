from bs4 import BeautifulSoup
import urllib3

def get_data():
    http = urllib3.PoolManager()
    res = http.request('GET', 'https://yahoo.co.jp')

    return res.data

if __name__ == "__main__":
    get_data()
