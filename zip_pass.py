from tqdm import tqdm
import zipfile

wordlist = 'wordlist.txt'
# the zip file you want to crack its password
zip_file = 'example.zip'

zip_file = zipfile.ZipFile(zip_file)
num_of_wordlist = len(list(open(wordlist, 'rb')))

# print('total password to test', num_of_wordlist)

with open(wordlist, 'rb') as wordlist:
    for word in tqdm(wordlist, total=num_of_wordlist, unit='word'):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print('[+] Password found:', word.decode().strip())
            exit(0)
print('[!] Password not found, try other wordlist.')