from mongoengine import (Document, StringField, ReferenceField, LongField,
                         DateTimeField)


class WalletAddressField(StringField):

    def __init__(self, **kwargs):
        max_length = 100
        regex = r'TA[a-zA-Z0-9]{95,}'
        super(WalletAddressField, self).__init__(max_length=max_length,
                                                 regex=regex, **kwargs)


class User(Document):
    user_id = StringField(max_length=20, required=True, unique=True)
    user_wallet_address = WalletAddressField(default=None)
    balance_wallet_address = WalletAddressField()


class Wallet(Document):
    wallet_address = WalletAddressField(required=True, unique=True)
    actual_balance = LongField(default=0)
    locked_balance = LongField(default=0)


class Transfer(Document):
    from_user = ReferenceField(User, required=True)
    to_user = ReferenceField(Wallet, required=True)
    amount = LongField(required=True)
    date = DateTimeField(required=True)
    tx_hash = StringField()


class Tip(Document):
    from_user = ReferenceField(User, required=True)
    to_user = ReferenceField(User, required=True)
    amount = LongField(required=True)
    date = DateTimeField(required=True)
    tx_hash = StringField()


class Withdrawal(Document):
    user = ReferenceField(User, required=True)
    amount = LongField(required=True)
    date = DateTimeField(required=True)
    tx_hash = StringField()


class EstimateFusion(Document):
    user = ReferenceField(User, required=True)
    threshold = LongField(required=True)
    fusion_ready_count = LongField()
    total_count = LongField()


class SendFusion(Document):
    user = ReferenceField(User, required=True)
    threshold = LongField(required=True)
    tx_hash = StringField()
