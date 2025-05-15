from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    # Get current date and time
    current_time = datetime.utcnow().isoformat() + "Z"
    
    # Get visitor IP address
    visitor_ip = request.remote_addr

    # Return JSON response
    return jsonify({
        "timestamp": current_time,
        "ip": visitor_ip
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

