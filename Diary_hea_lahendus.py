class Diary:

    def __init__(self):
        self.sissekanded = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        entry = f"{self.count}: {text}"
        self.sissekanded.append(entry)

    def remove_entry(self, index):
        self.sissekanded.pop(index - 1)
        self.count -= 1

    def __str__(self):
         return "\n".join(self.sissekanded)
    
class DiaryPersistence:

    @staticmethod
    def save(diary, filename):
        with open(filename, "w") as f:
            for entry in diary.sissekanded:
                f.write(entry + "\n")

    @staticmethod
    def load(filename):
        diary = Diary()
        with open(filename, "r") as f:
            for line in f:
                diary.sissekanded.append(line)
                diary.count += 1
        return diary

class DiaryStatistics:
    
    @staticmethod
    def print_statistics(diary):
        text_length = 0
        for entry in diary.sissekanded:
            text = entry.split(":", 1)[1]
            text_length += len(text)

        average_length = text_length / diary.count
        print(f"count: {diary.count}")
        print(f"average letter count: {average_length}")


if __name__ == "__main__":

    diary = Diary()

    diary.add_entry("Täna oli ilus ilm.")

    diary.add_entry("Õppisin programmeerimist.")

    diary.add_entry("SRP on tegelikult väga loogiline.")

 

    print("---- DIARY SISU ----")

    print(diary)

    print()




# Statistika (kasutame staticmethod'e)

    print("---- STATISTIKA ----")

    DiaryStatistics.print_statistics(diary)

    print()




# Salvestame faili (EI loo Persistence objekti)

    filename = "diary.txt"

    DiaryPersistence.save(diary, filename)

 

    print(f"Salvestatud faili: {filename}")

    print()




# Laeme uuesti failist

    loaded_diary = DiaryPersistence.load(filename)

 

    print("---- FAILIST LAETUD ----")

    print(loaded_diary)

    print()




# Kontrollime, kas loendur töötab edasi

    loaded_diary.add_entry("See lisati pärast laadimist.")

 

    print("---- PÄRAST UUT LISAMIST ----")

    print(loaded_diary)
