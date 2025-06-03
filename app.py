
from flask import Flask, request, jsonify
from monique_core import monique

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(monique.status())

@app.route('/log-deal', methods=['POST'])
def log_deal():
    data = request.json
    monique.log_deal(data.get('deal_name', 'Unnamed Deal'))
    return jsonify(monique.status())

@app.route('/confirm-agent', methods=['POST'])
def confirm_agent():
    data = request.json
    monique.confirm_agent_ready(data.get('agent_name', 'Unknown'))
    return jsonify(monique.status())

@app.route('/attempt-transition')
def attempt_transition():
    return jsonify({"transition_result": monique.attempt_transition()})
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
