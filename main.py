import shodan
import csv
try:
    from secret import API_KEY
except:
    print("checking for custom key")
from config import KEY
from datetime import datetime
import json
import pyfiglet


DT = datetime.now()
TRAILER = DT.strftime("%m%d%Y_%H:%M:%S")

def server_search(country,port,key):

    # obtain results from shodan
    results = key.search(query=f"port:{port} country:{country}")['matches']


    # loop through results adding fields and results data to output
    output = [['ip_address','os']]
    for r in results:
        os = r['os'] if r['os'] is not None else "unknown" # checks if OS is known
        output.append([r['ip_str'],os])

    # creates csv of results
    with open(f"server_search-{TRAILER}.csv",'w') as f:
        csv_write = csv.writer(f)
        csv_write.writerows(output)


def intel_lookup(domain,key):

    output = {"subdomains":[]}
    results = key.dns.domain_info(f"{domain}", history=False, type=None)['data']

    # This loop would be used to build the JSON output
    for r in results:
        sub = 'none' if r['subdomain'] == '' else r['subdomain']
        type = r['type']
        if type != 'MX': # checks it's not an MX record
            output['subdomains'].append({
                'subdomain':sub,
                'type':r['type'],
                'value':r['value']
            })
    # will write to a json file
    with open(f"{domain}-domains-{TRAILER}.json", 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=4)


def main():
    # getters and seters for key
    try:
        SET_API = API_KEY
    except:
        SET_API = KEY
        print("Added Custom key")
        if len(SET_API) < 30:
            print("\n\nKey is invalid  - Please check config.py file")
            return

    api = shodan.Shodan(SET_API)
    ascii_banner = pyfiglet.figlet_format("ShodanSearch")
    print(ascii_banner)
    print("\n\n\nWelcome to the Shodan API Search Tool\n")
    print("Created by:Version-Laa")
    print("Github: shodan_search\n\n\n")

    active = True

    while active:
        print("Select From Menu Below:\n")
        print("1 - Open Server Ports By Country Search")
        print("2 - Find Subdomains by Domain Search")
        print("3 - Exit")
        user_resp = input("\nEnter option: ")

        try:
            if int(user_resp) == 3:
                print("\ngoodbye!\n")
                active = False
            elif int(user_resp) == 2:
                domain = input("Enter domain?")
                intel_lookup(domain,api)
                print("\n\n Results exported successfully\n\n")
            elif int(user_resp) == 1:
                country = input("Enter Country Code: ")
                port = input("Enter a port: ")
                ss = server_search(country,port,api)
                print("\n\n Results exported successfully\n\n")


            else:
                print("\nNot a valid option - try again\n")
        except:
            print("\n\nExiting Program - key error\n\n")
            return


main()
