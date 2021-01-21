import csv

with open('filename.csv','r') as csv_out:

    thewriter = csv.DictReader(csv_out)
    with open('outside.csv', 'w') as csv_in:
        filed = ['name','lastname','email']
        thereader = csv.DictWriter(csv_in,fieldnames=filed)

        for line in thewriter:
            thereader.writerows(line)



