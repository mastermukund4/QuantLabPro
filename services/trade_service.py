from importers.algotest import AlgoTestImporter
from importers.parser import TradeParser

from analytics.monthly import MonthlyAnalyzer


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

        # Monthly Analysis
        analyzer = MonthlyAnalyzer()
        report = analyzer.analyze(trades)

        # Print Monthly Report
        self.print_report(report)

    def print_report(self, report):

        print("\n")
        print("=" * 80)
        print("QUANTLAB PRO - MONTHLY ANALYTICS TEST")
        print("=" * 80)

        for month in report.months:

            print(f"\n📅 {month.month}")
            print("-" * 80)
            print(f"{'Total Trades':30} : {month.total_trades}")
            print(f"{'Winning Trades':30} : {month.winning_trades}")
            print(f"{'Losing Trades':30} : {month.losing_trades}")
            print(f"{'Gross Profit':30} : ₹{month.gross_profit:,.2f}")
            print(f"{'Gross Loss':30} : ₹{month.gross_loss:,.2f}")
            print(f"{'Net Profit':30} : ₹{month.net_profit:,.2f}")
            print(f"{'Average P&L / Trade':30} : ₹{month.average_pnl:,.2f}")
            print(f"{'Best Trade':30} : ₹{month.best_trade:,.2f}")
            print(f"{'Worst Trade':30} : ₹{month.worst_trade:,.2f}")
            print(f"{'Win Rate':30} : {month.win_rate:.2f}%")
            print(f"{'Profit Factor':30} : {month.profit_factor:.2f}")

        print("\n" + "=" * 80)