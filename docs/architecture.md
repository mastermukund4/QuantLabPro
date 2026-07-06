# QuantLab Pro Architecture

**Version:** v1.1.0  
**Status:** Phase 1 Complete  
**Last Updated:** 2026-07-06  

---

## 1. Purpose

QuantLab Pro is a quantitative research platform for options trading strategies.

Its purpose is to convert raw AlgoTest strategy reports into structured analytics, professional Excel reports, and eventually portfolio-level and AI-assisted research.

---

## 2. High-Level Architecture

```text
CSV File
   ↓
AlgoTest Importer
   ↓
DataCleaner
   ↓
TradeParser
   ↓
Trade Objects
   ↓
PerformanceAnalyzer
   ↓
PerformanceReport
   ↓
Console Report + Excel Workbook
```

---

## 3. Import Pipeline

### 3.1 AlgoTest Importer

Location:

```text
importers/algotest.py
```

Responsibility:

- Read AlgoTest CSV files.
- Validate file existence.
- Pass raw dataframe to the cleaner.
- Return a cleaned dataframe.

The importer does not calculate analytics.

---

### 3.2 DataCleaner

Location:

```text
cleaners/data_cleaner.py
```

Responsibility:

- Convert date columns into Python date objects.
- Convert time columns into Python time objects.
- Convert numeric columns into numeric values.
- Normalize AlgoTest CSV quirks before parsing.

This keeps the parser clean and reliable.

---

### 3.3 TradeParser

Location:

```text
importers/parser.py
```

Responsibility:

- Convert cleaned dataframe rows into Trade objects.
- Detect summary rows such as `1.0`, `2.0`, `3.0`.
- Attach leg rows such as `1.1`, `1.2` to the correct Trade.
- Return a list of Trade objects.

---

## 4. Core Data Models

### 4.1 Trade

Location:

```text
models/trade.py
```

Represents one full strategy-level trade.

Contains:

- Trade ID
- Strategy
- Symbol
- Expiry Type
- Entry Date
- Entry Time
- Exit Date
- Exit Time
- Total P&L
- VIX
- Trade legs

---

### 4.2 TradeLeg

Represents one leg of a multi-leg options strategy.

Contains:

- Leg number
- Buy/Sell
- Option type
- Strike
- Quantity
- Entry price
- Exit price
- Leg P&L

---

## 5. Analytics Pipeline

Main orchestrator:

```text
analytics/performance.py
```

The `PerformanceAnalyzer` coordinates all analytics modules.

```text
PerformanceAnalyzer
   ├── ActivityAnalyzer
   ├── ReturnsAnalyzer
   ├── EdgeAnalyzer
   ├── EquityAnalyzer
   ├── DrawdownAnalyzer
   ├── MonthlyAnalyzer
   ├── WeeklyAnalyzer
   ├── WeekdayAnalyzer
   ├── DurationAnalyzer
   ├── StreakAnalyzer
   ├── CalendarAnalyzer
   └── RiskAnalyzer
```

Each analyzer has one responsibility and returns its own report dataclass.

---

## 6. Analytics Modules

### Activity Analytics

Location:

```text
analytics/activity.py
models/activity_report.py
```

Calculates:

- Total trades
- Winning trades
- Losing trades
- Breakeven trades
- Win rate
- Loss rate

---

### Returns Analytics

Location:

```text
analytics/returns.py
models/returns_report.py
```

Calculates:

- Gross profit
- Gross loss
- Net profit
- Average winning trade
- Average losing trade
- Average P&L per trade
- Best trade
- Worst trade

---

### Strategy Edge Analytics

Location:

```text
analytics/edge.py
models/edge_report.py
```

Calculates:

- Payoff ratio
- Profit factor
- Expectancy (R)

---

### Equity Analytics

Location:

```text
analytics/equity.py
models/equity_report.py
```

Calculates:

- Starting capital
- Ending capital
- Trade numbers
- Cumulative P&L
- Equity curve

---

### Drawdown Analytics

Location:

```text
analytics/drawdown.py
models/drawdown_report.py
```

Calculates:

- Maximum drawdown
- Maximum drawdown %
- Current drawdown
- Current drawdown %
- Drawdown curve

---

### Monthly Analytics

Location:

```text
analytics/monthly.py
models/monthly_report.py
```

Calculates month-wise performance.

---

### Weekly Analytics

Location:

```text
analytics/weekly.py
models/weekly_report.py
```

Calculates ISO week-wise performance.

---

### Weekday Analytics

Location:

```text
analytics/weekday.py
models/weekday_report.py
```

Calculates weekday-wise performance.

---

### Duration Analytics

Location:

```text
analytics/duration.py
models/duration_report.py
```

Calculates performance by holding duration buckets.

---

### Streak Analytics

Location:

```text
analytics/streak.py
models/streak_report.py
```

Calculates:

- Longest winning streak
- Longest losing streak
- Average winning streak
- Average losing streak
- Current streak
- Streak-wise P&L

---

### Calendar Analytics

Location:

```text
analytics/calendar.py
models/calendar_report.py
```

