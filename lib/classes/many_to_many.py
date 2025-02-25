class Coffee:
    def __init__(self, name):
        self.name = name
        
    @property
    def name_getter(self):
        return self._name
    
    @name_getter.setter
    # name of method needs to be "name" so it matches the instance
    def name(self, name_value):
        if (not hasattr(self, 'name') and (type(name_value) == str) and (len(name_value) >= 3)):
            self._name = name_value

    # Relationship: 1 Order has many Coffees (1-to-Many Relationship)
    def orders(self):
        # returns a list of all orders for that coffee
        return [order for order in Order.all if order.coffee is self]
    
    # Relationship: Many-to-Many Relationship
    def customers(self):
        # returns a unique list of all customers who have ordered a particular coffee
        return list(set([order.customer for order in self.orders()]))

    def num_orders(self):
        return len(self.orders())

    # I THINK MAYBE SOMETHING ABOUT THIS IS WRONG....
    def average_price(self):
        if self.num_orders() == 0:
            return 0
        else:
            price_list = [order.price for order in self.orders()]
            return sum(price_list) / len(price_list)

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name_getter(self):
        return self._name
    
    @name_getter.setter
    def name(self, name_value):
        if (type(name_value) == str) and (1 <= len(name_value) <= 15):
            self._name = name_value
        
    # Relationship: 1 Customer has many orders (1-to-Many Relationship):
    def orders(self):
        # returns a list of all orders for that customer
        return [order for order in Order.all if order.customer is self]

    # Relationship: 1 Customer has many coffees (through Order) (Many-to-Many Relationship):
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))

    def create_order(self, coffee, price):
        # Order expects: self, customer, coffee, price in that order --- customer comes from Customer class
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(coffee):
        # use max
        pass

class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price_getter(self):
        return self._price
    
    @price_getter.setter
    def price(self, price_value):
        if (not hasattr(self, 'price') and (type(price_value) == float) and (1.0 <= price_value <= 10.0)):
            self._price = price_value

    @property
    def customer_getter(self):
        return self._customer
    
    @customer_getter.setter
    def customer(self, customer_value):
        if isinstance(customer_value, Customer):
            self._customer = customer_value

    @property
    def coffee_getter(self):
        return self._coffee
    
    @coffee_getter.setter
    def coffee(self, coffee_value):
        if isinstance(coffee_value, Coffee):
            self._coffee = coffee_value

    