from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def main(request):
    return render(request, "index.html")
def covid(request):
    return render(request, "covid.html")
def search(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        # API_KEY = '6621546e1a94625a215c063e4320d66d'
        covid_API=f'https://covid-api.mmediagroup.fr/v1/cases?country={country}'
        res=requests.get(covid_API)
        data=res.json()
        confirmed=data['All']['confirmed']
        recovered=data['All']['recovered']
        deaths=data['All']['deaths']
        count=data['All']['country']
        population=data['All']['population']
        token_API = f"https://covid-api.mmediagroup.fr/v1/cases"
        covid= requests.get(token_API)
        covid_json=covid.json()
        cheknumber=[]
        chekcountry=[]
        finish={}
        for i in covid_json:
            cheknumber.append(covid_json[i]['All']['confirmed'])
            chekcountry.append(i)
            # print(covid_json[i]['All']['confirmed'],i)
        a=max(cheknumber[:-1])
        index = cheknumber.index(a)
        # print(index)
        print(chekcountry[index])
        for i in range(10):
            lst=[]
            a=max(cheknumber[:-1])
            index = cheknumber.index(a)
            finish[chekcountry[index]]=cheknumber[index]
            chekcountry.pop(index)
            cheknumber.pop(index)
            lst.append(finish)
            print(type(finish))
        print(type(lst))
        return render(request,  'covid.html', {'data' :data, 'covid' :covid, 'recovered' :recovered, 'deaths' :deaths, 'count' :count, 'population' :population, 'confirmed' :confirmed, 'finish' :finish, 'lst' :lst})
