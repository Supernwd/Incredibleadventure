#! usr/bin/python 
# -*- coding: utf-8 -*-

"""
Un jeu d'aventure basique.
"""
__author__ = 'nwd inspired by Phillip Johnson'

# import pour gestion fenêtres 
from tkinter import *

# imports pour moteur de jeu
import world
from player import Player

# On crée une classe qui contiendra toute la fenêtre. Cette classe hérite de Frame, c'est-à-dire d'un cadre Tkinter
class Interface(Frame):
    
    """La fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=800, height=600, borderwidth=1, **kwargs)
        
# configuration de la fenêtre principale
        self.master.title("L'incroyable aventure")
        self.master.geometry("800x600+50+50")
        self.pack(fill=BOTH)
       
        self.titre = Label(self, text ="Un jeu d'aventure basique mais incroyablement trépidant peut être même épileptogène")
        self.message = Label(self, width =40, relief ='sunken', wraplength =250, justify='left', text="Oui c'est vraiment un jeu d'aventure basique mais il me faut une phrase plus longue.") 
        self.info = Label(self, text="Options possibles :")
        self.question = Label(self, text ="Qu'allez vous faire maintenant ?")
        self.entr1 = Entry(self)
        
        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_cliquer = Button(self, text="Commencer", fg="red",
            command=self.cliquer)

        # création d'un widget 'Canvas' contenant une image bitmap :
        self.can1 = Canvas(self, width =320, height =200, bg ='white')
        self.photo = PhotoImage(file ='resources/torche.gif')
        self.can1.create_image(160, 100, image =self.photo) 
        # Mise en page à l'aide de la méthode 'grid' :
#       rappel : ne pas utiliser pack() et grid() dans une mm fonction !
        self.titre.grid(row =1, column =1, columnspan =3)
        self.message.grid(row =2, column =1, columnspan =2)
        self.info.grid(row =3, column =1, columnspan =2)
        self.question.grid(row=4, column =1)
        self.entr1.grid(row =4, column =2)
        self.bouton_quitter.grid(row =5, column =3, sticky =E)
        self.bouton_cliquer.grid(row=5, column =1, sticky =W)
        self.can1.grid(row=2, column=3, columnspan=1, rowspan=3,
               sticky=W+N, padx=5, pady=5)


    def cliquer(self):
        """Il y a eu un clic sur le bouton.
        On change la valeur du label message."""
        world.load_tiles()
        player = Player()
        room = world.tile_exists(player.location_x, player.location_y)
        self.message["text"] = room.intro_text()
#        self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)
        while player.is_alive() and not player.victory:
            room = world.tile_exists(player.location_x, player.location_y)
            room.modify_player(player)
            # Check again since the room could have changed the player's state
            if player.is_alive() and not player.victory:
                self.question["text"] = "Alors humain, que faire maintenant ?\n"
                available_actions = room.available_actions()
# definition du séparateur
                s="\n"
# définition d'une liste de string seq avec pour premier item le texte déjà affiché
                seq=[self.info["text"]]
# boucle de recherche et affichage des actions disponibles à afficher
                for action in available_actions:
                    seq.append(action.name)
                self.info["text"] = s.join(seq) + "\n" 
# TODO : ajouter un bouton Go validant la saisie pour remplacer la fonction input ci dessous
                    #action_input = input('Action: ')
                #for action in available_actions:
             #      if action_input == action.hotkey:
             #          player.do_action(action, **action.kwargs)
                break


#    def play():
#       world.load_tiles()
#       player = Player()
#       room = world.tile_exists(player.location_x, player.location_y)
#       print(room.intro_text())
#       while player.is_alive() and not player.victory:
#       room = world.tile_exists(player.location_x, player.location_y)
#       room.modify_player(player)
        # Check again since the room could have changed the player's state
#       if player.is_alive() and not player.victory:
#            print("Qu'allez vous faire maintenant ?\n")
#            available_actions = room.available_actions()
#            for action in available_actions:
#                print(action)
#            action_input = input('Action: ')
#            for action in available_actions:
#                if action_input == action.hotkey:
#                    player.do_action(action, **action.kwargs)
#                    break

if __name__ == "__main__":
    fenetre = Tk()
    interface = Interface(fenetre)
    interface.mainloop()
    interface.destroy()


