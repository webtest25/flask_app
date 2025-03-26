from fask import Flask

app = Flask(__name__)

@app.route('/')
def home():
  return 'hello from flask app!'

if __name__ == '__main__':
  app.run()
