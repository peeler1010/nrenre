from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import FileResponse

def home(request):
    return render(request, 'home.html', {})
def list(request):
    keyword = request.GET.get('keyword')
    datalist = []
    url = keyword
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    a = soup.find(class_="thread")
    title = soup.find(class_="container container_body mascot")
    content = title.find("h1")
    for items in a.find_all(class_="post"):
        c = items.find(class_="message")
        message = c.find(class_="escaped")
        datalist.append(message.text+"\n")
    file_path = 'myfile.txt'
    f = open('myfile.txt', 'w', encoding='UTF-8')
    f.writelines(datalist)
    f.close()
    return FileResponse(open(file_path, "rb"), as_attachment=True, filename=content.text)