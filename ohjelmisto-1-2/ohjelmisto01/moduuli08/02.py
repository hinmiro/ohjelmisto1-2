import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='flight_game',
    user='py_flight',
    password='p@ssword',
    autocommit=True
)


def airports(code):
    sql = "SELECT type, count(*)"
    sql += " FROM airport"
    sql += " WHERE iso_country ='" + code + "'"
    sql += " GROUP BY type;"
    cursori = connection.cursor()
    cursori.execute(sql)
    result = cursori.fetchall()
    if cursori.rowcount > 0:
        return result
    else:
        print("Lentoasemaa ei löytynyt.")
        return list()


airport_iso = input("Anna maatunnus, haetaan sen maan lentokentät: ")
result_ports = airports(airport_iso)

for row in result_ports:
    print(f"{row[0]} tyyppisiä lentokenttiä on {row[1]}")
connection.close()
