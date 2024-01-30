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



class Addproto_Node(Node):
    def __init__(self):
        super().__init__()

        self.title_text = "Add TEST"
        self.type_text = "Logic Nodes"
        self.set_color(title_color=(128, 128, 128))

        self.add_pin(name="Ex In data", is_output=False, execution=True)
        self.add_pin(name="Ex Out data", is_output=True, execution=True)

        self.add_pin(name="input Accccc", is_output=False)
        self.add_pin(name="input Bccccc", is_output=False)
        self.add_pin(name="output", is_output=True)
        self.build()
        
    def execute(self):
        print('execution add proto')
        # Get the values from the input pins
        inA = self.get_pin("input Accccc")
        print('is a', inA.is_connected())
        nameInA = inA.name
        print(nameInA)
        inA.get_data()
        
    # def execute_inputs(self):
    #     pass
    
        
        
    # def test_validity(self):
        
    #     pinA = self._pin
        
    #     print(pinA)
        
        
        
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
        self.execute()
        
