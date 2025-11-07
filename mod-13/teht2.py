from credentials import MYSQL_PASSWORD
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{MYSQL_PASSWORD}@localhost/flight_game'
db = SQLAlchemy(app)


@app.route('/airport/<ident>')
def airport(ident):
    try:
        query = text("SELECT ident, name, municipality FROM airport WHERE ident = :ident")
        result = db.session.execute(query, {"ident": ident}).fetchone()
        if result is None:
            return jsonify({"error": "Airport not found"}), 404
        response = {
            "ICAO": result[0],
            "Name": result[1],
            "Location": result[2]
        }
        return jsonify(response)

    except ValueError:
        error_code = 400
        response = {
            "status": error_code,
            "description": "Invalid ICAO code"
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
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
