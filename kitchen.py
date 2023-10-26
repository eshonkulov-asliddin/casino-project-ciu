from collections import deque
import random


class Kitchen:

    def __init__(self):
        self.seats = 5
        self.current_user = []
        self.visited = {}
        self.payment = {}
        self.queue = deque()


    def get_visited(self):
        return self.visited

    def get_current_user(self):
        return self.current_user

    def get_payment(self):
        return self.payment

    def queue_length(self):
        return len(self.queue)

    def is_queue_empty(self):
        return len(self.queue) == 0

    def has_available_seats(self):
        return self.seats > 0

    def decrement_seats(self):
        self.seats -= 1

    def increment_seats(self):
        self.seats += 1

    def get_index_of_current_user(self, user_id):
        for i in range(len(self.current_user)):
            if (self.current_user[i] == user_id):
                return i

        return -1

    def leave_kitchen(self, user_id):
        if user_id in self.current_user:
            index = self.get_index_of_current_user(user_id)
            if (index != -1):
                self.current_user.pop(index)
                self.increment_seats()
                print(f' user with id {user_id} leaved kitchen')
            else:
                print(f"User with id {user_id} doesn't exist")
        else:
            print(f"User with id {user_id} doesn't exist")

    def has_user_entered_before(self, id):
        for user_id, count in self.visited.items():
            if (user_id == id):
                return True
        return False


    def get_user_entered_times(self, times):
        users_id = []
        for user_id, count in self.visited.items():
            if (count == times):
                users_id.append(user_id)

        return users_id

    def get_daily_profit(self):
        profit = 0
        for user_id, payment in self.payment.items():
            profit += payment
        return profit

    def has_not_entered_user_in_queue(self):
        for user_id in self.queue:
            if (not user_id in self.visited):
                return True
        return False

    def ask_user_credentials(self):
        user_id = int(input("Enter your id: "))
        return user_id

    #add user to the kitchen
    def add_user(self, user_id):
        if (user_id in self.current_user):
            print(f"user with id {user_id} already exists")
        else:
            if (self.has_available_seats()):

                if (self.is_queue_empty()):

                    self.current_user.append(user_id)
                    self.visited[user_id] = 1
                    self.payment[user_id] = random.randint(5, 100)

                    self.decrement_seats()  # decrease seats by one
                    print(f"user with id {user_id} entered kitchen")

                else:
                    print(f"we have user waiting in kitchen...")
                    self.add_user_from_queue()
            else:
                print("we don't have place, please go to queue...")
                self.queue.append(user_id)


    def add_user_from_queue(self):
        if (not self.is_queue_empty()):
            user_id = self.queue.popleft()
            print(f"popped user id {user_id}")

            if (self.is_queue_empty() or
                    not self.has_user_entered_before(user_id)):

                self.current_user.append(user_id)
                self.visited[user_id] = self.visited.get(user_id, 0) + 1
                print(f"user with id {user_id} from queue added to kitchen")
            else:

                # do we have not entered user in queue
                if (self.has_not_entered_user_in_queue()):
                    self.queue.append(user_id)
                    print(f"user with id {user_id} added to the end of queue because this user has entered kitchen before")
                    self.add_user_from_queue()  # call funtion again to add user
                else:
                    print(f"user with id {user_id} from queue added to kitchen")
                    self.visited[user_id] = self.visited.get(user_id, 0) + 1
        else:
            print("queue is empty")

    def get_daily_report(self):
        print("###########user entered once##############")
        print(self.get_user_entered_times(1))
        print("###########user entered twice##############")
        print(self.get_user_entered_times(2))
        print("##################overall daily profit###########")
        print(f"${self.get_daily_profit()}")
