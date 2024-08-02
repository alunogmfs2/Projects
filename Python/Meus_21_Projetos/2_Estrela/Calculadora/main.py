import customtkinter as ctk

def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb

class Janela(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora")
        self.geometry('400x500+700+200')
        self.resizable(False, False)

        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('blue')

        # Configuração de grid para a janela principal
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)  # Colunas responsivas
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)  # Linhas responsivas

        # Linha de exibição do resultado
        self.resultado = ctk.CTkLabel(self,
                                      text="",
                                      fg_color=rgb_to_hex((32, 32, 32)),
                                      width=380,
                                      height=50,  # Define uma altura fixa
                                      corner_radius=10,
                                      anchor="w")
        self.resultado.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

        # Botão AC
        ctk.CTkButton(self, text="AC", command=self.limpar).grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        # Linha dos botões
        botoes = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('÷', 2, 3, self.divisao),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('x', 3, 3, self.multiplicacao),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3, self.subtracao),
            ('0', 5, 0), ('=', 5, 2, self.mostrarRes), ('+', 5, 3, self.soma)
        ]

        for (text, row, col, *cmd) in botoes:
            command = (cmd[0] if cmd else lambda t=text: self.adicionarConta(t))
            ctk.CTkButton(self, text=text, command=command).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Ajuste para o botão '0' para ocupar mais espaço
        ctk.CTkButton(self, text='0', command=lambda: self.adicionarConta('0')).grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        self.numero = ""
        self.conta = []

    def soma(self):
        self.adicionarConta("+")

    def subtracao(self):
        self.adicionarConta("-")

    def multiplicacao(self):
        self.adicionarConta("*")

    def divisao(self):
        self.adicionarConta("/")

    def mostrarRes(self):
        try:
            resultado = eval(''.join(self.conta))
            self.resultado.configure(text=str(resultado))
            self.numero = str(resultado)
            self.conta = [self.numero]
        except Exception as e:
            self.resultado.configure(text="Erro")
            self.numero = ""
            self.conta = []

    def adicionarConta(self, digito):
        if self.resultado.cget("text") == "Erro":
            self.numero = ""
            self.conta = []

        self.numero += digito
        self.conta.append(digito)
        self.resultado.configure(text=self.numero)

        print(self.numero)
        print(self.conta)

    def limpar(self):
        self.resultado.configure(text="")
        self.numero = ""
        self.conta = []


if __name__ == "__main__":
    janela = Janela()
    janela.mainloop()
