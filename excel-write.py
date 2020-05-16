import openpyxl 

# Excelファイルを開く
filename = "test.xlsx"
book = openpyxl.load_workbook(filename)

# アクティブになっているシートを得る
#sheet = book.active
sheet = book.worksheets[0]

# 書き込む
sheet['A4'] = "Total"
sheet['C4'] = "total"

# 書き込んだ内容をファイルへ保存
filename = "test-write.xlsx"
book.save(filename)
print("ok")

