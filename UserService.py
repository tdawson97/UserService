import UserService
import json
import sqlite3
import os
from flask import Flask, jsonify, request

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))

with sqlite3.connect('database.db') as connection:
  cursor = connection.cursor()

  create = '''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL);'''

  cursor.execute(create)
  connection.commit()


@app.route('/signup', methods=['POST'])
def signup():
  if request.method == 'POST':
    if request.headers['Content-Type'] != 'application/json':
      return jsonify({'error': 'Unsupported Media Type'}), 415
    username = request.json.get('username')
    password = request.json.get('password')

    with sqlite3.connect('database.db') as connection:
      cursor = connection.cursor()

      insert = '''
        INSERT INTO Users (username, password)
        VALUES (?, ?);'''
      
      cursor.execute(insert, (username, password))

      connection.commit()

      select = '''
        SELECT id FROM Users WHERE username = ?'''
      cursor.execute(select, (username,))
      id = cursor.fetchone()
    return jsonify({'id':id[0]}), 200

  
@app.route('/login', methods=['POST'])
def login():
  if request.method == 'POST':
    if request.headers['Content-Type'] != 'application/json':
      return jsonify({'error': 'Unsupported Media Type'}), 415
    username = request.json.get('username')
    password = request.json.get('password')

    with sqlite3.connect('database.db') as connection:
      cursor = connection.cursor()

      select = '''
        SELECT id FROM Users WHERE username = ? AND password = ?'''
      cursor.execute(select, (username, password))
      id = cursor.fetchone()

      if id is None:
        return jsonify({'error': 'No account exists with that username and password'}), 401
      else:
        return jsonify({'id':id[0]}), 200
      
  
@app.route('/change_password', methods=['POST'])
def change_password():
  if request.method == 'POST':
    if request.headers['Content-Type'] != 'application/json':
      return jsonify({'error': 'Unsupported Media Type'}), 415
    username = request.json.get('username')
    password = request.json.get('password')
    newPassword = request.json.get('newPassword')

    with sqlite3.connect('database.db') as connection:
      cursor = connection.cursor()

      update = '''
          UPDATE Users SET password = ? WHERE username = ? AND password = ?'''
      cursor.execute(update, (newPassword, username, password))

      connection.commit()
        
      return jsonify({'data': 'Password changed successfully'}), 200
    

if __name__ == "__main__":
  app.run(port=5000, debug=True)