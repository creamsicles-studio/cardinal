# main_tpss.py

import tkinter as tk
from tkinter import filedialog, messagebox
from tpss_classes import TPSS, Tournament, Player

class TPSSGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("TPSS - Tournament Seeding System")
        self.tpss = TPSS()
        self.tournaments = []
        self.setup_gui()

    def setup_gui(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        # Import Results Button
        self.import_btn = tk.Button(self.main_frame, text="Import Tournament Results", command=self.import_results)
        self.import_btn.grid(row=0, column=0)

        # Rank Display
        self.rank_listbox = tk.Listbox(self.main_frame, width=50)
        self.rank_listbox.grid(row=1, column=0, pady=20)

    def import_results(self):
        filepath = filedialog.askopenfilename(title="Select Results File", filetypes=[("Text files", "*.txt")])

        if filepath:
            try:
                with open(filepath, 'r') as f:
                    lines = f.readlines()
                
                tournament_name = lines[0].split(":")[1].strip()
                prestige = float(lines[1].split(":")[1].strip())
                tournament = Tournament(tournament_name, prestige)

                for line in lines[3:]:
                    parts = line.split(',')
                    player_name = parts[0]
                    wins = int(parts[1].split(":")[1])
                    placements = int(parts[2].split(":")[1])
                    
                    tournament.update_match_results(player_name, wins, placements)
                
                self.tournaments.append(tournament)
                self.tpss.assign_points_based_on_results(tournament)
                self.calculate_ranks()

                messagebox.showinfo("Success", f"Tournament {tournament_name} imported and processed.")
            
            except Exception as e:
                messagebox.showerror("Error", f"Failed to import results: {e}")

    def calculate_ranks(self):
        self.tpss.calculate_dynamic_rank()
        self.display_ranks()

    def display_ranks(self):
        self.rank_listbox.delete(0, tk.END)
        for player in self.tpss.players:
            self.rank_listbox.insert(tk.END, f"{player.name} - Points: {player.points}, Rank: {player.rank}")

# Run the main TPSS GUI
root = tk.Tk()
app = TPSSGUI(root)
root.mainloop()
