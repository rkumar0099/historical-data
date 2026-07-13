import os
import time
import pandas as pd
from datetime import datetime

def get_src_file(symbol, year, month, day):
    interval = "1m"
    basepath = f"../data/{year}/{month}/futures/um/daily/klines/{symbol.upper()}/{interval}"
    if (day < 10):
        day = "0" + str(day)
    return f"{basepath}/{symbol}-{interval}-{year}-{month}-{day}.csv"

def get_date():
    #value = time.time()
    value = 1735603380000/1000
    dt_obj = datetime.fromtimestamp(value).isoformat(sep=' ', timespec='milliseconds')
    print(dt_obj.__str__())


def get_filename(symbol, date):
    year = date.split("-")[0]
    month = date.split("-")[1]
    return f"{basepath}\\{year}\\{month}\\{symbol}\\{date}.csv"
    #return f"{basepath}\\{date}\\{symbol}.csv"

def format_file(symbol, year, month, day, interval):
    rows = []
    cols = ["date", "open", "high", "low", "close", "volume", "quote_volume"]
    #print(date, file)
    filename = get_src_file(symbol, year, month, day)
    print(filename)
    try:
        df = pd.read_csv(filename)
    except Exception as exc:
        print(exc)
        return
    dfs = []
    df_count = 0
    count = 0
    
    if(df.columns.values[0] != "open_time"):
        keys = ["open_time","open","high","low","close","volume","close_time","quote_volume","count","taker_buy_volume","taker_buy_quote_volume","ignore"]
        df.columns = keys
        #df.set_index(keys)
    df = df.rename(columns={"open_time": "timestamp"})
    #df = df.set_index(["open_time","open","high","low","close","volume","close_time","quote_volume","count","taker_buy_volume","taker_buy_quote_volume","ignore"])
    for value in df['timestamp']:
        #print(value)

        value = int(value/1000)
        dt_obj = datetime.fromtimestamp(value)
        dt_obj_str = dt_obj.date().__str__()
        '''
        if (cur_date != dt_obj_str):
            dfs.append(pd.DataFrame(rows, columns=cols))
            #analyse_frame(dfs[df_count])
            dfs[df_count].to_csv(f"{date}_algousdt.csv")
            rows = []
            cur_date = dt_obj_str
            df_count += 1
        '''
        row = [dt_obj.__str__(), df['open'][count], df['high'][count], df['low'][count], df['close'][count], df['volume'][count], df['quote_volume'][count]]
        #print(row)
        count += 1
        rows.append(row)
        #print(dt_obj.date().__str__())
        #'''
    #print(len(rows), len(cols))
    dfs.append(pd.DataFrame(rows, columns=cols))
    #analyse_frame(dfs[df_count])
    dst_file = f"/mnt/c/users/rabindar kumar/web/trading/data"
    if not (os.path.isdir(f"{dst_file}/{year}")):
        os.mkdir(f"{dst_file}/{year}")
    dst_file += f"/{year}"
    if not (os.path.isdir(f"{dst_file}/{month}")):
        os.mkdir(f"{dst_file}/{month}")
    dst_file += f"/{month}"
    if not (os.path.isdir(f"{dst_file}/{symbol}")):
        os.mkdir(f"{dst_file}/{symbol}")
    dst_file += f"/{symbol}"

    if not (os.path.isdir(f"{dst_file}/{interval}")):
        os.mkdir(f"{dst_file}/{interval}")
    dst_file += f"/{interval}"

    if (day < 10):
        day = "0" + str(day)
    date = f"{year}-{month}-{day}"
    dst_file += f"/{date}.csv"
    print(dst_file)
    dfs[df_count].to_csv(dst_file)
    return dfs
    #return pd.DataFrame(rows, cols)
        #print(datetime.fromtimestamp(value))

def print_days(start=30, end=1):
    count = start
    days = []
    while count >= end:
        days.append(count)
        count -= 1
    print(days)


year = "2022"
month = "12"
years_symbols = {
    "2021": ['BTCUSDT', 'ETHUSDT', 'ALGOUSDT', 'SOLUSDT', 'DOGEUSDT', '1000PEPEUSDT', 'AAVEUSDT', 'AVAXUSDT', 'BNBUSDT', 'FILUSDT', 'FTMUSDT', 'WLDUSDT', 'XLMUSDT', 'XRPUSDT', 'GRTUSDT', 'XMRUSDT', 'UNIUSDT', "ADAUSDT"]
}
symbols = ['BTCUSDT', 'ETHUSDT', 'ALGOUSDT', 'SOLUSDT', 'DOGEUSDT', '1000PEPEUSDT', 'AAVEUSDT', 'AVAXUSDT', 'BNBUSDT', 'FILUSDT', 'FTMUSDT', 'WLDUSDT', 'XLMUSDT', 'XRPUSDT', 'GRTUSDT', 'XMRUSDT', 'UNIUSDT', "ADAUSDT"]

