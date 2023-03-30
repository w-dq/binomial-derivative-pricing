


#define your derivative value functions and change accordingly in "binomial.py" file
def call_value_func(s,k):
    return max(0,s-k)

def put_value_func(s,k):
    return max(0,k-s)