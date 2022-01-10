# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 06:16:53 2021

@author: liali
"""

import requests
for i in range(200):
    req = requests.get('http://services.fms.gov.ru/services/captcha.jpg', stream=True)
    req.raise_for_status()
    with open(f'capthcas\captcha{i}.jpg', 'wb') as fd:
        for chunk in req.iter_content(chunk_size=50000):
            print(f'Received a Chunk {i}')
            fd.write(chunk)
