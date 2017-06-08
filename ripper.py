import csv
with open('csvs/ripper.csv', 'r') as csvfile:
    our_reader = csv.reader(csvfile)
    data = [row for row in our_reader]

#new_row = ['ID', 'index','journal','date', 'text']
#data.append(new_row)
#print(data[-1])

with open('csvs/ripper.csv', 'r') as csvfile:
     our_reader = csv.reader(csvfile)
     all_texts = [column[4] for column in our_reader]
print(all_texts)

with open('csvs/ripper.csv', 'w') as fout:
    csvwriter = csv.writer(fout)
    csvwriter.writerow(map(str.lower, all_texts))
