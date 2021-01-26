import tkinter
from random import choice


class RockPaperScissors(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.pack()

        self.root.geometry("450x450")
        self.root.title("Rock Paper Scissors")

        self.create_widgets()


    def create_widgets(self):
        self.game_name = tkinter.Label(self, text="Rock Paper Scissors", font="courier 24 bold")
        self.game_name.grid(row=0, column=0, columnspan=2, pady=10)

        self.instruction_text = tkinter.Label(self, text="Choose rock, paper or scissors", font="Arial 12", pady=20)
        self.instruction_text.grid(row=1, column=0, columnspan=2)

        self.user_label = tkinter.Label(self, text="Your choice:", font="Arial 10")
        self.user_label.grid(row=2, column=0, sticky="e", padx=5, pady=10)

        self.user_choice = tkinter.StringVar()
        self.user_entry = tkinter.Entry(self, textvariable=self.user_choice, width=12, font="Arial 12")
        self.user_entry.grid(row=2, column=1, sticky="w", padx=5)

        self.play_btn = tkinter.Button(self, text="PLAY", command=self.play, font="Arial 14", bg="#ffb829")
        self.play_btn.grid(row=3, column=0, columnspan=2, pady=20)

        self.computer_label = tkinter.Label(self, text="Computer choice:", font="Arial 10")
        self.computer_label.grid(row=4, column=0, sticky="e", padx=5, pady=10)

        self.computer_choice = tkinter.StringVar()
        self.computer_entry = tkinter.Entry(self, text=self.computer_choice, width=12, font="Arial 12")
        self.computer_entry.grid(row=4, column=1, sticky="w", padx=5)

        self.result = tkinter.Label(self, text="Result:", font="Arial 10")
        self.result.grid(row=5, column=0, columnspan=2, pady=10)

        self.game_result = tkinter.StringVar()
        self.result_entry = tkinter.Entry(self, text=self.game_result, font="Arial 12", justify="center")
        self.result_entry.grid(row=6, column=0, columnspan=2)

        self.reset_btn = tkinter.Button(self, text="Reset", command=self.reset, font="Arial 14", bg="#ffb829")
        self.reset_btn.grid(row=7, column=0, columnspan=2, pady=20)


    def play(self):
        user_pick = self.user_choice.get()
        symbols = ["rock", "paper", "scissors"]
        comp_choice = choice(symbols)
        self.computer_choice.set(comp_choice)

        if ((user_pick == 'rock' and comp_choice == 'rock') or
            (user_pick == 'paper' and comp_choice == 'paper') or
            (user_pick == 'scissors' and comp_choice == 'scissors')):
                self.game_result.set("Dead-heat")

        elif ((user_pick == 'rock' and comp_choice == 'scissors') or
            (user_pick == 'paper' and comp_choice == 'rock') or
            (user_pick == 'scissors' and comp_choice == 'paper')):
                self.game_result.set("You win!")

        elif ((user_pick == 'rock' and comp_choice == 'paper') or
            (user_pick == 'paper' and comp_choice == 'scissors') or
            (user_pick == 'scissors' and comp_choice == 'rock')):
                self.game_result.set("You lost!")


    def reset(self):
        self.user_entry.delete(0, 'end')
        self.computer_entry.delete(0, 'end')
        self.result_entry.delete(0, 'end')


root = tkinter.Tk()
rock_paper_scissors = RockPaperScissors(root)
root.mainloop()