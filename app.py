from flask import Flask, render_template
<<<<<<< HEAD
import requests, json
=======
import requests #, schedule
>>>>>>> 99a5f52bbdc58e2cd3f98eafd030a7c88865289a

app = Flask (__name__)

def jabar():
    api_url = 'https://api.kawalcorona.com/indonesia/provinsi'
    rstl= requests.get(api_url).json()
    cek=rstl[1]
    ambil_dic= cek ['attributes']
    a=[ambil_dic]
    return a

<<<<<<< HEAD
=======
#realtime_jabar = schedule.every(2).seconds.do(jabar)

#cek schedule
#while True:
 #   schedule.run_pending()

>>>>>>> 99a5f52bbdc58e2cd3f98eafd030a7c88865289a
data_jabar = jabar()

@app.route('/')
def index():
    return render_template('index.html', data_jabar=data_jabar)

<<<<<<< HEAD
if __name__=='__main__':
    app.run(debug=True)
=======
if __name__=="__main__":
    app.run(debug=True)
>>>>>>> 99a5f52bbdc58e2cd3f98eafd030a7c88865289a
