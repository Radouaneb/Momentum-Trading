import pandas


def rsi(price, n=14):
    ''' rsi indicator '''
    delta = price.diff()
    dUp, dDown = delta.copy(), delta.copy()
    dUp[dUp < 0] = 0
    dDown[dDown > 0] = 0

    # RolUp = pandas.rolling_mean(dUp, n)
    RolUp = dUp.rolling(n).mean()
    # RolDown = pandas.rolling_mean(dDown, n).abs()
    RolDown = dDown.rolling(n).mean().abs()
    RS = RolUp / RolDown
    rsi = 100.0 - (100.0 / (1.0 + RS))
    return rsi

def bbands(price, length=20, numsd=2):
    """ returns average, upper band, and lower band"""
    #ave = pandas.stats.moments.rolling_mean(price, length)
    ave = price.rolling(length).mean()
    #sd = pandas.stats.moments.rolling_std(price, length)
    sd = price.rolling(length).mean().std()
    upband = ave + (sd * numsd)
    dnband = ave - (sd * numsd)
    # return (price.values[-1] - dnband.values[-1]) / (upband.values[-1] - dnband.values[-1])
    bbandsdn = (price.values[-1] - dnband.values[-1]) / (upband.values[-1] - dnband.values[-1])
    bbandsup = (- price.values[-1] + dnband.values[-1]) / (- upband.values[-1] + dnband.values[-1])
    return bbandsdn, bbandsup

def bbands_b(price,length=20,numsd=2):
    """ returns average, upper band, and lower band"""
    # ave = pandas.stats.moments.rolling_mean(price, length)
    ave = price.rolling(length).mean()
    # sd = pandas.stats.moments.rolling_std(price, length)
    sd = price.rolling(length).mean().std()
    upband = ave + (sd * numsd)
    dnband = ave - (sd * numsd)
    # return (price.values[-1] - dnband.values[-1]) / (upband.values[-1] - dnband.values[-1])
    # bbandsdn = (price.values[-1] - dnband.values[-1]) / (upband.values[-1] - dnband.values[-1])
    # bbandsup = (- price.values[-1] + dnband.values[-1]) / (- upband.values[-1] + dnband.values[-1])
    bbandsdn = (price - dnband) / (upband - dnband)
    return bbandsdn, dnband, upband, ave
