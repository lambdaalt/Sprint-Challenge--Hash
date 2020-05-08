def get_indices_of_item_weights(weights, length, limit):
    w = {}
    # would a keysfrom() be a better use here?
    for i in range(length):
        key = limit - weights[i]
        if key in w.values():
            return [i, weights.index(key)]
        else:
            w[i] = weights[i]
            i+=1
    return None
    

    # return None
