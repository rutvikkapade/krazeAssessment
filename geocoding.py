import requests
from functools import cache
import os

API_KEY='AIzaSyAVddq24VUnrb2u8uM44FQQppHsQHx1OZA'
API_URL='https://maps.googleapis.com/maps/api/geocode/json?address='

def compute():
    line=read_file('input.txt')
    os.remove('input.txt')
    return compute_geocode(clean_data(line))

def read_file(filename):
    f=open(filename,'r')
    line=f.readlines()
    f.close()
    return line

def clean_data(line):
    cities=[city.strip() for city in line if len(city.strip())!=0]
    return cities


def compute_geocode(cities):
    if not len(cities):
        return False
    coordinates=[geocode_util(city) for city in cities]
    output=open('output.txt','w')
    for data in coordinates:
        vals=''
        if 'lat' in data:
            vals=vals+str(data['lat'])+','+str(data['lng'])+'\n'
            output.write(vals)
        else:
            output.write('Invalid City Name\n')
    output.close()
    return True

    
@cache
def geocode_util(city):
    data=requests.get(API_URL+city+'&key='+API_KEY)
    res=data.json()
    if len(res['results'])==0:
        return {}
    return res['results'][0]['geometry']['location']
