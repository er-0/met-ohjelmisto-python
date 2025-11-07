from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/prime_number/<number>')
def prime(number):
    try:
        number = int(number)
        is_prime = True
        if number < 2:
            is_prime = False
        else:
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
        response = {
            "Number": number,
            "isPrime": is_prime
        }
        return response

    except ValueError:
        error_code = 400
        response = {
            "status": error_code,
            "description": "Invalid number"
        }

    return jsonify(response), error_code

@app.errorhandler(404)
def page_not_found(error):
    response = {
        "status": error.code,
        "message": error.description
    }

    return jsonify(response), error.code

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)