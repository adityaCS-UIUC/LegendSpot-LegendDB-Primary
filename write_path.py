class WritePath:
    def __init__(self, lsm, rdma, owner_mgr, node_id):
        self.lsm = lsm
        self.rdma = rdma
        self.owner_mgr = owner_mgr
        self.node_id = node_id

    def write(self, key, value):
        owner = self.owner_mgr.owner_of(key)
        if owner is None or owner == self.node_id:
            self.lsm.write(key, value)
        else:
            self.rdma.forward(key, value)