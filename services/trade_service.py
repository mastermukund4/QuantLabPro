from importers.algotest import AlgoTestImporter
from importers.parser import TradeParser
from analytics.performance import PerformanceAnalyzer


class TradeService:

    def __init__(self, filepath):
        self.filepath = filepath

    def run(self):

        # Load CSV
        importer = AlgoTestImporter(self.filepath)
        df = importer.load()

        # Parse Trades
        parser = TradeParser()
        trades = parser.parse(df)

        # Analyze Performance
        report = PerformanceAnalyzer().analyze(trades)

        # Print Report
        self.print_report(report)

    def print_report(self, report):

        print("\n")
        print("=" * 75)
        print("QUANTLAB PRO - PERFORMANCE REPORT")
        print("=" * 75)

        # ==========================================================
        # TRADING ACTIVITY
        # ==========================================================

        print("\n📊 TRADING ACTIVITY")
        print("-" * 75)

        print(f"{'Total Trades':35} : {report.activity.total_trades}")
        print(f"{'Winning Trades':35} : {report.activity.winning_trades}")
        print(f"{'Losing Trades':35} : {report.activity.losing_trades}")
        print(f"{'Breakeven Trades':35} : {report.activity.breakeven_trades}")

        print(f"{'Win Rate':35} : {report.activity.win_rate:.2f}%")
        print(f"{'Loss Rate':35} : {report.activity.loss_rate:.2f}%")

        # ==========================================================
        # RETURNS
        # ==========================================================

        print("\n💰 RETURNS")
        print("-" * 75)

        print(f"{'Gross Profit':35} : ₹{report.returns.gross_profit:,.2f}")
        print(f"{'Gross Loss':35} : ₹{report.returns.gross_loss:,.2f}")
        print(f"{'Net Profit':35} : ₹{report.returns.net_profit:,.2f}")

        print(f"{'Average Winning Trade':35} : ₹{report.returns.average_winning_trade:,.2f}")
        print(f"{'Average Losing Trade':35} : ₹{report.returns.average_losing_trade:,.2f}")
        print(f"{'Average P&L / Trade':35} : ₹{report.returns.average_pnl_per_trade:,.2f}")

        print(f"{'Best Trade':35} : ₹{report.returns.best_trade:,.2f}")
        print(f"{'Worst Trade':35} : ₹{report.returns.worst_trade:,.2f}")

        # ==========================================================
        # STRATEGY EDGE
        # ==========================================================

        print("\n🎯 STRATEGY EDGE")
        print("-" * 75)

        print(f"{'Payoff Ratio':35} : {report.edge.payoff_ratio:.2f}")
        print(f"{'Profit Factor':35} : {report.edge.profit_factor:.2f}")
        print(f"{'Expectancy (R)':35} : {report.edge.expectancy_r:.3f}")

        # ==========================================================
        # EQUITY
        # ==========================================================

        print("\n📈 EQUITY")
        print("-" * 75)

        print(f"{'Starting Capital':35} : ₹{report.equity.starting_capital:,.2f}")
        print(f"{'Ending Capital':35} : ₹{report.equity.ending_capital:,.2f}")

        # ==========================================================
        # DRAWDOWN
        # ==========================================================

        print("\n📉 DRAWDOWN")
        print("-" * 75)

        print(f"{'Maximum Drawdown':35} : ₹{report.drawdown.max_drawdown_rupees:,.2f}")
        print(f"{'Maximum Drawdown %':35} : {report.drawdown.max_drawdown_percent:.2f}%")

        print(f"{'Current Drawdown':35} : ₹{report.drawdown.current_drawdown_rupees:,.2f}")
        print(f"{'Current Drawdown %':35} : {report.drawdown.current_drawdown_percent:.2f}%")

        print("=" * 75)