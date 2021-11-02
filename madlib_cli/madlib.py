import re
from typing import Text
def welcome_message () :
    print('\n  Welcome to MADLIB game!\n')

def read_template(path):
    try:
        with open(path) as link:
            content=link.read()
    except FileNotFoundError:
        return "file link is not found"
    else:
        return content

def parse_template(path):
    text=read_template(path)
    x=re.findall("{.*?}",text)
    i=0
    answers=[]
    while i < len(x):
        answer=input("enter  "+x[i]+"  ")
        answers+=[answer]
        i+=1
    return answers,x    

def merge(path):
    text=read_template(path)
    content=text
    x=re.findall("{.*?}",text)
    i=0
    answers=[]
    while i < len(x):
        answer=input("enter  "+x[i]+"  ")
        answers+=[answer]
        content=content.replace( x[i] , answers[i],1)
        i+=1
    print(content)

welcome_message()