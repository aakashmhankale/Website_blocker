import time
from datetime import datetime as dt
host_temp="hosts"
host_path="C:\\Windows\\System32\\drivers\\etc"
redirect="127.0.0.1"
website_list=["www.att.com","www.wellsfargo.com"] #websites which we want to block

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,20):
        print("Working Hours.....")
        with open(host_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours.........")
    time.sleep(5)
