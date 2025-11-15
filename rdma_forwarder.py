class RDMAForwarder:
    def __init__(self, home_node):
        self.home_node = home_node

    def forward(self, key, value):
        print(f"[RDMA] Forwarding write for key={key} to node={self.home_node}")