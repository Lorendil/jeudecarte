class JeuDeCartes(object):
    """Permet de créer un jeu de carte et d'interagir avec. Pour respecter l'exercice demandé, je n'ai pas créé de classe "Carte" qui aurait à mon sens aurait été plus simple à gérer"""
    def __doc__():
        """"C'est un programme"""
    
    def __init__(self):
        self.cartes = []
        listevaleur = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        listecouleur = [0,1,2,3]
        for j in range (len(listecouleur)):
            for i in range(len(listevaleur)):
                carte=(listevaleur[i],listecouleur[j])
                self.cartes.append(carte)
        
    def nom_carte(self,n):
        """Fonction permettant d'afficher une carte"""
        numero = self.cartes[n][0]-2
        couleur = self.cartes[n][1]
        listevaleur = [2,3,4,5,6,7,8,9,10,"Valet","Dame","Roi","As"]
        listecouleur = ["Coeur","Carreau","Trèfle","Pique"]
        print("{} de {}".format(listevaleur[numero],listecouleur[couleur]))
    
    def battre(self):
        """Permet de rendre aléatoire les cartes de la liste"""
        import random
        random.shuffle(self.cartes)

    def tirer(self):
        """Permet de tirer une carte s'il en reste une"""
        for n in range(len(self.cartes)):
            self.nom_carte(n)                

    def affiche_liste(self):
        """Permet d'afficher la liste de toutes les cartes"""
        print(self.cartes)
    
class Bataille(JeuDeCartes):
        """Permet de faire affronter deux joueurs"""
        
        def __init__(self):
            """Initialisation"""
            #On crée les 2 jeux de cartes des deux joueurs et on mélange les jeux
            self.j1jeu = JeuDeCartes()
            self.j2jeu = JeuDeCartes()
            self.j1jeu.battre()
            self.j2jeu.battre()
        
        def jouer(self, j1 = "Joueur A", j2 = "Joueur B"):
            """Fonction permettant de faire une bataille entre deux joueurs disposant chacun d'un jeu de 52 cartes"""
            sc1 = 0
            sc2 = 0
            compte = 0
            print("{} joue sa carte en premier, {} joue sa carte en second".format(j1,j2))
            while compte < 52:
                import time
                #On va tirer les cartes jusqu'à la fin et comparer uniquement la valeur de la carte, non pas sa couleur
                v1 = self.j1jeu.cartes[compte][0]
                self.j1jeu.nom_carte(compte)
                v2 = self.j2jeu.cartes[compte][0]
                self.j2jeu.nom_carte(compte)
                if v1 > v2:
                    sc1 = sc1 + 1
                elif v2 > v1:
                    sc2 = sc2 + 1
                print("Le score actuel de {} est de {}, celui de {} est de {}".format(j1,sc1,j2,sc2))
                compte = compte +1
                time.sleep(1)
            if sc1 > sc2:
                print("{} remporte la partie avec un score de {} face aux {} points de {}".format(j1,sc1,sc2,j2))
            elif sc2> sc1:
                print("{} remporte la partie avec un score de {} face aux {} points de {}".format(j2,sc2,sc1,j1))
            else:
                print("La partie se finit sur un match nul de {} à {} points".format(sc1,sc2))



partie = Bataille()
partie.jouer("Joueur 1", "Joueur 2")