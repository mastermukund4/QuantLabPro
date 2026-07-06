from openpyxl import Workbook

from exports.sheets.dashboard_sheet import DashboardSheet
from exports.sheets.performance_sheet import PerformanceSheet
from exports.sheets.trade_log_sheet import TradeLogSheet
from exports.sheets.trade_legs_sheet import TradeLegsSheet

from exports.sheets.monthly_sheet import MonthlySheet
from exports.sheets.weekly_sheet import WeeklySheet
from exports.sheets.weekday_sheet import WeekdaySheet
from exports.sheets.duration_sheet import DurationSheet
from exports.sheets.streak_sheet import StreakSheet
from exports.sheets.calendar_sheet import CalendarSheet


class ExcelExporter:

    def export(self, report, trades):

        workbook = Workbook()

        workbook.remove(workbook.active)

        DashboardSheet().build(workbook, report)
        PerformanceSheet().build(workbook, report)
        TradeLogSheet().build(workbook, trades)
        TradeLegsSheet().build(workbook, trades)

        MonthlySheet().build(workbook, report)
        WeeklySheet().build(workbook, report)
        WeekdaySheet().build(workbook, report)
        DurationSheet().build(workbook, report)
        StreakSheet().build(workbook, report)
        CalendarSheet().build(workbook, report)

        workbook.save("exports/QuantLab_Report.xlsx")

        print("\n✅ Excel workbook created successfully.")