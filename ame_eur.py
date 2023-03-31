from binomial import Binomial_Tree
from BSM import bsm_option_price
import importlib

import matplotlib.pyplot as plt

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

    x_axis = []
    ame_list = []
    eur_list = []

    # for k in range(60,200,10):
    for r in [-0.2,-0.1,-0.05, 0 ,0.01, 0.05]:
        x_axis = []
        ame_list = []
        eur_list = []
        for k in range(10,150,10):
            x_axis.append(k)

            american = False
            tree = Binomial_Tree(s0,T,sigma,N,r,k,american,ko,value_func)
            tree.forward()
            tree.backwards()
            eur_list.append(tree.get_price())

            american = True
            tree = Binomial_Tree(s0,T,sigma,N,r,k,american,ko,value_func)
            tree.forward()
            tree.backwards()
            ame_list.append(tree.get_price())


        fig, ax = plt.subplots()
        ax.plot(x_axis, ame_list, label="American")
        ax.plot(x_axis, eur_list, label="European")
        ax.legend()
        ax.set_xlabel("Strike (K)")
        ax.set_title(f"American and European price comparison r:{r}, S:100")
        # plt.show()
        plt.savefig(f"ame_eur_result/{r}.png")
