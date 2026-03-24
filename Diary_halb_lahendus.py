class Diary:

    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        entry = f"{self.count}: {text}"
        self.entries.append(entry)

    def remove_entry(self, index):
        if 0 <= index < len(self.entries):
            self.entries.pop(index)
        else:
            print("Invalid index")

    def save(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for entry in self.entries:
                f.write(entry + "\n")

    def load(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            self.entries = [line.strip() for line in f]
        self.count = len(self.entries)

    def print_statistics(self):
        total_entries = len(self.entries)
        if total_entries == 0:
            avg_length = 0
        else:
            total_chars = sum(len(entry) for entry in self.entries)
            avg_length = total_chars / total_entries

        print(f"Entries: {total_entries}")
        print(f"Average length: {avg_length:.2f}")

    def __str__(self):
        return "\n".join(self.entries)
