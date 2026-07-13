import datetime
from  binance_historical_data import BinanceDataDumper


year = "2024"
month = "12"

date_start = datetime.date(year=int(year), month=int(month), day=1)
date_end = datetime.date(year=int(year), month=int(month), day=7)

data_dumper = BinanceDataDumper(
        asset_class="um",  # spot, um, cm
        path_dir_where_to_dump="../downloads",
        data_type="klines",  # aggTrades, klines, trades
        data_frequency="1m",  # argument for data_type="klines"
    )

data_dumper.dump_data(
    tickers='ETHUSDT',
    date_start=date_start,
    date_end=date_end,
    is_to_update_existing=False,
    tickers_to_exclude=["UST"],
)
