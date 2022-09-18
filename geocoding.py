import requests
from functools import cache
import os

#enter your API key here
API_KEY=''

#enter your API url here
API_URL=''


def compute():
    line=read_file('input.txt')
    os.remove('input.txt')
    return compute_geocode(clean_data(line))

#function to read all the cities provided in input file
#returns array of cities
def read_file(filename):
    f=open(filename,'r')
    line=f.readlines()
    f.close()
    return line

#cleans the data , removes empty strings and returns cities list
def clean_data(line):
    cities=[city.strip() for city in line if len(city.strip())!=0]
    return cities


#computes geo code for each city and writes lat and longi in output file
#returns true if output file successfully created ,else false
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


#calls google geocode api by passing city name as the parameter
#returns lat and longi of particular city, this function is cached 
# in memory to limit number of API calls
@cache
def geocode_util(city):
    data=requests.get(API_URL+city+'&key='+API_KEY)
    res=data.json()
    if len(res['results'])==0:
        return {}
    return res['results'][0]['geometry']['location']
