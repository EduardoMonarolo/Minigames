import tkinter as tk
import sys
import os

# Função para abrir o jogo Space Game
def abrir_space_game():
    os.system(r"python D:\Minigames\Space-Game\space-game.py")  # Caminho correto

# Função para abrir o jogo Ligue 4
def abrir_ligue_4():
    os.system(r"python D:\Minigames\Ligue-4\Ligue4.py")  # Substitua pelo caminho correto do arquivo Ligue 4

# Função para sair do programa
def sair():
    root.destroy()
    sys.exit()

# Configuração da janela principal
root = tk.Tk()
root.title("Menu de Jogos")
root.configure(bg="black")
root.geometry("600x400")

# Título
titulo = tk.Label(root, text="Selecione o Jogo", font=("Helvetica", 24, "bold"), fg="white", bg="black")
titulo.pack(pady=20)

# Botão para Space Game
btn_space_game = tk.Button(root, text="Space Game", font=("Helvetica", 18), width=20, command=abrir_space_game, bg="blue", fg="white")
btn_space_game.pack(pady=10)

# Botão para Ligue 4
btn_ligue_4 = tk.Button(root, text="Ligue 4", font=("Helvetica", 18), width=20, command=abrir_ligue_4, bg="red", fg="white")
btn_ligue_4.pack(pady=10)

# Botão para sair
btn_sair = tk.Button(root, text="Sair", font=("Helvetica", 18), width=20, command=sair, bg="gray", fg="white")
btn_sair.pack(pady=10)

# Iniciar a interface
root.mainloop()
