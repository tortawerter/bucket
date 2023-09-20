import itertools
import string
import numpy
import winwifi

def generate_all_passwords(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    for password in itertools.product(characters, repeat=length):
        yield ''.join(password)


print(generate_all_passwords(2))
#ssid = 'timofey'
#winwifi.WinWiFi.connect('timofey', 'aaaf')
# for password in generate_all_passwords(4):

    # print("PASSWORD: ", password)
# print(True_password)
#print(winwifi.__version__)

