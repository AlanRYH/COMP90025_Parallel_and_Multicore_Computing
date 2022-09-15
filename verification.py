import networkx as nx
import sys

G = nx.read_edgelist(sys.argv[1], create_using=nx.DiGraph(), data=(("capacity", float),))

min_max_flow = sys.float_info.max
for u in G.nodes:
    for v in G.nodes:
        if u == v:
            continue

        flow_value, flow_dict = nx.maximum_flow(G, u, v)
        #print(u + ", " + v + ": " + str(flow_value))

        if flow_value > 0:
            min_max_flow = min(min_max_flow, flow_value)

print(min_max_flow)