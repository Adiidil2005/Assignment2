# member_register.py (Student B - Issue #2)

class MemberRegistry:
    def __init__(self):
        self.members = {}

    def register(self, member_id, name, email):
        if not name or not name.strip():
            raise ValueError("Name is required")

        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("Invalid email")

        if member_id in self.members:
            raise ValueError("Member ID already exists")

        self.members[member_id] = {
            "name": name,
            "email": email
        }

        return True

    def count(self):
        return len(self.members)