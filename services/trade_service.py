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
        analyzer = PerformanceAnalyzer()
        report = analyzer.analyze(trades)

        # Print Report
        self.print_report(report)

    def print_report(self, report):

        print("\n")
        print("=" * 70)
        print("QUANTLAB PRO - PERFORMANCE REPORT")
        print("=" * 70)

        # ------------------------------------------------------
        # TRADING ACTIVITY
        # ------------------------------------------------------

        print("\n📊 TRADING ACTIVITY")
        print("-" * 70)

        print(f"{'Total Trades':30} : {report.total_trades}")
        print(f"{'Winning Trades':30} : {report.winning_trades}")
        print(f"{'Losing Trades':30} : {report.losing_trades}")
        print(f"{'Breakeven Trades':30} : {report.breakeven_trades}")

        # ------------------------------------------------------
        # RETURNS
        # ------------------------------------------------------

        print("\n💰 RETURNS")
        print("-" * 70)

        print(f"{'Gross Profit':30} : ₹{report.gross_profit:,.2f}")
        print(f"{'Gross Loss':30} : ₹{report.gross_loss:,.2f}")
        print(f"{'Net Profit':30} : ₹{report.net_profit:,.2f}")

        print(f"{'Average Winning Trade':30} : ₹{report.average_winning_trade:,.2f}")
        print(f"{'Average Losing Trade':30} : ₹{report.average_losing_trade:,.2f}")
        print(f"{'Average P&L / Trade':30} : ₹{report.average_pnl_per_trade:,.2f}")

        print(f"{'Best Trade':30} : ₹{report.best_trade:,.2f}")
        print(f"{'Worst Trade':30} : ₹{report.worst_trade:,.2f}")

        # ------------------------------------------------------
        # STRATEGY EDGE
        # ------------------------------------------------------

        print("\n🎯 STRATEGY EDGE")
        print("-" * 70)

        print(f"{'Win Rate':30} : {report.win_rate:.2f}%")
        print(f"{'Loss Rate':30} : {report.loss_rate:.2f}%")
        print(f"{'Payoff Ratio':30} : {report.payoff_ratio:.2f}")
        print(f"{'Profit Factor':30} : {report.profit_factor:.2f}")
        print(f"{'Expectancy (R)':30} : {report.expectancy_r:.3f}")

        print("=" * 70)