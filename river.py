"""File to define River class"""

from fish import Fish
from bear import Bear

class River:
    
    fish: list[Fish]
    bears: list[Bear]
    day: int
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())
    
    
    def remove_fish(self, amount: int):
        return None

    def remove_bears(self, amount: int):
        return None
    
    def bears_eating(self):
        return None
    
    def check_hunger(self):
        return None
                
    def check_ages(self):
        return None
        
    def repopulate_fish(self):
        return None
    
    def repopulate_bears(self):
        return None
            
    def one_river_day(self):
        self.day += 1
        for bear in self.bears:
            bear.one_day()
        for fish in self.fish:
            fish.one_day()
        self.bears_eating()
        self.check_hunger()
        self.check_ages()
        self.repopulate_fish()
        self.repopulate_bears()
            
    def one_week(self):
        return None
    
    def view_river(self):
        return None