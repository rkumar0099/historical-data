import os
import datetime
from  src.binance_historical_data import BinanceDataDumper

year = "2024"
month = "12"

def initialize():
    year = "2023"
    months = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    data_dump_path = "../data"
    if not os.path.isdir(f"{data_dump_path}/{year}"):
        os.mkdir(f"{data_dump_path}/{year}")
    data_dump_path += f"/{year}"
    for month in months:
        if month < 10:
            month = "0" + str(month)
        if not os.path.isdir(f"{data_dump_path}/{month}"):
            os.mkdir(f"{data_dump_path}/{month}")

def fetch_data(symbol, year, month, day_start, day_end):
    date_start = datetime.date(year=year, month=month, day=day_start)
    date_end = datetime.date(year=year, month=month, day=day_end)

    if month < 10:
        month = "0" + str(month)

    data_dumper = BinanceDataDumper(
        asset_class="um",  # spot, um, cm
        path_dir_where_to_dump=f"../data/{year}/{month}",
        data_type="klines",  # aggTrades, klines, trades
        data_frequency="15m",  # argument for data_type="klines"
    )

    data_dumper.dump_data(
    tickers=symbol,
    date_start=date_start,
    date_end=date_end,
    is_to_update_existing=False,
    tickers_to_exclude=["UST"],
    )


year = "2026"
#months = {"01": (31, 1), "02": (28, 1), "03": (31, 1), "04": (30, 1), "05": (31, 1), "06": (30, 1), "07": (31, 1), "08": (31, 1), "09": (30, 1), "10": (31, 1), "11": (30, 1), "12": (31, 1)}
#months = {"01": (31, 1), "02": (28, 1), "03": (31, 1), "04": (30, 1)}
#symbol = "BTCUSDT"
#symbols = ['ETHUSDT', 'ALGOUSDT', 'SOLUSDT', 'DOGEUSDT', '1000PEPEUSDT', 'AAVEUSDT', 'AVAXUSDT', 
#           'BNBUSDT', 'FILUSDT', 'FTMUSDT', 'WLDUSDT', 'XLMUSDT', 'XRPUSDT', 'GRTUSDT', 'XMRUSDT',
#             'UNIUSDT', "IPUSDT", "JASMYUSDT", "JUPUSDT", "KAITOUSDT", "LINKUSDT", "LTCUSDT",
#               "MATICUSDT", "MEMEUSDT", "MEWUSDT", "NEARUSDT", "NOTUSDT", "ONDOUSDT", "CHZUSDT", 
#               "FETUSDT", "GRASSUSDT", "ADAUSDT", "BAKEUSDT", "BOMEUSDT", "1000BONKUSDT", 
#               "1000FLOKIUSDT", "1000SATSUSDT"]
month = "05"
#symbols = ["WIFUSDT"]
#months = {"12": (31, 1), "11": (30, 1), "10": (31, 1), "09": (30, 1), "08": (31, 1), "07": (31, 1), "06": (30, 1), "05": (31, 1), "04": (30, 1), "03": (31, 1), "02": (28, 1), "01": (31, 1)}
#months = {"07": (31, 1), "06": (30, 1), "05": (31, 1), "04": (30, 1), "03": (31, 1), "02": (28, 1), "01": (31, 1)}
start = 1
end=31
symbols = ['BTCUSDT']
#symbols = ['ETHUSDT', 'ALGOUSDT', 'SOLUSDT', 'DOGEUSDT', '1000PEPEUSDT', 'AAVEUSDT', 'AVAXUSDT', 'BNBUSDT', 'FILUSDT', 'FTMUSDT', 'WLDUSDT', 'XLMUSDT', 'XRPUSDT', 'GRTUSDT', 'XMRUSDT', 'UNIUSDT', "ADAUSDT"]
#symbols = ["ADAUSDT", "BAKEUSDT", "BOMEUSDT"]
#symbols = ["CHZUSDT", "FETUSDT", "GRASSUSDT"]
#symbols = ["IPUSDT", "JASMYUSDT", "JUPUSDT", "KAITOUSDT", "LINKUSDT", "LTCUSDT", "MATICUSDT", "MEMEUSDT", "MEWUSDT", "NEARUSDT", "NOTUSDT", "ONDOUSDT"]

#for month in months:
#    start = months[month][1]
#    end = months[month][0]
#    for symbol in symbols:
#        fetch_data(symbol, int(year), int(month), start, end)

for symbol in symbols:
    fetch_data(symbol, int(year), int(month), start, end)



#symbol = "FILUSDT"
#symbols = ['GRTUSDT']
#symbols = ['XMRUSDT', 'UNIUSDT', "SOLUSDT", "ADAUSDT"]

#for symbol in symbols:
#    fetch_data(symbol, int(year), int(month), start, end)

#for symbol in symbols:
#    if (symbol == "BTCUSDT"):
#        continue
#    fetch_data(symbol, int(year), int(month), 14, 31)    

#symbols = ['FILUSDT', 'WLDUSDT', 'XLMUSDT', 'XRPUSDT']

months = {12: (31, 1), 11: (30, 1), 10: (31, 1), 9: (30, 1), 8: (31, 1), 7: (31, 1), 6: (30, 1), 5: (31, 1), 4: (30, 1), 3: (31, 1), 2: (28, 1), 1: (31, 1)}

#months = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#months = [12]
#for symbol in symbols:
#    for month in months:
#        fetch_data(symbol, int(year), month, months[month][1], months[month][0])

#fetch_data("BTCUSDT", int(year), int(month), start, end)    



#initialize()

#fetch_data()


