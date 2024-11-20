import tkinter as tk
import random
import pygame

# Configurações do jogo
linhas = 6
colunas = 7
Tabuleiro = [["" for _ in range(colunas)] for _ in range(linhas)]
cores = {"Azul": "blue", "Vermelho": "red"}
jogador = "Azul"
cell_size = 100  # Aumentar o tamanho de cada célula

def printarTabuleiro():
    for x in range(linhas):
        for y in range(colunas):
            canvas = cells[x][y]
            canvas.delete("all")
            if Tabuleiro[x][y] == "Azul":
                canvas.create_oval(10, 10, cell_size - 10, cell_size - 10, fill="blue", outline="")
            elif Tabuleiro[x][y] == "Vermelho":
                canvas.create_oval(10, 10, cell_size - 10, cell_size - 10, fill="red", outline="")

def checarVencedor(chip):
    # Verificar horizontal
    for x in range(linhas):
        for y in range(colunas - 3):
            if all(Tabuleiro[x][y + i] == chip for i in range(4)):
                return True

    # Verificar vertical
    for y in range(colunas):
        for x in range(linhas - 3):
            if all(Tabuleiro[x + i][y] == chip for i in range(4)):
                return True

    # Verificar diagonais
    for x in range(linhas - 3):
        for y in range(colunas - 3):
            if all(Tabuleiro[x + i][y + i] == chip for i in range(4)):
                return True
        for y in range(3, colunas):
            if all(Tabuleiro[x + i][y - i] == chip for i in range(4)):
                return True
    return False

def adicionarPeca(col):
    global jogador
    for x in reversed(range(linhas)):
        if Tabuleiro[x][col] == "":
            Tabuleiro[x][col] = jogador
            printarTabuleiro()
            if checarVencedor(jogador):
                mostrarMensagemVitoria(f"{jogador} venceu!")
                desativarJogo()
            else:
                jogador = "Vermelho" if jogador == "Azul" else "Azul"
                status.config(text=f"Vez do jogador {jogador}", fg=cores[jogador])
            break

def desativarJogo():
    for btn in botoes:
        btn.config(state="disabled")

def mostrarMensagemVitoria(mensagem):
    mensagem_vitoria.config(text=mensagem, fg=cores[jogador])
    mensagem_vitoria.place(relx=0.5, rely=0.5, anchor="center")


# Fechar o jogo ao pressionar ESC
def fechar_jogo(event):
    root.destroy()

# Interface gráfica usando tkinter
root = tk.Tk()
root.title("Lig 4")
root.configure(bg="black")

# Alterar o tamanho inicial da janela (mesmo tamanho do jogo Space Game)
root.geometry(f"{colunas * cell_size + 20}x{linhas * cell_size + 150}")  # Tamanho ajustado com base no tabuleiro

# Bind para capturar a tecla ESC
root.bind("<Escape>", fechar_jogo)

# Status do jogo
status = tk.Label(root, text=f"Vez do jogador {jogador}", font=("Helvetica", 24), fg=cores[jogador], bg="black")
status.pack()

# Números das colunas
frame_jogo = tk.Frame(root, bg="black")
frame_jogo.pack()

frame_botoes = tk.Frame(frame_jogo, bg="black")
frame_botoes.grid(row=0, column=0, columnspan=colunas)
botoes = []
for y in range(colunas):
    btn = tk.Button(frame_botoes, text=str(y + 1), width=5, height=2, command=lambda y=y: adicionarPeca(y), bg="black", fg="white", font=("Helvetica", 18))
    btn.grid(row=0, column=y)
    botoes.append(btn)

# Criação do tabuleiro com canvas para círculos e divisórias
frame_tabuleiro = tk.Frame(frame_jogo, bg="black")
frame_tabuleiro.grid(row=1, column=0)
cells = [[None for _ in range(colunas)] for _ in range(linhas)]
for x in range(linhas):
    for y in range(colunas):
        cell = tk.Canvas(frame_tabuleiro, width=cell_size, height=cell_size, bg="black", highlightthickness=1, highlightbackground="white")
        cell.grid(row=x, column=y, padx=2, pady=2)
        cells[x][y] = cell

# Exibir o tabuleiro inicial
printarTabuleiro()

# Mensagem de vitória centralizada
mensagem_vitoria = tk.Label(root, text="", font=("Helvetica", 36, "bold"), bg="black")
pygame.time.wait(2000)

root.mainloop()
