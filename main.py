import shodan
import pandas as pd
from secret import API_KEY

"""
1) Search forweb servers within the USA that have port 3389 open. Limit your results to
the first IW responses.
b. Output a CSV with the IP addresses listed, and the Operating system detected on each
of the IP addresses.

2) a. use an appropriate endpoint to look up the DNS information for "paychex.com".
b. Iterate through the results and print the "subdomain", "type" and "value" where the
type is not "MY.
c. Provide your output in 'SON to the user.

"""
Custom_Key = '' # place key here


 # place api here

# print(len(api.search(query='port:3389 country:US')['matches']))



def server_search(country,port):
    api = shodan.Shodan(API_KEY)
    # obtain results from shodan
    results = api.search(query=f"port:{port} country:{country}")['matches']

    output = [['ip_address','os']]

    for r in results:
        output.append(r['ip_str'],r['os'])
    return results

def intel_lookup(domain):
    pass


def main():
    if API_KEY:
        API = API_KEY
    else:
        API = Custom_Key

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
            pass
        elif int(user_resp) == 1:
            country = input("Enter Country Code")
            port = input("Enter a port")
            ss = server_search(country,port)
            print(ss)

        else:
            print("\nNot a valid option - try again\n")



main()
