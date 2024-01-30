# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 09:36:59 2023

@author: UTILISATEUR
"""
from PySide6 import QtWidgets
#import sys
#sys.path.insert(1, 'D:\Desktop\ENSG\ING3 Cours\Projet info\test node editor\python-node-editor-master\node_editor')
#from node_editor.node import Node

from node_editor.node import Node
from node_editor.common import Node_Status


class Conv2D_Node(Node):
    def __init__(self):
        super().__init__()
        
        self.in_size = [None, 0, 0, 0]
        self.out_size = [None, 0, 0, 0]

        # Viz
        self.title_text = "Conv2D"
        self.type_text = "Layer ({},{},{},{})".format(*self.out_size)
        self.set_color(title_color=(128, 128, 128))

        # Pins
        self.add_pin(name="Input", pintype="data", is_output=False, execution=True)
        self.add_pin(name="Output", pintype="data", is_output=True, execution=True)

        self.add_pin(name="Filters", pintype="int", is_output=False)
        self.add_pin(name="Kernel size", pintype="list2", is_output=False)
        self.add_pin(name="Activation", pintype="activation", is_output=False)
        
        #Parameters
        self.filters = 32
        self.kernel_size = (3, 3)
        self.activation = 'relu'
        
        self.build()
        
    def execute(self):
        pinIn = self.get_pin("Input")
        order_node = pinIn.get_all_fct()
        return order_node
    
    def clear_attribut(self):
        
        # Set attributes and sizes to default
        self.filters = 32
        self.kernel_size = (3, 3)
        self.activation = 'relu'
        
        self.in_size = [None, 0, 0, 0]
        self.out_size = [None, 0, 0, 0]
    
    def update_validity(self):
        pinIn = self.get_pin("Input")
        self.in_size = pinIn.get_data(self.in_size)
        self.update_out_size()
        
        if not pinIn.is_connected():
            self.status = Node_Status.DIRTY
            return False
        elif len(self.in_size) !=4 :
            self.status = Node_Status.ERROR
            return False
        elif self.out_size[1] <= 0 or self.out_size[2] <= 0 or self.out_size[3] <= 0:
            self.status = Node_Status.ERROR
            return False
        elif self.kernel_size[0] <= 0 or self.kernel_size[1] <= 0:
            self.status = Node_Status.ERROR
            return False
        else :
            self.status = Node_Status.CLEAN
            return True

    def update_in_size(self):
        pinIn = self.get_pin("Input")
        self.in_size = pinIn.get_data(self.in_size)
        
    def update_attribut(self):
        # print('Node conv2D update_attribut')
        
        # Get the values from the input pins
        pinF = self.get_pin("Filters")
        pinK = self.get_pin("Kernel size")
        pinA = self.get_pin("Activation")
        
        # Update values (if changed)
        self.filters = pinF.get_data(self.filters)
        self.kernel_size = pinK.get_data(self.kernel_size)
        self.activation = pinA.get_data(self.activation)
        
    def update_out_size(self):
        
        self.out_size[1] = self.in_size[1] - (self.kernel_size[0]//2 * 2)
        self.out_size[2] = self.in_size[2] - (self.kernel_size[1]//2 * 2)
        self.out_size[3] = self.filters
        
    def update_out_size_display(self):
        
        self.type_text = "Layer ({},{},{},{})".format(*self.out_size)
        self.build()
        
    def write_fct(self):
        
        code = '\tx = layers.Conv2D({}, kernel_size=({}, {}), activation="{}")(x)'.format(
            self.filters, self.kernel_size[0], self.kernel_size[1], self.activation)
        print(code)
        
        
    def init_widget(self):
        self.widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        btn = QtWidgets.QPushButton("Button test")
        btn.clicked.connect(self.btn_cmd)
        layout.addWidget(btn)
        self.widget.setLayout(layout)

        proxy = QtWidgets.QGraphicsProxyWidget()
        proxy.setWidget(self.widget)
        proxy.setParentItem(self)

        super().init_widget()

    def btn_cmd(self):
        # print("Methode command")
        valid = self.update_validity()
        print(valid)
        if valid :
            self.update_in_size()
            self.update_attribut()
            self.update_out_size()
            self.update_out_size_display()
            self.write_fct()
        
        self.build()
        
