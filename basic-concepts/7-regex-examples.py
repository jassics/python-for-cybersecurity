import re

urls = ["https://www.facebook.com","https://www.google.com","https://www.amazon.in"]

def checkValidURL(url):
    url_reg_ex = "^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?"
    data = re.search(url_reg_ex,url)
    if data is not None:
        return True
    return False

def parseDomain(url):
    domain = url.split("//")[1].split("www")[1].split(".")[1]
    print(domain)


if __name__ == "__main__":
    for url in urls:
        url_status = checkValidURL(url)
        if url_status:
            parseDomain(url)


    