um = input("")
dois = input("")
tres = input("")

if um == "vertebrado":
    if dois == "ave":
        if tres == "carnivoro":
            print("aguia")
        
        if tres == "onivoro":
            print("pomba")
    
    if dois == "mamifero":
        if tres == "onivoro":
            print ("homem")
    
        if tres == "herbivoro":
            print ("vaca")
    

if um == "invertebrado":
    if dois == "inseto":
        if tres == "hematofago":
            print ("pulga")

        if tres  == "herbivoro":
            print ("lagarta")   

    if dois == "anelideo":
        if tres == "hematofago":
            print("sanguessuga")

        if tres == "onivoro":
            print ("minhoca")