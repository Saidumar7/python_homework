# # 1
# list1 = list(map(int, input("Enter space seperated elements of the first list: ").split()))
# list2 = list(map(int, input("Enter space seperated elements of the second list: ").split()))
# for i in list1:
#     if i in list2:
#         c1 = list1.count(i)
#         c2 = list2.count(i)
#         for j in range(c1):
#             list1[list1.index(i)] = None
#         for k in range(c2):
#             list2[list2.index(i)] = None

# uncommon_elements = []
# for w in (list1+list2):
#     if w != None:
#         uncommon_elements.append(w)
# print(uncommon_elements)

# # 2
# n = int(input("Enter n: "))
# for i in range(1,n):
#     print(i**2)

# 3
txt = input("Enter the text: ")
vowels = {'a', 'o', 'e', 'u', 'i'}
result = []
count = 0

i = 0
while i < len(txt):
    result.append(txt[i])  
    count += 1

    if count == 3:
        if (i + 1 < len(txt)) and (txt[i] not in vowels):  
            result.append("_")
            count = 0  
        else:
            count -= 1  
    i += 1

print("".join(result))
