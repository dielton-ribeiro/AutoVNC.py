#AutoVNC
import os
import tkinter as tk

def abrir_conexao_vnc(event=None):
    loja = loja_entry.get()
    pdv = pdv_entry.get()

    loja = loja.lstrip('0')
    pdv = pdv.lstrip('0')

    if int(pdv) < 10:
        pdv = '0' + pdv

    config = f"""[Connection]
ConnMethod=tcp
ConnTime=2021-10-17T18:00:35.134Z
Host=172.25.{loja}.1{pdv}
Password=bd48bfa22ac2d114
RelativePtr=0
Uuid=c4fb904e-bfb6-437d-9e99-ceb59c4535ea"""

    with open("config.vnc", "w") as file:
        file.write(config)

    os.system("start config.vnc")

    # Apaga as informações dos campos de entrada
    loja_entry.delete(0, tk.END)
    pdv_entry.delete(0, tk.END)

    loja_entry.focus_set()

root = tk.Tk()
window_width = 250
window_height = 100
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{window_width}x{window_height}")

root.title("Conexão VNC")

frame_loja = tk.Frame(root)
frame_loja.pack(pady=10)
tk.Label(frame_loja, text="Digite o número da loja:").pack(side=tk.LEFT)
loja_entry = tk.Entry(frame_loja, width=10)
loja_entry.pack(side=tk.RIGHT)

frame_pdv = tk.Frame(root)
frame_pdv.pack(pady=5)
tk.Label(frame_pdv, text="Digite o número do PDV:").pack(side=tk.LEFT)
pdv_entry = tk.Entry(frame_pdv, width=10)
pdv_entry.pack(side=tk.RIGHT)

tk.Button(root, text="Abrir Conexão VNC", command=abrir_conexao_vnc).pack(pady=1)

loja_entry.bind("<Return>", lambda event: pdv_entry.focus_set())
pdv_entry.bind("<Return>", abrir_conexao_vnc)

root.mainloop()
