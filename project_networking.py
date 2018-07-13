import urllib.request
import socket
import os
import tkinter
import datetime
import pickle

class main_app:
    def __init__(self, parent):
        self.top=parent
        self.top.title('Network Easy v1.1')
        self.top.geometry('400x250')
        self.frame_1=tkinter.Frame(self.top,borderwidth=4,relief='sunken')
        self.frame_1.pack(fill='x',padx=5,pady=5)
        self.label_2_frame_1=tkinter.Label(self.frame_1,text='Enter:',bg='green',fg='white',font=("Helvetica", 10))
        self.label_2_frame_1.pack(side='left',padx=2)

        self.var_entry_1=tkinter.StringVar()                      #### creating a string variable for input
        self.var_disp_1=tkinter.StringVar()                       #### creating a string variable for display
        self.var_error_1=tkinter.StringVar()
        
     
        
        ############## creating entry field #########################

        self.entry_1_frame_1=tkinter.Entry(self.frame_1,textvariable=self.var_entry_1,width=150,fg='white',bg='blue',font=('CONALAS',10))
        self.entry_1_frame_1.pack(side='left',pady=2,padx=2)
        #self.entry_1_frame_1.insert(0,'pls enter')                 ### inserting intial data    

        ####### creating display frame ###########################

        self.frame_2=tkinter.Frame(self.top,borderwidth=2,relief='raised')
        self.frame_2.pack(padx=2,pady=4)
        self.label_2_frame_2=tkinter.Label(self.frame_2,text='Results:',fg='white',bg='green',font=('CONALAS',10))
        self.label_2_frame_2.pack(side='left',padx=2,pady=2) 
        self.label_1_frame_1=tkinter.Label(self.frame_2,textvariable=self.var_disp_1,width=150)
        self.label_1_frame_1.pack(side='left',padx=2)


        
        #################################### get local ip######################################################

        def get_ipaddr():
            
            try:
                tuple1=socket.gethostbyname_ex(socket.gethostname())
                list1=tuple1[2]
        
                if len(list1)==0:             ## empty list no interface connected
                    self.glob_disp_label='no interface connected !!!!'
                
                if len(list1)==1:             ## only one interface 
                    self.glob_disp_label='ip@interface1 :'+list1[0]
        
                if len(list1)==2:             ## only two interface
                    self.glob_disp_label='ip@interface1 :'+list1[0]+' ip@interface2 :'+list1[1]
        
                if len(list1)==3:             ## only three inteface
                    self.glob_disp_label='ip@interface1 :'+list1[0]+' ip@interface2 :'+list1[1]+' ip@interface3 :'+list1[2]
                  
                self.var_disp_1.set(self.glob_disp_label)                                               ## display variable 
            except:
                self.glob_error_label="some error occured during execution ip-address! pls try again"
                self.var_error_1.set('error caused in ip address')                                        ## display error
                
                
        
                                ################ip release##############################
        def ip_release():
            try:
                os.system('ipconfig/release')
                os.system('cls')
                self.var_disp_1.set('success ip relese')

        
            except:
                self.glob_error_label='some error has caused during releasing ip'
                self.var_error_1.set('error caused in ip release')
        
                            ################## ip renew ###################################
        def ip_renew():
            try:
                os.system('ipconfig/renew')
                os.system('cls')
                self.var_disp_1.set('success ip renew')
        
            except:
                self.glob_error_label='some error has been generated during ip renew'
                self.var_error_1.set('error caused in ip renew')
                                                                
                ############################## url fetch ############################

        def url_fetch():
            try:
                                  
                entry_1_get=self.var_entry_1.get()                                 ### some error handling
                if len(entry_1_get)==0:
                    self.var_error_1.set('pls enter address "www.xyz.com"')

                entry_1_get='http://'+entry_1_get
                date_obj=datetime.date.today()
                file_loc=date_obj.strftime('%Y%m%d%H%M%S')+'_urlfetch'+'.html'
                file_obj=open(file_loc,'wb')
                url_obj=urllib.request.urlopen(entry_1_get)
                url_recv=url_obj.read()
                url_recv_decode=url_recv.decode('utf8')
                print(url_recv_decode)                                                                
                pickle.dump(url_recv_decode,file_obj)
                self.var_disp_1.set('url fetch successfull ')


            except:
                print('some error caused in url_fetch')
                #self.var_error_1.set('error caused in url fetch')

        ##################### ip ping #############################################
        def ip_ping():
            try:
                entry_1_get=self.var_entry_1.get()
                if len(entry_1_get)==0:
                    self.var_error_1.set('pls enter address "www.xyz.com"')
                entry_1_get='ping '+entry_1_get
                ping_response=os.system(entry_1_get)
                
                if ping_response==0:                    ### ping response successfull
                    self.var_disp_1.set('host live')
                
                else:
                    self.var_disp_1.set('host not live')
                                
            except:
                print('error caused in ip ping')
                self.var_error_1.set('error caused in ping')

                #######################  n/a #####################################

        def na():
            pass
        
                      

        ############ creating buttons frame and grid   ##################

        self.frame_3=tkinter.Frame(self.top,relief='raised',borderwidth=4)
        self.frame_3.pack(padx=2,pady=4)

        self.button_src=tkinter.Button(self.frame_3,text='URL FETCH',relief='raised',width=13,fg='white',bg='black',command=url_fetch)
        #self.button_src.pack()
        self.button_src.grid(row=0,column=0,padx=2,pady=2)
        
        self.button_ipaddr=tkinter.Button(self.frame_3,text='IP-ADDR',relief='raised',fg='white',bg='black',width=13,command=get_ipaddr,)
        #self.button_ipaddr.pack()
        self.button_ipaddr.grid(row=0,column=1,padx=2,pady=2)

        self.button_iprnw=tkinter.Button(self.frame_3,text='IP-RENEW',relief='raised',fg='white',bg='black',width=13,command=ip_renew)
        #self.button_iprnw.pack()
        self.button_iprnw.grid(row=1,column=0,padx=2,pady=2)

        self.button_iprls=tkinter.Button(self.frame_3,text='IP-RELEASE',relief='raised',fg='white',bg='black',width=13,command=ip_release)
        #self.button_iprls.pack()
        self.button_iprls.grid(row=1,column=1,padx=2,pady=2)

        self.button_ping=tkinter.Button(self.frame_3,text='PING',relief='raised',fg='white',bg='black',width=13,command=ip_ping)
        #self.button_ping.pack()
        self.button_ping.grid(row=2,column=0,padx=2,pady=2)

        self.button_empty=tkinter.Button(self.frame_3,text='N/A',relief='solid',fg='white',bg='black',width=13,command=na)
        #self.button_empty.pack()
        self.button_empty.grid(row=2,column=1,padx=2,pady=2)


        ############### label for showing error########################
        self.frame_4=tkinter.Frame(self.top,relief='sunken',width=150,borderwidth=2)
        self.frame_4.pack(padx=2,pady=9)

        self.label_1_frame_4=tkinter.Label(self.frame_4,textvariable=self.var_error_1,width=100,relief='raised',font=('CONALAS',16),bg='red',fg='white')
        self.var_error_1.set('no error')
        self.label_1_frame_4.pack()


       
