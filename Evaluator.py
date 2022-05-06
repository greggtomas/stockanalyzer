#!/usr/bin/env python3
from tokenize import String
from turtle import clear
from yahooquery import Ticker
import pprint

class Evaluator:

    def __init__(self, ticker) -> None:
        self.ticker = ticker

    def get_stock_info(ticker):
        aapl = Ticker(ticker)
        key_stats_dict = aapl.key_stats
        return key_stats_dict
        
    def get_book_value(self) -> String:
        # get the key stat dictionary for the ticker provided
        k_dict = Evaluator.get_stock_info(self.ticker)
        book_value = k_dict[self.ticker]['bookValue']
        print(book_value)
        if book_value < 1:
            return 'Undervalued'
        elif book_value >= 1 and book_value < 3:
            return 'Fair'
        elif book_value >= 3 and book_value <= 5:
            return 'Grey Area'
        else:
            return 'OVER Valued'

    def print_key_stats(self, key_stats_dict):
        pprint.pprint(key_stats_dict)
        

eval=Evaluator('msft')
print(eval.get_book_value())
# eval.print_key_stats(stats_dict)