import tkinter as tk
from tkinter.messagebox import showinfo,showerror

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Binomial coefficient')
        self.geometry('400x200')

        ## create widgets
        self.frame = tk.Frame()
        self.labelInfo = tk.Label(self.frame, text='n!/(k!*(n-k)!)', pady=2)
        self.entryUp = tk.Entry(self.frame)
        self.entryDown = tk.Entry(self.frame)
        self.entryUp.insert(0, 6)
        self.entryDown.insert(0, 2)
        self.labelResult = tk.Label(self.frame,text='', padx=2)
        self.buttonEquals = tk.Button(self.frame, text='=', pady=2, padx=20, command=lambda: self.checkInput())
        self.labelN = tk.Label(self.frame, text='n: ')
        self.labelK = tk.Label(self.frame, text='k: ')

        ## position widgets in frame
        self.labelInfo.grid(row=0, column=0, columnspan=3)
        self.labelN.grid(row=1,column=0)
        self.entryUp.grid(row=1, column=1)
        self.labelK.grid(row=2,column=0)
        self.entryDown.grid(row=2, column=1)
        self.labelResult.grid(row=1, column=2, rowspan=2)
        self.buttonEquals.grid(row=3, column=0, columnspan=3)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        ## bind Enter key to window (pointed by self)
        self.bind('<Return>', lambda x: self.checkInput())

    def checkInput(self,event=None):
        noError=True

        ## check if inputs ar positive intigers
        try:
            n = int(self.entryUp.get())
            if n<0:
                raise ValueError
        except (ValueError):
            noError=False
            tk.messagebox.showerror('Error', 'n must be a positive intiger')

        try:
            k = int(self.entryDown.get())
            if k<0:
                raise ValueError
        except (ValueError):
            noError=False
            tk.messagebox.showerror('Error', 'k must be a positive intiger')

        ## check if n<k
        if noError and n<k:
            noError=False
            tk.messagebox.showerror('Error', 'k must be smaller or equal ')

        ## do the math
        if noError:
            ## case of (0 0), (1 0), (n 1)
            if k in (0,1):
                if n==0:
                    self.labelResult['text']=1
                else:
                    self.labelResult['text']=n
            ## default
            else:
                self.countNewton(n,k)

    def countNewton(self,n,k):
        ## multiply list element-wise
        def elementMultiply(l):
            out=1;
            for element in l:
                out*=element
            return out

        nList=[num for num in range(2,n+1)]
        kList=[num for num in range(2,k+1)]
        nMinusKList=[num for num in range(2,(n-k)+1)]

        ## delete the bigger list from n and count the coefficient
        if len(kList)>len(nMinusKList):
            nList=[num for num in nList if num not in kList]
            result = elementMultiply(nList)/elementMultiply(nMinusKList)
        else:
            nList=[num for num in nList if num not in nMinusKList]
            result = elementMultiply(nList)/elementMultiply(kList)

        self.labelResult['text'] = int(result)



if __name__=='__main__':
    app = App()
    app.mainloop()