from tkinter import *


class Application(Frame):
    """ГУІ пріложеніе с кнопкамі."""

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Опросник - КИНО"
              ).grid(row=0, column=0, sticky=W)
        Label(self, text="Укажите ваши любимые жанры кино:"
              ).grid(row=1, column=0, sticky=W)
        self.favourite = StringVar()
        self.favourite.set(None)
        Radiobutton(self,
                    text="Комедия",
                    variable=self.favourite,
                    value="комедия",
                    command=self.update_text
                    ).grid(row=2, column=0, sticky=W)
        Radiobutton(self,
                    text="Драма",
                    variable=self.favourite,
                    value="драма",
                    command=self.update_text
                    ).grid(row=3, column=0, sticky=W)
        Radiobutton(self,
                    text="Кино о любви",
                    variable=self.favourite,
                    value="кино о любви",
                    command=self.update_text
                    ).grid(row=4, column=0, sticky=W)
        self.results_text = Text(self, width=40,
                                 height=5, wrap=WORD)
        self.results_text.grid(row=5, column=0, columnspan=3)


    def update_text(self):
        likes = "Ваш любимый киножанр - "
        likes += self.favourite.get()
        self.results_text.delete(0.0,END)
        self.results_text.insert(0.0,likes)


root = Tk()
root.title("Кино")
app = Application(root)
root.mainloop()
