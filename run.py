

from binomial import Binomial_Tree

if __name__ == "__main__":
    s0 = 0              # Current price of underlying
    T = 1               # Time to expire
    sigma = 1           # Volatility 
    N = 1               # Number of steps
    r = 0               # Risk-free rate
    k = 0               # Stirke price, if applicable
    american = False    # If American-style
    tree = Binomial_Tree(s0,T,sigma,N,r,k,american)
