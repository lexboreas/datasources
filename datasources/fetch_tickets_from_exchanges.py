import json
import logging
import time

import ccxt

from requests import get, RequestException



logger = logging.getLogger(__name__)

def fetch_data_from(ccxt_exchange):
    data = ccxt_exchange.fetch_tickers()
    return data 

def send_message(source, data, timestamp):
    print("\n\n>>SEND_MESSAGES to: {}\n{}".format(source, len(data)))

def save_message_to_db(source, data, timestamp):
    print("\n\n>>SAVE TO DB: {}\n{}".format(source, len(data)))

if __name__ == "__main__":
    exchanges = {
        'poloniex': ccxt.poloniex(),
        'bitfinex': ccxt.bitfinex2(),
        'binance': ccxt.binance(),
    }

    for exchange, ccxt_exchange in exchanges.items(): 
        data = fetch_data_from(ccxt_exchange    )
        timestamp = time.time()
        send_message(source=exchange, data=data, timestamp=timestamp)
        save_message_to_db(source=exchange, data=data, timestamp=timestamp)
