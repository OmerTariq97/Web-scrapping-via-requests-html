from requests_html import HTMLSession
def test():
    session = HTMLSession()
    # r = session.get('https://propakistani.pk/price/oppo-a58x/')
    r = session.get('https://propakistani.pk/price/categories/mobile/')

    # title = r.html.xpath('//*[@id="single-featured"]/div[2]/div[1]/h1/strong')
    # camera = r.html.xpath('//*[@id="specifications"]/ul/li[1]/div/div[2]')
    # processor = r.html.xpath('//*[@id="specifications"]/ul/li[2]/div/div[2]')
    # storage = r.html.xpath('//*[@id="specifications"]/ul/li[3]/div/div[2]')
    # battery = r.html.xpath('//*[@id="specifications"]/ul/li[4]/div/div[2]')
    # ram = r.html.xpath('//*[@id="specifications"]/ul/li[5]/div/div[2]')
    # display = r.html.xpath('//*[@id="specifications"]/ul/li[6]/div/div[2]')

    phones = r.html.find('.thumb-area')
    for phone in phones:
        name = phone.find('.title', first = True)
        name_list = list(name.links)
        
        r = session.get(f'{name_list[0]}')
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
    
        list1 = [title, price, status, camera, processor, storage, battery, ram, display]
        return list1
        # print(title.text ,camera, processor, storage, 
        #       battery, ram, display)

        # camera = r.html.xpath('//*[@id="specifications"]/ul/li[1]/div/div[2]', first = True)
        # if "camera" in camera.text.lower():
        #     print(camera.text)

        # processor = r.html.xpath('//*[@id="specifications"]/ul/li[2]/div/div[2]', first = True)
        # if 'processor' in processor.text.lower():
        #     print(processor.text)

        # storage = r.html.xpath('//*[@id="specifications"]/ul/li[3]/div/div[2]', first = True)
        # if 'storage' in storage.text.lower():
        #     print(storage.text)
        # battery = r.html.xpath('//*[@id="specifications"]/ul/li[4]/div/div[2]', first = True)
        # if 'battery' in battery.text.lower():
        #     print(battery.text)
        # ram = r.html.xpath('//*[@id="specifications"]/ul/li[5]/div/div[2]', first = True)
        # if 'ram' in ram.text.lower():
        #     print(ram.text)
        # display = r.html.xpath('//*[@id="specifications"]/ul/li[6]/div/div[2]', first = True)
        # # if display is not None and 'display' in display.text.lower():
        #     # print(display.text)
        # try:
        #     print(display.text)
        # except AttributeError:
        #     print('no such attribute')
        # print(title.text ,camera.text, processor[0].text, storage[0].text, 
        # battery[0].text, ram[0].text, display[0].text)


