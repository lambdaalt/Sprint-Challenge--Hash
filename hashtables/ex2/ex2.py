#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = {} # dict instead of hashtable
    route = []

    for i in range(length):
        ht[tickets[i].source] = tickets[i].destination
        i = i+1

    curr_source = ht['NONE']

    while curr_source != 'NONE':
        route.append(curr_source)
        curr_source = ht[curr_source]
    route.append(curr_source)

    return route
