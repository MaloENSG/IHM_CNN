from PySide6 import QtWidgets

from node_editor.node import Node

def unwrape_list(node_list):
    """unwrape the embeded list
    

    Parameters
    ----------
    node_list : list
        embeded list 

    Returns
    -------
    unwraped : list
        normal list of the nodes in the node editor 

    """
    unwraped = []
    for node in node_list :
        if type(node) == list :
            unwraped.extend(unwrape_list(node))
        else :
            unwraped.append(node)
    return unwraped

class Run_Node(Node):
    def __init__(self):
        super().__init__()

        self.title_text = "Run "
        self.type_text = "Output "
        self.set_color(title_color=(128, 0, 0))

        self.add_pin(name="Input", pintype="data", is_output=False, execution=True)

        self.build()
        
    def execute(self):
        print('def create_model():\n\t"""\n\tmodel created with IHM_CNN\n\t"""')
        pinIn = self.get_pin("Input")
        order_nodes = pinIn.get_all_fct()
        all_node = unwrape_list(order_nodes)
        # print(len(all_node))
        for node in reversed(all_node) :
            node.write_fct()
        
    def write_fct(self):
        code = '\treturn model'
        print(code)

    def init_widget(self):
        self.widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        btn = QtWidgets.QPushButton("Execute")
        btn.clicked.connect(self.btn_cmd)
        layout.addWidget(btn)
        self.widget.setLayout(layout)

        proxy = QtWidgets.QGraphicsProxyWidget()
        proxy.setWidget(self.widget)
        proxy.setParentItem(self)

        super().init_widget()

    def btn_cmd(self):
        print("btn command")
        self.execute()
