import os
import shutil


def testar_arquivo(arquivo, tipo_arquivo):
    if arquivo.endswith(tipo_arquivo):
        return True
    return False


def main():
    arquivos = os.listdir("C://Users//flavi//Downloads//")
    for arquivo in arquivos:
        if testar_arquivo(arquivo, ".txt"):
            try:
                os.mkdir("C://Users//flavi//Downloads//.txt")
                print(f"Diretório .txt criado com sucesso.")
            except:
                pass
            shutil.move(f"C://Users//flavi//Downloads//{arquivo}", "C://Users//flavi//Downloads//.txt//")
        elif testar_arquivo(arquivo, ".pdf"):
            try:
                os.mkdir("C://Users//flavi//Downloads//.pdf")
                print(f"Diretório .pdf criado com sucesso.")
            except:
                pass
            shutil.move(f"C://Users//flavi//Downloads//{arquivo}", "C://Users//flavi//Downloads//.pdf//")
        elif testar_arquivo(arquivo, ".stl"):
            try:
                os.mkdir("C://Users//flavi//Downloads//.stl")
                print(f"Diretório .stl criado com sucesso.")
            except:
                pass
            shutil.move(f"C://Users//flavi//Downloads//{arquivo}", "C://Users//flavi//Downloads//.stl//")
        elif testar_arquivo(arquivo, ".zip"):
            try:
                os.mkdir("C://Users//flavi//Downloads//.zip")
                print(f"Diretório .zip criado com sucesso.")
            except:
                pass
            shutil.move(f"C://Users//flavi//Downloads//{arquivo}", "C://Users//flavi//Downloads//.zip//")
        elif testar_arquivo(arquivo, ".exe"):
            try:
                os.mkdir("C://Users//flavi//Downloads//.exe")
                print(f"Diretório .exe criado com sucesso.")
            except:
                pass
            shutil.move(f"C://Users//flavi//Downloads//{arquivo}", "C://Users//flavi//Downloads//.exe//")
        elif testar_arquivo(arquivo, ".jpg"):
            try:
                os.mkdir("C://Users//flavi//Downloads//.jpg")
                print(f"Diretório .jpg criado com sucesso.")
            except:
                pass
            shutil.move(f"C://Users//flavi//Downloads//{arquivo}", "C://Users//flavi//Downloads//.jpg//")
        elif testar_arquivo(arquivo, ".png"):
            try:
                os.mkdir("C://Users//flavi//Downloads//.png")
                print(f"Diretório .png criado com sucesso.")
            except:
                pass
            shutil.move(f"C://Users//flavi//Downloads//{arquivo}", "C://Users//flavi//Downloads//.png//")
        elif testar_arquivo(arquivo, ".mp4"):
            try:
                os.mkdir("C://Users//flavi//Downloads//.mp4")
                print(f"Diretório .mp4 criado com sucesso.")
            except:
                pass
            shutil.move(f"C://Users//flavi//Downloads//{arquivo}", "C://Users//flavi//Downloads//.mp4//")
        elif testar_arquivo(arquivo, ".jpeg"):
            try:
                os.mkdir("C://Users//flavi//Downloads//.jpeg")
                print(f"Diretório .jpeg criado com sucesso.")
            except:
                pass
            shutil.move(f"C://Users//flavi//Downloads//{arquivo}", "C://Users//flavi//Downloads//.jpeg//")
        elif testar_arquivo(arquivo, ".log"):
            try:
                os.mkdir("C://Users//flavi//Downloads//.log")
                print(f"Diretório .log criado com sucesso.")
            except:
                pass
            shutil.move(f"C://Users//flavi//Downloads//{arquivo}", "C://Users//flavi//Downloads//.log//")
        elif testar_arquivo(arquivo, ".msi"):
            try:
                os.mkdir("C://Users//flavi//Downloads//.msi")
                print(f"Diretório .msi criado com sucesso.")
            except:
                pass
            shutil.move(f"C://Users//flavi//Downloads//{arquivo}", "C://Users//flavi//Downloads//.msi//")
        elif testar_arquivo(arquivo, ".jar"):
            try:
                os.mkdir("C://Users//flavi//Downloads//.jar")
                print(f"Diretório .jar criado com sucesso.")
            except:
                pass
            shutil.move(f"C://Users//flavi//Downloads//{arquivo}", "C://Users//flavi//Downloads//.jar//")
        elif testar_arquivo(arquivo, ".odt"):
            try:
                os.mkdir("C://Users//flavi//Downloads//.odt")
                print(f"Diretório .odt criado com sucesso.")
            except:
                pass
            shutil.move(f"C://Users//flavi//Downloads//{arquivo}", "C://Users//flavi//Downloads//.odt//")
        elif testar_arquivo(arquivo, ".pem"):
            try:
                os.mkdir("C://Users//flavi//Downloads//.pem")
                print(f"Diretório.pem criado com sucesso.")
            except:
                pass
            shutil.move(f"C://Users//flavi//Downloads//{arquivo}", "C://Users//flavi//Downloads//.pem//")
        elif testar_arquivo(arquivo, ".scad"):
            try:
                os.mkdir("C://Users//flavi//Downloads//.scad")
                print(f"Diretório.scad criado com sucesso.")
            except:
                pass
            shutil.move(f"C://Users//flavi//Downloads//{arquivo}", "C://Users//flavi//Downloads//.scad//")
        elif testar_arquivo(arquivo, ".py"):
            try:
                os.mkdir("C://Users//flavi//Downloads//.py")
                print(f"Diretório.py criado com sucesso.")
            except:
                pass
            shutil.move(f"C://Users//flavi//Downloads//{arquivo}", "C://Users//flavi//Downloads//.py//")
        elif testar_arquivo(arquivo, ""):
            try:
                os.mkdir("C://Users//flavi//Downloads//Pastas")
                print(f"Diretório Pastas criado com sucesso.")
            except:
                pass
            shutil.move(f"C://Users//flavi//Downloads//{arquivo}", "C://Users//flavi//Downloads//Pastas//")


if __name__ == "__main__":
    main()

