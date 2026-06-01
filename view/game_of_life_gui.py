import tkinter as tk
from typing import List


class GameOfLifeView:
    """View-Klasse: Verantwortlich für die Darstellung."""
    
    def __init__(self, root: tk.Tk, width: int, height: int, cell_size: int):
        self.root = root
        self.cell_size = cell_size
        self.width = width
        self.height = height
        
        # Canvas
        canvas_width = width * cell_size
        canvas_height = height * cell_size
        self.canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
        self.canvas.pack(padx=10, pady=10)
        
        # Control Frame
        control_frame = tk.Frame(root)
        control_frame.pack(pady=5)
        
        # Buttons
        self.start_button = tk.Button(control_frame, text="Start", width=10)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.step_button = tk.Button(control_frame, text="Schritt", width=10)
        self.step_button.pack(side=tk.LEFT, padx=5)
        
        self.reset_button = tk.Button(control_frame, text="Reset", width=10)
        self.reset_button.pack(side=tk.LEFT, padx=5)
        
        self.clear_button = tk.Button(control_frame, text="Löschen", width=10)
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        # Speed Control
        speed_frame = tk.Frame(root)
        speed_frame.pack(pady=5)
        
        tk.Label(speed_frame, text="Geschwindigkeit:").pack(side=tk.LEFT, padx=5)
        self.speed_scale = tk.Scale(speed_frame, from_=10, to=500, orient=tk.HORIZONTAL)
        self.speed_scale.set(100)
        self.speed_scale.pack(side=tk.LEFT, padx=5)
    
    def draw_grid(self, grid: List[List[int]]):
        """Zeichnet das Grid auf der Canvas."""
        self.canvas.delete("all")
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    x1 = x * self.cell_size
                    y1 = y * self.cell_size
                    x2 = x1 + self.cell_size
                    y2 = y1 + self.cell_size
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="")
    
    def set_start_button_text(self, text: str):
        """Setzt den Text des Start-Buttons."""
        self.start_button.config(text=text)
    
    def get_delay(self) -> int:
        """Gibt die aktuelle Verzögerung zurück."""
        return self.speed_scale.get()
