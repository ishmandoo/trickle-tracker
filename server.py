from flask import Flask, render_template
app = Flask(__name__)
import pickle

f = open('out.pkl', 'rb')   # Pickle file is newly created where foo1.py is
data = pickle.load(f)
f.close() 
'''
data = [
    {'lat': 33.81066, 'lon': -116.697426, 'name': 'N Fork San Jacinto River', 'prediction': 1}, 
    {'lat': 33.317172, 'lon': -116.626687, 'name': 'Agua Caliente Creek, last crossing.', 'prediction': 0.2}, 
    {'lat': 32.608, 'lon': -116.498991, 'name': 'Creeklet', 'prediction': 0.8}, 
    {'lat': 32.729263, 'lon': -116.490416, 'name': 'Cottonwood Creek bed', 'prediction': 0.5}, 
    {'lat': 32.715239, 'lon': -116.499008, 'name': 'Cottonwood Creek Bridge, usually dry.', 'prediction': 0.8}
    ]

'''

for loc in data:
    pred = loc['prediction']
    if  pred > 0.8:
        loc['class'] = 'r'
    elif pred > 0.5:
        loc['class'] = 'p'
    else:
        loc['class'] = 'u'

print(data)

@app.route('/')
def hello():    
    return render_template("index.html", data=data)



if __name__ == '__main__':
    app.run(debug=True)