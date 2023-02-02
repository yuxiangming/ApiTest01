import api.api_init
import tool.Tool
from api.api_mp import ApiMp
from tool.Tool import Com_token


class Test_login:
    def setup(self):
        self.api_login = ApiMp()

    def test_mp_login(self, mobile="13911111111", code="246810"):
        r = self.api_login.api_mp_login(mobile, code)
        print(r.json())
        Com_token.get_token(r)
        print("headers信息为：", api.api_init.headers)
        Com_token.get_assert(r, 201)
