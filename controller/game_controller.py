from model.game_of_life import GameOfLifeModel
from view.game_of_life_gui import GameOfLifeView


class GameOfLifeController:
    """Controller-Klasse: Verbindet Model und View."""
    
    def __init__(self, model: GameOfLifeModel, view: GameOfLifeView):
        self.model = model
        self.view = view
        self.running = False
        
        # Event-Handler binden
        self.view.start_button.config(command=self.toggle_simulation)
        self.view.step_button.config(command=self.step)
        self.view.reset_button.config(command=self.reset)
        self.view.clear_button.config(command=self.clear)
        self.view.canvas.bind("<Button-1>", self.on_canvas_click)
        
        # Initial anzeigen
        self.update_view()
    
    def toggle_simulation(self):
        """Startet oder stoppt die Simulation."""
        self.running = not self.running
        if self.running:
            self.view.set_start_button_text("Stop")
            self.run_simulation()
        else:
            self.view.set_start_button_text("Start")
    
    def run_simulation(self):
        """Führt die Simulation aus."""
        if self.running:
            self.model.next_generation()
            self.update_view()
            delay = self.view.get_delay()
            self.view.root.after(delay, self.run_simulation)
    
    def step(self):
        """Führt einen einzelnen Schritt aus."""
        self.model.next_generation()
        self.update_view()
    
    def reset(self):
        """Setzt das Grid zurück und randomisiert neu."""
        self.running = False
        self.view.set_start_button_text("Start")
        self.model.randomize()
        self.update_view()
    
    def clear(self):
        """Löscht alle Zellen."""
        self.running = False
        self.view.set_start_button_text("Start")
        self.model.clear()
        self.update_view()
    
    def on_canvas_click(self, event):
        """Behandelt Klicks auf die Canvas."""
        x = event.x // self.view.cell_size
        y = event.y // self.view.cell_size
        self.model.toggle_cell(x, y)
        self.update_view()
    
    def update_view(self):
        """Aktualisiert die View mit den aktuellen Daten aus dem Model."""
        grid = self.model.get_grid()
        self.view.draw_grid(grid)
