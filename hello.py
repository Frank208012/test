import xlrd
import matplotlib.pyplot as plt

print("hello world")
name = input()
print("hello", name)


xls_path = "C:\\zPYWorkSpace\\pythonThree\\test.xlsx"
workbook = xlrd.open_workbook(xls_path)
data_sheet = workbook.sheets()[0]

rowNum = data_sheet.nrows
colNum = data_sheet.ncols


print(rowNum)
print(colNum)

head = []
itemInfo = [[0] * colNum] * (rowNum - 1)
print(itemInfo)

for i in range(0,colNum):
    print(i, end="")
    head.append(data_sheet.cell_value(0, i))
print("")


for j in range(1, rowNum):
    print(j, end=""),
    for i in range(0,colNum):
        print(i, end=""),
        itemInfo[j-1][i] = data_sheet.cell_value(j, i)
    print("")

print(head)
print(itemInfo)

plt.plot([1,2,3],[4,5,6],'ro')
plt.show()