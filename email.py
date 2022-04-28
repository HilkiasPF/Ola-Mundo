import csv

data = ['João', 'Lucas', 'Maria']
email = {}
count = 0
for c in data:
    email[c] = (f'{c}{count}@email.com')
    count += 1

print(email)
csv_file = 'email.csv'

w = csv.writer(open('email.csv','w'))

for c, n in email.items():
    w.writerow([c, n])