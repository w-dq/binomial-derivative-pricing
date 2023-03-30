import numpy
import math

from derivative_value import put_value_func


# parent u refers to the node that goes a down path to reach the current node

class Node:
    def __init__(self,american = False):
        self.s_t = None
        self.excercise_value = None
        self.expected_value = None
        self.value = 0
        self.american = american

    def construct(self, s, ev):
        self.s_t = s
        self.excercise_value = ev
    
    def update(self,u_val,d_val,p):
        self.expected_value = p * u_val + (1 - p)*d_val
        if self.american:
            self.value = max(self.excercise_value,self.expected_value)
        else:
            self.value = self.expected_value
    
    def update_leaf(self):
        self.expected_value = self.excercise_value
        self.value = self.expected_value 
    
    def __str__(self):
        return f"({self.s_t:.2f},{self.value:.2f})"


class Binomial_Tree:
    def __init__(self, s0 = 0, T = 1, sigma = 1, N = 1,r = 0, k = 0, american = False, value_func = put_value_func):
        self.s0 = s0
        self.time_to_expire = T
        self.sigma = sigma
        self.steps = N
        self.risk_free = r
        self.strike = k
        self.value_func = value_func
        
        self.deltaT = T / N
        self.number_of_nodes = int(((N+2)*(N+1))/2)
        self.node_list = [Node(american) for _ in range(self.number_of_nodes)]
        self._compute_CRR()


    
    def _compute_CRR(self):
        self.up_move = math.exp(self.sigma * math.sqrt(self.deltaT))
        self.down_move = 1 / self.up_move
        self.p = (math.exp(self.risk_free * self.deltaT) - self.down_move) / (self.up_move - self.down_move)

    def _find_layer_head(self, layer_i):
        return int((layer_i*(layer_i + 1))/2)

    def _find_layer(self, idx):
        for i in range(self.number_of_nodes + 1):
            head = self._find_layer_head(i)
            if idx - head <= i:
                return i

    def _find_child_idx(self, idx):
        layer_n = self._find_layer(idx)
        if idx + layer_n + 2 >= self.number_of_nodes:
            return 0,0
        return idx + layer_n + 1, idx + layer_n + 2
    
    def forward(self):
        ev = self.value_func(self.s0,self.strike)
        self.node_list[0].construct(self.s0,ev)
        
        for layer_i in range(1,self.steps+1):
            head = self._find_layer_head(layer_i)
            for node_i in range(layer_i+1):
                s_t = self.s0 * (self.up_move ** (layer_i-node_i)) * (self.down_move ** node_i)
                ev = self.value_func(s_t,self.strike)
                self.node_list[head+node_i].construct(s_t, ev)

    def backwards(self):
        for layer_i in range(self.steps,-1,-1):
            for node_i in range(layer_i+1):
                head = self._find_layer_head(layer_i)
                node_idx = head + node_i
                child_u,child_d = self._find_child_idx(node_idx)
                # print(f"parent:{node_idx},u:{child_u},d:{child_d}")
                if child_u and child_d: 
                    self.node_list[node_idx].update(self.node_list[child_u].value,self.node_list[child_d].value,self.p)
                else:
                     self.node_list[node_idx].update_leaf()

    def get_price(self):
        root = self.node_list[0]
        return root.value
    
    def print_tree(self):
        print("0:",self.node_list[0])
        for layer_i in range(1,self.steps+1):
            head = self._find_layer_head(layer_i)
            for node_i in range(layer_i+1):
                print(head+node_i, ":", self.node_list[head+node_i],end=" | ")
            print()