from tkinter import *


def start_main_page():
    def start_game(args):   # import sub packages
        if args == 1:
            from loops import circle
            circle.main()
    def option():

        lab_img1 = Button(
            main_window,
            text="Select your favorite category",
            border=0,
            justify='center',
            font=("High Tower Text", 12)

        )
        sel_btn1 = Button(
            text="Square",
            width=18,
            borderwidth=8,
            font=("High Tower Text", 18),
            fg="white",
            bg="black",
            cursor="hand1",
            command=lambda: start_game(1),
        )


        lab_img1.grid(row=0, column=0, padx=20)
        sel_btn1.grid(row=0, column=4, pady=(10, 0), padx=50, )

    def show_option():
        start_btn.destroy()

        lab_img.destroy()
        option()

    main_window = Tk()

    main_window.geometry("800x500+500+200")
    main_window.resizable(0, 0)
    main_window.title("loops")
    main_window.configure(background="#e6fff5")
    

    lab_img = Label(
        main_window,
        text="Click the button to choose the shapes to learn",
        font=("High Tower Text", 28)
    )
    lab_img.pack(pady=(50, 0))

    start_btn = Button(
        main_window,
        text="Loops",
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
