import tkinter
from random import choice


class RockPaperScissors(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.pack()

        self.root.geometry("400x400")
        self.root.title("Rock Paper Scissors")

        self.create_widgets()


    def create_widgets(self):
        self.game_name = tkinter.Label(text="Rock Paper Scissors", font="courier 24")
        self.game_name.pack(side="top")

        self.instruction_text = tkinter.Label(text="Choose rock, paper or scissors", font="Arial 12", height=3)
        self.instruction_text.pack(side="top")

        self.user_label = tkinter.Label(text="Your choice:")
        self.user_label.pack()

        self.user_choice = tkinter.StringVar()
        self.user_entry = tkinter.Entry(textvariable=self.user_choice, font="Arial 12")
        self.user_entry.pack()

        self.play_btn = tkinter.Button(text="Play", command=self.play, font="Arial 14")
        self.play_btn.pack()

        self.computer_label = tkinter.Label(text="Computer choice:")
        self.computer_label.pack()

        self.computer_choice = tkinter.StringVar()
        self.computer_entry = tkinter.Entry(text=self.computer_choice, font="Arial 12")
        self.computer_entry.pack()

        self.result = tkinter.Label(text="Result:")
        self.result.pack()

        self.game_result = tkinter.StringVar()
        self.result_entry = tkinter.Entry(text=self.game_result, font="Arial 12")
        self.result_entry.pack()

        self.reset_btn = tkinter.Button(text="Reset", command=self.reset, font="Arial 14")
        self.reset_btn.pack()


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