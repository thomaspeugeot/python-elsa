mdp=int(input("Veuillez saisr le mot de passe"))


if mdp == 1234:
    print("Votre mot de passe est correct")

    nbr=int(input("Donne un chiffre pour afficher sa table :")) # pour demander quelle table et affecter la variable
    nbr2=nbr*2
    nbr3=nbr*3
    nbr4=nbr*4
    nbr5=nbr*5
    nbr6=nbr*6
    nbr7=nbr*7
    nbr8=nbr*8
    nbr9=nbr*9
    nbr10=nbr*10
    print(nbr, nbr2, nbr3, nbr4, nbr5, nbr6, nbr7, nbr8, nbr9, nbr10)

else:
    print("Votre mot de passe est incorrect")




