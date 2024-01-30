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



class Flatten_Node(Node):
    def __init__(self):
        super().__init__()
        
        self.in_size = [None, 0, 0, 0]
        self.out_size = [None, 0]

        # Viz
        self.title_text = "Flatten"
        self.type_text = "Layer ({},{})".format(*self.out_size)
        self.set_color(title_color=(128, 128, 128))

        # Pins
        self.add_pin(name="Input", pintype="data", is_output=False, execution=True)
        self.add_pin(name="Output", pintype="data", is_output=True, execution=True)
        
        #Parameters
        
        self.build()
        
    def execute(self):
        pinIn = self.get_pin("Input")
        order_node = pinIn.get_all_fct()
        return order_node
        
    def update_in_size(self):
        pinIn = self.get_pin("Input")
        self.in_size = pinIn.get_data(self.in_size)
        
    def update_attribut(self):
        print('\t\tFlatten execution')
        # Get the Input
        pinIn = self.get_pin("Input")
        
        #if pinF.is_connected():
        self.in_size = pinIn.get_data(self.in_size)
          
        
    def update_out_size(self):
        
        # get input shape
        
        self.out_size[1] = self.in_size[1]*self.in_size[2]*self.in_size[3]
        self.type_text = "Layer ({},{})".format(*self.out_size)
        
        self.build()
        
    def write_fct(self):
        
        code = '\tx = layers.Flatten()(x)'
        
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
        self.update_in_size()
        self.update_attribut()
        self.update_out_size()
        self.write_fct()
        self.execute()
        
