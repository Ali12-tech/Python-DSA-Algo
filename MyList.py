import ctypes

class MyList:
    def __init__(self):
        self.size = 1
        self.n = 0 
        self.A = self.__make_array(self.size)

    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()

    def __len__(self):
        return self.n

    def __resize(self,new_capacity):
        B = self.__make_array(new_capacity)
        self.size = new_capacity

        for i in range(self.n):
            B[i] = self.A[i]

        self.A = B

    def append(self,value):
        if self.size == self.n:
            self.__resize(self.size*2)

        self.A[self.n] = value
        self.n += 1

    def __str__(self):

        result = ""
        for i in range(self.n):
            result = result + str(self.A[i]) + ","


        return '['+result[:-1]+']' 


    def __getitem__(self,index):
        if isinstance(index,slice):
            start, stop, step = index.start, index.stop, index.step
            if index.start == None:
                start = 0
            if index.stop == None:
                stop = self.n
            if index.step == None:
                step = 1

            result = MyList()
            for i in range(start,stop,step):
                result.append(self.A[i])
            return result
        else:
            if index < 0:
                index = self.n + index

            if 0<= index < self.n:
                return self.A[index]
        
            raise IndexError("Item Not Found")


    def pop(self):
        if self.n == 0:
            return "Empty List"
        
        print(self.A[self.n-1])
        self.n = self.n - 1

    def clear(self):
        self.size = 1
        self.n = 0

        
    def find(self,item):
        
        for i in range(self.n):
            if self.A[i] == item:
                return i
        
        return "Item not found"


    def insert(self,index,item):

        if self.size == self.n:
            self.__resize(self.size*2)

        for i in range(self.n,index,-1):
            self.A[i] = self.A[i-1]

        self.A[index] = item
        self.n += 1



    def __delitem__(self,pos):
        if 0<=  pos < self.n:
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]

            self.n -= 1

    def remove(self,item):
        pos = self.find(item)

        if type(pos) == int:
            return self.__delitem__(pos)
        else:
            return pos            


    def sort(self):
        
        for i in range(self.n):
            for k in range(0,self.n-i-1):
                if self.A[k] > self.A[k+1]:
                    self.A[k],self.A[k+1] = self.A[k+1],self.A[k]

            
    def min(self):
        if self.n == 0:
            raise ValueError("Empty List")

        min_value = self.A[0]

        for i in range(1,self.n):
            if self.A[i] < min_value:
                min_value = self.A[i]

        return min_value


    def sum(self):

        if self.n == 0:
            raise ValueError("List Empty")

        data = self.A[0]

        for i in range(1,self.n):
            data += self.A[i]


        return data

            
    def extend(self,extension_value):

        if extension_value is None:
            raise ValueError("extension value can not be None")

        new_size = self.n + extension_value

        if new_size > self.size:
            self.__resize(new_size)

        for i in range(new_capacity):
            self.append(extension_value)


    def merg_array(self,new_array):
        if self.n == 0:
            raise ValueError("Array do not exist")

        for item in new_array:
            self.append(item)

        return str(self)

    



    

        
            
        

             





        










        


