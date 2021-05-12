import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Investar import Analyzer


mk = Analyzer.MarketDB()
stocks = ['삼성전자', 'SK하이닉스']
df = pd.DataFrame()
for s in stocks:
    df[s] = mk.get_daily_price(s, '2016-01-04', '2020-12-31')['close']


df