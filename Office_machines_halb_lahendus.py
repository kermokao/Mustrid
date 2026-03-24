class Machine:

    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass

class MultiFunctionPrinter(Machine):
    def print(self, document):
        print("Hello World")

    def fax(self, document):
        print("Test document")

    def scan(self, document):
        raise NotImplementedError("Printer cannot scan")


class OldFashionedPrinter(Machine):
    def print(self, document):
        print("Hello World")

    def fax(self, document):
        pass

    def scan(self, document):
        raise NotImplementedError("Printer cannot scan")
    
printer = OldFashionedPrinter()

printer.print("Hello world")
printer.fax("Test document")
printer.scan("Important document")
