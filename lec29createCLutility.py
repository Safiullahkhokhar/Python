# create command line utility in python

import argparse # A parser for command-line arguments.
import sys # access to system functions, such as exiting the program.
import requests # simple and lightweight HTTP library for Python


def download_file(url, local_file_name): #function takes two arguments
# URL of the file to download.
#local_file_name: name of the file to save the downloaded file to.
    
    #default file name
   #  local_file_name= url.split("/")[-1]
    with requests.get(url, stream=True) as r: #stream=True parameter tells the requests library to stream the response, meaning that the downloaded file will be written to disk in chunks. 
        r.raise_for_status()
        with open(local_file_name, 'wb') as f: #open() function to open the local file for writing.
# wb mode tells the open() function to open the file in binary mode, which is necessary for writing binary files
            for chunk in r.iter_content(chunk_size = 8192):# The chunk_size parameter tells the iter_content() method to return chunks of 8192 bytes in size.
                f.write(chunk)
    return local_file_name
#ArgumentParser object to parse the command-line arguments.
parse = argparse.ArgumentParser()

#add_argument() method of the ArgumentParser object allows you to add command-line arguments to the argument parser.
# add command line arguments
parse.add_argument("url", help = "Url of the file to download")
parse.add_argument("output", help = "by which name do you want to save your file")

# parse the arg
args = parse.parse_args()

# use the arg in your code

print(args.url)
print(args.output)
download_file(args.url, args.output)

"""
Import the required libraries.

argparse: This library provides a parser for command-line arguments.
sys: This library provides access to system functions, such as exiting the program.
requests: This library provides a simple and lightweight HTTP library for Python.
Define a function to download a file from a URL.

The download_file() function takes two arguments:

url: The URL of the file to download.
local_file_name: The name of the file to save the downloaded file to.
The function works by first using the requests library to download the file from the URL. The stream=True parameter tells the requests library to stream the response, meaning that the downloaded file will be written to disk in chunks. This is more efficient than downloading the entire file in memory, especially for large files.
The download_file() function then uses the open() function to open the local file for writing. The wb mode tells the open() function to open the file in binary mode, which is necessary for writing binary files.
Next, the function iterates over the chunks of the downloaded file and writes each chunk to the local file. The iter_content() method of the requests.Response object returns an iterator over the chunks of the response. The chunk_size parameter tells the iter_content() method to return chunks of 8192 bytes in size.
Finally, the download_file() function closes the local file.
Create an ArgumentParser object to parse the command-line arguments.
The ArgumentParser object provides a way to parse command-line arguments into a Python object.
Add command-line arguments to the ArgumentParser object.
The add_argument() method of the ArgumentParser object allows you to add command-line arguments to the argument parser.

In the example code, we add two command-line arguments:

url: The URL of the file to download.
output: The name of the file to save the downloaded file to.
We also specify the help argument for each command-line argument. This is the help text that will be displayed to the user when they run the program with the -h or --help option.

Parse the command-line arguments.

The parse_args() method of the ArgumentParser object parses the command-line arguments and returns a Python object with the parsed arguments.

Print the command-line arguments.

We print the command-line arguments to the console so that the user can verify that the program is using the correct arguments.

Download the file from the URL.

We call the download_file() function with the URL and output file name that we parsed from the command-line arguments.

Example usage:

python download_file.py https://example.com/file.txt output.txt
This will download the file file.txt from the URL https://example.com/file.txt and save it to the file output.txt.

Additional notes:

The download_file() function can be easily modified to download files from other sources, such as Amazon S3 or Google Cloud Storage.
The download_file() function can also be modified to support downloading multiple files at once.
The ArgumentParser object provides a number of other options for customizing the parsing of command-line arguments. For more information, please see the ArgumentParser documentation: https://docs.python.org/3/library/argparse.html.
"""