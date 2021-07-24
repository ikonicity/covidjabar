from flask import Flask, render_template
import requests, json


app = Flask (__name__)



data_jabar = jabar()

def jabar():
    api_url = 'https://api.kawalcorona.com/indonesia/provinsi'
    rstl= requests.get(api_url).json()
    cek=rstl[1]
    ambil_dic= cek ['attributes']
    a=[ambil_dic]
    return a


@app.route('/')
def index():
    return render_template('index.html', data_jabar=data_jabar)


if __name__=='__main__':
    app.run(debug=True)
