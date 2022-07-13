from tqdm import tqdm

import zipfile

import argparse
from os import path


# Function that checks if specified file exists (for argparse)
def file_location(location: str) -> str:
    if path.exists(location):
        return location
    else:
        print(f"Error: Specified file does not exist -> {location}")
        exit(1)


# Create Argument Parser and parse specified arguments
parser = argparse.ArgumentParser(description="Brute force ZIP file passwords")
parser.add_argument('zip_file', type=file_location, help="Password protected zip file")
parser.add_argument('wordlist_file', type=file_location, help="Wordlist file")
args = vars(parser.parse_args())  # Arguments are stored in `args` dictionary

# the password list path
wordlist = args['wordlist_file']
# the zip file you want to crack its password
zip_file = args['zip_file']

zip_file = zipfile.ZipFile(zip_file)
# count the number of words in this wordlist
n_words = len(list(open(wordlist, "rb")))
# print the total number of passwords
print("Total passwords to test:", n_words)
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit=" word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)
print("[!] Password not found, try other wordlist.")
