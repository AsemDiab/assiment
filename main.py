
def Task1(sales):
    sum=0
    for x in sales:
        sum+=x
    if(len(sales)!=0):
        avg=sum/len(sales)
    else:
        avg=0
    print("sumation =",sum)
    print("average=",avg)
def Task2(prductDict,basket):
    totalCost=0
    for x in basket:
        totalCost+=prductDict[x]
    discont=0.1*totalCost
    print("total Cost Before Discont ="+totalCost)
    print("10% Discont ="+discont)
    print("total Cost After Discont ="+totalCost-discont)
if __name__ == '__main__':
    sales=[100,200,0,300,400,500]
    basket=["pizza","books","patata"]
    prductDict={
        "pizza":10,
        "books":20,
        "patata":5,
        "prduct4":100
    }
    Task1(sales)
    Task2(prductDict,basket)


