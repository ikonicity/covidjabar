from flask import Flask, render_template
import requests, schedule

app = Flask (__name__)

def jabar():
    api_url = "https://api.kawalcorona.com/indonesia/provinsi"
    rstl= requests.get(api_url).json()
    cek=rstl[1]
    ambil_dic= cek ["attributes"]
    a=[ambil_dic]
    return a

realtime_jabar = schedule.every(2).seconds.do(jabar)

#cek schedule
#while True:
 #   schedule.run_pending()

data_jabar = jabar()
#print(data_jabar)


'''attributes: {FID: 12, Kode_Provi: 32, Provinsi: "Jawa Barat", Kasus_Posi: 277553, Kasus_Semb: 243650,…}
FID: 12
Kasus_Meni: 3678
Kasus_Posi: 277553
Kasus_Semb: 243650
Kode_Provi: 32
Provinsi: "Jawa Barat"
'''
@app.route("/")
def index():
    #return render_template('TESTLAGI.HTML')
    return render_template('index.html', data_jabar=data_jabar)

if __name__=="__main__":
    app.run(debug=True)