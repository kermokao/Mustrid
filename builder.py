class CodeBuilder:

    def __init__(self, class_name):
        self.class_name = class_name
        self.elements = []
    
    def add_field(self, name, value):
        self.elements.append((name, value))
        return self

    def __str__(self):
        indent_size = "  "
        output = []

        output.append(f"class {self.class_name}:")
        output.append("")

        output.append(f"{indent_size}def __init__(self):")
        output.append("")

        for name, value in self.elements:

            output.append(f"{indent_size * 2}self.{name} = {value}")


        return "\n".join(output)

cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0') 
print(cb)

