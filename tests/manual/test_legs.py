from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from importers.algotest import AlgoTestImporter
from importers.parser import TradeParser

from analytics.legs import LegsAnalyzer


FILE_PATH = "data/raw/algotest/calendar_trade.csv"


def print_group(title, stats):

    print()
    print(title)
    print("-" * 80)

    for item in stats:

        print()
        print(f"Group                 : {item.group_name}")
        print(f"Total Legs            : {item.total_legs}")
        print(f"Winning Legs          : {item.winning_legs}")
        print(f"Losing Legs           : {item.losing_legs}")
        print(f"Gross Profit          : ₹{item.gross_profit:,.2f}")
        print(f"Gross Loss            : ₹{item.gross_loss:,.2f}")
        print(f"Net Profit            : ₹{item.net_profit:,.2f}")
        print(f"Average P&L / Leg     : ₹{item.average_pnl:,.2f}")
        print(f"Best Leg              : ₹{item.best_leg:,.2f}")
        print(f"Worst Leg             : ₹{item.worst_leg:,.2f}")
        print(f"Win Rate              : {item.win_rate:.2f}%")
        print(f"Profit Factor         : {item.profit_factor:.2f}")


def main():

    importer = AlgoTestImporter(FILE_PATH)
    df = importer.load()

    parser = TradeParser()
    trades = parser.parse(df)

    report = LegsAnalyzer().analyze(trades)

    print()
    print("=" * 80)
    print("QUANTLAB PRO - TRADE LEGS ANALYTICS TEST")
    print("=" * 80)

    print_group("OPTION TYPE ANALYSIS", report.option_type_stats)

    print_group("BUY / SELL ANALYSIS", report.buy_sell_stats)

    print()
    print("=" * 80)


if __name__ == "__main__":
    main()