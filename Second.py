'''While loop'''
# learn comments
from typing import Any, Union

'''magicNumber =5
i=0
while i<10:
    if i is magicNumber:
        print(i)
        break
    i=i+1'''

# continue

'''numbersTaken =[2,5,12,33,17]
print('Here are the numbers that are still available:')

for n in range(1,20):
    if n in numbersTaken:
        continue
    print(n)'''

# Functions

'''def writeLog(message):
    print(message)

writeLog('Hello How Are You')
writeLog('I am Good')
writeLog('How about u')'''

# Return values
'''

def allowed_dating_age(my_age):
    girl_age = my_age / 2 + 7
    return girl_age


age = allowed_dating_age(10)
print(age)
'''

# functions with default values
'''
def get_gender(sex='Unknown'):
    if sex is 'm':
        print('Male')
    elif sex is 'f':
        print('Female')
    else:
        print(sex)

get_gender('m')
get_gender('f')
get_gender()
'''

# arguments

'''
def dumb_sentence(name='Bucky', action='ate', item='tuna'):
    print(name, action, item)

dumb_sentence()

dumb_sentence('ram', 'drink', 'gently')

dumb_sentence(item='ausin', action='go')

'''

# Flexible number of arguments

'''
def add_numbers(*args):
    z=0
    for i in args:
       z=z+i
    return z


total  = add_numbers(1,2,3,4,5,6,7,8)

print(total)

'''

# Unpacking arguments
'''
def heath_calculator(age, apples_ate, aigs_smoked):
    answer = (100 - age) + (apples_ate * 2) + aigs_smoked * 5
    print(answer)


health = [12, 10, 23]

heath_calculator(*health)
heath_calculator(health[0], health[1], health[2])

'''

# Modules example

'''

import tuna as a

a.flash()

'''

# Download image from web

'''
import random
import urllib.request

def download_web_image(url):
    name=random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjsytzklP3gAhWRM-wKHYAzCpoQjRx6BAgBEAU&url=https%3A%2F%2Fwww.homedepot.com%2Fp%2FMea-Nursery-FRAGRANT-Red-Mister-Lincoln-Rose-62014%2F304937447&psig=AOvVaw2fEAVroMI5IypIILxDDmKV&ust=1552499315339750")

'''

# Read and write files
'''
fw = open('test.txt', 'w')
fw.write("Hello Ram, How Are You")
fw.write("I lile becon")
fw.close()

fr = open('test.txt','r')
print(fr.read())
fr.close()
'''

# Download files from web

from urllib import request

google_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1549994555&period2=1552413755&interval=1d&events=history&crumb=kekH1WFqa/M'


def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_sr = str(csv)
    lines = csv_sr.split("\\n")
    fw = open(r"google.csv", 'w')
    for line in lines:
        fw.writeline(line + '\n')
    fw.close()


download_stock_data(google_url)
