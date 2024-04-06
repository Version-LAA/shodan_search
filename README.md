# Shodan_Sleuth

<img width="784" alt="Screenshot 2024-04-06 at 11 04 57 AM" src="https://github.com/Version-LAA/shodan_sleuth/assets/53385426/de695e3d-6fbb-408d-ad4f-b69e32cec408">

## Introduction
Need a way to do some quick searching on Shodan for open ports or subdomains? Shodan_Sleuth aids cybersecurity analyst, researchers, and IT personnel by helping with identifying specific servers or subdomains with a simply search utility. Leveraging the power of Shodan, the world's first search engine for Internet-connected devices, this tool facilitates targeted searches to uncover valuable information with precision and ease.

## Features
- Server Identification by Port and Country: Users can specify a port and a country, and Shodan_Sleuth will conduct a thorough search on Shodan to identify servers that have the specified port open. The output is a neatly organized CSV file containing the IP addresses and operating systems of the identified servers, provided this information is available.

- Subdomain Discovery: For those interested in mapping the digital territory of a domain, Shodan_Sleuth offers the capability to identify all associated subdomains, their DNS record types, and corresponding IP addresses. The findings are compiled into a JSON file, offering a structured overview of a domain's subdomain architecture and its distribution across the internet.

## Installation and Setup
```bash
git clone https://github.com/Version-LAA/shodan_sleuth.git
cd repository
# Open config.py and place your api key
python main.py
