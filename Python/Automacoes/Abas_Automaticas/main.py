import sys
import webbrowser

URLS = {'Curtir':['https://www.youtube.com/'], 
        'Minecraft':['https://www.youtube.com/', 'https://www.chunkbase.com/apps/seed-map'], 
        'Programar':['https://www.youtube.com/', 'https://github.com/alunogmfs2']}


def open_urls(urls):
    for url in urls:
        webbrowser.open_new_tab(url)

if __name__ == "__main__":
    try:
        set_name = sys.argv[1]
    except:
        print('Opção inválida')


    urls = URLS[set_name]
    open_urls(urls)
