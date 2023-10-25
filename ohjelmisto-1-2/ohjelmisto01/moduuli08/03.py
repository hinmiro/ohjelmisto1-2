import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='flight_game',
    user='py_flight',
    password='p@ssword',
    autocommit=True
)


def distance_calc(icao):
    sql = "SELECT latitude_deg, longitude_deg"
    sql += " FROM airport"
    sql += " WHERE ident ='" + icao + "';"
    cursori = connection.cursor()
    cursori.execute(sql)
    result = cursori.fetchall()
    if cursori.rowcount > 0:
        return result


icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Anna toisen lentokentän ICAO-koodi: ")

coordinates1 = distance_calc(icao1)
coordinates2 = distance_calc(icao2)

print(f"Lentokenttien etäisyys on {distance.distance(coordinates1[0], coordinates2[0]).km:.2f}")
