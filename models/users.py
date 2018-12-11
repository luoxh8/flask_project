import datetime

from flask_login import UserMixin
from mongoengine import *


class User(Document, UserMixin):
    id = StringField(required=True, primary_key=True)
    nickname = StringField(required=True, max_length=50)
    phone = StringField(required=True, min_length=11, max_length=20)
    password = StringField(max_length=128)
    email = StringField(max_length=20)
    notify_phone = StringField(max_length=20)  # 接收通知的手机号码, 可以和phone 不一致
    level = IntField(default=0)
    avatar = StringField(max_length=200)
    sex = IntField(default=1)  # 1男2女

    platform = StringField(max_length=20)
    device_id = StringField(max_length=40, unique=True)  # 设备id 安卓:mac ios:idfa
    register_ip = StringField(max_length=20)
    intro = StringField(max_length=300)  # 个人简介
    aphorism = StringField(max_length=200)  # 个人签名

    oauth_from = StringField(max_length=20, default='')  # 认证来源 tel_pwd, weibo, wechat, qq
    oauth_openid = StringField(max_length=128)  # openid， 对于微信， 是unionid（用openid 会导致公众号和手机客户端不一致）
    oauth_userinfo = StringField()  # 来自第三方平台的用户额外信息
    oauth_time = DateTimeField()  # 绑定第三方帐号时间
    oauth_nickname = StringField(max_length=50)
    oauth_avatar = StringField(max_length=200)

    modified = DateTimeField(default=datetime.datetime.now())
    created = DateTimeField(default=datetime.datetime.now())

    def to_dict(self):
        return dict(
            id=self.id,
            nickname=self.nickname,
            phone=self.phone,
            email=self.email,
            level=self.level,
            avatar=self.avatar,
            sex=self.sex,
            platform=self.platform,
            device_id=self.device_id,
            register_ip=self.register_ip,
            intro=self.intro,
            aphorism=self.aphorism,
            oauth_from=self.oauth_from,
            oauth_openid=self.oauth_openid,
            oauth_userinfo=self.oauth_userinfo,
            oauth_time=self.oauth_time,
            oauth_nickname=self.oauth_nickname,
            oauth_avatar=self.oauth_avatar,
            modified=self.modified,
            created=self.created,
        )


class UserBalance(Document):
    id = ReferenceField(User, True, CASCADE, primary_key=True)
    balance = IntField(null=False)  # 余额
    total = IntField(null=False, default=0)  # 累计充值

    def to_dict(self):
        return dict(
            id=self.id,
            balance=self.balance,
            total=self.total,
        )


class UserBalanceLog(Document):
    id = StringField(primary_key=True)
    user_id = IntField(null=False)  # 用户ID
    exec_type = IntField(null=False)  # 操作类型（1增加，2减少）
    money = IntField(null=False)  # 金额（单位：分）
    corresponding = StringField(max_length=20, null=False)
    corresponding_id = StringField(max_length=500, null=False)  # 对应ID
    book_id = StringField(max_length=45, null=False, default='0')  # 购买书籍ID
    remark = StringField(max_length=45)  # 备注
    created_time = DateTimeField(null=False, default=datetime.datetime.now())  # 记录时间
    platform = StringField(max_length=20)

    def to_dict(self):
        return dict(
            id=self.id,
            user_id=self.user_id,
            exec_type=self.exec_type,
            money=self.money,
            corresponding=self.corresponding,
            corresponding_id=self.corresponding_id,
            book_id=self.book_id,
            remark=self.remark,
            created_time=self.created_time,
            platform=self.platform,
        )
