from PySide6.QtCore import Qt, QObject
from node_editor.gui.pin_graphics import Pin_Graphics



class Pin(Pin_Graphics, QObject):
    #PinChanging = pyqtSignal(object)
    def __init__(self, parent, scene):
        super().__init__(parent, scene)

        self.name = None
        self.node = None
        self.connection = None
        self.pintype = None
        
    def pinName(self):
        return self.name

    def set_execution(self, execution):
        self.execution = execution
        super().set_execution(execution)
    
    def set_pintype(self, pintype):
        self.pintype = pintype

    def set_name(self, name):
        self.name = name
        super().set_name(name)

    def clear_connection(self):
        if self.connection:
            self.connection.delete()

    def can_connect_to(self, pin):
        if not pin:
            return False
        if pin.node == self.node:
            return False
        if pin.pintype != self.pintype:
            return False

        return self.is_output != pin.is_output

    def is_connected(self):
        return bool(self.connection)
    
    # @property()
    # def connexionChange(self):
    #     return  bool(self.connection)
    
    # @connexionChange.setter
    # def connexionChange(self,value):
    #     self.connexion = value
        # self.PinChanging.emit()
    
    def emit_connection_changed(self):
        print('emission')
        self.clicked.emit(self.is_connected())
        print('ok emit')
        
    def changeValue (self, Pin, Node):
        print('azefdzgrqhejhdkntlfj')
        
    def update_pin_node(self):
        print(self.name)   # nom du pin du node input
        newConnexion = self.connection
        start_node, end_node = newConnexion.nodes()
        end_node.btn_cmd()
        
    def get_all_fct(self):
        
        order = []
        anode = self.node
        order.append(anode)
        if self.is_connected():
            connect = self.connection
            start_node, end_node = connect.nodes()
            order.append(start_node.execute())
            return order
        else :
            return order
        pass

    def get_data(self, default):
        # Get a list of nodes in the order to be computed. Forward evaluation by default.
        
        def get_node_compute_order(node, forward=False):
            # # Create a set to keep track of visited nodes
            # visited = set()
            # # Create a stack to keep track of nodes to visit
            # stack = [node]
            # # Create a list to store the evaluation order
            # order = []
            pass

        
        def get_next_input_node(node):
            pass
        
        def get_next_output_node(node):
            pass
        
        # Get the next nodes that this node is dependent on
        def get_next_param_node(node):
            print('get_next_param_node')
            con = self.connection
            print(con)
            if self.is_connected() :
                start_node, end_node = con.nodes()
                print(start_node.out_param)
                return start_node.out_param
            else :
                return default

        # Get the next nodes that is affected by the input node.
        def get_next_size_node(node):
            print('get_next_param_node')
            con = self.connection
            print(con)
            if self.is_connected() :
                start_node, end_node = con.nodes()
                print(start_node.out_size)
                return start_node.out_size
            else :
                return default

        # if pin isn't connected, return it current data
        if self.execution == False :
            print('pin parametre')
            return get_next_param_node(self)
        if self.execution == True :
            print('pin exe')
            return get_next_size_node(self)
        
        # get the evalutation order of the owning node of the pin

        # loop over each node and process it

        # return the pin's data
