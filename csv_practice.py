import csv

#with open('csvs/basic.csv', 'r') as csvfile:
    #our_reader = csv.reader(csvfile)
    #names = [row for row in our_reader]

#print(names[0][3])

#len(names)

# find the length of each first name
#for row in names:
    #print(len(row[2]))

# find the longest first name
#longest = ""
#for row in names:
    #if len(row[2]) > len(longest):
        #longest = row[2]
#print(longest)

# construct a new list consisting of only the last names we have here.
#last_names = [column[1] for column in names]
#last_names.reverse()
#print(last_names)

#new_row = [2, 'wayne','graham','meh']
#names.append(new_row)
#print(names)

#new_row2 = [3, 'Victoria','Davis','trying']
#names.append(new_row2)
#print(names)

#a_row = [4, 'fox', 'eliza,' 'too cool']
#print(names + a_row)

with open('csvs/practice.csv', 'w') as fout:
    csvwriter = csv.writer(fout)
    for i in range(0, 100, 10):
        csvwriter.writerow([i + 5, i + 10, i +15, i + 20, i + 25, i + 30])

with open('csvs/practice.csv', 'r') as fin:
    our_reader = csv.reader(fin)
    data = [row for row in our_reader]
    print(data)
