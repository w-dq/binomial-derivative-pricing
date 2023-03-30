

from binomial import Binomial_Tree

if __name__ == "__main__":
    s0 = 100              # Current price of underlying
    T = 1               # Time to expire
    sigma = 0.1           # Volatility 
    N = 5               # Number of steps
    r = 0               # Risk-free rate
    k = 110               # Stirke price, if applicable
    american = False    # If American-style
    tree = Binomial_Tree(s0,T,sigma,N,r,k,american)
    tree.forward()
    # tree.print_tree()
    tree.print_tree()
