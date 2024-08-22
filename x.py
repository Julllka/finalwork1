
import time
import requests
import pprint
from tqdm import tqdm
import configparser


class VK:
    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}


    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id, 'screen_name': self.name}
        response = requests.get(url,params={**self.params, **params})
        return response.json()

    def photos_info(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.id, 'album_id': 'profile', 'count': 5, 'extended': 1}
        response = requests.get(url, params={**self.params, **params})
        return response.json()

    def long_function(self):
        for i in tqdm(range(100)):
            time.sleep(0.1)
        return True

    #def save_fotos(self):
        #response = requests.get(imageUrl)
        #with open ('image.jpg', 'wb') as f:
            #f.write(response.content)
            #filename = 'imageUrl'.split('/')[-1]

    class TwitterConfig(Config):
        config = configparser.ConfigParser()
        config.read("settings.ini")
        return(config["access_token"]["user_id"]['token'])

#access_token = 'e83d6ed1e83d6ed1e83d6ed1e3eb277292ee83de83d6ed18e82289be8632788ba3298ee'
#user_id = '23193179'
#vk = VK(access_token, user_id)

pprint.pprint(vk.photos_info())

if __name__ == '__main__':

