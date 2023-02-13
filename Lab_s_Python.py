print('Enter the number of nodes: ', end = '\t')
n = int(input()) 
temp = 0

infinity = 10000
graf = [[0] *n for i in range(n)]

for  i in range(n):

    graf[i][i] = 0
    for j in range(i + 1, n, 1):
        print ('Distanse form ', i + 1, ' to ', j + 1, ' : ', end = '\t')
        graf[i][j] = int(input())
        graf[j][i] = graf[i][j]

print('\n\n')
for i in range(n):
    for j in range(n):
        print (graf[i][j], end = '\t')
    print()

print('\n\n')
dist = [infinity] * n
nodes_visited = [1] * n


dist[0] = 0

while True:

    index_min = infinity
    weight_min = infinity

    for i in range(n):
        if ((nodes_visited[i] == 1) & (dist[i] < weight_min)):
            weight_min = dist[i]
            index_min = i

    if (index_min != infinity):
        for i in range(n):
            if (graf[index_min][i] > 0):
                temp = weight_min + graf[index_min][i]
                if (temp < dist[i]):
                    dist[i] = temp
        nodes_visited[index_min] = 0

    if (weight_min == infinity): 
        break


end_node = n - 1

nodes = [0] * n

nodes[0] = end_node + 1
index_past_node = 1
weight_end_node = dist[end_node]
begin_index = 0

while (end_node != begin_index):
    for i in range(n):
        if (graf[i][end_node] != 0):
            temp = weight_end_node - graf[i][end_node]
            if (temp == dist[i]):
                weight_end_node = temp
                end_node = i
                nodes[index_past_node] = i + 1
                index_past_node += 1

print('\nMinimum way: ', end = '\t')

for i in range(index_past_node):
    print(nodes[i], end = '\t')
