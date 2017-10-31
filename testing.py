foo=['User business', 'User science', 'User tech', 'User interview', 'User pickup lines']

# def machine(foo):
#     for cat in foo:
#         temp=cat.split(' ')[1]
#         result=(temp,temp)
#         print (result)


def machine(foo):
    categories=[]
    for cat in foo:
        temp=cat.split(' ')[1]
        result=(temp,temp)
        categories.append(result)
    return categories
