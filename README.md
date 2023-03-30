# binomial-derivative-pricing



### How to use

Run `python run.py` to get the price of a function

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



!!! `sigma` is not presented as percentage

!!! Define `value_function` in `derivative_value.py` and put the value as the name of the function

​	`call_value_func` and `put_value_func` are provided