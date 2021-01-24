import tkinter
from random import choice


class RockPaperScissors(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.pack()

        root.geometry("400x400")
        root.title("Rock Paper Scissors")

        self.create_widgets()


    def create_widgets(self):
        self.game_name = tkinter.Label(text="Rock Paper Scissors", font="courier 24")
        self.game_name.pack()

        self.instruction_text = tkinter.Label(text="Choose rock, paper or scissors", font="Arial 12", height=3)
        self.instruction_text.pack()

        self.user_choice = tkinter.StringVar()
        self.user_entry = tkinter.Entry(textvariable=self.user_choice, font="Arial 12")
        self.user_entry.pack()

        self.play_btn = tkinter.Button(root, text="Play", command=self.play, font="Arial 14")
        self.play_btn.pack()

        self.game_result = tkinter.StringVar()
        self.computer_entry = tkinter.Entry(root, text=self.game_result, font="Arial 12")
        self.computer_entry.pack()

        self.reset_btn = tkinter.Button(root, text="Reset", command=self.reset, font="Arial 14")
        self.reset_btn.pack(side="bottom")


    def play(self):
        user_pick = self.user_choice.get()
        symbols = ["rock", "paper", "scissors"]
        comp_choice = choice(symbols)

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


root = tkinter.Tk()
rock_paper_scissors = RockPaperScissors(root)
root.mainloop()