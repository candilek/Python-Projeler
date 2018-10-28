print("""
************************************
Kullanıcı Girişi
************************************
""")
sys_kullanıcı_adı="Dilek"
sys_parola="123456"
kullanıcı_adı= input("Kullanıcı Adı: ")
parola= input("Parola: ")

if (kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
    print("parola Hatalı!")
elif (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
    print("Kullanıcı Adı HAtalı!")
elif(kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
    print("Kullanıcı adı ve Parola Hatalı!")
else:
    print("Sisteme başarılı bir şekilde giriş yapıldı...")