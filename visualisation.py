# plotting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_rsi(new, ticker,buy_signal,sell_signal):
    # the first plot is the actual close price with long/short positions
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(211)
    new['Close'].plot(label=ticker)
    ax.plot(new.loc[new['signals'] == 1].index,
            new['Close'][new['signals'] == 1],
            label='LONG', lw=0, marker='^', c='g')
    ax.plot(new.loc[new['signals'] == -1].index,
            new['Close'][new['signals'] == -1],
            label='SHORT', lw=0, marker='v', c='r')

    plt.legend(loc='best')
    plt.grid(True)
    plt.title('Positions')
    plt.xlabel('Date')
    plt.ylabel('price')
    # plt.show()
    fig.savefig("C:/Users/bensa/Downloads/Trading/pdf/" + ticker + "_position.pdf", bbox_inches='tight')

    # the second plot is rsi with overbought/oversold interval capped at 30/70
    fig = plt.figure(figsize=(8, 8))
    bx = fig.add_subplot(212)
    new['rsi'].plot(label='relative strength index', c='#522e75')
    bx.fill_between(new.index, buy_signal, sell_signal, alpha=0.5, color='#f22f08')
    bx.text(new.index[-45], 75, 'overbought', color='#594346', size=12.5)
    bx.text(new.index[-45], 25, 'oversold', color='#594346', size=12.5)

    plt.xlabel('Date')
    plt.ylabel('value')
    plt.title('RSI')
    plt.legend(loc='best')
    plt.grid(True)
    # plt.show()
    fig.savefig("C:/Users/bensa/Downloads/Trading/pdf/" + ticker + "_rsi.pdf", bbox_inches='tight')


def plot_bb(newbie, ticker):
    # plotting positions on price series and bollinger bands

    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.plot(newbie['Close'], label='price')
    ax.fill_between(newbie.index, newbie['lower band'], newbie['upper band'], alpha=0.2, color='#45ADA8')
    ax.plot(newbie['mid band'], linestyle='--', label='moving average', c='#132226')
    # ax.plot(newbie['slope'], linestyle='--', label='slope', c='#132226')
    ax.plot(newbie['Close'][newbie['signals'] == 1], marker='^', markersize=12,
            lw=0, c='g', label='LONG')
    ax.plot(newbie['Close'][newbie['signals'] == -1], marker='v', markersize=12,
            lw=0, c='r', label='SHORT')

    plt.legend(loc='best')
    plt.title('Bollinger Bands Pattern Recognition')
    plt.ylabel('price')
    plt.grid(True)
    # plt.show()
    fig.savefig("C:/Users/bensa/Downloads/Trading/pdf/" + ticker + "_bb.pdf", bbox_inches='tight')
