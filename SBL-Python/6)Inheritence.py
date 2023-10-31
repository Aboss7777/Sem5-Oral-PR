class Plant:
    def __init__(self, name):
        self.name = name

    def grow(self):
        pass
class Tree(Plant):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    def grow(self):
        self.height += 2
        print("Tree has grown by 2 meter\n")

    def show_height(self):
        print(f"{self.name} is currently {self.height} meters tall\n")

tree = Tree("Oak", 15)
tree.show_height()
tree.grow()
tree.show_height()
