from flask import Flask, request, jsonify
import conection
# Configuración de Flask
app = Flask(__name__)


#-----------------------------------------------------------------------#
# LISTAR 
@app.route('/categorias', methods=['GET'])
def listarCategoria():
    try:
        connection = conection.conectar()
        with connection:
            with connection.cursor() as cursor:
                sql = 'SELECT id, nombre FROM categorias'
                cursor.execute(sql)
                results = cursor.fetchall()
                user_data = []
                for row in results:
                    user_data.append({'id': row['id'], 'nombre': row['nombre']})
                return jsonify({'data': user_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
        
# FIN LISTAR    


# REGISTRAR
@app.route('/categorias', methods=["POST"])
def crearCategoria():
    data = request.get_json()

    try:
        connection = conection.conectar()
        with connection.cursor() as cursor:
            sql = "INSERT INTO categorias (nombre) VALUES (%s)"
            cursor.execute(sql, (data['nombre']))
        connection.commit()
        return jsonify({'message': 'Categoría creada correctamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# FIN REGISTRAR



# ACTUALIZAR
@app.route('/categorias/<int:id>', methods=["PUT"])
def actualizarCategoeria(id):
    data = request.get_json()

    try:
        connection = conection.conectar()
        with connection.cursor() as cursor:
            sql = "UPDATE categorias SET nombre = %s WHERE id = %s"
            cursor.execute(sql, (data['nombre'], id))
        connection.commit()
        return jsonify({'message': 'Categoría actualizada'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# FIN ACTUALIZAR


# ELIMINAR
@app.route('/categorias/<int:id>', methods=["DELETE"])
def eliminarCategoria(id):
    try:
        connection = conection.conectar()
        with connection.cursor() as cursor:
            sql = "DELETE FROM categorias WHERE id = %s"
            cursor.execute(sql, (id,))
        connection.commit()
        return jsonify({'message': 'Categoría eliminada'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# FIN ELIMINAR
#-----------------------------------------------------------------------#


#------------------- PRODUCTOS -----------------------------------------#
#-----------------------------------------------------------------------#
# LISTAR 
@app.route('/productos', methods=['GET'])
def listarProductos():
    try:
        connection = conection.conectar()
        with connection:
            with connection.cursor() as cursor:
                sql = 'SELECT id, nombre, precio, categoria_id FROM productos'
                cursor.execute(sql)
                results = cursor.fetchall()
                user_data = []
                for row in results:
                    user_data.append({'id': row['id'], 'nombre': row['nombre'], 'precio': row['precio'], 'categoria_id': row['categoria_id']})
                return jsonify({'data': user_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
        
# FIN LISTAR    


# REGISTRAR
@app.route('/productos', methods=["POST"])
def crearProducto():
    data = request.get_json()

    try:
        connection = conection.conectar()
        with connection.cursor() as cursor:
            sql = "INSERT INTO productos (nombre, precio, categoria_id) VALUES (%s, %s, %s)"
            cursor.execute(sql, (data['nombre'], data['precio'], data['categoria_id']))
        connection.commit()
        return jsonify({'message': 'Producto creado correctamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# FIN REGISTRAR



# ACTUALIZAR
@app.route('/productos/<int:id>', methods=["PUT"])
def actualizarProducto(id):
    data = request.get_json()

    try:
        connection = conection.conectar()
        with connection.cursor() as cursor:
            sql = "UPDATE productos SET nombre = %s, precio = %s, categoria_id = %s WHERE id = %s"
            cursor.execute(sql, (data['nombre'], data['precio'], data['categoria_id'], id))
        connection.commit()
        return jsonify({'message': 'Producto actualizado'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# FIN ACTUALIZAR


# ELIMINAR
@app.route('/productos/<int:id>', methods=["DELETE"])
def eliminarProducto(id):
    try:
        connection = conection.conectar()
        with connection.cursor() as cursor:
            sql = "DELETE FROM productos WHERE id = %s"
            cursor.execute(sql, (id,))
        connection.commit()
        return jsonify({'message': 'Producto eliminado'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# PRODUCTO POR CATEGORIA
@app.route('/categorias/<int:id>/productos', methods=["GET"])
def ProductoPorCategoria(id):
    try:
        connection = conection.conectar()
        with connection:
            with connection.cursor() as cursor:
                sql = 'SELECT p.id, p.nombre, p.precio, p.categoria_id FROM productos p INNER JOIN categorias c ON p.categoria_id = c.id WHERE c.id =%s'
                cursor.execute(sql, (id,))
                results = cursor.fetchall()
                user_data = []
                for row in results:
                    user_data.append({'id': row['id'], 'nombre': row['nombre'], 'precio': row['precio'], 'categoria_id': row['categoria_id']})
                return jsonify({'data': user_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# FIN 
#-----------------------------------------------------------------------#

    
# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)

