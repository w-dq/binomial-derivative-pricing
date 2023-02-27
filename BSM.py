import math
from scipy.stats import norm

def bsm_option_price(S, K, r, sigma, T, option_type='call'):
    """
    Computes the price of a European call or put option using the Black-Scholes-Merton formula.

    S:           float, the initial stock price
    K:           float, the strike price of the option
    r:           float, the risk-free interest rate
    sigma:       float, the volatility of the underlying stock
    T:           float, the time to expiration of the option (in years)
    option_type: str, either 'call' or 'put', representing the type of the option

    Returns:
    The price of a European call or put option.
    """
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == 'call':
        option_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        option_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type")

    return option_price