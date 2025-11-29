from pyscript import display, document

# main.py
# School clubs data

# Dictionary of school clubs
clubs = {
    "Science Club": {
        "Name of the Club": "Science Club",
        "Description": "A club for students who enjoy experiments and discovery.",
        "Meeting Time": "Monday, 3:00 PM",
        "Location": "Room 201",
        "Club Moderator": "Mr. Santos",
        "Number of Members": 25
    },
    "Art Club": {
        "Name of the Club": "Art Club",
        "Description": "A club for students who love drawing, painting, and creativity.",
        "Meeting Time": "Wednesday, 4:00 PM",
        "Location": "Art Room",
        "Club Moderator": "Ms. Reyes",
        "Number of Members": 18
    },
    "Math Club": {
        "Name of the Club": "Math Club",
        "Description": "A club for students who enjoy solving math puzzles.",
        "Meeting Time": "Friday, 2:30 PM",
        "Location": "Room 105",
        "Club Moderator": "Mr. Cruz",
        "Number of Members": 30
    }
}

# Function to display club info in terminal
def show_club_info(club_name):
    if club_name in clubs:
        club = clubs[club_name]
        print("=== " + club_name + " ===")
        for key, value in club.items():
            print(f"{key}: {value}")
    else:
        print("Club not found.")

# Example usage
if __name__ == "__main__":
    print("Available clubs: Science Club, Art Club, Math Club")
    choice = input("Enter a club name: ")
    print()
    show_club_info(choice)
