class CustomerFirstName(object):
    def __init__(self, first_name):
        self.first_name = first_name

    def __str__(self):
        return(self.first_name)

class CustomerLastName(object):
    def __init__(self, last_name):
        self.last_name = last_name

    def __str__(self):
        return(self.last_name)
    #when using a function, it returns a serialized object
    #def last_name(self):
    #    return(last_name)

class CustomerAddress(object):

    def __init__(self, street_number, city, state, zip):
        self.street_number = street_number
        self.city = city
        self.state = state
        self.zip = zip

    def customer_address(self):
        return (street_number)
        return (city)
        return (state)
        return (zip)


class CustomerEmail(object):
    def customer_email_address(self, email):
        self.email = email


class CustomerInfo(CustomerFirstName, CustomerLastName, CustomerAddress, CustomerEmail):
    def customer_info(self):
        self.customer_info = customer_info
