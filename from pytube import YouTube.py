from pytube import YouTube

def descargar_video(url, ruta_descarga='./videos'):
    try:
        # Crear objeto YouTube
        yt = YouTube(url)

        # Obtener la mejor calidad disponible
        video = yt.streams.get_highest_resolution()

        # Crear la carpeta de descarga si no existe
        import os
        if not os.path.exists(ruta_descarga):
            os.makedirs(ruta_descarga)

        # Descargar el video
        print(f'Descargando video: {yt.title}')
        video.download(ruta_descarga)
        print('Descarga completada.')

    except Exception as e:
        print(f'Ocurrió un error: {str(e)}')

if __name__ == "__main__":
    # Ingresa la URL del video de YouTube que deseas descargar
    url_video = input("Ingresa la URL del video de YouTube: ")

    # Ingresa la ruta de descarga (opcional, se usará './videos' por defecto si no se proporciona)
    ruta_descarga = input("Ingresa la ruta de descarga (opcional, presiona Enter para usar './videos'): ")
    if not ruta_descarga:
        ruta_descarga = './videos'

    # Llamar a la función para descargar el video
    descargar_video(url_video, ruta_descarga)
