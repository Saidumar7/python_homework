import copy 
dict_1 = {2 : "two", 4: "four", 6: "six", "two": "two", "nested": {12: "twelve"}}
dict_2 = {8: "eight", 10: "ten"}   

# 1
if 2 in dict_1:
    value_2 = dict_1[2]
else:
    value_2 = "not found"
print(value_2)

if 22 in dict_1:
    value_22 = dict_1[22]
else:
    value_22 = "not found"
print(value_22)


# 2
if 2 in dict_1:
    print(True)
else:
    print(False)


# 3
if len(dict_1) == 0:
    print("Dictionary is empty")
else:
    print(len(dict_1))


# 4
keys = []
for key in dict_1:
    keys.append(key)
print(keys)


# 5
values = []
for key in dict_1:
    values.append(dict_1.get(key))
print(values)


# 6 merging two dictionaries
merged = copy.deepcopy(dict_1)
merged.update(dict_2)
print(merged)


# 7
d_copy = copy.deepcopy(dict_1)
if 2 in d_copy:
    del d_copy[2]
    print(d_copy)
else:
    print("key is not in ", d_copy)


# 8
d_clear = copy.deepcopy(dict_1)
d_clear = d_clear.clear()
print(d_clear)

# 9
if len(dict_1)==0:
    print("Dictionary is empty")
else:
    print("Dictionary is not empty")


# 10
if 2 in dict_1:
    pair = {2 : dict_1.get(2)}
else:
    pair = None
print(pair)


# 11
d_copy1 = dict_1.copy()
if 2 in d_copy1:
    d_copy1.update({2, "not two"})
    print(d_copy1)
else:
    print("key is not in dictionary")


# 12
value_to_count = "two"
count = 0
for key in dict_1:
    if dict_1[key]==value_to_count:
        count+=1
print("value", value_to_count, "appeared", count, "times")


# 13
invert = {}
for key in dict_1:
    value1 = dict_1.get(key)
    if type(value1) != dict:
        invert.update({value1: key})
print(invert)


# 14
value_to_find = "two"
keys_with_that_value = []
for key in dict_1:
    if dict_1[key]==value_to_find:
        keys_with_that_value.append(key)
print(keys_with_that_value)


# 15
keys_list = [1, 3]
values_list = ["one", "three"]
dict_from_list = {}
for i in range(len(keys_list)):
    dict_from_list[keys_list[i]]=values_list[i]
print(dict_from_list)


# 16
flag=False
for key in dict_1:
    if type(dict_1[key]) == dict:
        flag = True
        break
print(flag)

#17
if "nested" in dict_1:
    nested_value = dict_1["nested"][12]
else:
    nested_value = None
print(nested_value)

# 18
default_value = dict_1.get(15, 'default')
print(default_value)

#19
unique_values = []
for key in dict_1:
    if dict_1[key] not in unique_values:
        unique_values.append(dict_1.get(key))
number_of_unique_values = len(unique_values)
print(number_of_unique_values)

# 20
all_keys = []
sorted_dict = {}
for i in dict_1:
    all_keys.append(i)
sorted_keys = sorted(all_keys)
for i in sorted_keys:
    sorted_dict[i]=dict_1[i]
print(sorted_dict)

# # 21
# all_values = list(dict_1.items())
# all_values.sort()
# sorted_by_value ={}
# for key, value in all_values: