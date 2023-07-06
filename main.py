from flask import Flask, jsonify, request
from flights_data import flights
app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify({
        'hello': 'mum',
        'goodbye': 'dad'
    })
@app.route('/flights')
def get_flights():
    return jsonify(flights)

@app.route('/flights/<int:id>')
def get_flight_by_id(id):
    flight = search_flight(id, flights)
    return jsonify(flights)

@app.route('/flights', methods=['POST'])
def add_flight():
    flight = request.get_json()
    flight.append(flight)
    return flight

def search_flight(id, flights):
    for flight in flights:
        if flight['flight_id'] == id:
            return flight
        return None


if __name__ == '__main__':
    app.run(debug=True)
