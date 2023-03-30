

from binomial import Binomial_Tree
from BSM import bsm_option_price

if __name__ == "__main__":
    s0 = 100              # Current price of underlying
    T = 1               # Time to expire
    sigma = 0.1           # Volatility 
    N = 50               # Number of steps
    r = 0               # Risk-free rate
    k = 100               # Stirke price, if applicable
    american = False    # If American-style
    tree = Binomial_Tree(s0,T,sigma,N,r,k,american)
    tree.forward()
    tree.backwards()
    # tree.print_tree()
    print(tree.get_price())
    print(bsm_option_price(s0,k,r,sigma,T))
