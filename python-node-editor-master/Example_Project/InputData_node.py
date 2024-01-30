from PySide6 import QtWidgets

from node_editor.node import Node
from Example_Project.common_widgets import FloatLineEdit


class InputData_Node(Node):
    def __init__(self):
        super().__init__()

        self.out_size = [None, 0, 0, 0]
        self.input_name = "Input_"

        self.title_text = "Input Data"
        self.type_text = "{} ({},{},{},{})".format(self.input_name, *self.out_size)
        self.set_color(title_color=(255, 165, 0))

        self.add_pin(name="Output", pintype="data", is_output=True, execution=True)

        self.build()
        
    def init_widget(self):
        self.widget = QtWidgets.QWidget()
        self.widget.setFixedWidth(100)
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.str_line = QtWidgets.QLineEdit(self.input_name)
        self.scaler_line1 = FloatLineEdit(str(self.out_size[1]))
        self.scaler_line2 = FloatLineEdit(str(self.out_size[2]))
        self.scaler_line3 = FloatLineEdit(str(self.out_size[3]))
        
        layout.addWidget(self.str_line)
        layout.addWidget(self.scaler_line1)
        layout.addWidget(self.scaler_line2)
        layout.addWidget(self.scaler_line3)
        self.widget.setLayout(layout)
        
        self.str_line.textChanged.connect(self.change_name)
        self.scaler_line1.textChanged.connect(self.change_value1)
        self.scaler_line2.textChanged.connect(self.change_value2)
        self.scaler_line3.textChanged.connect(self.change_value3)

        proxy = QtWidgets.QGraphicsProxyWidget()
        proxy.setWidget(self.widget)
        proxy.setParentItem(self)

        super().init_widget()
        
    def change_name (self, text):
        
        self.input_name = text
        self.type_text = "{} ({},{},{},{})".format(self.input_name, *self.out_size)
        self.build()
        
    def change_value1 (self, text):
        
        value1 = int(text.replace(',', '.'))
        self.out_size[1] = value1
        
        self.type_text = "{} ({},{},{},{})".format(self.input_name, *self.out_size)
        self.build()
        
    def change_value2 (self, text):
        
        value2 = int(text.replace(',', '.'))
        self.out_size[2] = value2
        
        self.type_text = "{} ({},{},{},{})".format(self.input_name, *self.out_size)
        self.build()
        
    def change_value3 (self, text):
        
        value3 = int(text.replace(',', '.'))
        self.out_size[3] = value3
        
        self.type_text = "{} ({},{},{},{})".format(self.input_name, *self.out_size)
        self.build()
        
    def execute(self):
        return self
        
    def write_fct(self):
        
        
        code = '\tinput_ = layers.Input(shape =({}, {}, {}) )'.format(*self.out_size[1:4])

        print(code)