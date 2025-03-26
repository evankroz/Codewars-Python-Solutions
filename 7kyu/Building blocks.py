class Block():
    def __init__(self, arr):
        self.w = arr[0]
        self.l = arr[1]
        self.h = arr[2]
    
    def get_width(self):
        return self.w

    def get_length(self):
        return self.l
    
    def get_height(self):
        return self.h

    def get_volume(self):
        return (self.h*self.w*self.l)
    
    def get_surface_area(self):
        return (2*(self.h*self.w + self.h*self.l + self.w*self.l))