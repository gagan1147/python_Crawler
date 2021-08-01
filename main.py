import requests
import os
import time
from bs4 import BeautifulSoup

count = 0
base_url = 'https://www.zalando.fr'
base_dir = os.getcwd()

header = {

    'if-none-match': 'W/"340-Q8hpQxylzf/opZmh35f98skFVWc"',
    'x-xsrf-token': 'AAAAAFC_g3k0kI-fo_KJZ9UrFBdKHZTaGteaQguJmt6p5A-FYxLoIW73ajdX2VCrk2yim9-UhLaNhffi72gyDR2THhCZMrH-3AHgDGm9XSXs4t252wmUF8QOeJGf6sNUCbl46aBJfNhT8UgNx2jVug==',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    'accept': '/',
    'authority': 'www.zalando.fr',
    'accept-encoding': 'gzip, deflate, br',
}


def imagedown(url, folder):
    print url
    file_dir = os.path.join(os.getcwd(), folder)
    #print file_dir
    try:
        os.mkdir(file_dir)
    except:
        pass
    os.chdir(file_dir)
    try:
        r = requests.get(url,headers = header)
        soup = BeautifulSoup(r.text, 'html.parser')
        divs = soup.find('div',{'class':'KVKCn3 u-C3dd jDGwVr mo6ZnF KLaowZ'})
        images = divs.find_all('img')
        #print len(images)
        #print(images)'
        count = 0
        for image in images:
            print image
            name = image['alt']
            link = image['src']
            with open(name.replace(' ', '-').replace('/', '') + str(count+1) +'.jpg', 'wb') as f:
                count +=1
                im = requests.get(link)
                f.write(im.content)
                print('Writing: ', name)
    except:
        pass
    os.chdir(base_dir)

for i in range(1,100):
    url = 'https://www.zalando.fr/t-shirts-tops-femme/?p='+str(i)
    print url
    r = requests.get(url,headers = header)
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    images = soup.find_all('a',{'class':'_LM JT3_zV g88eG_ VfpFfd g88eG_ oHRBzn LyRfpJ'})
    #count = 0
    for img in images:
        imagedown(img['href'],"img"+str(count))
        #print base_url+img['href'],'\n'
        time.sleep(2)
        count = count + 1
