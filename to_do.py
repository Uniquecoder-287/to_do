class todoApp():
    def __init__(self):
        self.tasks = []
        self.nxt_id = 1
        
    def createTsk(self, name, date):
        new_task = {
            "id" : self.nxt_id,
            "name" : name,
            "date" : date
        }
        
        self.tasks.append(new_task)
        print(f"Task {self.nxt_id} successfully created.")
        self.nxt_id += 1
        
    def displayTsk(self):
        print("\n")
        print("Here is your task list:")
        for tsk in self.tasks:
            print(f"{tsk['id']}. {tsk['name']} - {tsk['date']}")
        
    def deletetsk(self, delete_selected_id):
        print("\n")
        for tsk in self.tasks:
            if tsk['id'] == delete_selected_id:
                self.tasks.remove(tsk)
                print(f"Task with id {delete_selected_id} successfully deleted.")
                return
            
        print(f"Task with id {delete_selected_id} not found.")
        
        

tsk_1 = todoApp()
tsk_1.createTsk("Buy groceries", "2024-06-15")
tsk_1.createTsk("Finish project report", "2024-06-20")
tsk_1.displayTsk()
tsk_1.deletetsk(1)
tsk_1.displayTsk()  
tsk_1.deletetsk(3)  