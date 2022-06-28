from django.shortcuts import render
from django.http import HttpResponse
from .models import urlClass
import requests
# Create your views here.
def home(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/neko").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#sfw
#waifu
def sfwwaifu(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/waifu").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#neko
def sfwNeko(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/neko").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#megumin
def sfwmegumin(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/megumin").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#shinobu
def sfwshinobu(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/shinobu").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#waifu
def sfwbully(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/bully").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#waifu
def sfwcuddle(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/cuddle").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#waifu
def sfwcry(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/cry").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#waifu
def sfwhug(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/hug").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#waifu
def sfwawoo(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/awoo").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#waifu
def sfwkiss(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/kiss").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#waifu
def sfwlick(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/lick").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#waifu
def sfwneko(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/neko").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#waifu
def sfwpat(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/pat").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#waifu
def sfwsmug(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/smug").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#bonk
def sfwbonk(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/bonk").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#yeet
def sfwyeet(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/yeet").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#blush
def sfwblush(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/blush").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#smile
def sfwsmile(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/smile").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#smile
def sfwwave(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/wave").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#highfive
def sfwhighfive(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/highfive").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#handhold
def sfwhandhold(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/handhold").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#nom
def sfwnom(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/nom").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#bite
def sfwbite(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/bite").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#glomp
def sfwglomp(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/glomp").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#slap
def sfwslap(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/slap").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#kill
def sfwkill(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/kill").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#kick
def sfwkick(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/kick").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#happy
def sfwhappy(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/happy").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#wink
def sfwwink(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/wink").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#poke
def sfwpoke(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/poke").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#dance
def sfwdance(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/dance").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
#cringe
def sfwcringe(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/sfw/cringe").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)

    return render(request   , "index.html", {'urlList': urls})
# nsfw
#waifu
def nsfwwaifu(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/nsfw/waifu").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)
    return render(request   , "index.html", {'urlList': urls})
#neko
def nsfwneko(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/nsfw/neko").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)
    return render(request   , "index.html", {'urlList': urls})
#trap
def nsfwtrap(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/nsfw/trap").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)
    return render(request   , "index.html", {'urlList': urls})
#smile
def nsfwblowjob(request):
    urls=[]
    for i in range(0,19):
        url = requests.get("https://api.waifu.pics/nsfw/blowjob").json()['url']
    
        urldic = urlClass()
        urldic.url = url
        urls.append(urldic)
    return render(request   , "index.html", {'urlList': urls})