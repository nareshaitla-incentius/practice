import csv
class Item:
    pay_rate=0.8
    all=[]
    def __init__(self,name:str,price:float,quantity:int):
        
        assert price>=0,f'price {price} is not greater than zero'
        assert quantity>=0 ,f'quantity {quantity} is not greater than zero'
        
        self.name=name
        self.price=price
        self.quantity=quantity
        #ACtion to excute
        Item.all.append(self)
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"
    def calculate_total_price(self):
        print(self.quantity*self.price)
    def apply_discount(self):
        self.price=self.price*self.pay_rate
    @classmethod 
    def instantiate_from_csv(cls):
        with open("items.csv" ,"r") as f:
            reader=csv.DictReader(f)
            items=list(reader)
         
        for item in items:
            Item(
                name=item.get("name"),
                price=int(item.get("price")),
                quantity=int(item.get("quantity")),
            )
        


Item.instantiate_from_csv()
print(Item.all)
# item1=Item("phone",100,4)  #creating an object or instance of a class

# item2=Item("laptap",1000,3)
# item3=Item("mouse",200,4)
# item4=Item("keyboard",300,3)

# print(item1.__dict__) # it will give the attributes that belong to the object and you will get the output as dictionary
# print(Item.__dict__)

# item1.apply_discount()
# print(item1.price)

# item2.pay_rate=0.7

# item2.apply_discount()
# print(item2.price)
 























'''class User:
    def __init__(self,user_email,name,password,job_title):
        self.email=user_email
        self.name=name
        self.password=password
        self.job_title=job_title
    def change_password(self,new_password):
        self.password=new_password
    def change_job_title(self,new_job_title):
        self.job_title=new_job_title
    def get_user_info(self):
        print(f"User {self.name} is currently doing a {self.job_title} to contact go with is {self.email}")
'''

