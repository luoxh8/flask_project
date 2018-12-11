import datetime
from json import dumps, loads

from mongoengine import *


class Banner(Document):
    id = StringField(primary_key=True)
    title = StringField(max_length=100)
    platform = StringField(max_length=50)
    activity = StringField(max_length=50)
    ios_activity = StringField(max_length=50)
    params = StringField(max_length=150)  # 客户端需要参数,保存字典,暂时需要{'book_id':111, 'book_name': u''}
    sex = IntField(default=1)  # 0: 所有 1：男；2: 女
    url = StringField(max_length=150)
    banner_url = StringField(max_length=150)
    level = IntField(default=0)
    showed = BooleanField(default=False)
    modified = DateTimeField(default=datetime.datetime.now())
    created = DateTimeField(default=datetime.datetime.now())
    m_id = IntField(default=-1)

    # def __init__(self, data):
    #     self.title = data.get('title', '')
    #     self.platform = data.get('platform', '')
    #     self.activity = data.get('activity', '')
    #     self.ios_activity = data.get('ios_activity', '')
    #     self.params = dumps(loads(data.get('params', dumps({}))))
    #     self.sex = int(data.get('sex', 0))
    #     self.url = data.get('url', '')
    #     self.banner_url = data['banner_url']
    #     self.level = int(data.get('level', 0))
    #     self.showed = 1 if int(data.get('showed', 0)) else 0
    #     self.m_id = int(data.get('m_id', -1))

    def update(self, data):
        print(data)
        self.title = data.get('title', '')
        self.platform = data.get('platform', '')
        self.activity = data.get('activity', '')
        self.ios_activity = data.get('ios_activity', '')
        self.params = dumps(loads(data.get('params', dumps({})))) or ''
        self.sex = int(data.get('sex', 0))
        self.url = data.get('url', '')
        self.banner_url = data['banner_url']
        self.level = int(data.get('level', 0))
        self.showed = 1 if int(data.get('showed', 0)) else 0
        self.m_id = int(data.get('m_id', -1))
        self.modified = datetime.datetime.now()

    def to_admin_dict(self):
        return dict(id=self.id,
                    title=self.title,
                    platform=self.platform,
                    activity=self.activity,
                    ios_activity=self.ios_activity,
                    params=loads(self.params) or '',
                    sex=self.sex,
                    url=self.url,
                    banner_url=self.banner_url,
                    level=self.level,
                    showed=int(self.showed),
                    created=self.created.strftime('%Y-%m-%d %H:%M:%S'),
                    modified=self.modified.strftime('%Y-%m-%d %H:%M:%S'))

    def to_dict(self):
        return dict(id=self.id,
                    title=self.title,
                    platform=self.platform,
                    activity=self.activity,
                    ios_activity=self.ios_activity,
                    params=self.params or '',
                    sex=self.sex,
                    url=self.url,
                    banner_url=self.banner_url,
                    level=self.level
                    )
