


class Node:
    def __init__(self, value, index = None, child_nodes = []):
        self.value = value
        self.index = index
        self.child_nodes = child_nodes
        self.is_updated = False

    def move_to_child(self):
        if len(child_nodes) == 0:
            return self.value
        
        for node in child_nodes:
            if node.is_updated == True:
                node.value += self.value/len(child_nodes)
            else:
                node.value = self.value/len(child_nodes)
                node.is_updated = True
        return True

    def reset_update(self):
        self.is_updated = False


def has_shared_element(list_1, list_2):
    for x in list_1:
        for y in list_2:
            if x == y:
                return True
    return False


nodes = [Node(12), Node(13), Node(14), Node(15)]
nodes[0].child_nodes.append(nodes[1])
nodes[0].child_nodes.append(nodes[2])
nodes[1].child_nodes.append(nodes[3])
nodes[2].child_nodes.append(nodes[3])

nodes[-1].index = len(nodes)

children = list(map(lambda x: x.child_nodes, nodes))


current_newly_indexed = [nodes[-1]]
while None in map(lambda x: x.index, nodes):
    newly_indexed = current_newly_indexed
    current_newly_indexed = []
    for node in newly_indexed:
        for childe in children:
            if node in childe:
                nodes[children.index(childe)].index = node.index - 1
                print(children)
                current_newly_indexed.append(nodes[children.index(childe)])
        
for x in children:
    for y in children:
        if (not x == y) and has_shared_element(x, y):
            x.index, y.index = max(x.index, y.index)

print(nodes)
print(map(lambda x: x.index, nodes))







