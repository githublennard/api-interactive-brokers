from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

contract = Stock('AAPL')
#contract = Forex('GBPUSD')
#contract = Forex('EURUSD')
#contract = Stock('AAPL','SMART','USD')
#contract = Forex('EUR','IDEALPRO','USD')
#contract = Stock('AAPL','ISLAND','USD')
bars = ib.reqHistoricalData(contract, endDateTime='', durationStr='1 D',
        barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=False)

# convert to pandas dataframe:
df = util.df(bars)
print(df[['date', 'open', 'high', 'low', 'close']]) #Are properties que devuelve con bars, las 5 pero hay mas