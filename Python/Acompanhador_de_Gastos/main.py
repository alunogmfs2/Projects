import customtkinter as ctk

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.startarJanela()

    def startarJanela(self):
        self.width = 800
        self.height = 600

        self.xwindow = 550
        self.ywindow = 200

        self.geometry(f"{self.width}x{self.height}+{self.xwindow}+{self.ywindow}")
        self.title("Acompanhador de Gastos")


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()