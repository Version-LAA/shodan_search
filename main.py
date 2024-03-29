import shodan
import csv
from secret import API_KEY
from datetime import datetime
import json

Custom_Key = '' # place key here
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
    SET_API = API_KEY if API_KEY else Custom_Key
    api = shodan.Shodan(SET_API)
    print("\nWelcome to the Shodan API Search Tool\n")

    active = True

    while active:
        print("Select From Menu Below:\n")
        print("1 - Server Port / Country Search")
        print("2 - Domain Intel Search")
        print("3 - Exit")
        user_resp = input("\nEnter option: ")

        if int(user_resp) == 3:
            print("\ngoodbye!\n")
            active = False
        elif int(user_resp) == 2:
            domain = input("Enter domain?")
            intel_lookup(domain,api)
        elif int(user_resp) == 1:
            country = input("Enter Country Code: ")
            port = input("Enter a port: ")
            ss = server_search(country,port,api)


        else:
            print("\nNot a valid option - try again\n")



main()
