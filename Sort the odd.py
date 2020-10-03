def sort_array(source_array):
    new_list = []
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            new_list.append(source_array[i])
            new_list.sort()
    for i in range(len(source_array)):
        if source_array[i] % 2 == 0:
            new_list.insert(i, source_array[i])
    return new_list


#def sort_array(arr):
 # odds = sorted((x for x in arr if x%2 != 0), reverse=True)
 # return [x if x%2==0 else odds.pop() for x in arr]

#def sort_array(source_array):
 #   odds = iter(sorted(v for v in source_array if v % 2))
 #   return [next(odds) if i % 2 else i for i in source_array]
print(sort_array([5, 3, 2, 8, 1, 4]))

