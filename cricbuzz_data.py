import requests
from bs4 import BeautifulSoup
import csv
url = "https://www.cricbuzz.com/live-cricket-scorecard/31647/aus-vs-ind-3rd-test-india-tour-of-australia-2020-21"
data = requests.get(url)
data.status_code
soup = BeautifulSoup(data.text,'html')
innings = []
for i in soup.find_all('div',attrs={'class':'cb-col cb-col-100 cb-scrd-hdr-rw'}):
    innings.append(i.text.strip())
playinfo=[]
for i in soup.find_all('div',attrs={'class':'cb-col cb-col-100 cb-scrd-sub-hdr cb-bg-gray'}):
    t = i.text.strip().split("  ")
    playinfo.append(t)
playdata = [ ]
for i in soup.find_all('div',attrs={'class':'cb-col cb-col-100 cb-scrd-itms'}):
    playdata.append(i.text.strip().split("  "))

try:
    score=[]
    for i in range(len(playdata)):
        score.append(playdata[i][3].split(" "))
except: IndexError
print()
try:
    sb = []
    for i in range(len(playinfo)):
        sb.append(playinfo[i][1].split(" "))
except: IndexError
with open('cricbuzz.csv', 'w+', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([innings[0]])
    writer.writerow([playinfo[0][0]," ",sb[0][0],sb[0][1],sb[0][2],sb[0][3],sb[0][4]])
    for i in range(len(playdata[0:4])):
        writer.writerow([playdata[0:4][i][0],playdata[0:4][i][2],score[i][0],score[i][1],score[i][2],score[i][3],score[i][4]])
h2 = []
for i in soup.find_all('div',attrs={'class':'cb-col cb-col-100 cb-scrd-sub-hdr cb-bg-gray text-bold'}):
    h2.append(i.text)
try:
    sb2 = []
    for i in playinfo[1]:
        sb2.append(i.split(" "))
except: IndexError
s2 = []
p2 = []
for i in playdata[7:11]:
    s2.append(i[1].strip().split(" "))
    p2.append(i[0])
with open('cricbuzz.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([h2[0]])
    writer.writerow([sb2[0][0]," ",sb2[0][1],sb2[0][2],sb2[0][3],sb2[0][4],sb2[0][5],sb2[0][6],sb2[0][7]])
    for i in range(len(playdata[7:11])):
        writer.writerow([p2[i]," ",s2[i][0],s2[i][1],s2[i][2],s2[i][3],s2[i][4],s2[i][5],s2[i][6],])
with open('cricbuzz.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([innings[1]])
    writer.writerow([playinfo[0][0]," ",sb[0][0],sb[0][1],sb[0][2],sb[0][3],sb[0][4]])
    for i in range(len(playdata[11:22])):
        writer.writerow([playdata[11:22][i][0],playdata[11:22][i][2],playdata[11:22][i][3].split(" ")[0],playdata[11:22][i][3].split(" ")[1],playdata[11:22][i][3].split(" ")[2],playdata[11:22][i][3].split(" ")[3],playdata[11:22][i][3].split(" ")[4]])
with open('cricbuzz.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([h2[0]])
    writer.writerow([sb2[0][0]," ",sb2[0][1],sb2[0][2],sb2[0][3],sb2[0][4],sb2[0][5],sb2[0][6],sb2[0][7]])
    for i in range(len(playdata[24:30])):
        writer.writerow([playdata[24:30][i][0]," ",playdata[24:30][i][1].split()[0],playdata[24:30][i][1].split()[1],playdata[24:30][i][1].split()[2],playdata[24:30][i][1].split()[3],playdata[24:30][i][1].split()[4],playdata[24:30][i][1].split()[5],playdata[24:30][i][1].split()[6]])
with open('cricbuzz.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([innings[2]])
    writer.writerow([playinfo[0][0]," ",sb[0][0],sb[0][1],sb[0][2],sb[0][3],sb[0][4]])
    for i in range(len(playdata[30:41])):
        writer.writerow([playdata[30:41][i][0],playdata[30:41][i][2],playdata[30:41][i][3].split(" ")[0],playdata[30:41][i][3].split(" ")[1],playdata[30:41][i][3].split(" ")[2],playdata[30:41][i][3].split(" ")[3],playdata[30:41][i][3].split(" ")[4]])
with open('cricbuzz.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([h2[0]])
    writer.writerow([sb2[0][0]," ",sb2[0][1],sb2[0][2],sb2[0][3],sb2[0][4],sb2[0][5],sb2[0][6],sb2[0][7]])
    for i in range(len(playdata[43:48])):
        writer.writerow([playdata[43:48][i][0]," ",playdata[43:48][i][1].split()[0],playdata[43:48][i][1].split()[1],playdata[43:48][i][1].split()[2],playdata[43:48][i][1].split()[3],playdata[43:48][i][1].split()[4],playdata[43:48][i][1].split()[5],playdata[43:48][i][1].split()[6]])        