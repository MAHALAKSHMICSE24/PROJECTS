#guess the word
from tkinter import *


def start_main_page():
    def start_game(args):
        main_window.destroy()       # import sub packages
        if args == 1:
            from options import basic
            basic.main()
        elif args == 2:
            from options import loops
            loops.main()

    def option():

        lab_img1 = Button(
            main_window,
            text="Select your favorite category",
            border=0,
            justify='center',
            font=("High Tower Text", 12)

        )
        sel_btn1 = Button(
            
            text="Basic",
            width=18,
            borderwidth=8,
            font=("High Tower Text", 18),
            fg="white",
            bg="black",
            cursor="hand1",
            command=lambda: start_game(1),
        )
        sel_btn2 = Button(
            text="Loops",
            width=18,
            borderwidth=8,
            font=("High Tower Text", 18),
            fg="white",

            bg="black",
            cursor="hand2",
            command=lambda: start_game(2),
        )

        lab_img1.grid(row=0, column=0, padx=20)
        sel_btn1.grid(row=0, column=4, pady=(10, 0), padx=50, )
        sel_btn2.grid(row=1, column=4, pady=(10, 0), padx=50, )

    def show_option():
        start_btn.destroy()

        lab_img.destroy()
        option()

    main_window = Tk()

    main_window.geometry("800x500+500+200")
    main_window.resizable(0, 0)
    main_window.title("MasterMind Word Guess")
    main_window.configure(background="#e6fff5")
    

    lab_img = Label(
        main_window,
        text="Welcome To MasterMind Word Guess",
        font=("High Tower Text", 28)
    )
    lab_img.pack(pady=(50, 0))

    start_btn = Button(
        main_window,
        text="Start",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("High Tower Text", 13),
        cursor="hand2",
        command=show_option,
    )
    start_btn.pack(pady=(50, 20))

    

    main_window.mainloop()


start_main_page()
