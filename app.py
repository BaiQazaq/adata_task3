from flask import Flask, request, jsonify, make_response
import json
import dicttoxml

app = Flask(__name__) # Create object of Flask

@app.route('/json_to_xml', methods=['POST']) #View for woking with POST requests
def json_to_xml():
    try:
        data = request.json # Extract Json data from request
        if not data:
            return make_response(jsonify({'error': 'Invalid JSON data'}), 400)
        
        xml_data = dicttoxml.dicttoxml(data) # Converting Json format from 'data' to XML format and write to 'xml_dat'
        return make_response(xml_data, 200, {'Content-Type': 'application/xml'}) # Return made response with XML
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)

if __name__ == '__main__':
    app.run(debug=True)
