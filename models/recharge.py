import datetime

from mongoengine import *


class RechargeOrder(Document):
    """充值订单表"""
    id = IntField(primary_key=True)
    order_id = StringField(max_length=64, null=False)  # 充值订单ID
    user_id = StringField(null=False)  # 用户ID
    pay_type = StringField(max_length=20, null=False)  # 支付类型（微信，京东，支付宝，银联...）
    money = IntField(null=False)  # 充值金额（单位：分）
    status = IntField(null=False)  # 订单状态（3：未处理，2：充值失败，1：成功）
    book_id = IntField(default=0)  # 如果是直接购买记录书籍ID，当充值回调时自动去购买
    ip = StringField(max_length=20, default='')  # 用户发起充值时ip
    device_type = IntField()  # 设备类型(1:android, 2:ios)
    created = DateTimeField(default=datetime.datetime.now())  # 订单创建时间

    def to_dict(self):
        return dict(
            id=self.id,
            order_id=self.order_id,
            user_id=self.user_id,
            pay_type=self.pay_type,
            money=self.money,
            status=self.status,
            book_id=self.book_id,
            ip=self.ip,
            device_type=self.device_type,
            created=self.created,
        )


class RechargeTag(Document):
    """充值订单所属活动标签"""
    id = StringField(primary_key=True)
    order_id = StringField(max_length=64, null=True)  # 订单id
    tag = StringField(max_length=32)  # 订单标签
    bind_id = IntField()  # 关联id

    def to_dict(self):
        return dict(
            id=self.id,
            order_id=self.order_id,
            tag=self.tag,
            bind_id=self.bind_id,
        )


class IapOrder(Document):
    """ios内购订单"""
    iap_id = StringField(max_length=64, primary_key=True)  # iap订单id
    order_id = StringField(max_length=64)  # 充值订单ID

    def to_dict(self):
        return dict(
            iap_id=self.iap_id,
            order_id=self.order_id,
        )
