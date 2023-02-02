
import requests

from api import api_init


class ApiMp:
    def __init__(self):
        self.url_login = api_init.host + "/mp/v1_0/authorizations"
        self.url_article = api_init.host + "/mp/v1_0/channels"

    def api_mp_login(self, mobile, code):
        data = {"mobile": mobile, "code": code}
        return requests.post(url=self.url_login, json=data, headers=api_init.headers)

    def api_mp_article(self, title, content, channel_id):
        data = {"title": title, "content": content, "channel_id": channel_id, "cover": {"type": 0, "images": []}}
        return requests.post(url=self.url_article, json=data, headers=api_init.headers)