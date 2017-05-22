import requests


LIMIT = 20

# 豆瓣喜剧排行榜链接
URL = 'https://movie.douban.com/j/chart/top_list?type=24&'\
        'interval_id=100%%3A90&action=&start=%s&limit=%s'


def scawler(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) '\
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 '\
        'Safari/537.36'
    }
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code != 200:
        raise ValueError('scawl error, http code: %s' % response.status_code)
    return response.json()


def save_db(data):
    '''
    title, url
    '''


if __name__ == '__main__':
    url = URL % (0, LIMIT)
    print(url)
    result = scawler(url)
    print(result[0])
    print(len(result))
