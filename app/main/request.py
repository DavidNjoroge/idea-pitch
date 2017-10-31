from ..models import Comment,User,Pitch,Category

def machine():
    cats=Category.query.all()
    categories=[]
    for cat in cats:
        tem=str(cat)
        temp=tem.split(' ')[1]
        result=(temp,temp)
        categories.append(result)
        # print (result)
    return categories
