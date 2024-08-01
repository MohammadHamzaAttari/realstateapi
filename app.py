from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

RAPIDAPI_HOST = "zillow56.p.rapidapi.com"
RAPIDAPI_KEY = "7162965176mshc59b3f298c80e10p19f027jsn3011fe8edd93"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_property_details', methods=['POST'])
def get_property_details():
    address = request.form['address']
    url = f'https://{RAPIDAPI_HOST}/search_address'
    headers = {
        'x-rapidapi-host': RAPIDAPI_HOST,
        'x-rapidapi-key': RAPIDAPI_KEY
    }
    params = {'address': address}
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({"error": "Failed to retrieve data"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
