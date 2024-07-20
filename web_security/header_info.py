import requests
import sys
import validators
from colorama import init, Fore, Back, Style

init(autoreset=True)

if len(sys.argv) == 2:
    url = sys.argv[1]
    if(validators.url(url)):
        url_request = requests.get(url)

        print("Printing Request and Response headers of url: " + Fore.GREEN + Style.BRIGHT + url )
        print(Fore.MAGENTA + Style.BRIGHT + "\nRequest Headers")

        request_header_data = url_request.request.headers

        for req_header in request_header_data:
            print('%s: %s' % (req_header, request_header_data[req_header]))
         
        print(Fore.CYAN + Style.BRIGHT + "\nResponse Headers")

        response_header_data = url_request.headers
        for resp_header in response_header_data:
            print('%s: %s' % (resp_header, response_header_data[resp_header]))
        print(Fore.GREEN + Style.DIM + "\n\n====== We are done with header info. THANK YOU ====== \n")
    else:
        print("Not a valid url")
else:
    print("Please pass the url to get header info")
    print("Ex: python3 {} <valid_url>".format(sys.argv[0]))

