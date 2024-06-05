
#------------------------- Vertex class -------------------------
class Vertex():
    #attributes
    __slots__ = ('element', 'horizon', 'vertical') #'visited')

    def __init__(self, x,  h = 0, v = 0):
        self.element = x
        self.horizon = h
        self.vertical = v

    def elements(self):
        '''Return element associated with this vertex'''
        return self.element
    
    # def __hash__(self):
    #     pass

