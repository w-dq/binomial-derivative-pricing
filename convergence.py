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

for k in [50,90,95,100,105,110,150]:
    diff = []
    x_axis = []
    tree_list = []
    bsm_list = []
    for N in range(1,300):
        tree = Binomial_Tree(s0,T,sigma,N,r,k,american,ko,value_func)
        tree.forward()
        tree.backwards()
        b_price = tree.get_price()
        a_price = bsm_option_price(s0,k,r,sigma,T)

        tree_list.append(b_price)
        bsm_list.append(a_price)
        diff.append(abs(b_price - a_price))
        x_axis.append(N)

    fig, ax = plt.subplots()
    ax.plot(x_axis, diff, label="CCR Price - BSM Price (abs)")
    ax.legend()
    ax.set_xlabel("Number of Steps (N)")
    ax.set_title(f"tree vs analytical K:{k}, S:100")
    plt.yscale('log')
    # plt.show()
    plt.savefig(f"convergence_result/{k}.png")

# print(final_price)  
# print(bsm_option_price(s0,k,r,sigma,T))
