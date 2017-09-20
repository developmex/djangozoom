from __future__ import absolute_import
import json

from zoomus import ZoomClient







client = ZoomClient('g7MZBr7GT3CdFn07F1F2Bw','jEJouAV2JgKAEHLHe0eQogUL7yvKHHaDXY3y')

def lista_meet():
    for user in json.loads(client.user.list().content)['users']:
        user_id = user['id']

        return user_id



import requests
import json
url = "https://api.zoom.us/v1/user/list/?api_key=g7MZBr7GT3CdFn07F1F2Bw&api_secret=jEJouAV2JgKAEHLHe0eQogUL7yvKHHaDXY3y&data_type=JSON&page_size=30&page_number=1/"
headers = {'content-type': 'application/json'}
data = {'data':[{'key1':'val1'}, {'key2':'val2'}]}
r=requests.post(url, data=json.dumps(data), headers=headers)
r


def ver_meetings(self, numero):

