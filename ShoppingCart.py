class Product:
   
 def _init_(self, name, price):
      
  self.name = name
        
self.price = price


class ShoppingCart:
    
def _init_(self):
        
self.items = []

    
def add_item(self, product, quantity):
       
 self.items.append((product, quantity))

  
  def remove_item(self, product):
        
self.items = [(p, q) for p, q in self.items if p != product]

  
  def calculate_total(self):
       
 total = sum(product.price * quantity for product, quantity in self.items)
        
return total


# Sample products

product1 = Product("Shirt", 20)

product2 = Product("Shoes", 50)

product3 = Product("Hat", 10)


# Sample cart

cart = ShoppingCart()


# Add items to cart

cart.add_item(product1, 2)

cart.add_item(product2, 1)


# Remove an item

cart.remove_item(product1)


# Calculate and print total

total = cart.calculate_total()
print(f"Total: ${total}")