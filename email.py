import csv

data = ['João', 'Lucas', 'Maria']
email = {}
count = 0
for c in data:
    email[c] = (f'{c}{count}@email.com')
    count += 1
print(email)

w = csv.writer(open('email.csv','w'))
w.writerow(['Nome','e-mail'])

for c, n in email.items():
    w.writerow([c, n])