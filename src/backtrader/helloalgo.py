import backtrader as bt
import yfinance as yf

from datetime import datetime
import backtrader as bt

# Create a subclass of Strategy to define the indicators and logic


class SmaCross(bt.Strategy):
    def __init__(self):
        sma1 = bt.ind.SMA(period=50)  # fast moving average
        sma2 = bt.ind.SMA(period=100)  # slow moving average
        self.crossover = bt.ind.CrossOver(sma1, sma2)  # crossover signal

    def next(self):
        if not self.position:  # not in the market
            if self.crossover > 0:  # if fast crosses slow to the upside
                self.buy()  # enter long

        elif self.crossover < 0:  # in the market & cross to the downside
            self.close()  # close long position


if __name__ == '__main__':
    # Create a cerebro instance, add our strategy, some starting cash at broker and a 0.1% broker commission
    cerebro = bt.Cerebro()

    data = yf.download(
        "AAPL", start="2011-01-01", multi_level_index=False)
    # tsla_df = yf.download(
    #     tickers='TSLA', start='2019-01-01', multi_level_index=False)
    feed = bt.feeds.PandasData(dataname=data)
    cerebro.adddata(feed)

    cerebro.addstrategy(SmaCross)
    cerebro.broker.setcommission(commission=0.001)
    cerebro.addsizer(bt.sizers.PercentSizer, percents=50)
    cerebro.addanalyzer(bt.analyzers.AnnualReturn, _name="areturn")
    # cerebro.broker.setcash(10000)

    print('<START> Brokerage account: $%.2f' % cerebro.broker.getvalue())
    teststrat = cerebro.run()
    print('<FINISH> Brokerage account: $%.2f' % cerebro.broker.getvalue())

    # Plot the strategy

    plt = cerebro.plot(style='candlestick', loc='grey', grid=False)
    # print(plt)
    print(teststrat[0].analyzers.areturn.get_analysis())
    # print(tsla_df)
