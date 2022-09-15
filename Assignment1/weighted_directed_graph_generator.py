#This is a random graph generator written by RAO YUNHUI
import random


#this function generates weighted directed graph
#and output the result in the form: src_node dest_node capacity
#and output the result into graph_n.txt where n is the index of the graph
#note: the node index will be from 0 to x-1
#note: the capacity is from 0 to 200 in a float form
def generate_graph(number_nodes, number_graphs):
    for g in range(number_graphs):
        filename = "graph" + str(g) + ".txt"
        f = open(filename, 'w')
        for i in range(number_nodes):
            for j in range(number_nodes):
                if i!=j:
                    f.write(str(i) + " " + str(j) + " " + str(round(random.uniform(0, 200), 2)) + "\n")
                    
                    
generate_graph(50, 5)