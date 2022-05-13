from selenium import webdriver as wbd
from selenium.webdriver.common.by import By


driver = wbd.Chrome()
driver.get('https://www.python.org/')
text = driver.find_element(By.XPATH,'/html/body/div/div[3]/div/section/div[3]/div[2]/div/ul')

texto = text.text
driver.close()

lista = []
txt = open('info.txt', 'at')
txt.write(texto)
txt.close()
h = open('info.txt','rt')
for c in h:
    lista.append(c.replace('\n',' '))
h.close()
count = 0
dict = {}
for c in range(len(lista)//2):
    dict[c] = [lista[count], lista[count+1]]
    count+= 2
print(lista)
print(dict)

novo = open('novo.txt', 'at')
for c in dict.items():
    novo.write(f'{str(c)}\n')
novo.close()