top=tkinter.Tk()
main_app(top)
top.update_idletasks()
top.mainloop()


















































'''
self.glob_disp_label=0
self.glob_error_label=0

#################################### get local ip######################################################
def get_ipaddr():
    try:
        tuple1=socket.gethostbyname_ex(socket.gethostname())
        list1=tuple1[2]

        if len(list1)==0:             ## empty list no interface connected
            self.glob_disp_label='no interface connected !!!!'
        
        if len(list1)==1:             ## only one interface 
            self.glob_disp_label='ip@interface1 :'+list1[0]

        if len(list1)==2:             ## only two interface
            self.glob_disp_label='ip@interface1 :'+list1[0]+' ip@interface2 :'+list1[1]

        if len(list1)==3:             ## only three inteface
            self.glob_disp_label='ip@interface1 :'+list1[0]+' ip@interface2 :'+list1[1]+' ip@interface3 :'+list1[2]
        
        print(self.glob_disp_label)

    except:
        self.glob_error_label="some error occured during execution ip-address! pls try again"
        
        

                        ################ip release##############################
def ip_release():
    try:
        os.system('ipconfig/release')
        os.system('cls')
        self.glob_disp_label='successfully ip is release'

    except:
        self.glob_error_label='some error has caused during releasing ip'

                    ################## ip renew ###################################
def ip_renew():
    try:
        os.system('ipconfig/renew')
        os.system('cls')
        self.glob_disp_label='successfully ip is renew'

    except:
        self.glob_error_label='some error has been generated during ip renew'

                      
'''



