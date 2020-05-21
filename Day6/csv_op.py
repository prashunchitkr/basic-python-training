import csv

subject = ['name', 'python', 'data_structure', 'physics']
mark = ['genzo', 30, 32, 40]

# first making csv file with the title
with open('marksheet.csv', 'w') as f:
    csv_writer = csv.writer(f, delimiter=',')
    csv_writer.writerow(subject)


marks = [
    ['john', 12, 23, 43],
    ['andrew', 32, 43, 12],
    ['angel', 80, 80, 80]
]

# append in a csv file
with open('marksheet.csv', 'a') as f:
    csv_writer = csv.writer(f, delimiter=',')
    csv_writer.writerows(marks)

#read from csv file
with open('marksheet.csv', 'r') as f:
    csv_reader = list(csv.reader(f, delimiter=','))
    for i in csv_reader:
        print(i)

with open('marksheet.csv', 'r+') as f:
    f.read()
    print(f.tell())
    csv_writer = csv.writer(f, delimiter=',')

# write in csv using dictionary
with open('marksheet.csv', 'w') as f:
    csv_writer = csv.DictWriter(f, delimiter=',', fieldnames=['name', 'math'])
    data = {'name': 'john', 'math': 40}
    csv_writer.writerow(data)

