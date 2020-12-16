from flask import Flask, jsonify, request

app = Flask(__name__)
stores = [
    {
        'name': 'apple',
        'items': [
            {
                'name': 'iphone',
                'price': 999.99
            }
        ]
    }
]


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    if not any(d['name'] == request_data['name'] for d in stores):
        new_store = {
            'name': request_data['name'],
            'items': []
        }
        stores.append(new_store)
        return jsonify(new_store)
    return jsonify({'message': 'store with same name already exists'}), 400


# <string:name> special flask syntax
@app.route('/store/<string:name>', methods=['GET'])
def get_store_name(name):
    for store in stores:
        print('store name: {}'.format(store['name']))
        if name == store['name']:
            return jsonify(store)
    return jsonify({'message': 'store not found'}), 404


@app.route('/store', methods=['GET'])
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def post_store_item(name):
    for store in stores:
        if name == store['name']:
            request_data = request.get_json()
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store does not exist'}), 404


@app.route('/store/<string:name>/item', methods=['GET'])
def get_store_name_item(name):
    for store in stores:
        if name == store['name']:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'}), 404


@app.route('/store/<string:name>/item/<string:item_name>', methods=['GET', 'DELETE'])
def get_or_delete_item(name, item_name):
    for store in stores:
        if name == store['name']:
            for item in store['items']:
                if item_name == item['name']:
                    if request.method == 'GET':
                        return jsonify(item)
                    elif request.method == 'DELETE':
                        store['items'].remove(item)
                        return jsonify({'items': store['items']})
    return jsonify({'message': 'item not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)

