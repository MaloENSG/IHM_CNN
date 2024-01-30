from PySide6 import QtWidgets

from node_editor.node import Node
from Example_Project.common_widgets import FloatLineEdit


class Kernel2D_Node(Node):
    def __init__(self):
        super().__init__()

        self.out_param = [3,3]

        self.title_text = "Kernel2D"
        self.type_text = "Parameter ({},{})".format(*self.out_param)
        self.set_color(title_color=(255, 165, 0))

        self.add_pin(name="value", pintype="list2", is_output=True)

        self.build()
        
    def init_widget(self):
        self.widget = QtWidgets.QWidget()
        self.widget.setFixedWidth(100)
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.scaler_line0 = FloatLineEdit(str(self.out_param[0]))
        self.scaler_line1 = FloatLineEdit(str(self.out_param[1]))
        
        layout.addWidget(self.scaler_line0)
        layout.addWidget(self.scaler_line1)
        self.widget.setLayout(layout)
        
        self.scaler_line0.textChanged.connect(self.change_value0)
        self.scaler_line1.textChanged.connect(self.change_value1)

        proxy = QtWidgets.QGraphicsProxyWidget()
        proxy.setWidget(self.widget)
        proxy.setParentItem(self)

        super().init_widget()
        
    def change_value0 (self, text):
        
        value0 = int(text.replace(',', '.'))
        self.out_param[0] = value0
        
        self.type_text = "Parameter ({},{})".format(*self.out_param)
        
        self.build()
        
    def change_value1 (self, text):
        
        value1 = int(text.replace(',', '.'))
        self.out_param[1] = value1
        
        self.type_text = "Parameter ({},{})".format(*self.out_param)
        
        self.build()
