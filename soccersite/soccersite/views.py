from django.shortcuts import render
import requests


# Create your views here.
def homescreen(request):
    r1 = requests.get('https://zenquotes.io/api/quotes')
    data = r1.json()
    events = data[1]['q']
    author0 = data[1]['a']

    r2 = requests.get('https://dog.ceo/api/breeds/image/random')
    res2 = r2.json()
    dog = res2['message']

    r3 = requests.get('https://dog.ceo/api/breeds/image/random')
    res3 = r3.json()
    dog2 = res3['message']

    r4 = requests.get('https://v2.jokeapi.dev/joke/Programming?type=twopart&amount=3')
    data1 = r4.json()
    setup1 = data1['jokes'][0]['setup']
    delivery1 = data1['jokes'][0]['delivery']

    setup2 = data1['jokes'][1]['setup']
    delivery2 = data1['jokes'][1]['delivery']

    r5 = requests.get('https://v2.jokeapi.dev/joke/Dark?type=twopart&amount=3')
    data2 = r5.json()
    setup3 = data2['jokes'][0]['setup']
    delivery3 = data2['jokes'][0]['delivery']

    setup4 = data2['jokes'][1]['setup']
    delivery4 = data2['jokes'][1]['delivery']

    r5 = requests.get('https://zenquotes.io/api/quotes')
    data3 = r5.json()
    quote1 = data3[0]['q']
    author1 = data3[0]['a']

    quote2 = data3[2]['q']
    author2 = data3[2]['a']

    quote3 = data3[3]['q']
    author3 = data3[3]['a']




 
    
    return render(request,'templates/index.html',{
        'events':events , 'author0':author0,
         'dog':dog , 'dog2':dog2 ,
          'setup1':setup1 , 'delivery1':delivery1 , 'setup2':setup2 , 'delivery2':delivery2 , 'setup3':setup3 , 'delivery3':delivery3 , 'setup4':setup4 , 'delivery4':delivery4 ,
          'quote1':quote1, 'author1':author1 , 'quote2':quote2, 'author2':author2 , 'quote3':quote3, 'author3':author3})