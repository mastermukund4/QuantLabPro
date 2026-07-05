from openpyxl import Workbook

from exports.sheets.dashboard_sheet import DashboardSheet
from exports.sheets.performance_sheet import PerformanceSheet
from exports.sheets.trade_log_sheet import TradeLogSheet
from exports.sheets.trade_legs_sheet import TradeLegsSheet


class ExcelExporter:

    def export(self, report, trades):

        workbook = Workbook()

        workbook.remove(workbook.active)

        DashboardSheet().build(workbook, report)

        PerformanceSheet().build(workbook, report)

        TradeLogSheet().build(workbook, trades)

        TradeLegsSheet().build(workbook, trades)

        workbook.save("exports/QuantLab_Report.xlsx")

        print("\n✅ Excel workbook created successfully.")