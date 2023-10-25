password = "rules"
user = "python"
times = 1
while times <= 5:
    u_user = input("Anna käyttäjätunnus: ")
    u_pass = input("Anna salasana: ")
    if u_user != user or u_pass != password:
        times += 1
        print("Pääsy evätty.")
    else:
        print("Tervetuloa")
        break
