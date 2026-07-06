# QuantLab Pro Folder Structure

**Version:** v1.1.0  
**Last Updated:** 2026-07-06

---

# Purpose

This document explains the responsibility of every major folder in QuantLab Pro.

Each folder has a single responsibility and should not contain unrelated functionality.

---

# Root Structure

```text
QuantLabPro/
│
├── analytics/
├── cleaners/
├── config/
├── data/
├── docs/
├── exports/
├── importers/
├── models/
├── services/
├── tests/
│
├── app.py
├── ROADMAP.md
├── BACKLOG.md
├── README.md
└── requirements.txt
```

---

# analytics/

Purpose

Contains all analytical calculations.

No file inside this folder should read CSV files or generate Excel reports.

Responsibilities

- Calculate metrics
- Aggregate statistics
- Produce report objects

Current Modules

```text
activity.py
returns.py
edge.py
equity.py
drawdown.py
monthly.py
weekly.py
weekday.py
duration.py
streak.py
calendar.py
performance.py
```

---

# analytics/risk/

Purpose

Contains modular financial risk calculations.

```text
risk.py
sharpe.py
sortino.py
calmar.py
ulcer.py
recovery.py
var.py
kelly.py
```

Each file implements one mathematical concept.

---

# cleaners/

Purpose

Normalize imported data before parsing.

Responsibilities

- Date conversion
- Time conversion
- Numeric conversion
- Missing value handling
- CSV normalization

Cleaners never calculate analytics.

---

# config/

Purpose

Central configuration for QuantLab Pro.

Examples

- Strategy Name
- Symbol
- Expiry Type
- Starting Capital
- File Paths
- Application Settings

Avoid hardcoding constants throughout the project.

---

# data/

Purpose

Contains datasets.

Suggested structure

```text
data/

raw/
processed/
sample/
```

Raw data should never be modified.

---

# docs/

Purpose

Official project documentation.

Contains

```text
Architecture.md
FolderStructure.md
CodingStandards.md
DeveloperGuide.md
```

Documentation must evolve with the project.

---

# exports/

Purpose

Generate output files.

Responsibilities

- Excel creation
- Future PDF reports
- Future HTML reports

No analytics should be calculated here.

---

# exports/sheets/

Purpose

One worksheet class per worksheet.

Current Sheets

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

Each sheet has one responsibility.

---

# exports/styles/

Purpose

Reusable Excel styling.

Examples

```text
formatter.py
colors.py
```

All formatting logic belongs here.

---

# importers/

Purpose

Load external data.

Responsibilities

- Read CSV
- Validate files
- Pass cleaned dataframe to parser

Importers never calculate analytics.

---

# models/

Purpose

Dataclasses representing project entities.

Contains

- Trade models
- Report models
- PerformanceReport

Models contain data only.

No business logic.

---

# services/

Purpose

Coordinate the application workflow.

Current Service

```text
trade_service.py
```

Responsibilities

- Load
- Parse
- Analyze
- Print
- Export

Services orchestrate work.

They do not perform calculations.

---

# tests/

Purpose

Testing infrastructure.

Current Layout

```text
tests/

manual/
```

Future

```text
unit/
integration/
performance/
```

---

# tests/manual/

Purpose

Standalone analyzer verification.

Examples

```text
test_weekday.py
test_duration.py
test_streak.py
test_calendar.py
test_risk.py
```

Every new analytics module should have a manual test before production integration.

---

# Root Files

## app.py

Application entry point.

---

## ROADMAP.md

Frozen development roadmap.

Only updated through explicit roadmap revisions.

---

## BACKLOG.md

Repository of future ideas.

Good ideas go here instead of changing the roadmap.

---

## README.md

Project overview and quick start.

---

## requirements.txt

Python dependencies.

---

# Folder Responsibilities

| Folder | Responsibility |
|---------|----------------|
| analytics | Business calculations |
| cleaners | Data normalization |
| config | Application configuration |
| data | Input datasets |
| docs | Project documentation |
| exports | Report generation |
| importers | Data loading |
| models | Dataclasses |
| services | Workflow orchestration |
| tests | Verification |

---

# Folder Design Principles

1. One responsibility per folder.
2. No circular dependencies.
3. Keep analytics independent from reporting.
4. Keep models free from business logic.
5. Keep services lightweight.
6. Documentation belongs inside `docs/`.
7. Tests must never overwrite production code.
8. Future modules should follow the existing folder structure.

---

# Revision History

| Version | Description |
|----------|-------------|
| v1.1.0 | Initial folder structure documentation |