Calculates trading-date-wise performance.

---

### Risk Analytics

Location:

```text
analytics/risk/
models/risk_report.py
```

Risk analytics is modular.

```text
analytics/risk/
   ├── sharpe.py
   ├── sortino.py
   ├── calmar.py
   ├── ulcer.py
   ├── recovery.py
   ├── var.py
   ├── kelly.py
   └── risk.py
```

Calculates:

- Standard deviation
- Downside deviation
- Sharpe ratio
- Sortino ratio
- Calmar ratio
- Ulcer index
- Recovery factor
- VaR 95%
- CVaR 95%
- Kelly %
- Half Kelly %

---

## 7. Master Performance Report

Location:

```text
models/performance_report.py
```

The `PerformanceReport` aggregates all analytics reports.

Contains:

- ActivityReport
- ReturnsReport
- EdgeReport
- EquityReport
- DrawdownReport
- MonthlyReport
- WeeklyReport
- WeekdayReport
- DurationReport
- StreakReport
- CalendarReport
- RiskReport

---

## 8. Reporting Pipeline

### Console Report

Location:

```text
services/trade_service.py
```

The console report is an executive summary.

It displays:

- Trading activity
- Returns
- Strategy edge
- Equity
- Drawdown
- Advanced analytics availability

The console does not print detailed monthly, weekly, weekday, duration, streak, calendar, or risk tables.

---

### Excel Export

Location:

```text
exports/excel_exporter.py
```

The Excel workbook is the full research output.

Current sheets:

```text
Dashboard
Performance
Trade Log
Trade Legs
Monthly
Weekly
Weekday
Duration
Streak
Calendar
Risk
```

---

## 9. Excel Sheet Architecture

Each worksheet has its own class.

Location:

```text
exports/sheets/
```

Examples:

```text
dashboard_sheet.py
performance_sheet.py
trade_log_sheet.py
trade_legs_sheet.py
monthly_sheet.py
weekly_sheet.py
weekday_sheet.py
duration_sheet.py
streak_sheet.py
calendar_sheet.py
risk_sheet.py
```

Each sheet class follows this pattern:

```python
class ExampleSheet:

    def build(self, workbook, report):
        ...
```

Some sheets also accept `trades`.

---

## 10. Styling Architecture

Location:

```text
exports/styles/
```

Contains:

```text
colors.py
formatter.py
```

Responsibilities:

- Title formatting
- Header formatting
- Currency formatting
- Percentage formatting
- Auto-width handling

The formatter handles Excel-specific quirks such as merged cells.

---

## 11. Service Layer

Location:

```text
services/trade_service.py
```

The TradeService coordinates the full workflow:

```text
Load CSV
   ↓
Clean data
   ↓
Parse trades
   ↓
Run analytics
   ↓
Print console report
   ↓
Generate Excel report
```

The service layer does not calculate analytics directly.

---

## 12. Manual Testing

Location:

```text
tests/manual/
```

Manual test files exist for standalone analyzer testing.

Examples:

```text
test_weekday.py
test_duration.py
test_streak.py
test_calendar.py
test_risk.py
```

Each test:

- Loads sample CSV data.
- Parses trades.
- Runs one analyzer.
- Prints results for verification.

Production files are not overwritten during standalone testing.

---

## 13. Development Workflow

Every sprint follows this workflow:

```text
Sprint Setup
   ↓
Report Dataclass
   ↓
Analyzer
   ↓
Standalone Test
   ↓
Integration
   ↓
Console Registration
   ↓
Excel Sheet
   ↓
Regression Test
   ↓
Git Commit
   ↓
Git Tag
```

---

## 14. Definition of Done

A sprint is complete only when all items are done:

- Report model created
- Analyzer created
- Standalone test passed
- Integrated into PerformanceAnalyzer
- Added to PerformanceReport
- Added to console advanced analytics section
- Added to Excel workbook
- Regression test passed
- Git commit completed
- Git tag created

---

## 15. Current Architecture Status

Phase 1 Core Analytics is complete.

Completed modules:

- Activity
- Returns
- Strategy Edge
- Equity
- Drawdown
- Monthly
- Weekly
- Weekday
- Duration
- Streak
- Calendar
- Risk

---

## 16. Future Architecture

Future phases will add:

- Strategy analytics
- Portfolio analytics
- Market intelligence
- AI insights
- Web dashboard
- Database layer
- Multiple strategy support

These future features must follow the existing architecture unless a roadmap revision is explicitly approved.

---

## 17. Key Design Principles

1. Never discard imported data.
2. Keep import, cleaning, parsing, analytics, and reporting separate.
3. Every analyzer has one responsibility.
4. Every analyzer returns a report dataclass.
5. Console is for executive summary.
6. Excel is for detailed analytics.
7. Production files are not overwritten during module testing.
8. New ideas go to BACKLOG.md.
9. ROADMAP.md remains the frozen product plan.
10. Every sprint must end in a stable commit.

---

## 18. Revision History

| Version | Description |
|--------|-------------|
| v1.1.0 | Initial architecture documentation after Phase 1 completion |