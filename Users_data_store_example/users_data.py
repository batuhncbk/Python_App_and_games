users = {}

while(1):
    sorgu = input("""
    **********************************
    | kişi eklemek için:         e   |
    | kişi sorgulamak için:      s   |
    | çıkış yapmak için:         q   |
    **********************************
    """)

    if (sorgu=="e"):
        numara = input("numara:")
        isim = input("isim:")
        yas = input("yaş:")
        mail = input("mail:")

        users.update({numara:{"isim":isim,"yaş":yas,"mail":mail}})

    elif(sorgu=="s"):
        print(50*"*")
        kisi_sorgu_no = input("Sorgulamak istediğiniz kişinin numarası:")
        print(users[kisi_sorgu_no])

    elif(sorgu=="q"):
        break

    else:
        print("komut dışı karakter girdiniz")
