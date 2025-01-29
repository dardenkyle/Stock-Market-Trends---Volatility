import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import os
import sys
import argparse
import logging
import json
import requests

def get_stock_data(ticker, start_date, end_date):
    # Get stock data
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

get_stock_data('AAPL', '2020-01-01', '2020-12-31')

