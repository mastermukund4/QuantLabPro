import config
from models.trade import Trade, TradeLeg


class TradeParser:
    """
    Converts AlgoTest DataFrame into
    a list of Trade objects.
    """

    def parse(self, df):

        trades = []

        current_trade = None

        for _, row in df.iterrows():

            index = str(row["Index"])

            # Summary Row (1.0, 2.0 ...)
            if index.endswith(".0"):

                if current_trade:
                    trades.append(current_trade)

                current_trade = Trade(
                    trade_id=index,
                    strategy=config.STRATEGY_NAME,
                    symbol=config.SYMBOL,
                    expiry_type=config.EXPIRY_TYPE,

                    entry_date=row["Entry Date"],
                    entry_time=row["Entry Time"],

                    exit_date=row["Exit Date"],
                    exit_time=row["Exit Time"],

                    total_pnl=float(row["P/L"]),

                    vix=row["Vix"]
                )

            else:

                leg = TradeLeg(
                    leg_no=len(current_trade.legs) + 1,

                    buy_sell=row["B/S"],

                    option_type=row["Type"],

                    strike=row["Strike"],

                    quantity=row["Qty"],

                    entry_price=row["Entry Price"],

                    exit_price=row["Exit Price"],

                    pnl=row["P/L"]
                )

                current_trade.legs.append(leg)

        if current_trade:
            trades.append(current_trade)

        return trades