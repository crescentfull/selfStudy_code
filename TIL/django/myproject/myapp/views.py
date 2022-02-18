#import random#랜덤모듈 사용

from tkinter.messagebox import NO
from django.shortcuts import render, HttpResponse, redirect


# def index(request):
#     return HttpResponse('<h1>random</h2>'+str(random.random())) #random만 하면 숫자라서 오류가 나기 때문에 랜덤함수를 스트링, 문자열로 치환해줘야한다
nextId = 4
topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ...'},
    {'id':2, 'title':'view', 'body':'view is ...'},
    {'id':3, 'title':'Model', 'body':'Model is ...'},   
]

def HTMLTemplate(articleTag, id=None):
    global topics #global로 전역변수 설정을 해줘야한다.
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li>
                <form action="/delete/" method="post">
                    <input type="hidden" name="id" value="{id}">
                    <input type="submit" value="delete">
                </form>
            </li>
        '''
        
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return HttpResponse(f'''
                        <html>
                        <body>
                            <h1><a href="/">Django</a></h1>
                            <ul>
                                {ol}
                            </ul>
                            {articleTag}
                            <ul>
                                <li><a href="/create/">create</a></li>
                                {contextUI}
                            </ul>
                        </body>
                        </html>
                        ''')
    
def index(request):
    article = '''
            <h2>welcom</h2>
            Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

def create(request):
    print('request.method :', request.method)
    global nextId
    if request.method == 'GET':
        article = '''
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        title    = request.POST['title']
        body     = request.POST['body']
        newTopic = {"id":nextId, "title":title, "body":body}
        
        topics.append(newTopic)
        url = '/read/'+str(nextId)
        nextId = nextId + 1
        
        return redirect(url) #HttpResponse(request.POST['title'])

def read(request, id):
    global topics
    article = ''
    
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article, id))

def delete(request):
    global topics
    if request.method == 'POST':
        id = request.POST['id']
        newTopics = []
        
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
                
        topics = newTopics
        print('id',id)
        return redirect('/')
