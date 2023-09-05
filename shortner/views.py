from django.shortcuts import render
from .models import ShortUrl
from .forms import CreateNewShortURL
from datetime import datetime
import random,string

# Create your views here.

def home(request):
    return render(request, 'shortner/home.html')

def createShortURL(request):
    if request.method=='POST':
        form =CreateNewShortURL(request.POST)
        if form.is_valid():
            original_website=form.cleaned_data['original_url']
            random_chars_list=list(string.ascii_letters) #randomly return of the letters from alphabet
            random_chars=''
            for i in range(6):
                random_chars+=random.choice(random_chars_list)
            while len(ShortUrl.objects.filter(short_url=random_chars))!=0: #to make sure that current generated url is unique one
                for i in range(6):
                    random_chars+=random.choice(random_chars_list)
            d=datetime.now()
            s=ShortUrl(original_url=original_website,short_url=random_chars,time_date_created=d)
            s.save()
            return render(request,'shortner/urlcreated.html',{'chars':random_chars}) 
    else:
        form=CreateNewShortURL()
        context={'form':form}
        return render(request,'shortner/create.html',context)       

def redirect(request,url):
    current_obj=ShortUrl.objects.filter(short_url=url)
    if len(current_obj)==0:
        return render(request,'shortner/pagenotfound.html')
    context={'obj':current_obj[0]} #getting the original url by indexing 
    return render(request,'shortner/redirect.html',context)
