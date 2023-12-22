class MessageNotFoundError(Exception):
    def __init__(self, message="Message not found"):
        self.message = message
        super().__init__(self.message)

def find_message(messages, target):
    if target not in messages:
        raise MessageNotFoundError(f"Message '{target}' not found")
    return target

# Example usage:
messages = ["smth", "nothing", "anything"]

try:
    target_message = input("Enter a message to search for: ")
    found_message = find_message(messages, target_message)
    print(f"Found message: {found_message}")
except MessageNotFoundError as e:
    print(f"Error: {e}")