# class Product:
#     def __int__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     # def __str__(self):
#     #     str=""+self.name+"{price:"+self.price+",\nquantity:"+self.quantity+"}"
#     #     return str
#
#
# name="product"
# price=10.0
# quantity=100
# p= Product(name,price,quantity)
#
# print(p)

class Product:
  def __init__(self, name, price,qty):
    self.name = name
    self.price = price
    self.quantity=qty

  def getPrice(self):
    return self.price
  def getQuanty(self):
      return self.quantity
  def getName(self):
        return name

  def setPrice(self,price):
       self.price=price

  def setQuanty(self,quantity):
       self.quantity=quantity

  def setName(self,name ):
       self.name
  def totalCost(self,qty):
        return self.price*qty
  def __str__(self):
    stro=""+self.name+"{\n  price:"+str(self.price)+",\n  quantity:"+str(self.quantity)+"\n}"
    return stro

name="product"
price=10.0
quantity=100
p= Product(name,price,quantity)
print(p)
print(p.totalCost(10))