from BSM import bsm_option_price
import importlib
import math
import numpy as np
import json
import matplotlib.pyplot as plt


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

discount = math.exp(-r*T)

x_axis = []
c_list = []
p_list = []
k_list = []
s_list = []

    

for k in range(10,2*s0,10):
    x_axis.append(k)
    k_list.append(k * discount)
    c_list.append(bsm_option_price(s0,k,r,sigma,T,'call'))
    p_list.append(bsm_option_price(s0,k,r,sigma,T,'put'))
    s_list.append(s0)

diff1 = np.subtract(c_list, p_list)
diff2 = np.subtract(s_list, k_list)

fig, axs = plt.subplots(3, 1, sharex=True, sharey=False)


axs[0].plot(x_axis, c_list, label="call")
axs[0].plot(x_axis, p_list, label="put")
axs[0].plot(x_axis, k_list, label="k*exp(-r*T)")
axs[0].plot(x_axis, s_list, label="spot")
axs[0].set_title("Seperate Components")

axs[1].plot(x_axis, diff1, label="call - put ", color = 'red')
axs[1].set_title("Call Price - Put Price")

axs[2].plot(x_axis, diff2, label="spot - pv(k)", color = 'red')
axs[2].set_title("Spot Price - PV(K)")
axs[2].set_xlabel("Strike Price (K)")

handles, labels = axs[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', ncol=4)
# axs[0].legend()
# axs[1].legend()
# axs[2].legend()

plt.show()

    

    



