from flask import Flask
import sys
app = Flask(__name__)
@app.route('/')
def Hello_name():
    return f'hello {sys.argv[1]}'

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
