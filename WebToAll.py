#!/usr/bin/python3

#################################################################
#email:-    nikhilkumaraur8241@gmail.com                        #
#linkedin:- https://www.linkedin.com/in/nikhil-kumar-4b8497271/ #
# github:-  https://github.com/NikhilVKumar                     #
#################################################################

import requests
from bs4 import BeautifulSoup
import webbrowser
from termcolor import colored
  

logo="""
-----------------------------
▀▄▀▄▀ 🢇 ꔪ ▀█▀ 🞉 ▅▀▅ █▄ █▄
Tools by Nikhil Kumar ᵥ.₀₁    
-----------------------------
"""
print(colored(logo,'yellow'))

class all_to_all:
    def resposes(self):
        print(1)
        print(2)
        choice = int(input("Enter your choice :- "))
        if (choice == 1):
            url = requests.Session()
            a = input(str('Enter your tag :- '))
            url = input(str('Enter your url :- '))
            resposes = requests.get(url)
            htmlcontent = resposes.content
            soup = BeautifulSoup(htmlcontent,'html.parser')
            print(soup.a)
            file = open('list.txt', 'wb')
            file.write(resposes.content)
            file.close()
            webbrowser.open("list.txt")
        if (choice == 2):
            url = input(str("Enter Your url :- "))
            d=input(str("Enter your tag :- "))
            c=input(str("Enter you interface :- "))
            resposes = requests.get(url)
            htmlcontent = resposes.content
            soup = BeautifulSoup(htmlcontent,'html.parser')
            for link in soup.find_all(d):
                print(link.get(c))
object=all_to_all()
object.resposes()
