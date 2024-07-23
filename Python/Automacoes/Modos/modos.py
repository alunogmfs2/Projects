import pyautogui as pyg
import sys
import webbrowser

pyg.PAUSE = 0.5

MODOS = {'Python': {'app':['visual studio code'], 'site':['https://youtube.com ', 'https://github.com/alunogmfs2 ']},
         'Minecraft': {'app': ['curseforge'],'site':['https://youtube.com ', 'https://www.chunkbase.com/apps/seed-map ']},
         'Normal': {'app': [], 'site': ['https://youtube.com ']}}


def abrir_app(app):
    pyg.press('winleft')
    pyg.write(app)
    pyg.press('enter')



def abrir_site(site):
    try:
        webbrowser.open(site)
    except:
        print(f'Site {site} nao encontrado.')
        return


if __name__ == '__main__':
    try:
        modo = sys.argv[1]

        mod = MODOS[modo]

        for app in mod['app']:
            abrir_app(app)

        for site in mod['site']:
            abrir_site(site)
        
        sys.exit(0)
    except:
        print('Modo inválido.')
        sys.exit(1)
