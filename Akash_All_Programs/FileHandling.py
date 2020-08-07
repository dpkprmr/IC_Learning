# file = open("D:\FileHandling\FileRead.txt",'r')
# print(file.read())
# print()
#
#
# file = open("D:\FileHandling\FileRead.txt",'r')
# print(file.read(5))
# print(file.readlines())
#
#
# # file = open("D:\FileHandling\FileRead.txt",'w')
# # file.write("Oeverwritten")
# # print(file.read(5))
# # print(file.readlines())
#
# # file = open("D:\FileHandling\Pycharmcreate.txt",'x')
# # file.write("Created by Pycharm")
# # file.close()
# # print(file.read(5))
# # print(file.readlines())
#
# file =open("D:\FileHandling\Pycharmcreate.txt",'a')
# file.write("     "  "Appended again ")
#
# file = open("D:\FileHandling\Pycharmcreate.txt",'r')
# print(file.read())
#
# import os
# if os.path.exists("FileRead.txt"):
#  os.remove("FileRead.txt")
# else:
#  print("file do not exist")
#  # os.rmdir("myfolder")

print("---------------------EXCEL--------------------")
import pandas as pd
import xlrd

# print(pd.__version__)
# print(pd.read_excel("D:\PycharmExcel.xlsx"))
# print(pd.read_excel("D:\PycharmExcel.xlsx", usecols="A:C",index_col=0))
# print(pd.read_excel("D:\PycharmExcel.xlsx", usecols=[0,3]))
# print(pd.read_excel("D:\PycharmExcel.xlsx", sheet_name=1,skiprows=[1,2]))
#
# print(pd.read_excel("D:\PycharmExcel.xlsx", sheet_name=1))
#
#
# sheet = pd.read_excel("D:\PycharmExcel.xlsx", sheet_name=1)

workbook = xlrd.open_workbook("D:\PycharmExcel.xlsx")

sheet = workbook.sheet_by_name("Sheet1")
# print(sheet.cell(0,0).value)
#
# print(sheet.nrows)
# print(sheet.ncols)
# for rows1 in range(sheet.ncols):
#  print(sheet.cell(0,rows1).value)

# i = 0
# j=0
# while(i<=sheet.nrows):
#  while(j<=sheet.ncols):
#  # for rows in range(sheet.ncols):
#   y = sheet.cell(i, j).value
#   print(y)
#   j=j+1
#  i=i+1

data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
print(data[0][0])

# i=0
# j=0
# while(i<=sheet.nrows):
#  i=i+1
#  while(j<=sheet.ncols):
#
#   print(data[i][j])
#   j=j+1



