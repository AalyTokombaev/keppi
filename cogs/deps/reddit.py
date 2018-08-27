import requests
from random import choice

class ImageRetriever:
    def __init__(self, link, client_id, client_secret, reddit_username, reddit_password):
        self.link = link
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = reddit_username
        self.password = reddit_password
        self.responce = self.request_token()
        self.token = self.responce["access_token"]
        # print(self.token)
        self.headers = {"Authorization": f"bearer {self.token}", "User-Agent": "Ned's disord bot by aiversen"}
        # print(self.headers)
        self.json = requests.get(link, headers=self.headers).json()
        # print(self.json)
        self.images = self.get_images()


    def request_token(self):
        print('getting token')
        client_auth = requests.auth.HTTPBasicAuth(self.client_id, self.client_secret)
        post_data = {"grant_type": "password", "username": self.username, "password": self.password}
        headers = {"User-Agent": "Ned's discord bot by aiversen"}
        response = requests.post('https://www.reddit.com/api/v1/access_token', auth=client_auth, data=post_data, headers=headers)

        token = response.json()
        return token 


    def get_images(self):
        return [image['data']['url'] for image in self.json['data']['children']]

    def get_image(self):
        if not self.images:
            if self.token["expires_in"] <= 10:
                self.token = self.request_token()
            self.images = self.get_images()
        image = self.images.pop(self.images.index(choice(self.images)))
        return image


class ImageRetieverV2:
    pass
    # TODO: Make a more secure version of ImageRetriever