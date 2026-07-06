from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from importers.algotest import AlgoTestImporter
from importers.parser import TradeParser

from analytics.duration import DurationAnalyzer


FILE_PATH = "data/raw/algotest/calendar_trade.csv"


def main():

    importer = AlgoTestImporter(FILE_PATH)
    df = importer.load()

    parser = TradeParser()
    trades = parser.parse(df)

    report = DurationAnalyzer().analyze(trades)

    print()
    print("=" * 80)
    print("QUANTLAB PRO - DURATION ANALYTICS TEST")
    print("=" * 80)

    for duration in report.durations:

        print()
        print(f"⏱️ {duration.bucket}")
        print("-" * 80)

        print(f"{'Total Trades':30}: {duration.total_trades}")
        print(f"{'Winning Trades':30}: {duration.winning_trades}")
        print(f"{'Losing Trades':30}: {duration.losing_trades}")
        print(f"{'Gross Profit':30}: ₹{duration.gross_profit:,.2f}")
        print(f"{'Gross Loss':30}: ₹{duration.gross_loss:,.2f}")
        print(f"{'Net Profit':30}: ₹{duration.net_profit:,.2f}")
        print(f"{'Average P&L / Trade':30}: ₹{duration.average_pnl:,.2f}")
        print(f"{'Best Trade':30}: ₹{duration.best_trade:,.2f}")
        print(f"{'Worst Trade':30}: ₹{duration.worst_trade:,.2f}")
        print(f"{'Win Rate':30}: {duration.win_rate:.2f}%")
        print(f"{'Profit Factor':30}: {duration.profit_factor:.2f}")

    print()
    print("=" * 80)


if __name__ == "__main__":
    main()