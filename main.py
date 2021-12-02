import pygame
from src import controller

def main():
	game = controller.Controller()
	game.mainloop()
	team = {"lead": "Spencer Mines and Matthew Kagan", "backend": "Matthew Kagan", "frontend": "Spencer Mines"}
	print("Software Lead is:", team["lead"])
	print("Backend is:", team["backend"])
	print("Frontend is:" , team["frontend"])

    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 2 LINES OF CODE ######
main()
