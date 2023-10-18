from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

class CSVORM:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.data = []
        self.load_data()

    def load_data(self):
        with open(self.csv_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            self.data = list(csv_reader)

    def list(self):
        return self.data

    def get(self, id):
        for row in self.data:
            if row['ID'] == id:
                return row
        return None

    def filter(self, column, value):
        filtered_data = []
        for row in self.data:
            if row.get(column) == value:
                filtered_data.append(row)
        return filtered_data

csv_orm = CSVORM(r'C:\Users\Stazzy\Desktop\IotReady\data.csv')

@app.route('/data', methods=['GET'])
def list_data():
    return jsonify(csv_orm.list())

@app.route('/data/<id>', methods=['GET'])
def get_data(id):
    data = csv_orm.get(id)
    if data:
        return jsonify(data)
    else:
        return 'Data not found', 404

@app.route('/filter', methods=['GET'])
def filter_data():
    column = request.args.get('column')
    value = request.args.get('value')
    if column and value:
        filtered_data = csv_orm.filter(column, value)
        return jsonify(filtered_data)
    else:
        return 'Invalid filter parameters', 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)
