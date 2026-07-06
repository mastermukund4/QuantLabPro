# QuantLab Pro Developer Guide

**Version:** v1.1.0  
**Last Updated:** 2026-07-06

---

# Purpose

This guide explains how to contribute to QuantLab Pro.

It documents the standard development workflow, sprint lifecycle, testing process, integration steps, and release process.

Every new feature should follow this guide.

---

# Development Philosophy

QuantLab Pro is developed using a sprint-based workflow.

Every sprint delivers production-ready software.

No sprint is considered complete until all checklist items are satisfied.

---

# Standard Sprint Workflow

Every sprint follows this sequence.

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
        ↓
Release
```

This workflow must not be skipped.

---

# Sprint Setup

Every sprint begins with a single terminal command that creates the required folders and files.

Example:

```bash
mkdir -p analytics/example \
&& touch \
analytics/example.py \
models/example_report.py \
tests/manual/test_example.py \
exports/sheets/example_sheet.py
```

The setup command eliminates repetitive manual file creation.

---

# Creating a New Analytics Module

Every analytics module follows the same architecture.

Example:

```text
analytics/
    example.py

models/
    example_report.py

tests/manual/
    test_example.py

exports/sheets/
    example_sheet.py
```

Never mix multiple analytics into one module.

---

# Creating the Report

Every analyzer returns a dedicated dataclass.

Example

```python
@dataclass
class ExampleReport:
    ...
```

Reports should contain only data.

Business logic belongs in analyzers.

---

# Creating the Analyzer

Responsibilities:

- Perform calculations
- Return one report object
- No printing
- No Excel generation
- No CSV reading

Example

```python
class ExampleAnalyzer:

    def analyze(self, trades):

        ...

        return ExampleReport(...)
```

---

# Standalone Testing

Every analyzer receives its own standalone test.

Location

```text
tests/manual/
```

Pattern

```text
Load CSV
↓

Parse Trades
↓

Run Analyzer
↓

Print Results
```

Standalone testing always occurs before production integration.

---

# Production Integration

After standalone testing succeeds:

Update

```text
PerformanceAnalyzer

↓

PerformanceReport
```

No other production files should change unless required.

---

# Console Integration

If appropriate, register the module under:

```text
Advanced Analytics
```

The console provides only an executive summary.

Avoid printing detailed tables.

---

# Excel Integration

Create one worksheet class.

Pattern

```python
class ExampleSheet:

    def build(self, workbook, report):
        ...
```

Then register the sheet in

```text
exports/excel_exporter.py
```

---

# Regression Testing

After integration:

```bash
python3 app.py
```

Regression testing is mandatory.

Production must remain stable.

---

# Git Workflow

Every sprint ends with:

```bash
git add .

git commit -m "Sprint X - Module"

git tag sprint-X

git push

git push origin sprint-X
```

Major milestones also receive semantic version tags.

Example

```text
v1.0.0
v1.1.0
```

---

# Documentation

Documentation is part of the product.

Whenever architecture changes:

Update

- Architecture.md
- FolderStructure.md
- CodingStandards.md
- DeveloperGuide.md

Documentation should never become outdated.

---

# Roadmap Discipline

ROADMAP.md defines the approved project plan.

During implementation:

- Do not expand scope.
- Do not redesign architecture.
- Do not introduce unrelated features.

Future ideas belong in:

```text
BACKLOG.md
```

Backlog items are reviewed later.

---

# Definition of Done

A sprint is complete only when all items below are complete.

- Report dataclass
- Analyzer
- Standalone test
- Production integration
- Console registration
- Excel sheet
- Regression test
- Git commit
- Git tag

---

# Project Versioning

QuantLab Pro uses two parallel versioning systems.

## Sprint Tags

Examples

```text
sprint-1
sprint-2
sprint-3
```

Sprint tags capture incremental progress.

---

## Release Versions

Examples

```text
v1.0.0

v1.1.0

v2.0.0
```

Release versions represent stable project milestones.

---

# Current Architecture

Phase 1 has established the following architecture.

```text
CSV
 │
 ▼
Importer
 │
 ▼
DataCleaner
 │
 ▼
TradeParser
 │
 ▼
Trade Objects
 │
 ▼
PerformanceAnalyzer
 │
 ├── Activity
 ├── Returns
 ├── Edge
 ├── Equity
 ├── Drawdown
 ├── Monthly
 ├── Weekly
 ├── Weekday
 ├── Duration
 ├── Streak
 ├── Calendar
 └── Risk
 │
 ▼
PerformanceReport
 │
 ├── Console
 └── Excel Workbook
```

Future development should extend this architecture rather than replace it.

---

# Engineering Principles

The project follows these principles.

1. Build production-quality software.
2. Prefer clarity over cleverness.
3. Keep modules independent.
4. Test before integration.
5. Never overwrite production code during testing.
6. Freeze the roadmap.
7. Capture future ideas in BACKLOG.md.
8. Finish every sprint with a stable release.

---

# Revision History

| Version | Description |
|----------|-------------|
| v1.1.0 | Initial developer guide |