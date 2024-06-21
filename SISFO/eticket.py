class ETicketSystem:
    def __init__(self):
        self.tickets = []

    def create_ticket(self, user_name, description):
        ticket = {
            "user_name": user_name,
            "description": description
        }
        self.tickets.append(ticket)
        print("Ticket created successfully! Our team will look into it.")

    def view_tickets(self):
        if not self.tickets:
            print("No tickets available.")
        else:
            print("Open Tickets:")
            for ticket in self.tickets:
                print(f"User Name: {ticket['user_name']}, Description: {ticket['description']}")
