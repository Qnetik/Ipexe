import requests 
import time
import sys
import ipaddress
from rich.console import Console 
console = Console()


def error(msg):
    console.print(f"Error: {msg}", style="bold red")
    time.sleep(1)

def mainstart(ip_user):
    try: 
        ipaddress.ip_address(ip_user)
    except ValueError: 
        error("Invalid IP address format")
        return
    
    url = f"http://ipwho.is/{ip_user}"

    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            error("Code 200 !")
            return
        dataget = response.json()  
    except Exception as e:
        error(e)
        return
    
    if not dataget.get("success", False):
        error("API request unsuccessful")
        return
    
    datainfo = f"""
    Success: {dataget.get('success', 'Nope')}  
    Type: {dataget.get('type', 'Nope')} 
    Continent: {dataget.get('continent', 'Nope')} 
    Country: {dataget.get('country', 'Nope')} 
    Region: {dataget.get('region', 'Nope')} 
    City: {dataget.get('city', 'Nope')}  
    Postal: {dataget.get('postal', 'Nope')} 
    coordinates: {dataget.get('latitude', 'Nope')}/{dataget.get('longitude', 'Nope')}
    Provider: {dataget.get('connection', {}).get('org', 'Nope')}
    Timezone: {dataget.get('timezone', {}).get('abbr', 'Nope')}
    Time: {dataget.get('timezone', {}).get('current_time', 'Nope')}"""

    print(datainfo)

def main():
    if len(sys.argv) != 2:
        console.print("Usage: ipexe <IP_ADDRESS>", style="bold yellow")
        return
    ip_user = sys.argv[1]
    mainstart(ip_user)

if __name__ == "__main__":
    main()