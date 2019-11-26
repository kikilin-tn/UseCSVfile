import csv

#寫入一個csv檔案,可收納name, count兩欄位字典的資料
with open('sample.csv', 'w', newline = '') as csv_file: #windows的情況下要加newline引述傳入空白字串
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    writer.writeheader()
 
    writer.writerow({'Name': 'A','Count':2}) 
    writer.writerow({'Name': 'B','Count':2}) 
    writer.writerow({'Name': 'C','Count':3})
"""
測試如何讓使用者輸入資料
    for i in range(3):
        name = input('input something for name\n')
        num = input('input integer for count\n')
        writer.writerow({'Name': name,'Count': num}) 
"""
with open ('sample.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])
