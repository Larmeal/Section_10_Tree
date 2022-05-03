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
            
            # if has a duplicate number return error
            if value == self.array[i]["value"]:
                return print("No duplicate vertex allowed!")
            
            # if don't has a node in dict. Added
            elif self.array[i]["value"] == None:
                self.array[i]["value"] = value
                return self.array
            
            # if has a node in dict. check the children has a node value
            else:
                
                if self.array[i]["left"] != None and self.array[i]["right"] != None and value < self.array[i]["value"]:
                    self.array.append(self.array_add[0])
                    self.array[i + 1]["value"] = self.array[i]["left"]
                    
                if self.array[i]["left"] != None and self.array[i]["right"] != None and value > self.array[i]["value"]:
                    self.array.append(self.array_add[0])
                    self.array[i + 1]["value"] = self.array[i]["right"]
                    
                # if left children don't has a node and the value more than the parent in this case the value added value in left children
                if self.array[i]["left"] == None and value < self.array[i]["value"]:
                    self.array[i]["left"] = value
                    return self.array
                
                # same way with left children 
                elif self.array[i]["right"] == None and value > self.array[i]["value"]:
                    self.array[i]["right"] = value
                    return self.array
                
                
                # if left children has a node. create new dict. and let new value = left children and check the number if more than new value
                # added the right new children
                # if not added the left new children
                elif self.array[i]["left"] != None and value < self.array[i]["value"]:
                    if value < self.array[i + 1]["value"]:
                        self.array[i + 1]["left"] = value
                        return self.array
                    
                    else:
                        self.array[i + 1]["right"] = value
                        return self.array
                    
                # same way with left children 
                elif self.array[i]["right"] != None and value > self.array[i]["value"]:
                    if value < self.array[i + 1]["value"]:
                        self.array[i + 1]["left"] = value
                        return self.array
                    
                    else:
                        self.array[i + 1]["right"] = value
                        return self.array
                

test_1 = Tree()
print(test_1.insert(5))
print(test_1.insert(9))
print(test_1.insert(3))
print(test_1.insert(6))
print(test_1.insert(2))
print(test_1.insert(12))