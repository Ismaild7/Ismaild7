events = {}
eidc = 0

def create_event():
    global eidc  
    start_date = input("Enter start date: ")
    end_date = input("Enter end date: ")
    for event in events.values():
        if (event['start_date'] <= start_date <= event['end_date']) or (event['start_date'] <= end_date <= event['end_date']):
            print("There Is Other Event In This Date,Please Choose Another Date")
            return 
    eidc += 1
    event_id = eidc
    print("Event ID :",event_id)
    event_title = input("Enter event title: ")
    reserved_members = input("Enter reserved members: ")
    
    event = {
        "event_title": event_title,
        "reserved_members": reserved_members,
        "start_date": start_date,
        "end_date": end_date
    }
    
    events[event_id] = event
    print("Event created successfully!")
def read_event():
    event_id = int(input("Enter event ID: "))
    
    if event_id in events:
        event = events[event_id]
        print("Event ID:", event_id)
        print("Event Title:", event["event_title"])
        print("Reserved Members:", event["reserved_members"])
        print("Start Date:", event["start_date"])
        print("End Date:", event["end_date"])
    else:
        print("Event not found!")


def update_event():
    event_id = int(input("Enter event ID: "))
    
    if event_id in events:
        event = events[event_id]
        print("Current Event Details:")
        print("Event ID:", event_id)
        print("Event Title:", event["event_title"])
        print("Reserved Members:", event["reserved_members"])
        print("Start Date:", event["start_date"])
        print("End Date:", event["end_date"])
        
        event_title = input("Enter new event title (leave blank to keep current): ")
        reserved_members = input("Enter new reserved members (leave blank to keep current): ")
        start_date = input("Enter new start date (leave blank to keep current): ")
        end_date = input("Enter new end date (leave blank to keep current): ")
        
        if event_title:
            event["event_title"] = event_title
        if reserved_members:
            event["reserved_members"] = reserved_members
        if start_date:
            event["start_date"] = start_date
        if end_date:
            event["end_date"] = end_date
        
        print("Event updated successfully!")
    else:
        print("Event not found!")

def delete_event():
    event_id = int(input("Enter event ID: "))
    
    if event_id in events:
        del events[event_id]
        print("Event deleted successfully!")
    else:
        print("Event not found!")

while True:
    print("\nEmployee Event Management System")
    print("1. Create Event")
    print("2. Read Event")
    print("3. Update Event")
    print("4. Delete Event")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        create_event()
    elif choice == "2":
        read_event()
    elif choice == "3":
        update_event()
    elif choice == "4":
        delete_event()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")


