class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.attributes = {}

    def add_field(self, type, name):
        self.attributes[type] = name
        return self

    def __str__(self):
        if self.attributes:
            attributes_str = "  def __init__(self):\n    "
            attributes_str += "\n    ".join("self.%s = %s"%(key, value) for key, value in self.attributes.items())
        else:
            attributes_str = "  pass"

        return 'class %s:\n'%(self.root_name) + \
            '%s'%(attributes_str)
    

cb = CodeBuilder('Person').add_field('name', '""')\
                          .add_field('age', '0')
print(cb)