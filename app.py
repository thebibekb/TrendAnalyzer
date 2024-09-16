from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the top 20 t-shirts, dresses, and skirts
top_20_tshirts = pd.read_csv('top_20_tshirts.csv')
top_20_dresses = pd.read_csv('top_20_dresses.csv')
top_20_skirts = pd.read_csv('top_20_skirts.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tshirt')
def tshirt():
    return render_template('products.html', products=top_20_tshirts.to_dict(orient='records'), category="T-shirts")

@app.route('/dress')
def dress():
    return render_template('products.html', products=top_20_dresses.to_dict(orient='records'), category="Dresses")

@app.route('/skirt')
def skirt():
    return render_template('products.html', products=top_20_skirts.to_dict(orient='records'), category="Skirts")

if __name__ == '__main__':
    app.run(debug=True)
