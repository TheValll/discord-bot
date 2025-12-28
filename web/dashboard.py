from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Chemins des fichiers
BIRTHDAYS_FILE = '../data/birthdays.json'
VOTES_FILE = '../data/votes.json'
LOGS_FILE = '../data/game_logs.txt'

def load_json(path):
    if not os.path.exists(path):
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    birthdays = load_json(BIRTHDAYS_FILE)
    votes = load_json(VOTES_FILE)
    
    logs = ""
    if os.path.exists(LOGS_FILE):
        with open(LOGS_FILE, 'r', encoding='utf-8') as f:
            logs = f.readlines()[-20:]
    
    return render_template('index.html', birthdays=birthdays, votes=votes, logs=logs)

@app.route('/add_member', methods=['POST'])
def add_member():
    server_key = request.form.get('server_key')
    name = request.form.get('name')
    date = request.form.get('date')
    
    data = load_json(BIRTHDAYS_FILE)
    if server_key in data:
        data[server_key]['members'].append({"name": name, "birthday": date})
        save_json(BIRTHDAYS_FILE, data)
    
    return redirect(url_for('index'))

@app.route('/edit_member/<server_key>/<int:member_id>', methods=['POST'])
def edit_member(server_key, member_id):
    name = request.form.get('name')
    date = request.form.get('date')
    
    data = load_json(BIRTHDAYS_FILE)
    if server_key in data and member_id < len(data[server_key]['members']):
        data[server_key]['members'][member_id] = {"name": name, "birthday": date}
        save_json(BIRTHDAYS_FILE, data)
    
    return redirect(url_for('index'))

@app.route('/delete_member/<server_key>/<int:member_id>', methods=['POST'])
def delete_member(server_key, member_id):
    data = load_json(BIRTHDAYS_FILE)
    if server_key in data and member_id < len(data[server_key]['members']):
        data[server_key]['members'].pop(member_id)
        save_json(BIRTHDAYS_FILE, data)
    
    return redirect(url_for('index'))

@app.route('/add_server', methods=['POST'])
def add_server():
    key = request.form.get('key').lower()
    name = request.form.get('server_name')
    channel_id = int(request.form.get('channel_id'))
    
    data = load_json(BIRTHDAYS_FILE)
    data[key] = {
        "server_name": name,
        "channel_id": channel_id,
        "members": []
    }
    save_json(BIRTHDAYS_FILE, data)
    return redirect(url_for('index'))

@app.route('/delete_server/<server_key>', methods=['POST'])
def delete_server(server_key):
    data = load_json(BIRTHDAYS_FILE)
    if server_key in data:
        del data[server_key]
        save_json(BIRTHDAYS_FILE, data)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)