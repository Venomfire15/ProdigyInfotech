import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        
        self.label = tk.Label(root, text="Guess the number between 1 and 100:")
        self.label.pack()
        
        self.guess_entry = tk.Entry(root)
        self.guess_entry.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
        
        self.check_button = tk.Button(root, text="Check", command=self.check_guess)
        self.check_button.pack()
        
        self.reset_button = tk.Button(root, text="Play Again", command=self.reset_game, state=tk.DISABLED)
        self.reset_button.pack()
    
    def check_guess(self):
        guess = self.guess_entry.get()
        
        try:
            guess = int(guess)
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a number.")
            return
        
        self.attempts += 1
        
        if guess < self.target_number:
            self.result_label.config(text="Too low! Try again.")
        elif guess > self.target_number:
            self.result_label.config(text="Too high! Try again.")
        else:
            self.result_label.config(text=f"Congratulations! You guessed the number {self.target_number} in {self.attempts} attempts.")
            self.check_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.NORMAL)
    
    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="")
        self.guess_entry.delete(0, tk.END)
        self.check_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
