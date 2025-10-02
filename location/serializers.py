class LocationSerializer:
    def __init__(self, instance):
        self.instance = instance

    def to_dict(self):
        return {
            "id": self.instance.id,
            "name": self.instance.name,
            "address": self.instance.address,
            "city": self.instance.city,
        }