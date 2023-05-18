from django.shortcuts import render
from .import utils
from requests_html import HTMLSession
from .models import mobile
import time
import pandas as pd
from rest_framework import viewsets
from . serializers import mobileSerializer
# Create your views here.

def home(request):
    session = HTMLSession()
    page_number = 1
    r = session.get('https://propakistani.pk/price/categories/mobile/')
    mobile_data = []

    # Loop through pages
    while page_number <= 5:
        print('new page' + str(page_number))
        phones = r.html.find('.thumb-area')
        # Loop through phones one by one
        for phone in phones:
            
            # Gets the link of a phone 
            name = phone.find('.title', first = True)
            name_list = list(name.links)
            r = session.get(f'{name_list[0]}')
            
            #None so we can use it later on if we don't get.
            camera = None
            processor = None
            storage = None
            battery = None
            ram = None
            display = None
            
            title = r.html.xpath('//*[@id="single-featured"]/div[2]/div[1]/h1/strong', first = True)
            price = r.html.xpath('//*[@id="single-featured"]/div[2]/div[1]/h2/span', first = True)
            status = r.html.xpath('//*[@id="single-featured"]/div[2]/div[1]/div[2]', first = True)

            specs = r.html.find('.spec-dt')
            
            for spec in specs:
                if 'camera' in spec.text.lower():
                    camera = spec.text
                    continue

                if 'processor' in spec.text.lower():
                    processor = spec.text
                    continue

                if 'storage' in spec.text.lower():
                    storage = spec.text
                    continue
                
                if 'battery' in spec.text.lower():
                    battery = spec.text
                    continue
                    
                if 'ram' in spec.text.lower():
                    ram = spec.text
                    continue
                
                if 'display' in spec.text.lower():
                    display = spec.text
                    continue
            
            if camera is None:
                camera = ''
            if processor is None:
                processor = ''
            if storage is None:
                storage = ''
            if battery is None:
                battery = ''
            if ram is None:
                ram = ''
            if display is None:
                display = ''
            
            # print specs of a phone 
            # print(title.text, price.text, status.text ,camera, processor, storage, 
            #     battery, ram, display)

            # creates a record of a phone
            # mobile.objects.create(name = title.text, price = price.text, status = status.text, camera = camera, processor = processor,
            #                       storage = storage, battery = battery, ram = ram, display = display)
            
            # list to hold data for pandas dataframe
            # mobile_data.append({
            #     'name': title.text,
            #     'price': price.text,
            #     'status': status.text,
            #     'camera': camera,
            #     'processor': processor,
            #     'storage': storage,
            #     'battery': battery,
            #     'ram': ram,
            #     'display': display
            # })

        # go to the url where all phones are listed
        r = session.get(f'https://propakistani.pk/price/categories/mobile/page/{page_number}/')
        page_number += 1
        next_page  = r.html.find('.next', first = True).links

        if next_page is not None:
            next_page_list = list(next_page)
            r = session.get(f'{next_page_list[0]}')
        time.sleep(3)
    
    # df = pd.DataFrame(mobile_data)
    # print(df.head())
    # df.to_csv('mobile_data.csv')
    return render(request, 'home.html')

class mobileViewSet(viewsets.ModelViewSet):
    queryset = mobile.objects.all()
    serializer_class = mobileSerializer
