# QuantLab Pro Coding Standards

**Version:** v1.1.0  
**Last Updated:** 2026-07-06

---

# Purpose

This document defines the official coding standards for QuantLab Pro.

Every contribution to the project must follow these standards to ensure consistency, readability, and maintainability.

---

# 1. General Principles

- Readability is more important than cleverness.
- Prefer explicit code over implicit behavior.
- One responsibility per class.
- One responsibility per function.
- Avoid unnecessary abstractions.
- Production stability is more important than optimization.

---

# 2. Naming Conventions

## Files

Use lowercase with underscores.

Examples:

```text
trade_service.py
performance_report.py
monthly_sheet.py
```

Never use:

```text
TradeService.py
MonthlySheet.py
```

---

## Classes

Use PascalCase.

Examples:

```python
TradeService
PerformanceAnalyzer
MonthlyAnalyzer
RiskSheet
TradeParser
```

---

## Functions

Use snake_case.

Examples:

```python
analyze()

build()

parse()

load()

calculate()

export()
```

---

## Variables

Use descriptive names.

Good

```python
gross_profit

current_drawdown

winning_trades
```

Avoid

```python
gp

cd

x

temp
```

---

# 3. Dataclasses

All report objects should be dataclasses.

Example

```python
@dataclass
class MonthlyReport:
    months: list[MonthStats]
```

Business logic must not exist inside dataclasses.

---

# 4. Analyzer Standards

Each analyzer:

- Performs one responsibility.
- Returns one report object.
- Never writes files.
- Never prints output.
- Never reads CSV directly.

Pattern

```python
Analyzer

↓

Report
```

---

# 5. Sheet Standards

Each worksheet must have its own class.

Pattern

```python
class MonthlySheet:

    def build(self, workbook, report):
        ...
```

Responsibilities

- Write worksheet
- Apply formatting
- No calculations

---

# 6. Import Order

Always follow this order.

1. Standard Library

```python
from pathlib import Path
import statistics
```

2. Third-party

```python
import pandas as pd
from openpyxl import Workbook
```

3. Local Imports

```python
from analytics.monthly import MonthlyAnalyzer
```

---

# 7. Type Hints

Use type hints where practical.

Example

```python
def analyze(self, trades):
```

Dataclasses should use explicit types.

---

# 8. Formatting

Follow PEP 8.

Guidelines

- Four spaces
- Blank lines between logical sections
- Descriptive comments
- No excessively long functions

---

# 9. Error Handling

Raise explicit exceptions.

Example

```python
FileNotFoundError
ValueError
```

Do not silently ignore errors.

---

# 10. Testing

Every analytics module requires:

- Standalone manual test
- Regression through app.py

Production code must not be modified solely for testing.

---

# 11. Excel Standards

Each worksheet:

- One file
- One class
- One build() method

Formatting should be reusable.

---

# 12. Git Standards

Every sprint ends with:

```bash
git add .

git commit -m "Sprint X - Module"

git tag sprint-X

git push

git push origin sprint-X
```

Major milestones receive version tags.

Example

```text
v1.0.0
v1.1.0
```

---

# 13. Documentation

Architecture changes require documentation updates.

The following documents must remain current.

- Architecture.md
- FolderStructure.md
- CodingStandards.md
- DeveloperGuide.md

---

# 14. Roadmap Discipline

ROADMAP.md is frozen.

New ideas belong in:

```text
BACKLOG.md
```

Do not expand sprint scope during implementation.

---

# 15. Development Philosophy

QuantLab Pro follows these principles.

- Build incrementally.
- Test before integration.
- Keep modules independent.
- Prefer maintainability over shortcuts.
- Deliver production-ready code at every sprint.

---

# Revision History

| Version | Description |
|----------|-------------|
| v1.1.0 | Initial coding standards |