import csv
from datetime import date

input_file = open('Birmingham_unclean.csv', 'r')
output_file = open('Birmingham_clean.csv', 'w')

reader = csv.reader(input_file)
writer = csv.writer(output_file)

start = date(1960, 03, 15)

for row in reader:
    # write header
    if row[0] == 'STATION':
        writer.writerow(row)

    # garbage row (TMIN TMAX are -9999):
    elif row[4] == '-9999'and row[5] == '-9999':
        pass

    # normal row:
    else:
        # find days elapsed since 1960
        end = date(int(row[2][:4]), int(row[2][4:6]), int(row[2][6:]))
        day = (end - start).days

        # if good TAVG, write row as-is with days elapsed
        if row[3] != '-9999':
            writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], str(day)])
        # if bad TAVG, write row with good TAVG with days elapsed
        else:
            avg = (float(row[4]) + (float(row[5]))) / 2
            writer.writerow([row[0], row[1], row[2], str(avg), row[4], row[5], str(day)])
    
input_file.close()
output_file.close()
