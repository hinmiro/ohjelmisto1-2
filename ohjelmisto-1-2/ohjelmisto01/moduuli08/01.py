import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    database='flight_game',
    user='py_flight',
    password='p@ssword',
    autocommit=True
)

print(connection)


def icao_searcher(name):
    sql = "SELECT airport.name, country.name"
    sql += " FROM airport"
    sql += " INNER JOIN country ON airport.iso_country = country.iso_country"
    sql += " WHERE airport.ident ='" + name + "';"
    cursori = connection.cursor()
    cursori.execute(sql)
    result = cursori.fetchone()
    if cursori.rowcount > 0:
        return result


airport_name = input("Anna lentokentän ICAO-koodi, etsitään vastaavan kentän nimi: ")
result_arr = icao_searcher(airport_name)
print(f"Lentokentän nimi on {result_arr[0]} ja maa jossa kenttä sijaitsee on {result_arr[1]}.")

connection.close()
