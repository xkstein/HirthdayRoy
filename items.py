class Item():
    #The Base class for all items
    def __init__(self, name, description, item_actions)
        self.name = name
        self.description = description
        self.item_actions = item_actions[]

    def __str__(self):
        return "{}\=====\nValue: {}\n".format(self.name, self.description, self.item_actions)
class Knife(Item):
    def __init__(self)
        super().__init__(name="knife"
                         description="A small kitchen knife, probably for cutting cheese."
                         item_actions=[use, drop]
                         )
