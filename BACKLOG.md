# QuantLab Pro Backlog

This document contains ideas, improvements and future enhancements that are **intentionally deferred**.

## Rules

- Items in this document do **not** change the current roadmap.
- They will be reviewed only after the current phase is completed.
- Critical bug fixes are **not** backlog items and may be implemented immediately.
- Every backlog item receives a unique ID.

---

# Status Legend

- 💡 Idea
- 🔍 Under Review
- 📅 Planned
- ✅ Implemented
- ❌ Rejected

---

# Architecture

## BL-001 💡
### MasterReport Aggregator

Create a top-level report object that aggregates:

- ActivityReport
- ReturnsReport
- StrategyEdgeReport
- EquityReport
- DrawdownReport
- MonthlyReport
- WeeklyReport
- WeekdayReport
- DurationReport
- StreakReport
- CalendarReport
- RiskReport

**Reason for deferral**

The current architecture supports the roadmap through Phase 1.

A MasterReport becomes significantly more valuable when multiple strategies and portfolio analytics are introduced in Phase 3.

**Target Phase**

Phase 3 – Portfolio Engine

---

# Data Layer

No items.

---

# Analytics

No items.

---

# Excel Reporting

No items.

---

# AI

No items.

---

# Future Integrations

No items.

---

# Notes

Whenever a new idea is proposed during development:

1. Assign a new Backlog ID.
2. Record the idea here.
3. Continue following the frozen roadmap.

---

## BL-002 💡
### Never Overwrite Production Files During Module Testing

**Description**

Module testing must never replace or modify production workflow files such as:

- `services/trade_service.py`
- `app.py`
- `analytics/performance.py` (unless the sprint specifically integrates the module)

Instead, every sprint should use dedicated test runners.

Example:

```
tests/
    manual/
        test_monthly.py
        test_weekly.py
        test_weekday.py
        test_duration.py
        test_streak.py
```

Each test runner should:

1. Import the module under development.
2. Load sample trades.
3. Execute only that analyzer.
4. Print results for verification.

Only after successful standalone testing should the analyzer be integrated into the production workflow.

**Benefits**

- Production code always remains runnable.
- Testing is isolated from production.
- Regression testing becomes simpler.
- Lower risk of accidental overwrites.
- Cleaner Git history.

**Reason for Deferral**

The current roadmap remains unchanged. This process improvement will be implemented after the completion of **Phase 1 – Core Analytics**, when we standardize the testing framework.

**Target Phase**

After Phase 1 – Core Analytics

---

## BL-003 💡
### Project Documentation Sprint

**Description**

After the successful completion of **Phase 1 – Core Analytics**, dedicate one sprint exclusively to documenting the project.

The objective is to ensure that QuantLab Pro is self-documenting, maintainable, and easy for future contributors (or ourselves months later) to understand.

### Deliverables

```
docs/

Architecture.md
FolderStructure.md
CodingStandards.md
DeveloperGuide.md
```

### Document Scope

#### Architecture.md

- High-level system architecture
- Data flow
- Analytics pipeline
- Excel export architecture
- Module dependency diagram

---

#### FolderStructure.md

Explain every major folder.

Example:

```
analytics/
cleaners/
config/
data/
exports/
importers/
models/
services/
tests/
docs/
```

---

#### CodingStandards.md

Development conventions such as:

- Naming conventions
- File structure
- Class design
- Function length guidelines
- Dataclass standards
- Error handling
- Type hints
- Import order
- Formatting standards

---

#### DeveloperGuide.md

Guide for future development.

Topics:

- How to add a new analytics module
- How to create a report model
- How to add an Excel sheet
- How to integrate into PerformanceAnalyzer
- Testing workflow
- Git workflow
- Release workflow

### Benefits

- Easier maintenance
- Consistent architecture
- Faster onboarding
- Better long-term scalability
- Reduced technical debt

### Reason for Deferral

Documentation should reflect a stable architecture. Completing it after **Phase 1 – Core Analytics** ensures the core analytics framework is mature enough to document accurately.

### Target Phase

Immediately after **Phase 1 – Core Analytics**, before starting **Phase 2 – Strategy Analytics**.

---

## BL-004 💡
### Advanced Professional Risk Metrics

**Description**

Extend the Risk Analytics engine with additional institutional-grade risk metrics.

### Proposed Metrics

#### Consecutive Risk

- Maximum Consecutive Profit (₹)
- Maximum Consecutive Loss (₹)

#### Performance Ratios

- Return / Drawdown Ratio
- Gain-to-Pain Ratio
- Expectancy Score (Normalized)

### Benefits

- Better strategy comparison
- Improved portfolio optimization
- Institutional-quality reporting
- Supports AI strategy ranking

### Reason for Deferral

Current Sprint 7 already satisfies the roadmap definition of "Risk Analytics."

These metrics enhance the module but are not required to complete Phase 1.

### Target Phase

Phase 2 — Strategy Analytics