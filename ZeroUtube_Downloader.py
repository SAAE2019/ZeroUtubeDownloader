import youtube_dl
import os
from pathlib import Path

# Empezamos ubicandonos en la carpeta de Downloads,
# esto para inicializar las variables

# Variable para manejar el while del main
opwhile = '1'

# Obtenemos la carpeta de Descargas
downloads_path = str(Path.home() / "Downloads")

# Crear carpeta donde se depositen las descargas
path = f"{downloads_path}\ZeroUtube Downloads"

try:
    os.mkdir(path)
except OSError:
    print("%s ya fue creado" % path)
else:
    print("Successfully created the directory %s " % path)

# Ubicarnos en la  carpeta downlooads
os.chdir(f"{path}")


def pathextension(extension):
    path=f"{downloads_path}\ZeroUtube Downloads\{extension}"
    try:
        os.mkdir(path)
    except OSError:
        print("%s ya fue creado" % path)
    else:
        print("Successfully created the directory %s " % path)
    os.chdir(f"{path}")

# Definimos la función para borrar la pantalla
def borrarPantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


# Setear las opciones para la descarga del audio MP3
opcionesmp3 = {
    'format': 'bestaudio/best',
    'ignoreerrors': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# MP3 para playlist
opcionesmp3playlist = {
    'format': 'bestaudio/best',
    'playlist': '--yes-playlist',
    'ignoreerrors': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# Setear las opciones para la descarga del video MP4
opcionesmp4 = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio',
    'ignoreerrors': True,
}

# MP4 para playlist
opcionesmp4playlist = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio',
    'playlist': '--yes-playlist',
    'ignoreerrors': True,
}


def descargar(opciones, url):
    with youtube_dl.YoutubeDL(opciones) as ydl:
        try:
            ydl.download([url])
        except:
            print("Error al descargar, omitiendo...")


print(" \n \n \t ZeroUtube Downloader \n")

# Main #
while opwhile == '1':
    op1 = input("Desea descargar un solo video o una playlist?\n 1: Un video\n 2: Playlist \n->")
    if op1 == '1':
        op2 = input("descargar en:\n 1: MP4\n 2: MP3\n->")
        if op2 == '1':
            input_url = input("Ingrese la URL del video: \n->")
            pathextension("Mp4")
            descargar(opcionesmp4, input_url)

        else:
            if op2 == '2':
                input_url = input("Ingrese la URL del video: \n->")
                pathextension("Mp3")
                descargar(opcionesmp3, input_url)
    else:
        if op1 == '2':
            op2 = input("descargar en:\n 1: MP4\n 2: MP3\n->")
            if op2 == '1':
                input_url = input("Ingrese la URL de la playlist: \n->")
                pathextension("Mp3")
                descargar(opcionesmp4playlist, input_url)

            else:
                if op2 == '2':
                    input_url = input("Ingrese la URL de la playlist: \n->")
                    pathextension("Mp3")
                    descargar(opcionesmp3playlist, input_url)

    opwhile = input("\nDesea descargar otra video/playlist?\n1: Si\n2: No\n->")
    borrarPantalla()  # Fallando
