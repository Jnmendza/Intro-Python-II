class Item:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description

    def on_take(self):
        print((f"You have picked up {self.item_name}"))

    def on_drop(self):
        print(f'You dropped {self.item_name}')

    def __str__(self):
        return f'{self.item_name} Description:{self.item_description}'
