from flask import Flask,render_template,request
from .user_input import *
def create_app():
    # initializes our app
    app = Flask(__name__)

    @app.route('/')
    def form():
        return render_template('base.html')

    @app.route('/data/', methods = ['POST', 'GET'])

    def data():
        if request.method == 'GET':
            return f"The URL /data is accessed directly. Try going to '/form' to submit form"
        if request.method == 'POST':
            form_data = request.form
            artist = request.form.get('artist', 'default')
            track = request.form.get('track', 'default')
            df = convert(artist, track)
        return render_template('data.html',form_data = form_data, artist=artist, track=track, df = df)
  
    return app


