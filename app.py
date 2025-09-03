# app.py
# A simple Flask application that provides a /status endpoint.

# app.py
from flask import Flask, jsonify, request, g
import os

app = Flask(__name__)

@app.before_request
def log_request_info():
    # Store the body data in the global 'g' object
    g.body = request.get_data()
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', g.body)

# Define the /status endpoint
@app.route('/status', methods=['GET', 'POST'])
def status():
    """
    Returns a simple JSON status indicating the application is running.
    """
    # Now you can access the body data from the 'g' object
    # You must decode it to use a JSON parser
    data = g.body
    headers = request.headers
    app.logger.debug("--------------------------------")
    app.logger.debug(data)
    app.logger.debug("--------------------------------")
    app.logger.debug('Headers: %s', headers)
    try:
        json_data = request.get_json()
        if json_data and json_data.get("type") == "url_verification":
            return jsonify({"challenge": json_data["challenge"]})
    except Exception as e:
        app.logger.error(f"Failed to parse JSON: {e}")
        pass # Handle cases where the body is not JSON

    return jsonify({"challenge": "3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P"})

# Main entry point for the Flask application
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

