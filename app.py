from flask import Flask, render_template
from flask_socketio import SocketIO
import re  # Regular expressions for simple keyword extraction

# Initialize Flask app
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('user_message')
def handle_message(msg):
    # Process the message and extract insights
    response = process_audit_report(msg)
    socketio.emit('bot_response', response)

def process_audit_report(report):
    # Simple function to extract keywords or insights from the report
    # This is a placeholder for more complex logic
    # For example, we could extract potential vulnerabilities using regex
    vulnerabilities = re.findall(r'(?i)\b(vulnerability|risk|issue|alert|fail)\b', report)
    insights = []

    if vulnerabilities:
        insights.append(f'Identified Vulnerabilities: {", ".join(vulnerabilities)}')
    else:
        insights.append('No vulnerabilities identified.')

    return 'Extracted Insights: ' + ', '.join(insights)

if __name__ == '__main__':
    socketio.run(app, debug=True)
