from flask import Flask,request,render_template, url_for
from tensorflow.python.keras.backend import set_session
import keras
from keras.models import load_model
import numpy as np
global model, graph, sess
import tensorflow as tf

sess = tf.Session()
graph = tf.get_default_graph()

set_session(sess)
model = load_model('profit_pred.h5')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/login', methods =['POST']) #when you click submit on html page it is redirection to this url
def login():#as soon as this url is redirected then call the below functionality
    a = request.form['a']
    b = request.form['b']
    c = request.form['c']
    d = request.form['s']
    if (d == "newyork"):
        s1=0
        s2=0
        s3 = 1
    if (d == "florida"):
        s1=0
        s2=1
        s3 = 0
    if (d == "california"):
        s1=1
        s2=0
        s3 = 0
        
    total = [[s1,s2,s3,a,b,c]]
    with graph.as_default():
        set_session(sess)
        ypred = model.predict(np.array(total))
        y = ypred[0][0]
        print(ypred)

    # from html page what ever the text is typed  that is requested from the form functionality and is stored in a name variable
    return render_template('index.html' ,abc = y)#after typing the name show this name on index.html file where we have created a varibale abc


if __name__ == '__main__':
    app.run(debug = False)