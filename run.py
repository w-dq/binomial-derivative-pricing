

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
    ko = config["knock_out"]                    # Knock out level, if none please use null
    ki = config["knock_in"]                     # Knock out level, if none please use null
    value_func_name = config["value_function"]  # Value function fo the derivative

    module = importlib.import_module("derivative_value")
    value_func = getattr(module, value_func_name)

    final_price = None
    if ki: 
        ko = ki
        tree = Binomial_Tree(s0,T,sigma,N,r,k,american,ko,value_func)
        tree.forward()
        tree.backwards()
        # tree.print_tree()
        ko_price = tree.get_price()

        ko = None
        tree = Binomial_Tree(s0,T,sigma,N,r,k,american,ko,value_func)
        tree.forward()
        tree.backwards()
        # tree.print_tree()
        rep_price = tree.get_price()

        final_price = rep_price - ko_price

    else:
        tree = Binomial_Tree(s0,T,sigma,N,r,k,american,ko,value_func)
        tree.forward()
        tree.backwards()
        # tree.print_tree()
        final_price = tree.get_price()

    print(final_price)  
    print(bsm_option_price(s0,k,r,sigma,T))
