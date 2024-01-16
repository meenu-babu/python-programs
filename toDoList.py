class ToDoList:
    def __init__(self):
        self.items=[]
    def add_items(self,item_name):
        self.items.append(item_name)
    def view_items(self):
        print(self.items)
        return self.items
    def remove_item(self, index):
        try:
            self.items.pop(index)
        except IndexError:
            print("Invalid index. Please provide a valid index.")

obj=ToDoList()
while True:
    print("Enter your choice")
    print("1.Add item")
    print("2.Remove item")
    print("3.view item")
    print("4.exit")
    print("Enter your choice")
    choice=int(input())
    if choice==1:
        print("Enter the item")
        item_name=input()
        obj.add_items(item_name)
    elif choice==2:
        print("Enter the index that you want to remove")
        index=int(input())
        obj.remove_item(index)
    elif choice==3:
        print("The listed items are:")
        obj.view_items()
    elif choice==4:
        print("You are going to exit..")
        break
    else:
        print("Wrong choice!!please enter 1/2/3/4 ")