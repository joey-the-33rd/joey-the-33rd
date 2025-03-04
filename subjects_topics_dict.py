subjects = {
    "Math": ["Algebra", "Geometry", "Calculus"],
    "Science": ["Physics", "Chemistry", "Biology"],
    "History": ["World War II", "Ancient Egypt", "Renaissance"],
    "Programming": ["Python", "Java", "C++"]
}

# Function to add a new subject
def add_subject():
    subject = input("Enter the subject name: ").strip()

    if subject in subjects:
        print(f"{subject} already exists.")
    else:
        subjects[subject] = []
        while True:
            topic = input(f"Enter a topic for {subject} (or type 'done' to finish): ").strip()
            if topic.lower() == "done":
                break
            subjects[subject].append(topic)
        
        print(f"{subject} added successfully!\n")

# Function to display subjects and topics
def display_subjects():
    print("\n--- Subjects and Topics ---\n")
    for subject, topics in subjects.items():
        topics.sort()  # Sort topics alphabetically
        print(f"{subject}:")
        for index, topic in enumerate(topics, start=1):
            print(f"  {index}. {topic}")
        print()  # Add a blank line for better readability

# Main loop
while True:
    print("\nOptions:")
    print("1. View subjects and topics")
    print("2. Add a new subject")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        display_subjects()
    elif choice == "2":
        add_subject()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
