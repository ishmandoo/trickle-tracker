from flask import Flask, render_template
app = Flask(__name__)
import pickle
import sys

f = open('out_combined.pkl', 'rb')   # Pickle file is newly created where foo1.py is
data = pickle.load(f)
f.close() 

data.sort(key=lambda i: i['mile'])

print(data)

@app.route('/')
def hello():    
    return render_template("index.html", data=data)



if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'prod':
        app.run(port=80, host='0.0.0.0')
    else:
        app.run(debug=True)