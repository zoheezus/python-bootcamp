my_dict = {"key1":"value1", "key2":"value2"}
print(my_dict)
print(my_dict["key1"])

prices_lookup = {"apple":2.99,"oranges":1.99,"milk":5.80}
print(prices_lookup["apple"])

d = {"k1":123,"k2":[0,1,2],"k3":{"insideKey":100}}
print(d["k2"])
print(d["k3"])
# stacking index calls
print(d["k3"]["insideKey"])

d["k4"] = "new value".upper()
print(d)

print(d.keys())
print(d.values())
print(d.items())