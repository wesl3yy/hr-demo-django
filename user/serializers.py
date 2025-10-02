class UserSerializer:
    def __init__(self, instance):
        self.instance = instance

    def to_dict(self):
        return {
            "id": self.instance.id,
            "first_name": self.instance.first_name,
            "last_name": self.instance.last_name,
            "email": self.instance.email,
            "phone": self.instance.phone,
            "status": self.instance.status,
            "organization_id": self.instance.organization_id,
            "department": self.instance.department_id,
            "location": self.instance.location_id,
            "position": self.instance.position_id,
            "manager": self.instance.manager_id,
        }