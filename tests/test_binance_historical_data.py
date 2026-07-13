import datetime


def test_import():
    from binance_historical_data import BinanceDataDumper

def test_main_class_init():
    from binance_historical_data import BinanceDataDumper
    '''
    data_dumper = BinanceDataDumper(
        path_dir_where_to_dump=".",
        data_type="klines",  # aggTrades, klines, trades
        data_frequency="1m",  # argument for data_type="klines"
    )
    '''

    ## usdm futures
    data_dumper = BinanceDataDumper(
        asset_class="um",  # spot, um, cm
        path_dir_where_to_dump="../downloads",
        data_type="klines",  # aggTrades, klines, trades
        data_frequency="1m",  # argument for data_type="klines"
    )
    datetime.date(year=2017, month=1, day=1)
    data_dumper.dump_data(
        tickers='BTCUSDT',
        date_start="2024",
        date_end=None,
        is_to_update_existing=False,
        tickers_to_exclude=["UST"],
    )