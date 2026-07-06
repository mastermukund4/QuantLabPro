from pathlib import Path
import sys

# --------------------------------------------------
# Add project root to Python path
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(PROJECT_ROOT))

# --------------------------------------------------

from importers.algotest import AlgoTestImporter
from importers.parser import TradeParser

from analytics.weekday import WeekdayAnalyzer


FILE_PATH = "data/raw/algotest/calendar_trade.csv"


def main():

    importer = AlgoTestImporter(FILE_PATH)

    df = importer.load()

    parser = TradeParser()

    trades = parser.parse(df)

    report = WeekdayAnalyzer().analyze(trades)

    print()
    print("=" * 80)
    print("QUANTLAB PRO - WEEKDAY ANALYTICS TEST")
    print("=" * 80)

    for day in report.weekdays:

        print()

        print(f"📅 {day.weekday}")

        print("-" * 80)

        print(f"{'Total Trades':30}: {day.total_trades}")
        print(f"{'Winning Trades':30}: {day.winning_trades}")
        print(f"{'Losing Trades':30}: {day.losing_trades}")

        print(f"{'Gross Profit':30}: ₹{day.gross_profit:,.2f}")
        print(f"{'Gross Loss':30}: ₹{day.gross_loss:,.2f}")
        print(f"{'Net Profit':30}: ₹{day.net_profit:,.2f}")

        print(f"{'Average P&L / Trade':30}: ₹{day.average_pnl:,.2f}")

        print(f"{'Best Trade':30}: ₹{day.best_trade:,.2f}")
        print(f"{'Worst Trade':30}: ₹{day.worst_trade:,.2f}")

        print(f"{'Win Rate':30}: {day.win_rate:.2f}%")
        print(f"{'Profit Factor':30}: {day.profit_factor:.2f}")

    print()
    print("=" * 80)


if __name__ == "__main__":
    main()