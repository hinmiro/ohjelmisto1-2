from flask import Flask, Response
import json
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='flight_game',
    user='py_flight',
    password='p@ssword',
    autocommit=True
)


def icao_searcher(icao):
    sql = f"SELECT airport.name, country.name"
    sql += f" FROM airport"
    sql += f" INNER JOIN country ON airport.iso_country = country.iso_country"
    sql += f" WHERE airport.ident ='{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if cursor.rowcount > 0:
        return result, 200
    else:
        return 'not_found', 'not_found', 400


@app.route('/kenttä/<icao>')
def get_icao(icao):
    try:
        query = icao_searcher(icao.upper())
        if int(query[1]) == 200:
            status_code = 200
            response_data = {"ICAO": icao, "Name": query[0][0], "Municipality": query[0][1]}
            response_data = json.dumps(response_data)
            response = Response(response=response_data, status=status_code, mimetype="application/json")
            return response

    except ValueError:
        response_data = {"ICAO": icao, "msg": "Faulty ICAO code"}
        status_code = 400

        response_data = json.dumps(response_data)
        response = Response(response=response_data, status=status_code, mimetype="application/json")
        return response


@app.errorhandler(404)
def page_not_found():
    response = {"status": "404", "msg": "Faulty endpoint"}
    return response, 404


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
