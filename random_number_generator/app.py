from flask import Flask
from rand_gen import random_number_generator

app = Flask(__name__)


@app.route('/')
def index():
    return "Random Number: %d " % (random_number_generator(1, 5))


app.run(host='0.0.0.0', port=8888)
