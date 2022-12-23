from collections import defaultdict, deque


def checkVisit(visit_info):

    return all(list(visit_info.values()))

def BFS(queue, graph, visit_info):

    node_count = 0

    min_node = 99999999999999
    max_node = 0

    while not checkVisit(visit_info):

        now_node = queue.popleft()
        visit_info[now_node] = True
        node_count += 1

        for node in graph[now_node]:
            if visit_info[node] == False and node not in queue:
                queue.append(node)
        
        if len(queue) == 0:
            if node_count < min_node:
                min_node = node_count
            
            if node_count > max_node:
                max_node = node_count
            
            node_count = 0

            for key in visit_info.keys():
                if not visit_info[key]:
                    queue.append(key)
                    break
    
    return [min_node, max_node]


def componentsInGraph(gb):
    # Write your code here

    graph = defaultdict(list)
    visit_info = {}

    for info in gb:
        if info[0] not in graph[info[1]]:
            graph[info[1]].append(info[0])

        if info[1] not in graph[info[0]]:
            graph[info[0]].append(info[1])
        
        visit_info[info[0]] = False
        visit_info[info[1]] = False
        

    queue = deque([list(graph.keys())[0]])

    answer = BFS(queue, graph, visit_info)
    
    return answer

print(componentsInGraph([[1, 6],[2, 7], [3, 8], [4,9], [2, 6]]))