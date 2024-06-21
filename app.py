# imports
from flask import Flask, render_template, request, redirect, flash
from flask_socketio import SocketIO

# setups and global variables
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages
socketio = SocketIO(app)

# app routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/media')
def media():
    return render_template('media.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# CALLING EVERYTHING TOGETHER
if __name__ == '__main__':
    socketio.run(app)