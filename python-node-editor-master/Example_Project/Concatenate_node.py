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



class Concatenate_Node(Node):
    def __init__(self):
        super().__init__()
        
        self.in_size1 = [None, 0, 0, 0]
        self.in_size2 = [None, 0, 0, 0]
        self.out_size = [None, 0, 0, 0]

        # Viz
        self.title_text = "Concatenate"
        self.type_text = "Layer ({},{},{},{})".format(*self.out_size)
        self.set_color(title_color=(128, 128, 128))

        # Pins
        self.add_pin(name="Input 1", pintype="data", is_output=False, execution=True)
        self.add_pin(name="Input 2", pintype="data", is_output=False, execution=True)
        self.add_pin(name="Output", pintype="data", is_output=True, execution=True)

        #Parameters
        
        self.build()
        
    def update_validity(self):
        pinIn1 = self.get_pin("Input 1")
        pinIn2 = self.get_pin("Input 2")
        in1 = pinIn1.get_data(self.in_size1)
        in2 = pinIn2.get_data(self.in_size2)
        
        if not pinIn1.is_connected() or not pinIn2.is_connected() :
            self.status = Node_Status.DIRTY
            return False
        elif len(in1) == len(in2):
            if in1 == in2:
                self.status = Node_Status.CLEAN
                return True
            else :
                self.status = Node_Status.ERROR
        else :
            self.status = Node_Status.ERROR
            return False
        
    def execute(self):
        pinIn1 = self.get_pin("Input 1")
        pinIn2 = self.get_pin("Input 2")
        order_node1 = pinIn1.get_all_fct()
        order_node2 = pinIn2.get_all_fct()
        return [order_node1[0], order_node1[1:], order_node2[1:]]
        
    def update_in_size(self):
        pinIn1 = self.get_pin("Input 1")
        self.in_size1 = pinIn1.get_data(self.in_size1)
        pinIn2 = self.get_pin("Input 2")
        self.in_size2 = pinIn2.get_data(self.in_size2)
        
    def update_attribut(self):
        pass
          
    def update_out_size(self):
        
        self.out_size = self.in_size1
        
    def update_out_size_display(self):
        
        self.type_text = "Layer ({},{},{},{})".format(*self.out_size)
        
    def write_fct(self):
        
        code = '\tx = layers.Concatenate()([x, input_2])'
        
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
        print("btn command")
        valid = self.update_validity()
        print(valid)
        if valid :
            self.update_in_size()
            self.update_attribut()
            self.update_out_size()
            # self.update_out_size_display()
            self.write_fct()
        
        self.build()
        
