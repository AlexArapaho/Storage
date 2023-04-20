class UserInterface:
    def wait_answer(self):
        print("Choice of action\n"
              "add book - 1\n"
              "see catalogue - 2\n"
              "see book infon - 3\n"
              "delete book - 4\n"
              "exit - q")
        answer = input("Select action: ")
        return answer
