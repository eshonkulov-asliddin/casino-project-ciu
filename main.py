from kitchen import Kitchen

def display_operations():
    print("======================================")
    print("Enter to kitchen: 1")
    print("Leave kitchen: 2")
    print("Get all visited: 3")
    print("Get queue: 4")
    print("Get dailyt report: 5")
    print("Get current user in kitchen: 6")
    print("exit - 0")
    print("======================================")



KITCHEN = Kitchen()


#constants
ENTER_KITCHEN = 1
LEAVE_KITCHEN = 2
GET_ALL_VISITED = 3
GET_ALL_FROM_QUEUE = 4
GET_REPORT = 5
GET_CURRENT_USERS_IN_KITCHEN = 6
EXIT = 0

while True:

    display_operations()
    operation = int(input("Enter the command: "))

    if (operation == ENTER_KITCHEN):
        user_id = KITCHEN.ask_user_credentials()
        KITCHEN.add_user(user_id)
    elif (operation == LEAVE_KITCHEN):
        user_id = KITCHEN.ask_user_credentials()
        KITCHEN.leave_kitchen(user_id)

        if (not KITCHEN.is_queue_empty()):
            KITCHEN.add_user_from_queue()
        else:
            print("queue is empty")
    elif (operation == GET_ALL_VISITED):
        print(KITCHEN.visited)
    elif (operation == GET_ALL_FROM_QUEUE):
        print(KITCHEN.queue)
    elif (operation == GET_REPORT):
        KITCHEN.get_daily_report()
    elif (operation == GET_CURRENT_USERS_IN_KITCHEN):
        print(KITCHEN.get_current_user())
    elif (operation == EXIT):
        break




