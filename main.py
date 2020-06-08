from tkinter import Tk, Label, ttk, Frame, StringVar
from gpsi import gspi_info
from tkintertable import TableCanvas, TableModel


class GPSIFrame(ttk.Frame):

    OPTIONS = [
        "Select the URL you want to check ",
        "all",
        "url1",
        "url2"
        ]
    table_headers = ["URL", "First Contentful Paint", "First Interactive" , "Performance DeskTop", "Performance Mobile"]

    table_content = []
    
    def __init__(self, parent):
        super(GPSIFrame, self).__init__() 
        self.parent = parent
        self.input_section()
        #Table setup
        self.gspi = gspi_info()
           
        
    def image_section(self):
        pass

    def input_section(self):
        pageList =  StringVar(self.parent)
        pageList.set(self.OPTIONS[0])
        label = ttk.Label(self.parent, text="")
        entry = ttk.OptionMenu(self.parent,pageList, *self.OPTIONS )
        accept = ttk.Button(self.parent, text="Accept", width=25, command= lambda : self.quote(pageList.get()))
        TableTitle =  ttk.Label(self.parent, text="URL's Google Page Speed Data")
        #TODO: Add the new window where they can add new URL
        add = ttk.Button(self.parent, text="add", width=10 )
        edit = ttk.Button(self.parent, text="Edit List", width=10)

        label.config(width="30")
        entry.config(width="45")

        label.grid(row=0,column=2)
        entry.grid(row=0, column=3)
        accept.grid(row=0, column=4)
        add.grid(row=0, column=5)
        edit.grid(row=0, column=6)
    
    def quote(self, element):
        if(element == "all"):
            print(element, "all") 
            self.table_section(self.parent) 
            for i in range(len(self.table_content)):                            
                for j in range(len(self.table_content[i])):                            
                    self.table.set(i, j, self.table_content[i][j])
                    #print("row:",i," col:",j, self.table_content[i][j])                   
                    #print(self.table_content[row][col]) 
                    self.table.update_idletasks() 
            self.table.grid(row=1, columnspan=7, pady=10)                    
        else:            
            print(element, "url")            

    def edit_section(self):
        pass


    def table_section(self,parent):         
        self.table_content =  self.gspi.get_full_request()       
        self.table = Table(parent, len(self.gspi.content)+1, len(self.table_headers))
        self.table_content.insert(0, self.table_headers)       


class main_window(ttk.Frame):
    def __init__(self, root):       
        self.root = root
        root.title("Test ")
        #add tab manager
        tabControl =  ttk.Notebook(root)

        GPITab = ttk.Frame(tabControl)
        GConsoleTab = ttk.Frame(tabControl)
        tabControl.add(GPITab, text="GPSI")
        tabControl.pack(expand=1, fill="both")

        GPSIFrame(GPITab)

        

if __name__ == "__main__":
    root = Tk();
    root.geometry("800x300")
    gui = main_window(root);    
    root.mainloop()              