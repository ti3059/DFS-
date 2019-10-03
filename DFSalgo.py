graph1 = {
    'A' : ['B','C'],
    'B' : ['A'],
    'C' : ['D', 'D', 'F', 'S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']

}


def dfs_iteratif(graph, node):
    visited = [node]                            #création tableau de noeuds visités
    stack = [node]                              #création tableau de noeuds empilés
    while stack:
        node = stack[-1]
        if node not in visited:                 #si le noeud n'est pas encore visité on ajoute aux visités le noeud en question
            visited.append(node)
        remove_from_stack = True                #retire de la pile le noeud est Vrai

        for next in graph[node]:                #pour le noeud suivant dans le graph si il n'est pas visité on colle le next dans le stack et on passe’
            if next  not in visited:
                stack.extend(next)
                remove_from_stack = False
                break
        if remove_from_stack:                   #si on rentre dans remove, on supprime la pille
            stack.pop()
    return visited


print(dfs_iteratif(graph1, 'A'))



