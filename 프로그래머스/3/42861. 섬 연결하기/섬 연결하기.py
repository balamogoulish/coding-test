#1. costs를 비용 순으로 정렬한다.
#2. 가장 작은 비용을 갖는 노드를 선택한다.
#3. 해당 섬을 노드에 추가한다.
#4. 노드에 포함된 섬을 갖는 costs 중 가장 낮은 cost를 선택해서 노드에 추가하고, answer에 cost를 더한다.
#5. 노드에 모든 섬이 포함되었을 때 answer을 출력한다.
def solution(n, costs):
    answer = 0
    nodes = set([])
    costs_sorted =list()
    for i in costs:
        costs_sorted.append([i[2],i[0],i[1]])
    costs_sorted.sort()
    
    answer += costs_sorted[0][0]
    nodes.update([costs_sorted[0][1], costs_sorted[0][2]])
    while len(nodes)!=n:
        for c in costs_sorted:
            if (c[1] in nodes and c[2] not in nodes) or (c[1] not in nodes and c[2] in nodes):
                nodes.update([c[1], c[2]])
                answer += c[0]
                break
                
    return answer