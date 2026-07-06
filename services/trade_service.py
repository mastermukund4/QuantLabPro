from importers.algotest import AlgoTestImporter
from importers.parser import TradeParser

from analytics.weekly import WeeklyAnalyzer


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

        # Weekly Analysis
        analyzer = WeeklyAnalyzer()

        report = analyzer.analyze(trades)

        self.print_report(report)

    def print_report(self, report):

        print()

        print("=" * 80)
        print("QUANTLAB PRO - WEEKLY ANALYTICS TEST")
        print("=" * 80)

        for week in report.weeks:

            print()

            print(f"📅 {week.week}")

            print("-" * 80)

            print(f"{'Total Trades':30} : {week.total_trades}")
            print(f"{'Winning Trades':30} : {week.winning_trades}")
            print(f"{'Losing Trades':30} : {week.losing_trades}")

            print(f"{'Gross Profit':30} : ₹{week.gross_profit:,.2f}")
            print(f"{'Gross Loss':30} : ₹{week.gross_loss:,.2f}")
            print(f"{'Net Profit':30} : ₹{week.net_profit:,.2f}")

            print(f"{'Average P&L / Trade':30} : ₹{week.average_pnl:,.2f}")

            print(f"{'Best Trade':30} : ₹{week.best_trade:,.2f}")
            print(f"{'Worst Trade':30} : ₹{week.worst_trade:,.2f}")

            print(f"{'Win Rate':30} : {week.win_rate:.2f}%")
            print(f"{'Profit Factor':30} : {week.profit_factor:.2f}")

        print()
        print("=" * 80)