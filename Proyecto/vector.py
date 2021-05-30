import collections
import math

class vector(collections.Sequence):
    PRECISION = 6
    __slots__ = ('_x', '_y', '_hash')

    def __init__(self, x, y):
        self._hash = None
        self._x = round(x, self.PRECISION)
        self._y = round(y, self.PRECISION)
# constructor vector, parametros x, y

    @property #get x
    def x(self):
        return self._x

    @x.setter #set x
    def x(self, value):
        if self._hash is not None:
            raise ValueError('no puede settear x')
        self._x = round(value, self.PRECISION)

    @property #get y
    def y(self):
        return self._y

    @y.setter #set y
    def y(self, value):
        if self._hash is not None:
            raise ValueError('no puede settear y')
        self._y = round(value, self.PRECISION)


    def __hash__(self):
        #val (x,y)
        if self._hash is None:
            pair = (self.x, self.y)
            self._hash = hash(pair)
        return self._hash

    def __len__(self):
        #longitud vec (x,y)=2
        return 2

    def __getitem__(self, index):
        #get1= x ; get2=y
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        raise IndexError

    def copy(self):
        #copia el vector
        type_self = type(self)
        return type_self(self.x, self.y)

    def __eq__(self, other): #collision
        if isinstance(other, vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def _iadd_(self, other):
        #suma al parametro x o y un valor ( mueve el vector)
        if self._hash is not None:
            raise ValueError('no se puede mover el vector')
        if isinstance(other, vector):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other
        return self

    def move(self, other):
        #mueve el vector
        self._iadd_(other)

    def desAcelerattion(self): #desaceleracion XY
        if(self.x>1 and self.x<5):
            self.x-=1
        if(self.x<-1 and self.x>-5):
            self.x+=1
        if(self.y>1 and self.y<5):
            self.y-=1
        if(self.y<-1 and self.y>-5):
            self.y+=1

    def Acelerattion(self): #aceleración XY
        if(self.x>=1 and self.x<4):
            self.x+=1
        if(self.x<=-1 and self.x>-4):
            self.x-=1
        if(self.y>=1 and self.y<4):
            self.y+=1
        if(self.y<=-1 and self.y>-4):
            self.y-=1
        
    def rotate(self, angle):
        #rota el vector tantos grados
        if self._hash is not None:
            raise ValueError('no se puede rotar el vector')
        radians = angle * math.pi / 180.0
        cosine = math.cos(radians)
        sine = math.sin(radians)
        x = self.x
        y = self.y
        self.x = x * cosine - y * sine
        self.y = y * cosine + x * sine
        print(self.x)
        print(self.y)
        
        