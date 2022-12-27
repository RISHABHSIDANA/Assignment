class CustomException(Exception):
    def __init__(self, message):
        self.message = message

def list_access(list_a, index):
    try:
        index = int(index)
        print(list_a[index])
    except ValueError:
        raise CustomException("Use an Integer value as the input.")
    except IndexError:
        raise CustomException(f"The index {index} is incorrect and index should lie between -{len(list_a)} and {len(list_a)-1}.")

list_a = [1, 2, 3, 4, 5]

try:
    list_access(list_a, 10)
except CustomException as e:
    print(e.message)


try:
    list_access(list_a, "abc")
except CustomException as e:
    print(e.message)
