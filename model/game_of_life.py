import random
from typing import List


class GameOfLifeModel:
    """Model-Klasse: Enthält die Daten und Logik des Spiels."""
    
    def __init__(self, width: int = 50, height: int = 20):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.randomize()
    
    def randomize(self):
        """Initialisiert das Grid mit zufälligen lebenden Zellen."""
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] = 1 if random.random() < 0.3 else 0
    
    def clear(self):
        """Löscht alle Zellen."""
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
    
    def toggle_cell(self, x: int, y: int):
        """Schaltet eine Zelle um."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = 1 - self.grid[y][x]
    
    def count_neighbors(self, x: int, y: int) -> int:
        """Zählt die lebenden Nachbarn einer Zelle."""
        count = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx = (x + dx) % self.width
                ny = (y + dy) % self.height
                count += self.grid[ny][nx]
        return count
    
    def next_generation(self):
        """Berechnet die nächste Generation basierend auf den Regeln."""
        new_grid = []
        
        for y in range(self.height):
            row = []
            for x in range(self.width):
                neighbors = self.count_neighbors(x, y)
                current = self.grid[y][x]
                
                if current == 1:
                    row.append(1 if 2 <= neighbors <= 3 else 0)
                else:
                    row.append(1 if neighbors == 3 else 0)
            
            new_grid.append(row)
        
        self.grid = new_grid
    
    def get_grid(self) -> List[List[int]]:
        """Gibt das aktuelle Grid zurück."""
        return self.grid
