from fask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return 'Hello from flask app!'
