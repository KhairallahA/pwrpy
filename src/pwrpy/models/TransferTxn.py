from pwrpy.models.Transaction import Transaction


class TransferTxn(Transaction):

    @classmethod
    def from_json(cls, json_data):
        instance = super().from_json(json_data)
        return instance

    def to_json(self):
        return super().to_json()
