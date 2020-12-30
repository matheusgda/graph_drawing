import sys
import network2tikz as tikz
import numpy as np

# drawing a 2D-grid

N = 1
M = 5

if len(sys.argv) > 2:
    N = int(sys.argv[1])
    M = int(sys.argv[2])

num_nodes = N * M
nodes = list(range(num_nodes))
canvas_size = (5, 5)


def grid2D(N, M, canvas_size=(6, 6)):

    edges = []
    vertex_layout = {}
    for i in range(N):
        for j in range(M):

            u = i * N + j
            vertex_layout[u] = (canvas_size[1] * j / M, canvas_size[0] * i / 2)

            for k in [1, -1]:

                disp = i + k
                if disp > -1 and disp < N:
                    edges.append((u, disp * N + j))

                disp = j + k
                if disp > -1 and disp < M:
                    edges.append((u, i * N + disp))
    return edges, vertex_layout

edges, vertex_layout = grid2D(N, M, canvas_size)

# add self loop
for i in range(num_nodes):
    edges.append((i, i))

style = {}
style['edge_directed'] = np.ones(len(edges), dtype=bool).tolist()
style['layout'] = vertex_layout
style['canvas'] = canvas_size
# style['edge_curved'] = 0.1
style['node_size'] = 0.5
style['edge_loop_position'] = 10
style['edge_color'] = (155, 155, 155)

print(edges)
tikz.plot((nodes, edges), 'test1.tex', **style)
