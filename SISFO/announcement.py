class announcementSystem:
    def __init__(self):
        self.announcement_list = []

    def create_announcement(self, description):
        announcement = description 
        self.announcement_list.append(announcement)
        print("Announcement has been posted")

    def view_announcement(self):
        if not self.announcement_list:
            print("No announcement yet.")
        elif len(self.announcement_list) == 1: 
            print(f"Announcement: {self.announcement_list[0]}")
        else:
            print("Announcements:")
            for announcement in self.announcement_list:
                print(announcement)
