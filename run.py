

from binomial import Binomial_Tree
from BSM import bsm_option_price
import importlib

import json

if __name__ == "__main__":
    with open("config.json", "r") as f:
        config = json.load(f)
    s0 = config["s0"]                           # Current price of underlying
    T = config["T"]                             # Time to expire
    sigma = config["sigma"]                     # Volatility 
    N = config["N"]                             # Number of steps
    r = config["r"]                             # Risk-free rate
    k = config["k"]                             # Stirke price, if applicable
    american = config["american"]               # If American-style
    value_func_name = config["value_function"]  # Value function fo the derivative

    module = importlib.import_module("derivative_value")
    value_func = getattr(module, value_func_name)

    tree = Binomial_Tree(s0,T,sigma,N,r,k,american,value_func)

    tree.forward()
    tree.backwards()
    # tree.print_tree()
    print(tree.get_price())
    print(bsm_option_price(s0,k,r,sigma,T))
