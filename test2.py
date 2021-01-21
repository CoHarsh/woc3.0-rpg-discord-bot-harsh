import csv
import pandas as pd

h1 = 'harsh492'
df = pd.read_csv('filename.csv')
cols = df['Id']
hp1 = df['HP']
print(cols[0])
id = 'harsh492'
hp = 100 
lent = 2
for i in range(lent):
    if(cols[i] == id):
        hp  = hp1[i]
    else:
        print("loose")

print(hp)
print(len(cols))

# with open('filename.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     with open('new_names.csv', 'w') as new_file:
#         fieldnames = ['Id', 'HP','XP','Class']

#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')

#         # csv_writer.writeheader()

#             # del line['email']
#         for line in csv_reader:
#             csv_writer.writerow(line)
