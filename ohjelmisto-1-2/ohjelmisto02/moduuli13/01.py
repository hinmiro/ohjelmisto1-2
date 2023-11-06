from flask import Flask

app = Flask(__name__)


@app.route('/alkuluku/<number>')
def get_prime(number):
    number = int(number)
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                response = {"Number": number, "isPrime": "false"}
                return response

        else:
            response = {"Number": number, "isPrime": "true"}
            return response
    else:
        response = {"Number": number, "isPrime": "false"}
        return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
