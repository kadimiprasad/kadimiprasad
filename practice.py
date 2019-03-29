import xlsxwriter
workbook = xlsxwriter.Workbook('detailsx5.xlsx')
worksheet = workbook.add_worksheet()
details= ([116789, "karthik"],[116799,  "suraj"],[116768,  "kranthi"],[11671723 ,"prasad"],)
row = 0
col = 0
for empid,name in details:
    worksheet.write(row, col,empid)
    worksheet.write(row, col + 1, name)
    row =row +1
workbook.close()