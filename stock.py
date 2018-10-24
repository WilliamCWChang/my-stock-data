from stock_list import stock_list
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import pandas as pd
import datetime

data_list = ["台泥", "亞泥", "嘉泥", "味全", "味王", "台塑", "南亞", "台聚", "台化", "中華電", "彰銀", "華南金", "富邦金", "兆豐金", "第一金"]

# data_list = ["台泥", "亞泥"]


def get_stock(code):

    url = "https://tw.stock.yahoo.com/q/q?s=" + str(code)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html5lib")
    table = soup.find_all('table')

    data = table[5].find_all('td', attrs={'align': 'center'})

    # for d in data:
    #     print(d.text)

    stock_data = {
        "stock_code": data[0].text.strip("加到投資組合"),           # 股票代號
        # "time": data[1].text,                 # 時間
        "transaction": data[2].text,          # 成交
        # "buy": data[3].text,                  # 買進
        # "sell": data[4].text,                 # 賣出
        # "ups_and_downs": data[5].text.split()[0],        # 漲跌
        "number_of_sheets": data[6].text,     # 張數
        # "yesterday": data[7].text,            # 昨收
        # "opening": data[8].text,              # 開盤
        # "highest": data[9].text,              # 最高
        # "lowest": data[10].text,              # 最低
    }

    # pprint(stock_data)
    return stock_data


# get stock dics
today_stock = []
for data in data_list:
    # print("{:s}{:d}\t:{:s}".format(data, stock_list[data], get_stock(stock_list[data])['yesterday']))
    print("{:s}{:d}\t:{:s}".format(data, stock_list[data], str(get_stock(stock_list[data]))))
    today_stock.append(get_stock(stock_list[data]))

# save as csv
filename = str(datetime.datetime.now().date()) + ".csv"
df = pd.DataFrame(today_stock)
df = df.set_index('stock_code')
df = df.T
df.to_csv(filename, encoding="big5")
