print("""********\n 3' e bölünen sayıları bulan program \n************""")
liste=[]
for i in range(1,101):
    if(i%3 != 0):
        continue
    else:
        liste.append(i)
print(liste)

