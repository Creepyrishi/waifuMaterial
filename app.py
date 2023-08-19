from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route('/')
def home():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/neko").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)
#sfw

@app.route('/sfw/waifu')
@app.route('/sfw/waifu')
def sfwwaifu():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/waifu").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)
#neko
@app.route('/sfw/waifu')
def sfwNeko():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/neko").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)
#megumin
@app.route('/sfw/waifu')
def sfwmegumin():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/megumin").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)
#shinobu
@app.route('/sfw/waifu')
def sfwshinobu():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/shinobu").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwbully():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/bully").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwcuddle():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/cuddle").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwcry():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/cry").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwhug():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/hug").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwawoo():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/awoo").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwkiss():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/kiss").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwlick():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/lick").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwneko():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/neko").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwpat():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/pat").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwsmug():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/smug").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwbonk():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/bonk").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)
@app.route('/sfw/waifu')
def sfwyeet():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/yeet").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwblush():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/blush").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwsmile():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/smile").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwwave():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/wave").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwhighfive():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/highfive").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwhandhold():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/handhold").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwnom():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/nom").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwbite():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/bite").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwglomp():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/glomp").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwslap():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/slap").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwkill():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/kill").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwkick():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/kick").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwhappy():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/happy").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/waifu')
def sfwwink():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/wink").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/poke')
def sfwpoke():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/poke").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/dance')
def sfwdance():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/dance").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/sfw/cringe')
def sfwcringe():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/sfw/cringe").json()['url']
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/nsfw/waifu')
def nsfwwaifu():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/nsfw/waifu").json()['url']        
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/nsfw/neko')
def nsfwneko():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/nsfw/neko").json()['url']        
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/nsfw/trap')
def nsfwtrap():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/nsfw/trap").json()['url']        
        urls.append(url)
    return render_template('index.html', urlList=urls)

@app.route('/nsfw/blowjob')
def nsfwblowjob():
    urls=[]
    for i in range(0,25):
        url = requests.get("https://api.waifu.pics/nsfw/blowjob").json()['url']        
        urls.append(url)
    return render_template('index.html', urlList=urls)



if __name__ == '__main__':
    app.run(debug=False)