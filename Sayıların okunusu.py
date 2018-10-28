birler=[" ","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar=[" ","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

def SayıOkunuşu(sayı):
    birler_bas =sayı % 10
    onlar_bas =sayı // 10
    return onlar[onlar_bas]+" "+ birler[birler_bas]

sayı=int(input("sayı girin: "))
print("Sayının okunşu: ",SayıOkunuşu(sayı))