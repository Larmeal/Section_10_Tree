class Tree:

    def __init__(self):
        self.array = [{
           "value": None,
            "left": None,
            "right": None
        },]
        
        self.array_add = [{
           "value": None,
            "left": None,
            "right": None
        },]

        self.value_ = None
        self.left_ = None
        self.right_ = None

    def insert(self, value):
        for i in range(len(self.array)):
            if self.array[i]["value"] == None:
                self.array[i]["value"] = value
                return self.array
            elif self.array[i]["value"] != None:
                if value < self.array[i]["value"] and self.array[i]["left"] == None:
                    self.array[i]["left"] = value
                    return self.array
                elif value < self.array[i]["value"] and self.array[i]["left"] != None:
                    self.array.append(self.array_add[0])
                    self.array[i + 1]["value"] = self.array[i]["left"]
                    if value < self.array[i + 1]["value"]:
                        self.array[i + 1]["left"] = value
                    elif value > self.array[i + 1]["value"]:
                        self.array[i + 1]["right"] = value
                elif value > self.array[i]["value"] and self.array[i]["right"] == None:
                    self.array[i]["right"] = value
                    return self.array
                
                elif value > self.array[i]["value"] and self.array[i]["right"] != None:
                    self.array.append(self.array_add[0])
                    self.array[i + 1]["value"] = self.array[i]["right"]
                    if value < self.array[i + 1]["value"]:
                        self.array[i + 1]["left"] = value
                    elif value > self.array[i + 1]["value"]:
                        self.array[i + 1]["right"] = value
                elif value == self.array[i]["value"]:
                    print("No duplicate vertex allowed!")
        return self.array

test_1 = Tree()
print(test_1.insert(5))
print(test_1.insert(9))
print(test_1.insert(3))
print(test_1.insert(6))
print(test_1.insert(2))