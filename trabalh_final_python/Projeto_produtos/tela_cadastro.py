import tkinter as tk
from tkinter import messagebox
from conexao import conectar

def abrir_cadastro():

    janela = tk.Toplevel()
    janela.title("Cadastro de Produtos")
    janela.geometry("500x400")
    janela.resizable(False, False)

    tk.Label(
        janela,
        text="Cadastro de Produtos",
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    tk.Label(
        janela,
        text="Nome",
        font=("Arial", 12)
    ).pack(pady=5)

    nome = tk.Entry(janela, width=35)
    nome.pack(pady=5)

    tk.Label(
        janela,
        text="Preço",
        font=("Arial", 12)
    ).pack(pady=5)

    preco = tk.Entry(janela, width=35)
    preco.pack(pady=5)

    tk.Label(
        janela,
        text="Quantidade",
        font=("Arial", 12)
    ).pack(pady=5)

    quantidade = tk.Entry(janela, width=35)
    quantidade.pack(pady=5)

    def salvar():

        if not nome.get() or not preco.get() or not quantidade.get():

            messagebox.showerror(
                "Erro",
                "Preencha todos os campos!"
            )
            return

        try:

            preco_valor = float(preco.get())
            quantidade_valor = int(quantidade.get())

            conexao = conectar()
            cursor = conexao.cursor()

            sql = """
            INSERT INTO produtos
            (nome, preco, quantidade)
            VALUES (%s, %s, %s)
            """

            valores = (
                nome.get(),
                preco_valor,
                quantidade_valor
            )

            cursor.execute(sql, valores)

            conexao.commit()

            messagebox.showinfo(
                "Sucesso",
                "Produto cadastrado com sucesso!"
            )

            nome.delete(0, tk.END)
            preco.delete(0, tk.END)
            quantidade.delete(0, tk.END)

        except ValueError:

            messagebox.showerror(
                "Erro",
                "Preço ou quantidade inválidos!"
            )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

        finally:

            try:
                cursor.close()
                conexao.close()
            except:
                pass

    tk.Button(
        janela,
        text="Salvar Produto",
        width=20,
        height=2,
        command=salvar
    ).pack(pady=20)