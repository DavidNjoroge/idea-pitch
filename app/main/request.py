from ..models import Comment,User,Pitch,Category

def current_user_id(name):
    cats=Category.query.all()
    categories=[]
    for cat in cats:
        tem=str(cat)
        temp=tem.split(' ')[1]
        result=(temp,temp)
        categories.append(result)
        # print (result)
    return id
