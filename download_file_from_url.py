import sys
import requests
import re
from colorama import init, Fore, Back, Style
import validators

# PURPOSE of this script
# Get a url with various files formats to download
# For example to get a ip ranges of AWS in json format, use below url
# AWS IP range url is: https://ip-ranges.amazonaws.com/ip-ranges.json

init(autoreset=True)

# Check if user has passed the file url to download or not
if len(sys.argv) == 2:
  file_url = sys.argv[1] # Getting the url from command line# extract file name form the url using re module

  # Proceed if url is valid
  if not validators.url(file_url):
    exit(Fore.RED + Style.BRIGHT + "Not a valid url")

  # this regex would also work as it with positive lookbehind (?:[^/][\d\w\.-]+)$(?<=\.\w{3,4})
  # file name with extension
  matched_file = re.search("(?=[\w\d-]+\.\w{3,4}$).+", file_url) # regex with positive lookahead
  if matched_file is not None:
    file_name_with_extension = matched_file.group(0)
  else:
      exit(Fore.CYAN + Style.BRIGHT + "Nothing to download")
  print("Downloading %s" % file_name_with_extension)

  response = requests.get(file_url, stream = True)

  with open(file_name_with_extension, "wb") as file_download:
    total_length = response.headers.get('content-length')
    total_length = int(total_length)
    print("Total length of the file is: {0:.3f} KB".format(total_length/1024))

    dl_bar = 0 # download bar

    for chunk in response.iter_content(chunk_size = 1024): #writing one chunk at a time to file_download
      if chunk:
        dl_bar += len(chunk)
        file_download.write(chunk)
        done = int(50 * dl_bar / total_length)
        sys.stdout.write(Fore.GREEN + Style.BRIGHT + "\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
        sys.stdout.flush()
  print("\nDownload Complete! \n")
else :
  print(Fore.RED + Style.BRIGHT + 'Please pass the url to download. Make sure it is downloadable url')
  print(Fore.GREEN + Style.BRIGHT + 'Ex: python {} <downloadable_url>'.format(sys.argv[0]))
