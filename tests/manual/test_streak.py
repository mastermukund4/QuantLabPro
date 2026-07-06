from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from importers.algotest import AlgoTestImporter
from importers.parser import TradeParser

from analytics.streak import StreakAnalyzer


FILE_PATH = "data/raw/algotest/calendar_trade.csv"


def main():

    importer = AlgoTestImporter(FILE_PATH)
    df = importer.load()

    parser = TradeParser()
    trades = parser.parse(df)

    report = StreakAnalyzer().analyze(trades)

    print()
    print("=" * 80)
    print("QUANTLAB PRO - STREAK ANALYTICS TEST")
    print("=" * 80)

    print(f"{'Longest Winning Streak':35}: {report.longest_winning_streak}")
    print(f"{'Longest Losing Streak':35}: {report.longest_losing_streak}")
    print(f"{'Average Winning Streak':35}: {report.average_winning_streak}")
    print(f"{'Average Losing Streak':35}: {report.average_losing_streak}")
    print(f"{'Total Winning Streaks':35}: {report.total_winning_streaks}")
    print(f"{'Total Losing Streaks':35}: {report.total_losing_streaks}")
    print(f"{'Current Streak Type':35}: {report.current_streak_type}")
    print(f"{'Current Streak Length':35}: {report.current_streak_length}")
    print(f"{'Largest Winning Streak P&L':35}: ₹{report.largest_winning_streak_pnl:,.2f}")
    print(f"{'Largest Losing Streak P&L':35}: ₹{report.largest_losing_streak_pnl:,.2f}")

    print()
    print("First 10 Streaks")
    print("-" * 80)

    for streak in report.streaks[:10]:
        print(
            f"{streak.streak_type:<10} | "
            f"Length: {streak.length:<3} | "
            f"P&L: ₹{streak.pnl:,.2f}"
        )

    print()
    print("=" * 80)


if __name__ == "__main__":
    main()