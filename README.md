# binomial-derivative-pricing

need `numpy` installed

### How to use

Run `python run.py` to get the price of an option in config.

Run `verify_pcp.py` to verify the put-call parity.

Run `convergence.py` to seed how tree and analytical price converges.

Run `high_KO.py` to see how the price of Konck-out option and simple option compares when knock-out level increases.

### How to config

```
{
    "s0": 100,													# Current price of underlying
    "T": 1,															# Time to expire
    "sigma": 0.1,												# Volatility
    "N": 50,														# Number of steps
    "r": 0,															# Risk-free rate
    "k": 100,														# Stirke price, if applicable
    "american": false,									# If American-style
    "knock_out": null,									# Knock out level, if none please use null
    "knock_in": null,										# Knock out level, if none please use null
    "value_function": "call_value_func"	# Value function fo the derivative
}
```

!!! Define `value_function` in `derivative_value.py` and put the value as the name of the function

​	`call_value_func` and `put_value_func` are provided

### Algorithm 

The Binomial tree is stored as a list of custom Node class.

The parent and child relation is solved numerically.

To run the model, we do a forward and backward operation. 

During the forward operation, each node is constructed with:

- The value of underlying $S_t$
- The value of the node if the option is exercised

During the backward operation, traverse the list in reverse order and:

- If St is Knocked out, the expected value is zero, 
- Otherwise:
  - If is leaf node, the expected value would be the exercised value stored in the construction
  - If is inner node, 
    - European: the expected value is is calculated using risk-neutral probability and discounted by the discount factor
    - American: the max between European expected value and exercised value stored in the construction

The value of the option will be stored in the expected value of the root node.