from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

contract = Forex('EURUSD')
bars = ib.reqHistoricalData(contract, endDateTime='', durationStr='1 D',
        barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=False)

# convert to pandas dataframe:
df = util.df(bars)
print(df[['date', 'open', 'high', 'low', 'close']]) #Are properties que devuelve con bars, las 5 pero hay mas