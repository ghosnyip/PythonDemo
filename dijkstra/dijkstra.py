# 迪杰斯特拉算法
graph = dict()
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# 定义开销和父节点
infinity = float("inf")
costs = {
    "a": 6,
    "b": 2,
    "fin": infinity
}

parents = {
    "a": "start",
    "b": "start",
    "fin": None
}
# 定义已处理列表
processed = []
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)  #找到开销最低的节点
while node is not None:  #遍历所有节点
    cost = costs[node]  #获取当前节点的开销
    neighbors = graph[node]  #获取当前节点的邻居
    for n in neighbors.keys():  #遍历邻居
        new_cost = cost + neighbors[n]  #计算邻居的开销
        if costs[n] > new_cost:  #如果邻居的开销更低
            costs[n] = new_cost  #更新开销
            parents[n] = node  #更新父节点
    processed.append(node)  #将当前节点加入已处理列表
    node = find_lowest_cost_node(costs)  #找到下一个节点

print(costs)
