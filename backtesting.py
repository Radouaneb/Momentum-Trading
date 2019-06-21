
import numpy as np
import pandas as pd
from indicator import rsi, bbands_b

def signal_generation(df,buy_signal,sell_signal,n=14):
    # indi df de rsi
    df_f = pd.DataFrame()
    df_f['Close'] = df
    df_f['rsi'] = rsi(df)           # [n:]
    df_f['positions'] = np.where(df_f['rsi'] < buy_signal, 1, np.where(df_f['rsi'] > sell_signal, -1, 0))
    df_f['signals'] = df_f['positions'].diff()
    # print(df_f)
    return df_f[n:]

def signal_generation2(df):
    # indi df de rsi
    df_f = pd.DataFrame()
    df_f['Close'] = df
    df_f['slope'], df_f['lower band'], df_f['upper band'], df_f['mid band'] = bbands_b(df)
    # df['rsi'][n:] = indic(df, n=14)
    df_f['positions'] = np.where(df_f['Close'] < df_f['lower band'], 1, np.where(df_f['Close'] > df_f['upper band'], -1,0))
    df_f['signals'] = df_f['positions'].diff()
    # print(df_f)
    return df_f
