from math import floor
from sqlite3 import OperationalError
import string
import sqlite3
from urllib.parse import urlparse

host = "http://127.0.0.1:8000/"


def table_check():
    create_table = """
        CREATE TABLE WEB_URL(
        ID INT,
        URL TEXT NOT NULL
        );
        """
    with sqlite3.connect('urls.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(create_table)
        except OperationalError as e:
            print(e)


def toBase62(num, b=62):
    if b <= 0 or b > 62:
        return 0
    base = string.digits + string.ascii_lowercase + string.ascii_uppercase
    r = num % b
    res = base[r]
    q = floor(num / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res


def toBase10(num, b=62):
    base = string.digits + string.ascii_lowercase + string.ascii_uppercase
    limit = len(num)
    res = 0
    for i in range(limit):
        res = b * res + base.find(num[i])
    return res


def home(original_url):
    if urlparse(original_url).scheme == '':
        original_url = 'http://' + original_url
    with sqlite3.connect('urls.db') as conn:
        cursor = conn.cursor()
        insert_row = """
            INSERT INTO WEB_URL (URL)
                VALUES ('%s')
            """ % (original_url)
        result_cursor = cursor.execute(insert_row)
        encoded_string = toBase62(result_cursor.lastrowid)
    short_url=host + encoded_string
    return short_url


def redirect_short_url(short_url):
    decoded_string = toBase10(short_url)
    redirect_url = 'http://localhost:5000'
    with sqlite3.connect('urls.db') as conn:
        cursor = conn.cursor()
        select_row = """
                SELECT URL FROM WEB_URL
                    WHERE ID=%s
                """ % (decoded_string)
        result_cursor = cursor.execute(select_row)
        try:
            redirect_url = result_cursor.fetchone()[0]
        except Exception as e:
            print(e)
    print(redirect_url)



table_check()
redirect_short_url(home('rauakmishra.com.np'))