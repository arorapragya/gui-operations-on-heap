# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 20:10:05 2020

@author: User
"""


from tkinter import Tk,Label,Button,Entry,Listbox,END

def heapify(arr, n, i):
    largest = i; # Initialize largest as root 
    l= 2 * i + 1; # left = 2*i +1 
    r= 2 * i + 2; # right = 2*i + 2 
    if l < n and int(arr[l]) > int(arr[largest]): 
        largest = l; 
    if r < n and int(arr[r])> int(arr[largest]): 
        largest = r; 
    if largest != i: 
        arr[i], arr[largest] = arr[largest], arr[i]; 
        heapify(arr,n,largest)
        

        
def buildHeap(arr, n): 
    startIdx=get_parent(arr,n) 
    for i in range(startIdx, -1, -1): 
        heapify(arr, n, i)


def insertion(ARR,val,n):
    ARR.append(val)
    n+=1
    buildHeap(ARR,n)     #doesn't work otherwise
    return n

#deletion
def print_nh(win):
        mywin.l13=Label(win,text='New heap is')
        mywin.l13.place(x=20,y=60)
        mywin.t5=Entry(win)
        mywin.t5.place(x=110,y=60)
        mywin.t5.delete(0,END)
        mywin.t5.insert(0,mywin.heap)

        
#PRIOIRTY QUEUE CODES!!!!!
# function to get the parent of a node of a tree
def get_parent(A, index):
        a=int((index+1)/2)-1
        if a<0:
            a=0
        return a
    
def heapify2(arr, i, n):            #for priority queue
    largest = i; # Initialize largest as root 
    l=2*i+1 # left = 2*i + 1 
    r=2*i+2; # right = 2*i + 2 
    if l<n and arr[l]>arr[largest]: 
        largest = l; 
    if r<n and arr[r]>arr[largest]: 
        largest = r; 
    if largest != i: 
        arr[i], arr[largest] = arr[largest], arr[i]; 
        heapify2(arr,largest,n)


def build_max_heap(A,n):
    for i in range(n//2, -1, -1):
        heapify2(A,i,n)
    return A
        
def maximum(A):
  return A[0]

def extract_max(A,n):
    maxx=A[0]
    A[0]=A[n-1]
    n-=1
    heapify2(A,0,n)
    A.remove(A[n-1])
    return maxx,n

def increase_key(A, index, key,n):
    A[index]=key
    while index>0 and int(A[get_parent(A, index)])<int(A[index]):
        print(index,get_parent(A, index))
        A[index],A[get_parent(A, index)]=A[get_parent(A, index)], A[index]
        index=get_parent(A,index)

def decrease_key(A, index, key,n):
    A[index]=key
    A=build_max_heap(A,n)
        

def insert(A,key,n):
    A.append(-1)
    increase_key(A,n,key,n)
    n+=1
    return n

def priority_queue(h,n):
    class MyWindow2: 
        def __init__(self,win):
            
            self.heap=h
            self.n=n
            #layout of opening window
            self.l3=Label(win,text='Select Menu')
            self.l4=Label(win,text='Option')   
                 
            #making menu option list
            self.lb=Listbox(win, height=6, selectmode='single')
            menu_op=['Insert','Extract Maximum','Increase Key','Decrease Key','Print heap','Exit']
            for x in menu_op:
                self.lb.insert(END,x)
            self.b2=Button(win,text='Submit',command=self.menu_selection)
            
            #locations 
            self.l3.place(x=20,y=50)
            self.l4.place(x=30,y=80)
            self.lb.place(x=150,y=50)
            self.b2.place(x=100,y=170)
            
            win.geometry("400x300+10+10")
        def build_heap(self):
            self.t2.delete(0, 'end')
            self.heap=self.t1.get().split()
            self.n=len(self.heap)
            self.heap=build_max_heap(self.heap,self.n)
            self.t2.insert(END,self.heap)
        
        def insert_2(self):
            self.t4.delete(0,'end')
            key=inself.t3.get()
            self.n=insert(self.heap,key,self.n)
            self.t4.insert(END,self.heap)
            
        def extract(self):
            maxx,self.n=extract_max(self.heap,self.n)  
            self.t5.delete(0,'end')
            self.t6.delete(0,'end')
            self.t5.insert(END,maxx)
            self.t6.insert(END,self.heap)
            
        def increase(self):
            self.t9.delete(0,'end')
            key=self.t7.get()
            index=int(self.t8.get())
            increase_key(self.heap,index,key,self.n)
            self.t9.insert(END,self.heap)
            
        def decrease(self):
            self.t12.delete(0,'end')
            key=self.t10.get()
            index=int(self.t11.get())
            decrease_key(self.heap,index,key,self.n)
            self.t12.insert(END,self.heap)
            
        def print_h(self):
            self.t13.delete(0,'end')
            self.t13.insert(END,self.heap)
                
        def menu_selection(self):
            ch=self.lb.curselection()
            ch=int(ch[0])
            if ch==0:
                win1=Tk()
                win1.title("Insert")
                self.l5=Label(win1,text='Enter element to be inserted').place(x=50,y=20)
                self.t3=Entry(win1)
                self.b3=Button(win1,text='Submit',command=self.insert_2).place(x=200,y=45)
                self.t4=Entry(win1)
                self.l6=Label(win1,text='New heap is').place(x=50,y=80)
                self.b4=Button(win1,text='Back',command=win1.destroy).place(x=280,y=150)
                self.t3.place(x=220,y=20)
                self.t4.place(x=220,y=80)
                win1.geometry("400x300+10+10")
                
            if ch==1:
                win2=Tk()
                win2.title("Extract Maximum")
                self.b5=Button(win2,text='Extract',command=self.extract).place(x=100,y=20)
                self.l7=Label(win2,text='The maximum is').place(x=50,y=70) 
                self.t5=Entry(win2)
                self.l8=Label(win2,text='New heap is').place(x=50,y=100)
                self.t6=Entry(win2)
                self.b6=Button(win2,text='Back',command=win2.destroy).place(x=280,y=170)
                self.t5.place(x=220,y=70)
                self.t6.place(x=220,y=100)
                win2.geometry("400x300+10+10")
                
            if ch==2:
                win3=Tk()
                win3.title("Increase Key")
                self.l8=Label(win3,text='Enter increased value').place(x=50,y=20)
                self.l9=Label(win3,text='Enter index').place(x=50,y=50)
                self.t7=Entry(win3)
                self.t8=Entry(win3)
                self.b7=Button(win3,text='Submit',command=self.increase).place(x=200,y=80)
                self.t9=Entry(win3)
                self.l10=Label(win3,text='New heap is').place(x=50,y=120)
                self.b8=Button(win3,text='Back',command=win3.destroy).place(x=280,y=150)
                self.t7.place(x=220,y=20)
                self.t8.place(x=220,y=50)
                self.t9.place(x=220,y=120)
                win3.geometry("400x300+10+10")
                
            if ch==3:
                win4=Tk()
                win4.title("Decrease Key")
                self.l11=Label(win4,text='Enter decreased value').place(x=50,y=20)
                self.l12=Label(win4,text='Enter index').place(x=50,y=50)
                self.t10=Entry(win4)
                self.t11=Entry(win4)
                self.b9=Button(win4,text='Submit',command=self.decrease).place(x=200,y=80)
                self.t12=Entry(win4)
                self.l13=Label(win4,text='New heap is').place(x=50,y=120)
                self.b10=Button(win4,text='Back',command=win4.destroy).place(x=280,y=150)
                self.t10.place(x=220,y=20)
                self.t11.place(x=220,y=50)
                self.t12.place(x=220,y=120)
                win4.geometry("400x300+10+10")
                
            if ch==4:
                win5=Tk()
                win5.title("Print Heap")
                self.b10=Button(win5,text='Print',command=self.print_h).place(x=100,y=20)
                self.l14=Label(win5,text='The heap is').place(x=50,y=70) 
                self.t13=Entry(win5)
                self.b11=Button(win5,text='Back',command=win5.destroy).place(x=280,y=110)
                self.t13.place(x=220,y=70)
                win5.geometry("400x300+10+10")
                
            if ch==5:
                return self.heap
                return self.n
                window2.destroy()
            
    window2=Tk()
    mywin2=MyWindow2(window2)
    mywin2.title('Priority Queue')
    mywin2.geometry("400x300+10+10")
    mywin2.mainloop() 
    
    

#PRIORITY QUEUE DONE






class MyWindow:
    
    def __init__(self,win):
        self.heap=[]
        self.n=0
        #layout of opening window
        self.l1=Label(win, text='Enter elements')
        self.t1=Entry()
        self.b1=Button(win,text='Submit',command=self.build_heap)
        self.l2=Label(win,text='Heap is')
        self.t2=Entry()
        self.l3=Label(win,text='Select Menu')
        self.l4=Label(win,text='Option')   
             
        #making menu option list
        self.lb=Listbox(win, height=6, selectmode='single')
        menu_op=['Insertion','Deletion','Search','Find top k values','Priority Queues','Exit']
        for x in menu_op:
            self.lb.insert(END,x)
        self.b2=Button(win,text='Submit',command=self.menu_selection)
        
        #locations
        self.l1.place(x=50,y=0)
        self.t1.place(x=150,y=0)
        self.b1.place(x=100,y=20)
        self.l2.place(x=50,y=60)
        self.t2.place(x=150,y=60)
        self.l3.place(x=50,y=130)
        self.l4.place(x=57,y=150)
        self.lb.place(x=150,y=130)
        self.b2.place(x=100,y=230)
    
    
    
        
        
    def insert(self):
        self.t4a.delete(0,'end')
        key=int(self.t3a.get())
        self.n=insertion(self.heap,key,self.n)
        self.t4a.insert(END,self.heap)
    

    def build_heap(self):
        self.t2.delete(0, 'end')
        self.heap=self.t1.get().split()
        self.n=len(self.heap)
        buildHeap(self.heap,self.n)   ##changed to buildHEap
        self.t2.insert(END,self.heap)
        
    
    def search(self):
        self.a2.delete(0,'end')
        val=self.a1.get()
        for i in range(self.n):
            if self.heap[i]==val:
                index=i
                break
        self.a2.insert(END,index)
                                         

    def menu_selection(self):
            
            ch=self.lb.curselection()
            ch=int(ch[0])
            
            if ch==0:
                win2=Tk()
                win2.title("Insertion")
                self.l5a=Label(win2,text='Enter element to be inserted').place(x=50,y=20)
                self.t3a=Entry(win2)
                self.b3a=Button(win2,text='Submit',command=self.insert).place(x=200,y=45)
                self.t4a=Entry(win2)
                self.l6a=Label(win2,text='New heap is').place(x=50,y=80)
                self.b4a=Button(win2,text='Back',command=win2.destroy).place(x=280,y=150)
                self.t3a.place(x=220,y=20)
                self.t4a.place(x=220,y=80)
                #code pending
                win2.geometry("400x300+10+10")
                
            if ch==1:
                win3=Tk()
                win3.title("Deletion")
                for i in range(0,len(self.heap)):
                    self.heap[i]=int(self.heap[i])   
                def heap_del():
                    ele=int(self.a.get())
                    for i in self.heap:
                        if ele==i:
                            self.heap.remove(ele)
                            break
                    self.n-=1
                    buildHeap(self.heap, self.n)
                    print_nh(win3)
                    
                self.l10=Label(win3,text='heap is')
                self.l10.place(x=20,y=1)
                self.t3=Entry(win3)
                self.t3.place(x=70,y=1)
                self.t3.delete(0,END)
                self.t3.insert(0,self.heap)
                self.l11=Label(win3,text='Enter the element to be deleted')
                self.l11.place(x=20,y=30)
                self.a=Entry(win3,width=4)
                self.a.place(x=200,y=30)
                self.b5=Button(win3,text='OK',command=heap_del)
                self.b5.place(x=260,y=30)
                win3.geometry("400x300+10+10")
                self.o2=Button(win3,text="Exit",command=win3.destroy)
                self.o2.place(x=200,y=150)
                
            if ch==2:
                win4=Tk()
                win4.title("Search")
                self.l12=Label(win4,text='Enter the element to be searched')
                self.l12.place(x=20,y=30)
                self.a1=Entry(win4,width=5)
                self.a1.place(x=200,y=30)
                self.b6=Button(win4,text='OK',command=self.search)
                self.b6.place(x=230,y=50)
                self.l13=Label(win4,text='Index of the searched element is')
                self.l13.place(x=20,y=100)
                self.a2=Entry(win4,width=5)
                self.a2.place(x=200,y=100)
                win4.geometry("400x300+10+10")
                self.o3=Button(win4,text="Exit",command=win4.destroy)
                self.o3.place(x=200,y=150)
                
            
            if ch==3:
                win5=Tk()
                win5.title("Top k")
                self.tkv=[]
                self.heap2=self.heap
                for i in range(0,self.n):
                    self.heap2[i]=int(self.heap2[i])
                def number():
                    self.k=int(self.E1.get())
                    if self.k<=self.n:#Condition for finding top k values
                        for i in range(0,self.k):
                            self.tkv.append(self.heap2[0])
                            self.heap2.remove(self.heap2[0])
                            heapify(self.heap2,len(self.heap2),0)
                            
                        self.l2=Label(win5,text="Top k values are ")
                        self.l3=Label(win5,text=self.tkv)
                        self.l2.place(x=20,y=25)
                        self.l3.place(x=110,y=25)
                    else:
                        self.l2=Label(win5,text="Not possible")
                        self.l2.place(x=20,y=25)
                
                        
                win5.geometry("400x300+10+10")
                win5.title("Find top k values")
                self.l1=Label(win5,text="Enter the value of k")
                self.E1=Entry(win5,width=10)
                self.l1.place(x=20,y=1)
                self.E1.place(x=160,y=1)
                self.o=Button(win5,text="OK",command=number)
                self.o.place(x=250,y=1)
                
                self.o1=Button(win5,text="Exit",command=win5.destroy)
                self.o1.place(x=125,y=50)


            if ch==4:
                self.heap,self.n=priority_queue(self.heap,self.n)
                
            if ch==5:
                 window.destroy()
           

window=Tk()
mywin=MyWindow(window)
window.title('Heaps')
window.geometry("400x300+10+10")
window.mainloop() 


