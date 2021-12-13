"""

"""
class VendingMachine(num_items, item_price):
    def buy(self, req_items, money, num_items, item_price):
        if req_items <= num_items :
            if money>= item_price:
                num_items -= req_items
                change = money-item_price
            if money < item_price:
                return ValueError("Not enough coins")
        if req_items > num_items:
            return ValueError("Not enough items in the machine")
        return change
    pass

if __name__ == '__main__':-
