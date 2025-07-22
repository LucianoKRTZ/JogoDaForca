import tkinter as tk
from tkinter import messagebox
from tools import Tools

class Main():
    def __init__(self):
        self.choosenWord = None
        self.characterList = []

        self.tentativas = 0
        self.vitorias = 0
        self.derrotas = 0
        self.vidasRestantes = 5
        self.vidasRestantesDefault = 5

        self.root = tk.Tk()
        self.root.title("Jogo da Forca")
        self.root.geometry("300x350+0+0")
        self.root.resizable(False, False)
        self.tools = Tools()

    def startGame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.choosenWord = self.tools.sortWord()

        for i in range(3):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(9):
            self.root.grid_rowconfigure(i, weight=1)

        tip_text = self.choosenWord['tip']
        # Quebra em linhas de até 100 caracteres
        tip_lines = [tip_text[i:i+100] for i in range(0, len(tip_text), 100)]
        tipLabel = tk.Label(self.root, text='\n'.join(tip_lines))
        tipLabel.grid(column=1, row=0, padx=10, pady=10, sticky="n")

        self.hiddenWordLabel = tk.Label(self.root, text=self.choosenWord['hiddenWord'])
        self.hiddenWordLabel.grid(column=1, row=1, padx=10, pady=10, sticky="n")

        self.inputCharacter = tk.Entry(self.root, width=5)
        self.inputCharacter.configure(validate="key", validatecommand=(self.root.register(lambda s: len(s) <= 1), "%P"), background="#fedc6e")
        self.inputCharacter.grid(column=1, row=2, padx=10, pady=10, sticky="n")
        self.inputCharacter.bind("<Return>", self.checkCharacter)

        self.usedCharactersTitle = tk.Label(self.root, text="Letras usadas:")
        self.usedCharactersTitle.grid(column=1, row=3, padx=10, pady=10, sticky="n")
     
        self.usedCharactersLabel = tk.Label(self.root, text=', '.join(self.characterList))
        self.usedCharactersLabel.grid(column=1, row=4, padx=10, pady=10, sticky="n")

        # Frame para agrupar os dados do placar
        placarFrame = tk.Frame(self.root)
        placarFrame.grid(column=1, row=5, padx=10, pady=10, sticky="n")

        # Imagem de coração
        self.heart_img = tk.PhotoImage(file="assets/heartRED.png")
        self.heart_black_img = tk.PhotoImage(file="assets/heartBLACK.png")
        self.heartsFrame = tk.Frame(placarFrame)
        self.heartsFrame.pack(pady=2)
        self.updateHearts()

        self.tentativasLabel = tk.Label(placarFrame, text=f"Tentativas: {self.tentativas}")
        self.tentativasLabel.pack(pady=2)
     
        self.vitoriasLabel = tk.Label(placarFrame, text=f"Vitórias: {self.vitorias}")
        self.vitoriasLabel.pack(pady=2)
     
        self.derrotasLabel = tk.Label(placarFrame, text=f"Derrotas: {self.derrotas}")
        self.derrotasLabel.pack(pady=2)

        self.root.update()
        

    def updateUsedCharactersLabel(self):
        text = ', '.join(self.characterList)
        # Quebra em linhas de até 60 caracteres
        lines = [text[i:i+30] for i in range(0, len(text), 30)]
        self.usedCharactersLabel['text'] = '\n'.join(lines)

    def updateHearts(self):
        # Remove corações antigos
        for widget in self.heartsFrame.winfo_children():
            widget.destroy()
        # Adiciona corações vermelhos para vidas restantes e pretos para vidas perdidas
        total_hearts = self.vidasRestantesDefault
        for i in range(total_hearts):
            if i < self.vidasRestantes:
                lbl = tk.Label(self.heartsFrame, image=self.heart_img)
            else:
                lbl = tk.Label(self.heartsFrame, image=self.heart_black_img)
            lbl.pack(side="left", padx=2)

    def checkCharacter(self, event):
        character = self.inputCharacter.get().strip().lower()
        self.inputCharacter.delete(0, tk.END)
        self.root.update_idletasks()

        self.tentativas += 1
        self.tentativasLabel['text'] = f"Tentativas: {self.tentativas}"

        if len(character) == 1 and character.isalpha():
            if character not in self.characterList:
                self.characterList.append(character)
                self.updateUsedCharactersLabel()  # Use a nova função
                validatedChar = self.tools.validateCharacter(character)
                if validatedChar['isValid']:
                    self.updateHiddenWord(character, validatedChar['indices'])
                else:
                    self.vidasRestantes -= 1
                    self.updateHearts()
            else:
                print("Letra já utilizada.")
        else:
            print("Por favor, insira apenas uma letra.")

        self.verificarVitoria()


    def updateHiddenWord(self, character, indices):
        hiddenWord = list(self.hiddenWordLabel['text'])
        for index in indices:
            hiddenWord[index] = character.upper()
        self.hiddenWordLabel['text'] = ''.join(hiddenWord)

    def verificarVitoria(self):
        if self.hiddenWordLabel['text'].replace(' ', '').upper() == self.choosenWord['word'].upper().replace(' ','-'):
            self.vitorias += 1
            self.vitoriasLabel['text'] = f"Vitórias: {self.vitorias}"
            self.vidasRestantes = 5
            self.characterList = []
            self.updateUsedCharactersLabel()
            messagebox.showinfo("Você ganhou!", f"Parabéns! A próxima palavra será escolhida em breve.")
            self.startGame()
        elif self.vidasRestantes <= 0:
            self.characterList = []
            self.updateUsedCharactersLabel()
            self.derrotas += 1
            self.derrotasLabel['text'] = f"Derrotas: {self.derrotas}"
            self.vidasRestantes = 5
            messagebox.showerror("Você perdeu!", f"A palavra era: {self.choosenWord['word']}")
            self.startGame()


if __name__ == "__main__":
    main = Main()
    main.startGame()
    main.root.mainloop()