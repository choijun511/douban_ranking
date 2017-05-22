import time
import requests
import pymysql

from config import DB_USER, DB_PASSWD

db = pymysql.connect('127.0.0.1', port=3306, user=DB_USER,
        passwd=DB_PASSWD, db='douban', charset='UTF8')
cursor = db.cursor()

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
    sql = 'insert into ranking_list (title, url) values (%s, %s)'
    for item in data:
        cursor.execute(sql, [item['title'], item['url']])
    db.commit()


def main():
    print('start scawl')
    start = 0
    while True:
        print('start: %s' % start)
        url = URL % (start, LIMIT)
        result = scawler(url)
        # 当返回结果是空列表，就终止
        if not result:
            break
        save_db(result)
        start += LIMIT
        time.sleep(10)
    cursor.close()
    db.close()
    print('scawl success!')


if __name__ == '__main__':
    main()
