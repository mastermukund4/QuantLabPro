from importers.algotest import AlgoTestImporter
from importers.parser import TradeParser

from analytics.performance import PerformanceAnalyzer
from exports.excel_exporter import ExcelExporter


class TradeService:

    def __init__(self, filepath):
        self.filepath = filepath

    def run(self):

        importer = AlgoTestImporter(self.filepath)

        df = importer.load()

        parser = TradeParser()

        trades = parser.parse(df)

        report = PerformanceAnalyzer().analyze(trades)

        self.print_report(report)

        ExcelExporter().export(report, trades)

    def print_report(self, report):

        print("\n")
        print("=" * 75)
        print("QUANTLAB PRO - PERFORMANCE REPORT")
        print("=" * 75)

        print(f"Trades : {report.activity.total_trades}")

        print(f"Net Profit : ₹{report.returns.net_profit:,.2f}")

        print(f"Profit Factor : {report.edge.profit_factor}")

        print("=" * 75)