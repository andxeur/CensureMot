from module import verifier_mot_censurer,taux_similarite

phrase = input("Entrez du texte : ")
verifier_mot_censurer(phrase)

print(f"le taux de similarite entre m*rde et merde est de : {taux_similarite("m*rde", "merde")}%")
