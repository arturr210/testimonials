from flask import Flask

app = Flask(__name__)

application = app

@app.route('/')
def index():
    return 'hellooujkk;lu!!'

@app.route('/api/testimonials')
def restimonials():
    return {'testimonial' : ['great', 'its ok', 'fantastic']}