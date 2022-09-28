import requests
from bs4 import BeautifulSoup
import base64

def iniciarConexion():
    uri = "https://www.google.com/search?q=pinarello+f12&rlz=1C1GCEU_esES852ES852&sxsrf=APq-WBvWAIZkzgmSYd3gsNEXSoSbPcLJXA:1645705148935&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiP8rm2qZj2AhVf_rsIHe4OD3sQ_AUoAnoECAEQBA&biw=1536&bih=268&dpr=1.25"
    headers = {'Host': 'www.google.com',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    res = requests.get(uri, headers=headers, allow_redirects=False)
    html = res.content
    document = BeautifulSoup(html, 'html.parser')
    return document
def descargarImagenes(document):
    img_results = document.find_all('img', {'class': 'rg_i Q4LuWd'})
    for idx, each in enumerate(img_results):
        src = ""
        if each.has_attr('src'):
            src = each['src']
        else:
            src = each['data-src']
        print(str(idx) + " " + src)
        img = None
        if src.find("data:image") != -1:
            # data:[<mime type>][;charset=<charset>][;base64],<encoded data>
            if src == "data:image/jpeg;base64,":
                img = base64.b64decode(src.replace("data:image/jpeg;base64,", ""))
            else:
                img = base64.b64decode(src.replace("data:image/gif;base64,", ""))
        else:
            res = requests.get(src)
            img = res.content
        file = open("./img/" + str(idx) + ".jpeg", "wb")
        file.write(img)
        file.close()






if __name__ == '__main__':
    document = iniciarConexion()
    descargarImagenes(document)
