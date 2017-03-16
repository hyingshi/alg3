import csv

input_file = open('Birmingham.csv', 'r')
output_file = open('Birmingham_clean.csv', 'w')

reader = csv.reader(input_file)
writer = csv.writer(output_file)

for row in reader:
    if row[0] == 'STATION' or row[3] != '-9999':
        writer.writerow(row)
    else:
        avg = (float(row[4]) + (float(row[5]))) / 2
        writer.writerow([row[0], row[1], row[2], str(avg), row[4], row[5]])

input_file.close()
output_file.close()
