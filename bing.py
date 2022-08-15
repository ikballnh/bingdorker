from ast import Break
from struct import pack
from tkinter import E
import requests
from requests.structures import CaseInsensitiveDict
import re
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

def save(filename, text):
  more_lines = [text, '']
  with open(filename, 'a', encoding="utf8") as f:
    f.writelines('\n'.join(more_lines))

def search(dork, pages):
  headers = CaseInsensitiveDict()
  headers["Host"] = "www.bing.com"
  headers["Cookie"] = 'MUID=34C5258064FF6DE81DA2345F65A96CC6; MUIDB=34C5258064FF6DE81DA2345F65A96CC6; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=1D5A59434F504296912B6428A75BE922&dmnchg=1; _UR=QS=0&TQS=0; MicrosoftApplicationsTelemetryDeviceId=bca04d53-9c29-415c-88df-7cdb2a4ffdb5; _EDGE_CD=m=id-id; imgv=flts=20220808; SUID=M; _SS=SID=07B57D04C2CB61C827326CFFC39D6036; _EDGE_S=SID=07B57D04C2CB61C827326CFFC39D6036&mkt=id-id; _HPVN=CS=eyJQbiI6eyJDbiI6NiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6NiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6NiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMi0wOC0wOVQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6NDB9; SRCHUSR=DOB=20220724&T=1660065927000&TPC=1660054832000; ipv6=hit=1660069529804&t=4; ai_session=AGZNodRVFCrohPs2YJluGm|1660065932853|1660065932853; SRCHHPGUSR=SRCHLANG=id&BRW=XW&BRH=M&CW=1519&CH=754&SW=1536&SH=864&DPR=1.3&UTC=420&DM=0&PV=7.0.0&HV=1660065991&WTS=63795662731&NEWWND=0&NRSLT=-1&LSL=0&ADLT=OFF&NNT=1&HAP=0&VSRO=1&SCW=1519&SCH=1864'
  headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36" 
  headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" 
  headers["Accept-Encoding"] = "gzip, deflate" 
  headers["Accept-Language"] = "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7" 
  
  r = requests.get("https://www.bing.com/search?q="+dork+"&go=Cari&qs=ds&first="+pages+"&FORM=PERE", headers=headers, timeout=30)
  a = r.text
  result = re.findall('<h2><a href="(.*?)"', a)
  page   = re.findall('Page \d+', a)
  mylist = list(dict.fromkeys(result))
  return [page, mylist]

def dorking(dork):
    pages = 1
    jmlpage = 2
    awal = 0

    while (awal < 999999999):
        cari = search(dork, str(pages))
        jumlah = len(cari[1])
        for xx in range(0,jumlah):
            x = cari[1][xx]
            print(x)
            save("result.txt", x)
        
        arreypage = cari[0]
        strjml = "Page "+str(jmlpage)+""
        posisi = jmlpage - 1
        c = strjml in arreypage
        if (c == True):
            print(posisi)
        else:
            print(posisi)
            break

        pages += 10
        jmlpage += 1

intro = """
  /$$$$$$$  /$$$$$$ /$$   /$$  /$$$$$$        /$$$$$$$   /$$$$$$  /$$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$ 
| $$__  $$|_  $$_/| $$$ | $$ /$$__  $$      | $$__  $$ /$$__  $$| $$__  $$| $$  /$$/| $$_____/| $$__  $$
| $$  \ $$  | $$  | $$$$| $$| $$  \__/      | $$  \ $$| $$  \ $$| $$  \ $$| $$ /$$/ | $$      | $$  \ $$
| $$$$$$$   | $$  | $$ $$ $$| $$ /$$$$      | $$  | $$| $$  | $$| $$$$$$$/| $$$$$/  | $$$$$   | $$$$$$$/
| $$__  $$  | $$  | $$  $$$$| $$|_  $$      | $$  | $$| $$  | $$| $$__  $$| $$  $$  | $$__/   | $$__  $$
| $$  \ $$  | $$  | $$\  $$$| $$  \ $$      | $$  | $$| $$  | $$| $$  \ $$| $$\  $$ | $$      | $$  \ $$
| $$$$$$$/ /$$$$$$| $$ \  $$|  $$$$$$/      | $$$$$$$/|  $$$$$$/| $$  | $$| $$ \  $$| $$$$$$$$| $$  | $$
|_______/ |______/|__/  \__/ \______/       |_______/  \______/ |__/  |__/|__/  \__/|________/|__/  |__/
                                                                                                                                                                                                                                                            
"""
print(intro)
print("BING DORKER WITH MULTI THREADING")
print("Author: Ikbal Nur Hakim")
print("Error ? Contact me https://web.facebook.com/ikbal.nurhakim.798/")

file = input("\nEnter list dork [ex: dork.txt]: ")
threads = input("How many threads [recommendation: 50]: ")
print("Saved in result.txt")
text_file= open(file,'r', encoding="utf8")
data=text_file.read()
dsplit = data.split("\n")

pool = ThreadPoolExecutor(max_workers=int(threads))
for isi in dsplit:
    a = urllib.parse.quote_plus(isi)
    lower = a.lower()
    pool.submit(dorking,isi)
pool.shutdown(wait=True)
