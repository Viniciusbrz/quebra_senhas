# Quebrando senhas básico Python -- _s3cret!

from random import *
import os
u_pwd = input("Digite a sua senha: ")
pwd=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','1','2','3','4','5','6','7','8','9']


pw=""
while(pw!=u_pwd):
    pw=""

    for letter in range(len(u_pwd)):
        guess_pwd = pwd[randint(0,17)]
        pw=str(guess_pwd)+str(pw)
        print (pw)
        print ("Sua senha está sendo quebrada... Aguarde!")
        os.system("cls")

        print("Sua senha é :", pw)


        # Senha vapo vapo