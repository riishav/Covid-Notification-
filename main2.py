from plyer import notification
from bs4 import BeautifulSoup
import requests

def notifyUs(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "F:\CovidNotification\coronaviruslogo.ico",
        timeout =15
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__" :
    #notifyUs("Rishav", "We'll stop this virus together")
    HtmlData = getData('https://www.mohfw.gov.in/')

    
    soup = BeautifulSoup(HtmlData, 'html.parser')

    #active_cases = soup.find("li",{'class': 'bg-blue'}).find("span",{'class': 'up'})
    #.find_all("strong",{'class': 'mob-hide'}) #.find('strong',{'class': 'mob-hide'})
    active_cases = soup.find("li",{'class': 'bg-blue'})
    active = active_cases.get_text().split()
    print(active[1])
    #discharged
    discharged_cases = soup.find("li",{'class': 'bg-green'})
    discharge = discharged_cases.get_text().split()
    print(discharge[1])
    #death
    death_cases= soup.find("li",{'class': 'bg-red'})
    death = death_cases.get_text().split()
    print(death[1])
    #total
    total_cases = int(active[1])+ int(discharge[1])+ int(death[1])
    print(total_cases)

    total_vaccination = soup.find("div",{'class': 'fullbol'}).find("span",{'class': 'coviddata'})
    vaccinated = total_vaccination.get_text()
    print(vaccinated)
    ntitle = 'Status of COVID-19 & Vaccination'
    ntext = f"Confirmed Cases : {total_cases}\nActive Cases :{active[1]}\nCured :{discharge[1]}  Deaths : {death[1]}\nVaccinated : {vaccinated}"
    notifyUs(ntitle, ntext)
