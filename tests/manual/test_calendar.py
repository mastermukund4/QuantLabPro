from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from importers.algotest import AlgoTestImporter
from importers.parser import TradeParser

from analytics.calendar import CalendarAnalyzer


FILE_PATH = "data/raw/algotest/calendar_trade.csv"


def main():

    importer = AlgoTestImporter(FILE_PATH)
    df = importer.load()

    parser = TradeParser()
    trades = parser.parse(df)

    report = CalendarAnalyzer().analyze(trades)

    print()
    print("=" * 80)
    print("QUANTLAB PRO - CALENDAR ANALYTICS TEST")
    print("=" * 80)

    print("\nFirst 10 Trading Days")
    print("-" * 80)

    for day in report.days[:10]:
        print(
            f"{day.trading_date} | "
            f"Trades: {day.total_trades} | "
            f"Net P&L: ₹{day.net_profit:,.2f} | "
            f"Win Rate: {day.win_rate:.2f}% | "
            f"PF: {day.profit_factor:.2f} | "
            f"Equity: ₹{day.cumulative_equity:,.2f}"
        )

    print()
    print(f"Total Trading Days: {len(report.days)}")
    print("=" * 80)


if __name__ == "__main__":
    main()