# Para las aplicaciones web creadas con Flask, debemos importar siempre el modulo 
from flask import Flask , request , render_template   

# Para poder servir plantillas HTML desde archivos, es necesario importar el modulo render_template
import sys
sys.path.append( "src" )

from datetime import date

from model.Usuario import Usuario
from controller.ControladorUsuarios import ControladorUsuarios
# la configuración que queremos para nuestra aplicación
app = Flask(__name__)     

# decorator: se usa para indicar el URL Path por el que se va a invocar nuestra función
@app.route('/parametros')      
def parametros():
   return request.args

@app.route('/usuario')      
def buscar_usuario():
   cedula_buscada= request.args["cedula"]
   usuario_buscado :Usuario = ControladorUsuarios.BuscarUsuarioCedula(cedula=cedula_buscada)
   return render_template ("usuario.html", usuario=usuario_buscado)
    
      
# Esta linea permite que nuestra aplicación se ejecute individualmente
if __name__=='__main__':
   app.run()