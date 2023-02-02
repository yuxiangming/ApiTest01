import api


class Com_token:
    @classmethod
    def get_token(cls, resp):
        token = resp.json().get("data").get("token")
        api.api_init.headers['authorizations'] = "Bearer " + token

    @classmethod
    def get_assert(cls, resp, status_code):
        assert status_code == resp.status_code
