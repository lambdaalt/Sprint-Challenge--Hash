def intersection(arrays):
    ht = {}
    # removed result = [] and append, works now
    
    for arr in arrays:
        for i in arr:
            if i not in ht:
                ht[i] = 1
            else:
                ht[i] += 1
    result = [key for key in ht if ht[key] == len(arrays)]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
