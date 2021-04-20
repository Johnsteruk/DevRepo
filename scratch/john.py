def make_car(manufacturer, model_name, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['manufacturer'] = manufacturer
    user_info['model_name'] = model_name
    return user_info

def print_message(myList, sent_messages):
    while myList:
        current_message = myList.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

def show_sent_messages(sent_messages):
    print("\nThe following messages have been sent:")
    for completed_message in sent_messages:
        print(completed_message)