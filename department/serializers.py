class DepartmentSerializer:
    def __init__(self, instance):
        self.instance = instance

    def to_dict(self):
        return {
            "id": self.instance.id,
            "name": self.instance.name,
            "description": self.instance.description,
            "organization_id": self.instance.organization_id,
        }