import onetimepass as otp
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_file = join(dirname(__file__), ".env")
load_dotenv(dotenv_file)

secret = os.environ.get("SECRET")

my_secret = secret
my_token = otp.get_totp(my_secret)

print(my_token)