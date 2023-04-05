from binomial import Binomial_Tree
from BSM import bsm_option_price
import importlib

import matplotlib.pyplot as plt

import json


with open("config.json", "r") as f:
    config = json.load(f)
s0 = config["s0"]                           # Current price of underlying
T = config["T"]                             # Time to expire
sigma = config["sigma"]                     # Volatility 
N = config["N"]                             # Number of steps
r = config["r"]                             # Risk-free rate
k = config["k"]                             # Stirke price, if applicable
american = config["american"]               # If American-style
ko = config["knock_out"]                    # Knock out level, if none please use null
ki = config["knock_in"]                     # Knock out level, if none please use null
value_func_name = config["value_function"]  # Value function fo the derivative

module = importlib.import_module("derivative_value")
value_func = getattr(module, value_func_name)

x_axis = []
ko_list = []
sim_list = []

# for k in range(60,200,10):
for ko in [120, 140, 160, 200, 250, 400]:
    x_axis = []
    ko_list = []
    sim_list = []
    for k in range(10,150,10):
        x_axis.append(k)


        tree = Binomial_Tree(s0,T,sigma,N,r,k,american,ko,value_func)
        tree.forward()
        tree.backwards()
        ko_list.append(tree.get_price())

        tree = Binomial_Tree(s0,T,sigma,N,r,k,american,None,value_func)
        tree.forward()
        tree.backwards()
        sim_list.append(tree.get_price())


    fig, ax = plt.subplots()
    ax.plot(x_axis, ko_list, label="With KO")
    ax.plot(x_axis, sim_list, label="Simple Call")
    ax.legend()
    ax.set_xlabel("Strike (K)")
    ax.set_title(f"American and European price comparison ko:{ko}, S:100")
    # plt.show()
    plt.savefig(f"high_KO_result/{ko}.png")
