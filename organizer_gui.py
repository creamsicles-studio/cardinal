# organizer_gui.py

import tkinter as tk
from tkinter import messagebox

class OrganizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tournament Organizer - Results Input")
        self.results = []
        self.setup_gui()

    def setup_gui(self):
        tk.Label(self.root, text="Tournament Name:").grid(row=0, column=0)
        self.tournament_name_entry = tk.Entry(self.root)
        self.tournament_name_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Tournament Prestige:").grid(row=1, column=0)
        self.prestige_entry = tk.Entry(self.root)
        self.prestige_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Player Name:").grid(row=2, column=0)
        self.player_name_entry = tk.Entry(self.root)
        self.player_name_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Wins:").grid(row=3, column=0)
        self.wins_entry = tk.Entry(self.root)
        self.wins_entry.grid(row=3, column=1)

        tk.Label(self.root, text="Placements:").grid(row=4, column=0)
        self.placements_entry = tk.Entry(self.root)
        self.placements_entry.grid(row=4, column=1)

        self.add_result_btn = tk.Button(self.root, text="Add Result", command=self.add_result)
        self.add_result_btn.grid(row=5, column=0, columnspan=2)

        self.export_btn = tk.Button(self.root, text="Export Results", command=self.export_results)
        self.export_btn.grid(row=6, column=0, columnspan=2)

    def add_result(self):
        player_name = self.player_name_entry.get()
        wins = self.wins_entry.get()
        placements = self.placements_entry.get()

        if player_name and wins.isdigit() and placements.isdigit():
            result = {
                "player_name": player_name,
                "wins": int(wins),
                "placements": int(placements)
            }
            self.results.append(result)
            messagebox.showinfo("Success", f"Result for {player_name} added.")
        else:
            messagebox.showerror("Error", "Please enter valid data for all fields.")

    def export_results(self):
        tournament_name = self.tournament_name_entry.get()
        prestige = self.prestige_entry.get()

        if tournament_name and prestige.isdigit() and self.results:
            filename = f"{tournament_name}_results.txt"
            with open(filename, 'w') as f:
                f.write(f"Tournament: {tournament_name}\n")
                f.write(f"Prestige: {prestige}\n")
                f.write("Results:\n")
                for result in self.results:
                    f.write(f"{result['player_name']},Wins:{result['wins']},Placements:{result['placements']}\n")
            messagebox.showinfo("Success", f"Results exported to {filename}.")
        else:
            messagebox.showerror("Error", "Please fill out all tournament information and results.")

# Run the organizer GUI
root = tk.Tk()
app = OrganizerGUI(root)
root.mainloop()
