
def build_graph(pipelines):
    graph = {}

    for pipeline in pipelines:
        if len(pipeline) >= 2:
            start, *destinations = pipeline
            if start not in graph:
                graph[start] = []
            for destination in destinations:
                if destination not in graph[start]:
                    graph[start].append(destination)
                if destination not in graph:
                    graph[destination] = []

    return graph

def bfs(active_pipelines, start):
    graph = build_graph(active_pipelines)
    visited = set()
    queue = [start]
    visited.add(start)
    while queue:
        current = queue.pop(0)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return visited


def find_connection_with_storages(graph, storages, cities):
    extended_storage_list = []
    for storage in storages:
        result = bfs(graph, storage)
        missing_cities = [city for city in cities if city not in result]
        extended_storage = [storage] + [missing_cities]
        extended_storage_list.append(extended_storage)
    return extended_storage_list


