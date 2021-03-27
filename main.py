import sqlite3
import requests
import json
import pandas as pd
from sqlalchemy import create_engine

payload = {'key1': 'value1', 'key2': 'value2'}
headers = {
    'Host': 'pintia.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/88.0.4324.146 Safari/537.36',
    'Accept': 'application/json;charset=UTF-8',
    'Cookie': '_ga=GA1.2.592894529.1582188659; _9755xjdesxxd_=32; __snaker__captcha=snqmc7MZHM1C4F3y; '
              'gdxidpyhxdE=Xwg4ZrMhoiZTkZGozSyjBij%5CJ5WS%5CIqVTOxAnUtaiVhlebKCASRSgp6n3'
              '%2BEQmKTfvSjYCEIj0PwEfPkdmjGsg83%5CXokL2hafAqSz%2F0NsZtwRQKT%5C8vWzK0qJe49v1vH8ONKPzyBhrB5A%2B%5CZwt'
              '%2FTcux0yYdnTNdBbSjBV54avVL%5CcHjHs%3A1597548356066; '
              '__gads=ID=4d43aea6bdcc8402-2250b33771c6005e:T=1616041663:RT=1616041663:S=ALNI_Mb2eHV_'
              '-0fE9jIjaByMiHmu6u9x-A; _gid=GA1.2.391097635.1616256328; JSESSIONID=0184424C37C152E19C839EC4F827A8B5 '
}
num_list = [733, 734, 735, 736, 737, 738, 739, 740, 741, 743, 744, 44932]
list_value1 = []
list_value2 = []
list_value3 = []


def get_data():
    for i in num_list:
        url = "https://pintia.cn/api/problem-sets/14/problems/" + str(i)
        res = requests.get(url, headers=headers)
        data = json.loads(res.text)
        data_1 = data['problemSetProblem']
        list_value1.append(data_1['title'])
        list_value2.append(data_1['author'])
        list_value3.append(data_1['content'])
    list_value = [list_value1, list_value2, list_value3]
    list_key = ['title', 'author', 'question']
    result = dict(zip(list_key, list_value))
    print(result)
    return result


def deal_data(result):
    db1 = pd.DataFrame(result, index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    print(db1)
    return db1


def create_data():
    conn = sqlite3.connect("D://mypython//PySQLITE1.db")
    c = conn.cursor()
    c.execute('''
                create table covid19data
                (
                    title CHAR(20),
                    author CHAR(50),
                    question CHAR(200)
                );
            ''')
    conn.commit()
    conn.close()


def change_data(db1):
    db1.to_excel('spiderdata.xlsx', sheet_name='spxls', index=False)
    db0 = pd.read_excel('spiderdata.xlsx', sheet_name='spxls')
    return db0


def up_data(db0):
    engine = create_engine(r'sqlite:///PySQLITE1.db')
    db0.to_sql('covid19data', engine, if_exists='append', index=False)


if __name__ == '__main__':
    # get_data()
    db1 = deal_data(get_data())
    dbo = change_data(db1)
    up_data(dbo)


# text-center black-3 text-4 font-weight-bold my-3
