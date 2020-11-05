class Node:
    ###########################---Attributes---############################
    id = int()
    cost = float()
    id_state = tuple()
    id_parent = tuple()
    action = str()
    depth = int()
    heuristic = int()
    value = float()

    ###########################---Constructor---###########################
    def __init__(self, identifier, cost, id_state, id_parent, action, depth, heuristic, value):
        self.id = identifier
        self.cost = cost
        self.id_state = id_state
        self.id_parent = id_parent
        self.action = action
        self.depth = depth
        self.heuristic = heuristic
        self.value = value
