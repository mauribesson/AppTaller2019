from google.cloud.storage import Blob
from google.cloud import storage 
import webbrowser, os
from modelos.imagenes import Imagenes
from pathlib import Path


def guardarImagen(imagenes, idProducto): 
    #Seteo de Credenciales 
    rutaCredenciales = str(Path(__file__).parent / "./credenciales.json")
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = rutaCredenciales   
  
    client = storage.Client(project='AIzaSyDk6jA_SFUMsjdZn7jvruPhXbh1YJxwQ0U')
    bucket = client.get_bucket("apptaller-18740.appspot.com")
       
    for imagen in imagenes:
            path_imagen = os.path.basename(imagen.filename)
            blob = Blob(path_imagen, bucket)
            blob.upload_from_string(imagen.read(), content_type=imagen.content_type)
            blob.make_public()
            url = blob.public_url
            imagenes = Imagenes()
            imagenes.set_idProducto(idProducto)
            imagenes.set_urlImagen(url)
            data = imagenes.alta_imagen()

            print(url)

# var firebaseConfig = {
#     "apiKey": "AIzaSyDk6jA_SFUMsjdZn7jvruPhXbh1YJxwQ0U",
#     "authDomain": "apptaller-18740.firebaseapp.com",
#     "databaseURL": "https://apptaller-18740.firebaseio.com",
#     "projectId": "apptaller-18740",
#     "storageBucket": "apptaller-18740.appspot.com",
#     "messagingSenderId": "1063070929375",
#     "appId": "1:1063070929375:web:014b6b8c4b0e7ba8feb46a",
#     "measurementId": "G-WBPR2YC2NG"
#     }


