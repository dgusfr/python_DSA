from typing import Optional, Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional["Node"] = None
