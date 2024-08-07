from flask import Flask, request, jsonify
from flask_cors import CORS
from googleMaps_Scrape import scrape_google_maps
import json
import os

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        data = request.get_json()
        keyword = data.get('keyword', 'lawyer')
        location = data.get('location', '')
        output_file = 'results.json'
        
        # Assuming your scrape_google_maps function takes keyword and output_file as parameters
        scrape_google_maps(f"{keyword} {location}", output_file)
        with open(output_file, 'r', encoding='utf-8') as f:
            results = json.load(f)
            
        return jsonify(results)
    except Exception as e:
        error_message = str(e)
        return jsonify({'error': error_message}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
