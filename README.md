# Shodan_Sleuth
<img width="743" alt="Screenshot 2024-04-06 at 10 57 39 AM" src="https://github.com/Version-LAA/shodan_sleuth/assets/53385426/1fd9dec4-da7c-4b85-9652-e041dec29e95">

## Introduction
Need a way to do some quick searching on Shodan for open ports or subdomains? Shodan_Sleuth aids cybersecurity analyst, researchers, and IT personnel by helping with identifying specific servers or subdomains with a simply search utility. Leveraging the power of Shodan, the world's first search engine for Internet-connected devices, this tool facilitates targeted searches to uncover valuable information with precision and ease.

## Features
- Server Identification by Port and Country: Users can specify a port and a country, and Shodan_Sleuth will conduct a thorough search on Shodan to identify servers that have the specified port open. The output is a neatly organized CSV file containing the IP addresses and operating systems of the identified servers, provided this information is available.

- Subdomain Discovery: For those interested in mapping the digital territory of a domain, Shodan_Sleuth offers the capability to identify all associated subdomains, their DNS record types, and corresponding IP addresses. The findings are compiled into a JSON file, offering a structured overview of a domain's subdomain architecture and its distribution across the internet.

## Installation
```bash
git clone https://github.com/Version-LAA/shodan_sleuth.git
<<<<<<< HEAD
=======
cd repository
>>>>>>> 654f909e8b2901bcdd85420010f826eb476ee83f
python main.py
