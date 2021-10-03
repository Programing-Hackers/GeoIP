#!/usr/bin/env python3

import requests
import re

class GeoIP():
 
    def __init__(self):
        
        print("""
        #####################################
        	Created by: Benyamin
        	(Programing-Hackers)
        	
        https://github.com/Programing-Hackers
        
        #####################################
        """)

        ip = input('IP a geolocalizar:> ').strip()
       
        print('Realizando la solicitud>>>')

        response = requests.get('https://es.geoipview.com/?q=%s&x=0&y=0' % format(ip))
        if(response.status_code == 200):

            items = {
                'host'      : r'del\s+Host:.+?class="host">(.*?)<',
                'ip'        : r'de\s+IP:.+?class="show2">(.*?)<',
                'country'   : r'País:.+?<td>(.*?)<',
                'region'    : r'Región:.+?<td>(.*?)<',
                'city'      : r'Ciudad:.+?class="show2">(.*?)<',
                'postal'    : r'Postal:.+?<td>(.*?)<',
                'latitude'  : r'Latitud:.+?<td>(.*?)<',
                'longitude' : r'Longitud:.+?<td>(.*?)<'
            }
            print('-' * 27)
            for item in items:
                matches = re.search(items[item], response.text, re.I | re.M)
                print(
                    '%s : %s' % (
                        item.title().ljust(9), # Key name
                        matches.group(1).replace('&nbsp;', ' ').strip() if matches else '-'
                    )
                )
        else:
            print('Error de respuesta (%s).' % str(response.status_code))
            
if __name__ == "__main__":
    try:
        GeoIP()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        raise e