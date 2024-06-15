import os
from flask import Flask, request, render_template_string
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection setup
mongo_uri = os.getenv('MONGO_URI', 'mongodb://104.237.3.15:27017/')
client = MongoClient(mongo_uri)
db = client.ip_database
collection = db.ip_addresses

def reverse_ip(ip_address):
    octets = ip_address.split('.')
    reversed_octets = octets[::-1]
    reversed_ip = '.'.join(reversed_octets)
    return reversed_ip

template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Reverse IP Address</title>
</head>
<body>
    <h1>Enter IP Address to Reverse</h1>
    <form method="post">
        IP Address: <input type="text" name="ip_address">
        <input type="submit" value="Reverse">
    </form>
    {% if reversed_ip %}
        <h2>Reversed IP Address: {{ reversed_ip }}</h2>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    reversed_ip = None
    if request.method == 'POST':
        ip_address = request.form.get('ip_address')
        if ip_address:
            reversed_ip = reverse_ip(ip_address)
            collection.insert_one({'original_ip': ip_address, 'reversed_ip': reversed_ip})
    return render_template_string(template, reversed_ip=reversed_ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
