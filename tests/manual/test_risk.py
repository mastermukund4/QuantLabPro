from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from importers.algotest import AlgoTestImporter
from importers.parser import TradeParser

from analytics.risk.risk import RiskAnalyzer


FILE_PATH = "data/raw/algotest/calendar_trade.csv"


def main():

    importer = AlgoTestImporter(FILE_PATH)
    df = importer.load()

    parser = TradeParser()
    trades = parser.parse(df)

    report = RiskAnalyzer().analyze(trades)

    print()
    print("=" * 80)
    print("QUANTLAB PRO - RISK ANALYTICS TEST")
    print("=" * 80)

    print(f"{'Standard Deviation':35}: ₹{report.standard_deviation:,.2f}")
    print(f"{'Downside Deviation':35}: ₹{report.downside_deviation:,.2f}")
    print(f"{'Sharpe Ratio':35}: {report.sharpe_ratio}")
    print(f"{'Sortino Ratio':35}: {report.sortino_ratio}")
    print(f"{'Calmar Ratio':35}: {report.calmar_ratio}")
    print(f"{'Ulcer Index':35}: {report.ulcer_index}")
    print(f"{'Recovery Factor':35}: {report.recovery_factor}")
    print(f"{'VaR 95%':35}: ₹{report.value_at_risk_95:,.2f}")
    print(f"{'CVaR 95%':35}: ₹{report.conditional_var_95:,.2f}")
    print(f"{'Kelly %':35}: {report.kelly_percent:.2f}%")
    print(f"{'Half Kelly %':35}: {report.half_kelly_percent:.2f}%")

    print("=" * 80)


if __name__ == "__main__":
    main()