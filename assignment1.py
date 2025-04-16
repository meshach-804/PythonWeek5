# Assignment 1: Design Your Own Class! 
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.
class Smartphone:
  def __init__(self, type,model, battery):
    selftype = type
    self.model = model
    self.battery = battery
  def call(self, connect):
    if connect == True:
      print("Call connected")
    else:
      print("Please try again later")
  
  def charge(self, battery, amount):
    self.battery = battery
    if battery >= 100:
      print("Fully charged, 100%")
    else:
      battery += amount

class GamingSmartphone(Smartphone):
  def __init__(self, brand, model, storage, battery, gpu_model, cooling_system):
        super().__init__(brand, model, battery)
        self.gpu_model = gpu_model
        self.cooling_system = cooling_system

  def play_game(self, game_name):
        if self._battery < 20:
            return f"Battery too low to play {game_name}. Please charge your device."
        return f"Launching {game_name} on {self.model} with {self.gpu_model} GPU..."