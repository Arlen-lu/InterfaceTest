import requests
import json
from common.get_cookie import GetCookies
from common.info import InfoPart


class HttpRequest(object):
    '''
        http_request: no cookie
        session_request:with cookie
        '''

    def __init__(self, cookie_status, http_method, url, params):
        self.cookie_status = cookie_status
        self.header = ""
        self.http_method = http_method
        self.url = url
        self.params = params

    def chosen_request(self):
        if self.cookie_status:
            s = requests.Session()
            s.cookies['Cookie'] = InfoPart.cookie
        else:
            s = requests
        return s
        # return requests.Session() if self.cookie_status else requests

    def http_request(self):
        if self.http_method.upper() == 'GET':
            res = self.chosen_request().get(
                self.url, headers=self.header, params=self.params)
        elif self.http_method.upper() == 'POST':
            res = self.chosen_request().post(
                self.url, headers=self.header, data=self.params)
        return res


if __name__ == "__main__":
    cookie_status = 1
    http_method = 'post'
    url = 'http://v.juhe.cn/laohuangli/d'
    params = {'key': '43fe516b14cd2eee8e7db8dcda379909', 'date': '2020-02-02'}
    res = HttpRequest(cookie_status, http_method, url, params).http_request()
    # res = http_requests.http_request()
    print(res.cookies)
    # print(res.text)
    # print(res.headers)
    # print(res.status_code)
    # print(res.json())
