import pandas

from email_file import SUBSCRIBE_LIST, email_login, send_mail
from data_access import read_yahooData
from indicator import rsi, bbands
from url import get_ETFSymbols
from backtesting import signal_generation, signal_generation2
from visualisation import plot_rsi, plot_bb


def find_validETF(filename, buy_signal, sell_signal):
    ls_etf = []
    ls_rsi = []
    ls_bbd = []
    for etf in get_ETFSymbols('nasdaq'):
        try:
            price = read_yahooData(etf)
        except IOError:
            continue
        relative_strength = rsi(price)
        bollinger_band, bollinger_band2 = bbands(price)
# ''' RSI is considered overbought when above 75 and oversold when below 25 '''

        if (relative_strength.values[-1] < buy_signal and bollinger_band < 0.) or (relative_strength.values[-1] > sell_signal and bollinger_band > 0.):
            ls_etf.append(etf)
            ls_rsi.append(round(relative_strength, 3))
            ls_bbd.append(round(bollinger_band, 3))
            new = signal_generation(price, buy_signal, sell_signal, n=14)
            plot_rsi(new, etf, buy_signal, sell_signal)
            newbie = signal_generation2(price)
            plot_bb(newbie, etf)

    df = pandas.DataFrame({
        'ETF': ls_etf,
        'Relative Strength': ls_rsi,
        'Bollinger Band': ls_bbd
    })
    df.set_index('ETF').to_csv(filename)

path = "C:/Users/bensa/Downloads/Trading/"
def run(me, password):
    sell_signal = 75.
    buy_signal = 25.
    find_validETF('ETF.csv', buy_signal, sell_signal)
    send_mail(
        send_from='bensallami.radouane1@gmail.com',
        send_to=SUBSCRIBE_LIST,
        subject='Suggested ETF',
        text="""Hello,
      # Attachment includes the ETFs with today's close lower than Bollinger Bottom and Relative Strength Index lower than 25.""",
        files=['ETF.csv'],
        server='smtp.gmail.com',
        username=me,
        password=password)

if __name__ == '__main__':
    me, password = email_login()
    run(me, password)
