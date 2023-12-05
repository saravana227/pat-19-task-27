import openpyxl
from openpyxl import Workbook

# Create a new Excel workbook and select the active sheet
wb = Workbook()
ws = wb.active

# Add headers to the sheet
headers = ["Test ID", "Username", "Password", "Date", "Time", "Tester", "Test Result"]
ws.append(headers)

# Save the workbook
wb.save("test_results.xlsx")