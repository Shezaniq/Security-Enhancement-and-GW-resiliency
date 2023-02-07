import csv
# Open sheet1.csv and read it into a list
with open('sheet1.csv', 'r') as sheet1_file:
    sheet1_reader = csv.reader(sheet1_file)
    sheet1_data = [row for row in sheet1_reader]
# Open sheet2.csv and read it into a list
with open('sheet2.csv', 'r') as sheet2_file:
    sheet2_reader = csv.reader(sheet2_file)
    sheet2_data = [row for row in sheet2_reader]
# Iterate through each row in sheet1_data
for sheet1_row in sheet1_data:
    if 'IKEP-1' in sheet1_row[0]:
        # Iterate through each row in sheet2_data
        for sheet2_row in sheet2_data:
            if sheet1_row[0][:21] == sheet2_row[0][:21]:
                print(sheet2_row[1])

