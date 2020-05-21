class Item:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category
        if price<=0:
            raise ValueError("Invalid value for price, got {}".format(self.price))
            
            
    def __str__(self):
        return "{}@{}-{}".format(self.name,self.price,self.category)
class Query:
    def __init__(self,field,operation,value):
        self.field=field
        self.value=value
        oper=['EQ','IN','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
        if operation in oper:
           self.operation=operation
        else:
           raise ValueError("Invalid value for operation, got {}".format(operation))
        
    def __str__(self):
        return "{} {} {}".format(self.field,self.operation,self.value)
        

class Store:
    def __init__(self):
        self.list1=[]
        
    def add_item(self,item):
        self.list1.append(item)

    def count(self):
        result=len(self.list1)
        return result
    
        
        
    def __str__(self):  
        if len(self.list1)>0:
            return "\n".join(map(str,self.list1))
        else:
            return "No items"
            

          
    def filter(self,query):
        result=Store()
        #print(self.list1)
        if query.operation=="IN":
            for i in self.list1:
                if i.category in query.value or i.name in query.value or i.price in query.value:
                    result.add_item(i)
                 
            return result    
        
        if query.operation=="EQ":
            for i in self.list1:
                if  query.field=="category" and i.category==query.value or  query.field=="name" and i.name==query.value or query.field=="price" and i.price==query.value:
                    result.add_item(i)
                 
            return result  
            
        if query.operation=="GT":
            for i in self.list1:
                if i.price > query.value:
                    result.add_item(i)
            return result
            
        if query.operation=="GTE":
            for i in self.list1:
                if i.price>=query.value:
                    result.add_item(i)
                    
            return result   
        
        if query.operation=="LT":
            for i in self.list1:
                if i.price<query.value:
                    result.add_item(i)
                    
            return result 
            
        if query.operation=="LTE":
            for i in self.list1:
                if i.price<=query.value:
                    result.add_item(i)
                    
            return result  
            
        
        if query.operation=="STARTS_WITH":
            for i in self.list1:
                if i.name.startswith(query.value) or i.category.startswith(query.value):
                    result.add_item(i)
                    
            return result
            
            
        if query.operation=="ENDS_WITH":
            for i in self.list1:
                if i.name.endswith(query.value) or i.category.endswith(query.value):
                    result.add_item(i)
                    
            return result 
        
        if query.operation=="CONTAINS":
            for i in self.list1:
                if query.field == "name" and query.value in i.name or query.field == "category" and query.value in i.category:
                    result.add_item(i)
                    
            return result 
            
    def exclude(self,query):
        query_1=Store()
        include=self.filter(query)
        #print(self.list1)
        [query_1.add_item(i) for i in self.list1 if i not in include.list1]
        return query_1
""" 
        if query.operation=="IN":
            for i in self.list1:
                if i.category not in query.value or i.name not in query.value or i.price in query.value:
                   query_1.add_item(i)
            return query_1   
            
        if query.operation=="GT":
            for i in self.list1:
                if i.price <= query.value:
                    query_1.add_item(i)
            return query_1
        
        if query.operation=="GTE":
            for i in self.list1:
                if i.price < query.value:
                    query_1.add_item(i)
            return query_1
            
        if query.operation=="LT":
            for i in self.list1:
                if i.price >= query.value:
                    query_1.add_item(i)
            return query_1
            
        if query.operation=="LTE":
            for i in self.list1:
                if i.price > query.value:
                    query_1.add_item(i)
            return query_1
            
            
        if query.operation=="STARTS_WITH":
            for i in self.list1:
                if i.name.startswith(query.value) or i.category.startswith(query.value):
                   query_1.add_item(i)
                else:
                  
"""
        
        
            
        
        
        
        
        
        
        
        
        
        
"""       
store = Store()  
item = Item(name="Oreo Biscuits", price=30, category="Food")  
store.add_item(item)  
item = Item(name="Boost Biscuits", price=20, category="Food")  
store.add_item(item)  
item = Item(name="ParleG Biscuits", price=10, category="Food")  
store.add_item(item)  
print(store)  
#Oreo Biscuits@30-Food  
#Boost Biscuits@20-Food  
#ParleG Biscuits@10-Food  
query = Query(field="price", operation="GT", value=15)  
results = store.exclude(query)  # exclude all items whose price is greater than 15 
print(results)  
#ParleG Biscuits@10-Food 
"""

 

        
        
        
        
        

