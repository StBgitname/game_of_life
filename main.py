import tkinter as tk

from model.game_of_life import GameOfLifeModel
from view.game_of_life_gui import GameOfLifeView
from controller.game_controller import GameOfLifeController


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Conway's Game of Life")
    
    # MVC-Instanzen erstellen
    model = GameOfLifeModel(width=60, height=40)
    view = GameOfLifeView(root, width=60, height=40, cell_size=12)
    controller = GameOfLifeController(model, view)
    
    root.mainloop()
