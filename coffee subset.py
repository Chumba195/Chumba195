class Coffee:
    def __init__(self):
        self.ounces = 11

    def drink(self, sip):
        self.ounces -= sip

Coffee = Coffee()

while Coffee.ounces:
    Coffee.drink(1)

print("Get shit done!")