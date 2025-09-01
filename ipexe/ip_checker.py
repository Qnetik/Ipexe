import requests 
import time
import sys
import socket
import ipaddress
from rich.console import Console 
from urllib.parse import urlparse
console = Console()

def error(msg):
    console.print(f"Error: {msg}", style="bold red")
    time.sleep(1)

def mark(value):
    return f"[bold green][+][/]" if value not in (None, "Nope") else f"[bold red][-][/]"

def mainstart(target: str):
    try:
       ipaddress.ip_address(target)
       final_ip = target
    except ValueError: 
        try:
           url = target.strip().lower()
           parsed = urlparse(url)
           domain = parsed.netloc if parsed.netloc else parsed.path
           domain = domain.rstrip("/")
           final_ip = socket.gethostbyname(domain)
        except socket.gaierror:
           error("Invalid IP or domain")
           return None
 
    url = f"https://ipwho.is/{final_ip}"

    try:
       response = requests.get(url, timeout=5)
       if response.status_code != 200:
           error("Code 200 !")
           return
       dataget = response.json()  
    except Exception as e:
       error(str(e))
       return
    

    if not dataget.get("success", False):
       error("API request unsuccessful")
       return
    
    


    datainfo = f"""{mark(dataget.get('success', 'Nope'))} Success: {dataget.get('success', 'Nope')}
{mark(dataget.get('type', 'Nope'))} Type: {dataget.get('type', 'Nope')}
{mark(dataget.get('ip', 'Nope'))} Ip: {dataget.get('ip', 'Nope')}
{mark(dataget.get('continent', 'Nope'))} Continent: {dataget.get('continent', 'Nope')}
{mark(dataget.get('country', 'Nope'))} Country: {dataget.get('country', 'Nope')}
{mark(dataget.get('region', 'Nope'))} Region: {dataget.get('region', 'Nope')}
{mark(dataget.get('city', 'Nope'))} City: {dataget.get('city', 'Nope')}
{mark(dataget.get('postal', 'Nope'))} Postal: {dataget.get('postal', 'Nope')}
{mark(dataget.get('latitude', 'Nope'))} Coordinates: {dataget.get('latitude', 'Nope')}/{dataget.get('longitude', 'Nope')}
{mark(dataget.get('connection', {}).get('org', 'Nope'))} Provider: {dataget.get('connection', {}).get('org', 'Nope')}
{mark(dataget.get('timezone', {}).get('abbr', 'Nope'))} Timezone: {dataget.get('timezone', {}).get('abbr', 'Nope')}
{mark(dataget.get('timezone', {}).get('current_time', 'Nope'))} Time: {dataget.get('timezone', {}).get('current_time', 'Nope')}"""

    console.print(datainfo, highlight=False)

def main():
    if len(sys.argv) != 2:
        console.print("Usage: ipexe <IP_ADDRESS>", style="bold yellow")
        return
    ip_user = sys.argv[1]
    mainstart(ip_user)

if __name__ == "__main__":
    main()