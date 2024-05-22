
import sys
sys.path.append( "src" )

import psycopg2

from model.Usuario import Usuario
import SecretConfig

class ControladorUsuarios :

    def CrearTabla():
        """ Crea la tabla de usuario en la BD """
        cursor = ControladorUsuarios.ObtenerCursor()

        cursor.execute("""create table usuarios (
  cedula varchar( 20 )  NOT NULL,
  nombre text not null,
  apellido text not null,
  telefono varchar(20),
  correo text,
  direccion text not null,
  codigo_municipio varchar(40) not null,
  codigo_departamento varchar(40) NOT NULL
); """)
        cursor.connection.commit()

    def EliminarTabla():
        """ Borra la tabla de usuarios de la BD """
        cursor = ControladorUsuarios.ObtenerCursor()

        cursor.execute("""drop table usuarios""" )
        # Confirma los cambios realizados en la base de datos
        # Si no se llama, los cambios no quedan aplicados
        cursor.connection.commit()


    def InsertarUsuario( usuario : Usuario ):
        """ Recibe un a instancia de la clase Usuario y la inserta en la tabla respectiva"""
        cursor = ControladorUsuarios.ObtenerCursor()
        cursor.execute( f"""insert into usuarios (cedula, nombre, apellido, 
                            direccion, telefono, 
                            codigo_municipio, codigo_departamento) 
                        values ('{usuario.cedula}', '{usuario.nombre}', '{usuario.apellido}',  
                            '{usuario.direccion}', '{usuario.telefono}',
                            '{usuario.codigo_municipio}', 'usuario.codigo_departamento')""" )

        cursor.connection.commit()

    def BuscarUsuarioCedula( cedula ):
        """ Trae un usuario de la tabla de usuarios por la cedula """
        cursor = ControladorUsuarios.ObtenerCursor()

        cursor.execute("""select cedula, nombre, apellido, direccion, correo, telefono, codigo_departamento, codigo_municipio
        from usuarios where cedula = '1234657'""" )
        fila = cursor.fetchone()
        resultado = Usuario( cedula=fila[0], nombre=fila[1], apellido=fila[2], direccion=fila[3],telefono=fila[4],
                            codigo_departamento=fila[5], codigo_municipio=fila[6], correo=fila[4]  )
        return resultado



    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor
