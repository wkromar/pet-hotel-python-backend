import flask
import psycopg2
from flask import request, jsonify, make_response
from psycopg2.extras import RealDictCursor
from config import config

app = flask.Flask(__name__)


@app.route('/api/owners', methods=['GET', 'POST'])
def api_all():
    params = config()
    connection = psycopg2.connect(**params)
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    if request.method == 'GET':
        query = 'SELECT "owners".*, COUNT("pets".id) AS "pet_count" FROM "owners" LEFT JOIN "pets" ON "owners".id = "pets".owner_id GROUP BY "owners".id, "pets".id;'
        # execute query
        cursor.execute(query)
        # Selecting rows from table using cursor.fetchall
        owners = cursor.fetchall()
        # respond, status 200 is added for us
        # print(owners)
        return jsonify(owners)
    elif request.method == 'POST':
        print('in post')
        owner = request.get_json()['name']
        print(owner)
        try:
            query = 'INSERT INTO "owners" ("name") VALUES (%s);'
            print('in try')
            cursor.execute(query, (owner, ))
            connection.commit()
            result = {'status': 'CREATED'}
            return make_response(jsonify(result), 201)
        except (Exception, psycopg2.Error) as error:
            if(connection):
                print("Failed to insert owner", error)
                # respond with error
                result = {'status': 'ERROR'}
                return make_response(jsonify(result), 500)
        finally:
            # closing database connection.
            if(connection):
                # clean up our connections
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
    else:
        print('no routes found')
        return 'no routes found'


@app.route('/api/owners/<id>', methods=['DELETE'])
def api_delete_owners(id):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute('DELETE FROM "owners" WHERE "id" = %s', (id,))
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return make_response(jsonify(id), 200)


@app.route('/api/pets', methods=["GET", "POST"])
def api_get_pets():
    params = config()
    connection = psycopg2.connect(**params)
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    if request.method == "GET":
        postgreSQL_select_Query = 'SELECT * FROM "pets";'
        # execute query
        cursor.execute(postgreSQL_select_Query)
        # Selecting rows from table using cursor.fetchall
        pets = cursor.fetchall()
        # respond, status 200 is added for us
        print(pets)
        return jsonify(pets)
    elif request.method == "POST":
        new_owner_id = request.get_json()['owner_id']
        new_pet_name = request.get_json()['pet_name']
        new_breed = request.get_json()['breed']
        new_color = request.get_json()['color']
        try:
            query = 'INSERT INTO "pets" ("owner_id", "pet_name", "breed", "color") VALUES(%s, %s, %s, %s);'
            cursor.execute(query, (new_owner_id, new_pet_name, new_breed, new_color, ))
            connection.commit()
            result={'status': 'CREATED'}
            return make_response(jsonify(result), 201)
        except (Exception, psycopg2.Error) as error:
            if(connection):
                print("Failed to insert owner", error)
                # respond with error
                result={'status': 'ERROR'}
                return make_response(jsonify(result), 500)
        finally:
            # closing database connection.
            if(connection):
                # clean up our connections
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
    else:
        print('no routes found')
        return 'no routes found'

    # elif request.method == 'POST':
    #     print('in post')
    #     owner = request.get_json()['name']
    #     print(owner)
    #     try:
    #         query = 'INSERT INTO "owners" ("name") VALUES (%s);'
    #         print('in try')
    #         cursor.execute(query, (owner, ))
    #         connection.commit()
    #         result = {'status': 'CREATED'}
    #         return make_response(jsonify(result), 201)
    #     except (Exception, psycopg2.Error) as error:
    #         if(connection):
    #             print("Failed to insert owner", error)
    #             # respond with error
    #             result = {'status': 'ERROR'}
    #             return make_response(jsonify(result), 500)
    #     finally:
    #         # closing database connection.
    #         if(connection):
    #             # clean up our connections
    #             cursor.close()
    #             connection.close()
    #             print("PostgreSQL connection is closed")


delete pets route
@app.route('/api/pets/<id>', methods=["DELETE"])
def delete(id):
    connection = None
    try:
        print(request.args)
        connection_params = config()
        # args = config()
        connection = psycopg2.connect(**connection_params)
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        postgreSQL_select_Query ='DELETE FROM "pets" WHERE id=%s'
        cursor.execute(postgreSQL_select_Query, (id,))
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

    return make_response(jsonify(id), 200)

# @app.route ('/api/pets/<id>', methods=["PUT"])
# def put(id, date):
#     connection = None
#     try:
#         print(request.connection)
#         connection_params = config()
#         connection = psycopg2.connect(**params)
#         cursor = connection.cursor(cursor_factory=RealDictCursor)
#         postgreSQL_select_Query = 'UPDATE "pets" WHERE id=%s SET "check_in"=%s WHERE id =%s'
#         cursor.execute(postgreSQL_select_Query, (id))
#         connection.commit()
#         cursor.close()

#     except (Exception, psycopg2.DatabaseError) as error:
#             print(error)
#     finally:
#             if connection is not None:
#                 connection.close()  



app.run()
