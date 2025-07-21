import requests
import os
from  dotenv import load_dotenv
load_dotenv()
THECAT_APIKEY = os.getenv('THECAT_APIKEY')

def get_cat_random_image_url():
   url = f"https://api.thecatapi.com/v1/images/search"
   headers = {"x-api-key": THECAT_APIKEY}
   response = requests.get(url, headers=headers)
   if response.status_code == 200:
      data = response.json()
      return data['url']
   else:
      return None


async def main():
   pass
