from flask import Flask, request, jsonify, Response
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

# Copyright © 2024 YuvrajMODZ
# Developed by [𝐌𝐀𝐓𝐑𝐈𝐗]
# Telegram Contact : @VZR7X

@app.route('/zipinfo', methods=['GET'])
def zip_info():
    format_type = request.args.get('format', 'json').lower()
    zipcode = request.args.get('zipcode')

    if format_type == 'xml':
        return jsonify({"error": "XML format not supported"}), 400

    if not zipcode:
        return jsonify({"error": "Zipcode parameter is required"}), 400

    url = f'https://pincode.net.in/{zipcode}'
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Failed to retrieve data"}), 500

    soup = BeautifulSoup(response.text, 'html.parser')

    offices = soup.select('.articles h2, .articles b, .articles a, .articles br')
    post_offices = []
    post_office_data = {}
    current_label = ""

    for item in offices:
        if item.name == 'h2':
            if post_office_data:
                post_offices.append(post_office_data)
            post_office_data = {"Details": item.get_text(strip=True)}
        elif item.name == 'b':
            current_label = item.get_text(strip=True).replace(":", "")
        elif item.name == 'a' and current_label:
            post_office_data[current_label] = item.get_text(strip=True)
        elif item.name == 'br':
            current_label = ""
    
    if post_office_data:
        post_offices.append(post_office_data)
        
    if format_type == 'json':
        return jsonify(post_offices)
    elif format_type == 'txt':
        txt_response = ""
        for office in post_offices:
            for key, value in office.items():
                txt_response += f"{key}: {value}\n"
            txt_response += "\n"
        return Response(txt_response, mimetype='text/plain')
    else:
        return jsonify({"error": "Invalid format specified"}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5003))
    app.run(host='0.0.0.0', port=port, debug=True)