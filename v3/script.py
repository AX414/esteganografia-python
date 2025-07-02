import getpass
import platform
import socket
import datetime
import requests
import os
import sys
from PIL import Image, ImageTk
import tkinter as tk

def resource_path(relative_path):
    """Obtem o caminho absoluto para o recurso, funciona para dev e para .exe"""
    try:
        # PyInstaller cria uma pasta temporária e coloca o path em _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

IMAGE_PATH = resource_path("icone.ico")

# Coleta de informações do sistema
usuario = getpass.getuser()
computador = platform.node()
sistema = platform.system()
arquitetura = platform.machine()
hora_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Obtém IP e provedor
try:
    resposta = requests.get("https://ipinfo.io", timeout=5)
    dados_ip = resposta.json()
    ip = dados_ip.get("ip", "N/A")
    provedor = dados_ip.get("org", "N/A")
    cidade = dados_ip.get("city", "N/A")
    regiao = dados_ip.get("region", "N/A")
    pais = dados_ip.get("country", "N/A")
except Exception as e:
    ip = provedor = cidade = regiao = pais = "Erro"
    print(f"Erro ao obter IP: {e}")

# Exibe imagem em fullscreen
root = tk.Tk()
root.title("Relatório")
root.attributes('-fullscreen', True)

img = Image.open(IMAGE_PATH)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
img = img.resize((screen_width, screen_height))
img_tk = ImageTk.PhotoImage(img)

label_img = tk.Label(root, image=img_tk)
label_img.place(x=0, y=0, relwidth=1, relheight=1)

# Texto com relatório
mensagem = (
    f"Relatório do sistema\n\n"
    f"Usuário: {usuario}\n"
    f"PC: {computador}\n"
    f"Sistema: {sistema} ({arquitetura})\n"
    f"Data/Hora: {hora_atual}\n"
    f"IP: {ip}\n"
    f"Provedor: {provedor}\n"
    f"Local: {cidade} - {regiao}, {pais}"
)

label_texto = tk.Label(
    root, text=mensagem,
    font=("Courier New", 16), fg="white", bg="black", justify="left"
)
label_texto.pack(pady=50, padx=50, anchor='nw')

# Sai ao pressionar Esc
root.bind("<Escape>", lambda e: root.destroy())
root.mainloop()
