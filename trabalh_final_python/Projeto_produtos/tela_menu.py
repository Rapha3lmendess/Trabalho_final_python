import tkinter as tk

from tela_cadastro import abrir_cadastro
from tela_consulta import abrir_consulta
from tela_atualizar import abrir_atualizar
from tela_excluir import abrir_excluir


def abrir_menu():

    janela = tk.Tk()
    janela.title("Sistema de Estoque")
    janela.geometry("500x450")

    tk.Label(
        janela,
        text="CONTROLE DE ESTOQUE",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    tk.Button(
        janela,
        text="Cadastrar Produto",
        width=25,
        command=abrir_cadastro
    ).pack(pady=10)

    tk.Button(
        janela,
        text="Consultar Produtos",
        width=25,
        command=abrir_consulta
    ).pack(pady=10)

    tk.Button(
        janela,
        text="Atualizar Produto",
        width=25,
        command=abrir_atualizar
    ).pack(pady=10)

    tk.Button(
        janela,
        text="Excluir Produto",
        width=25,
        command=abrir_excluir
    ).pack(pady=10)

    tk.Button(
        janela,
        text="Sair",
        width=25,
        command=janela.destroy
    ).pack(pady=20)

    janela.mainloop()