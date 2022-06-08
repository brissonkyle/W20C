from dbcreds import *
import mariadb
from flask import jsonify
from flask import Flask, request, Response
app = Flask(__name__)

@app.get('/api/animals')
def user_get():
    conn = mariadb.connect(user=user,
                    password=password,
                    host=host,
                    port=port,
                    database=database
                    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM animals')
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result), 200

@app.post('/api/animals/post')
def user_post():
    conn = mariadb.connect(user=user,
                    password=password,
                    host=host,
                    port=port,
                    database=database
                    )
    cursor = conn.cursor()
    cursor.execute('INSERT INTO animals (animals) VALUES ("Penguin") ')
    cursor.close()
    conn.close()
    user_response = {'' : ''}
    return Response(
        jsonify(Response), 200
    )

@app.patch('/api/animals/patch')
def user_patch():
    conn = mariadb.connect(user=user,
                    password=password,
                    host=host,
                    port=port,
                    database=database
                    )
    cursor = conn.cursor()
    cursor.execute('UPDATE animals SET animals="Penguin" WHERE animals="Monkey"')
    cursor.close()
    conn.close()
    return Response(
        print("You've updated Successfully")
    )


@app.patch('/api/animals/delete')
def user_delete():
    conn = mariadb.connect(user=user,
                    password=password,
                    host=host,
                    port=port,
                    database=database
                    )
    cursor = conn.cursor()
    cursor.execute('DELETE FROM animals WHERE animals="Penguin"')
    cursor.close()
    conn.close()
    return Response(
        print('Youve Deleted an animal')
        print(jsonify(), 200)
    )

