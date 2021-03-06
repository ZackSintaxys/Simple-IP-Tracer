from colorama import *
import requests, json

init()

#Consts
mas = f'          [{Fore.GREEN}+{Fore.WHITE}]'
menos = f'          [{Fore.LIGHTRED_EX}-{Fore.WHITE}]'
wait = f'          [{Fore.LIGHTGREEN_EX}>>{Fore.WHITE}]'
error = f'          [{Fore.RED}!{Fore.WHITE}]'

def banner():
	print(f"          [{Fore.GREEN}+{Fore.WHITE}] IP Scanner by ZackSintaxys")
	print("")
api_url = "http://ip-api.com/json/"

parametros = 'status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query'
data = {"fields":parametros}

def ip_scraping(ip=""):

 res = requests.get(api_url+ip, data=data)

 api_json_res = json.loads(res.content)
 return api_json_res

if __name__ == '__main__':
 banner()
 print(f'{wait} IP: ', end="")
 ip = input()
 
 par = parametros.split(",")
 for x in par:
  print(f'{mas} {x.upper()}', ":", end=" ")
  print(ip_scraping(ip)[x])
print(f'{wait} Scan completado, presione enter para salir.')
x = input()
if(x == ""):
	exit()
else:
	exit()
