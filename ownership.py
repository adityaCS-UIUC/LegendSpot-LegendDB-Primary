class OwnershipManager:
    def __init__(self):
        self.owners = {}

    def assign(self, key, node):
        self.owners[key] = node

    def owner_of(self, key):
        return self.owners.get(key, None)