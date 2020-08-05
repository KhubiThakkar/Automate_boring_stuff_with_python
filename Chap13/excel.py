import openpyxl
wb  = openpyxl.load_workbook('example.xlsx')
print(wb.sheetnames)
sheet = wb['Sheet3']
print(sheet)
print(type(sheet))
print(sheet.title)
anothersheet = wb.active
print(anothersheet)