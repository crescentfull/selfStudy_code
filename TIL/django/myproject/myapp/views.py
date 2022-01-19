import random

from this import d #랜덤모듈 사용

from django.shortcuts import render, HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse('<h1>random</h2>'+str(random.random())) #random만 하면 숫자라서 오류가 나기 때문에 랜덤함수를 스트링, 문자열로 치환해줘야한다

topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ...'},
    {'id':2, 'title':'view', 'body':'view is ...'},
    {'id':3, 'title':'Model', 'body':'Model is ...'},   
]

def HTMLTemplate(articleTag):
    global topics #global로 전역변수 설정을 해줘야한다.
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
    return HttpResponse('create')

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))