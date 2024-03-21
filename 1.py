a=open('products.txt').readlines() # Считали файл
K=[]
for i in range(len(a)):
    K.append(a[i].split(';'))
    K[i][4]=K[i][4][:-1]
K[0].append('total') # добавили новый столбец total
for i in range(1,len(K)):
    K[i].append(str(float(K[i][3])*float(K[i][4]))) #умножели стоимость единицы продукции на количество проданных единиц
print(K)
with open('products_new.csv','w',encoding='utf-8') as F:
    for i in range(len(K)):
        F.writelines(*K[i])