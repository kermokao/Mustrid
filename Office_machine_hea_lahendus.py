class Printer():
    def print(self, document):
        pass

class Scan():
    def scan(self, document):
        pass

class Fax():
    def fax(self, document):
        pass

class MyPrinter(Printer):

    def print(self, document):
        print(f"printing: {document}")

class Photocopier(Printer, Scan):

    def print(self, document):
        print(f"printing: {document}")

    def scan(self, document):
        print(f"scanning: {document}")

class MultiFunctionPrinter(Printer, Scan, Fax):
    def print(self, document):
        print(f"printing: {document}")

    def fax(self, document):
        print(f"faxing: {document}")

    def scan(self, document):
        print(f"scanning: {document}")


if __name__ == "__main__":

    printer = MyPrinter()
    photocopier = Photocopier()

    printer.print("Hello from printer")

    photocopier.print("Copy this document")
    photocopier.scan("Scanned document")

    mfm = MultiFunctionPrinter()
    mfm.print("Delegated print")
    mfm.scan("Delegated scan")
