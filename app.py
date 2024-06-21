# imports
from flask import Flask, render_template, request, redirect, flash
from flask_socketio import SocketIO

# setups and global variables
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages
socketio = SocketIO(app)

# app routes
@app.route('/templates/index')
def home():
    return render_template('index.html')

@app.route('/templates/about')
def about():
    return render_template('about.html')

@app.route('templates//media')
def media():
    return render_template('media.html')

@app.route('templates/events')
def events():
    return render_template('events.html')

@app.route('templates/contact')
def contact():
    return render_template('contact.html')

# CALLING EVERYTHING TOGETHER
if __name__ == '__main__':
    socketio.run(app)
