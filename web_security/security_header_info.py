import requests
import sys
import validators
from colorama import init, Fore, Back, Style

# Our next level script after this script should be comparable with results of https://securityheaders.com/?q=null.co.in&followRedirects=on

init(autoreset=True)

if len(sys.argv) == 2:
    try:
        url = sys.argv[1]
        if(validators.url(url)):
            # Chrome User-Agent is "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
            headers = {'User-Agent': user_agent}

            session = requests.Session()
            url_request = session.get(url, headers = headers)

            print("Printing Response headers of url: " + Fore.GREEN + Style.BRIGHT + url )

            print("Request Method: {}".format(url_request.request.method))

            response_security_headers = ['Server', 'Content-Type', 'Via', 'X-Frame-Options','X-Powered-By', 'Strict-Transport-Security:', 
                                'X-Content-Type-Options', 'X-XSS-Protection', 'X-Permitted-Cross-Domain-Policies', 'Set-Cookie', 'Cache-Control',
                                'Transfer-Encoding', 'Access-Control-Allow-Methods', 'Access-Control-Allow-Origin', 'Content-Security-Policy', 'Referrer-Policy']
            for header in response_security_headers:
                try:
                    result = url_request.headers[header]
                    print('%s: %s' % (header, result))
                except Exception as error:     
                    print (header + ': ' + Fore.RED + Style.BRIGHT + 'Not found')

            print(Fore.GREEN + Style.DIM + "\n\n====== We are done with header info. THANK YOU ====== \n")
        else:
            print("Not a valid url")
    except:
        print(Fore.MAGENTA + Style.BRIGHT + "Something went wrong! Figure out Bruh ;)")
else:
    print(Fore.RED + Style.BRIGHT + "Please pass the url to get header info")
    print(Fore.GREEN + Style.BRIGHT + "Ex: python3 {} <valid_url>".format(sys.argv[0]))