#symbols = ['BTCUSDT', 'ETHUSDT', 'ALGOUSDT', 'SOLUSDT', 'DOGEUSDT', '1000PEPEUSDT', 'AAVEUSDT', 'AVAXUSDT', 'BNBUSDT', 'FILUSDT', 'WLDUSDT', 'XLMUSDT', 'XRPUSDT']
#symbols = ['BTCUSDT']
#whitelist_months = ["02", "01"]
#months = {"12": (23, 18)}
months = {"12": (31, 1), "11": (30, 1), "10": (31, 1), "09": (30, 1), "08": (31, 1), "07": (31, 1), "06": (30, 1), "05": (31, 1), "04": (30, 1), "03": (31, 1), "02": (28, 1), "01": (31, 1)}
#days = ["13", "12", "11", "10", "09", "08", "07", "06"]
#days = ["05", "04", "03", "02", "01"]
#days = ["30", "29", "28", "27", "26", "25", "24", "23", "22", "21", "20", "19", "18", "17", "16", 
#        "15", "14", "13", "12", "11", "10", "09", "08", "07", "06", "05", "04", "03", "02", "01"]

#print_days(start=30, end=1)

days = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8,
         7, 6, 5, 4, 3, 2, 1]
#for day in days:
#    date = f"{year}-{month}-{day}"
#    format_file(symbol, date)
#days = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#format_file(symbol, year, "08", 10)

#symbols = years_symbols[year]


'''
for symbol in symbols:
    for month in months:
    #if not month in whitelist_months:
    #    continue
        day = months[month][0]
        end = months[month][1]
        while day >= end:
            print(symbol, month, day)
            format_file(symbol, year, month, day)
            day -= 1
'''

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
#symbols = ['ETHUSDT', 'ALGOUSDT', 'SOLUSDT', 'DOGEUSDT', '1000PEPEUSDT', 'AAVEUSDT', 'AVAXUSDT', 'BNBUSDT', 'FILUSDT', 'FTMUSDT', 'WLDUSDT', 'XLMUSDT', 'XRPUSDT', 'GRTUSDT', 'XMRUSDT', 'UNIUSDT', "IPUSDT", "JASMYUSDT", "JUPUSDT", "KAITOUSDT", "LINKUSDT", "LTCUSDT", "MATICUSDT", "MEMEUSDT", "MEWUSDT", "NEARUSDT", "NOTUSDT", "ONDOUSDT", "CHZUSDT", "FETUSDT", "GRASSUSDT", "ADAUSDT", "BAKEUSDT", "BOMEUSDT", "1000BONKUSDT", "1000FLOKIUSDT", "1000SATSUSDT"]
#days = [27, 28, 29, 30, 31]
#symbols = ['ETHUSDT', 'ALGOUSDT', 'SOLUSDT', 'DOGEUSDT', '1000PEPEUSDT', 'AAVEUSDT', 'AVAXUSDT', 
#           'BNBUSDT', 'FILUSDT', 'FTMUSDT', 'WLDUSDT', 'XLMUSDT', 'XRPUSDT', 'GRTUSDT', 'XMRUSDT',
#             'UNIUSDT', "IPUSDT", "JASMYUSDT", "JUPUSDT", "KAITOUSDT", "LINKUSDT", "LTCUSDT",
#               "MATICUSDT", "MEMEUSDT", "MEWUSDT", "NEARUSDT", "NOTUSDT", "ONDOUSDT", "CHZUSDT", 
#               "FETUSDT", "GRASSUSDT", "ADAUSDT", "BAKEUSDT", "BOMEUSDT", "1000BONKUSDT", 
#               "1000FLOKIUSDT", "1000SATSUSDT"]
#symbols = ["WIFUSDT"]
year = "2026"
#month = "02"
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
#months = ["04", "05", "06", "07"]
#symbols = ["1000BONKUSDT", "1000FLOKIUSDT", "1000SATSUSDT"]
#symbols = ["ADAUSDT", "BAKEUSDT", "BOMEUSDT"]
#symbols = ["CHZUSDT", "FETUSDT", "GRASSUSDT"]
#symbols = ["IPUSDT", "JASMYUSDT", "JUPUSDT", "KAITOUSDT", "LINKUSDT", "LTCUSDT", "MATICUSDT", "MEMEUSDT", "MEWUSDT", "NEARUSDT", "NOTUSDT", "ONDOUSDT"]
symbols = ['BTCUSDT']
for month in months:
    for symbol in symbols:
        for day in days:
            format_file(symbol, year, month, day, "1m")
#df = format_timeframe("60m", symbol, year, month, days)
#print(df)


#date = "2024-12-09"
#symbol = "ALGOUSDT"

#format_file(symbol, date)
#format_to_timeframe("10m", symbol, date)
#filename = "10_2024-11-24_algousdt.csv"
#df = pd.read_csv(filename)
#analyse_frame(df)



#timestamp_value = 1549836078
#timestamp_value =  1732419016

#print(f"{timestamp_to_date(timestamp_value)}")

#get_date()