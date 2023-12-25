class Publication:
    publisher_name = "Default Publisher"

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def dispaly(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")


class Book(Publication):
    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn

    def dispaly(self):
        super().dispaly()
        print(f"Isbn: {self.isbn}")


class Magazine(Publication):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def dispaly(self):
        super().dispaly()
        print(f"Issue number: {self.issue_number}")


Alan_Wake = Book(
    "Welcome to Bright Falls-a seemingly idyllic small town in the Pacific Northwest.",
    "Rick Burroughs",
    2011,
    765366479,
)
Alan_Wake.publisher_name = "Tor Books"

Alan_Wake.dispaly()
print(Alan_Wake.publisher_name)


Time_magazine = Magazine(
    "Here Come the AI Health Coaches",
    "Will Henshall",
    2023,
    "https://time.com/6549810/ai-health-coach/",
)
Time_magazine.publisher_name = "TIME USA, LLC"

Time_magazine.dispaly()
print(Time_magazine.publisher_name)
