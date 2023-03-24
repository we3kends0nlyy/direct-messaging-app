import tkinter as tk
from tkinter import ttk, filedialog
from typing import Text
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
import tkinter
import os
import re
from tkinter import messagebox
from tkinter import *
import user
from Profile import *
import ds_messenger
from ds_messenger import DirectMessenger
from ds_protocol import SaveFilePath
import ds_client
import datetime


def os_error():
    new_wind = Toplevel()
    new_wind.geometry("250x125+460+235")
    new_wind.title("Error!")
    er_msg = Label(new_wind, text="Please choose a viable \nfolder to store your profile.").pack(pady=10)
    close = Button(new_wind, text="Ok", command=new_wind.destroy).pack(pady=10)

def os_error():
    new_wind = Toplevel()
    new_wind.geometry("250x125+460+235")
    new_wind.title("Error!")
    er_msg = Label(new_wind, text="Invalid entry.").pack(pady=10)
    close = Button(new_wind, text="Ok", command=new_wind.destroy).pack(pady=10)

def connection_error():
    new_wind = Toplevel()
    new_wind.geometry("350x150+460+235")
    new_wind.title("Error!")
    er_msg = Label(new_wind, text="Connection error. Invalid IP.").pack(pady=10)
    
    close = Button(new_wind, text="Ok", command=new_wind.destroy).pack(pady=10)

def invalid_server():
    pass

def user_error():
    new_wind = Toplevel()
    new_wind.geometry("250x150+460+235")
    new_wind.title("Error!")
    er_msg = Label(new_wind, text="This username is taken already. \nPlease choose a new one.").pack(pady=10)
    close = Button(new_wind, text="Ok", command=new_wind.destroy).pack(pady=10)

def user_error2():
    new_wind = Toplevel()
    new_wind.geometry("375x188+460+235")
    new_wind.title("Error!")
    er_msg = Label(new_wind, text="Once you create a profile,\n you cannot change the password.\n Or the username you\n chose already exists.\nYour change was not saved.").pack(pady=10)
    close = Button(new_wind, text="Ok", command=new_wind.destroy).pack(pady=10)

def space_error():
    new_wind = Toplevel()
    new_wind.geometry("350x150+460+235")
    new_wind.title("Error!")
    er_msg = Label(new_wind, text="Username/password can't have spaces.").pack(pady=10)
    close = Button(new_wind, text="Ok", command=new_wind.destroy).pack(pady=10)

def profile_load_error():
    new_wind = Toplevel()
    new_wind.geometry("350x150+460+235")
    new_wind.title("Error!")
    er_msg = Label(new_wind, text="Please load a profile first.").pack(pady=10)
    close = Button(new_wind, text="Ok", command=new_wind.destroy).pack(pady=10)

class Body(tk.Frame):
    def __init__(self, root, recipient_selected_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._contacts = [str]
        self._select_callback = recipient_selected_callback
        self._draw()

    def node_select(self, event):
        try:
            index = int(self.posts_tree.selection()[0])
            entry = self._contacts[index]
            if self._select_callback is not None:
                self._select_callback(entry)
                #self.entry_editor.delete('1.0', tk.END)
        except IndexError:
            pass

    def del_conts(self):
        self.posts_tree.delete(*self.posts_tree.get_children())
        for x in self._contacts:
            self._contacts.remove(x)

    def insert_contact2(self, contact: str):
        self._contacts.append(contact)
        id = len(self._contacts) - 1
        self._insert_contact_tree(id, contact)

    def _insert_contact_tree(self, id, contact: str):
        if len(contact) > 25:
            entry = contact[:24] + "..."
        id = self.posts_tree.insert('', id, id, text=contact)


    def insert_contact(self, contact: str, path):
        if contact is None or len(contact) == 0:
            return False
        else:
            try:
                if len(path) > 0:
                    assign = Profile()
                    assign.load_profile(path)
                    if contact not in assign.contacts and " " not in contact:
                        self._contacts.append(contact)
                        id = len(self._contacts) - 1
                        self._insert_contact_tree(id, contact)
                    else:
                        pass
            except (NameError, TypeError):
                profile_load_error()
            '''
                try:
                    if len(dsu_file) > 0:
                        assign = Profile()
                        assign.load_profile(dsu_file)
                        if contact not in assign.contacts and " " not in contact:
                            self._contacts.append(contact)
                            id = len(self._contacts) - 1
                            self._insert_contact_tree(id, contact)
                        else:
                            pass
                except (NameError, TypeError):
                    profile_load_error()
            '''

    def insert_user_message(self, message:str, recip, time):
        '''
        This method inserts messages that the user has sent outward to other users.
        '''
        self.entry_editor.insert(1.0, time + '\n' + 'Sent to: ' + recip + '\n' + 'Message: ' +  message + '\n', 'entry-right')

    def insert_contact_message(self, message:str, usr, time):
        '''
        This method inserts messages that the user has received from other users.
        '''
        self.entry_editor.insert(1.0, time + '\n' + 'From: ' + usr + '\n' +  'Message: ' + message + '\n', 'entry-left')

    def get_text_entry(self) -> str:
        return self.message_editor.get('1.0', 'end').rstrip()

    def set_text_entry(self, text:str):
        self.message_editor.delete(1.0, tk.END)

    def clear_box(self):
        self.entry_editor.delete(1.0, tk.END)

    def _draw(self):
        posts_frame = tk.Frame(master=self, width=250)
        posts_frame.pack(fill=tk.BOTH, side=tk.LEFT)

        self.posts_tree = ttk.Treeview(posts_frame)
        self.posts_tree.bind("<<TreeviewSelect>>", self.node_select)
        self.posts_tree.pack(fill=tk.BOTH, side=tk.TOP,
                             expand=True, padx=5, pady=5)

        entry_frame = tk.Frame(master=self, bg="")
        entry_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        editor_frame = tk.Frame(master=entry_frame, bg="red")
        editor_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        scroll_frame = tk.Frame(master=entry_frame, bg="blue", width=10)
        scroll_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

        message_frame = tk.Frame(master=self, bg="yellow")
        message_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

        self.message_editor = tk.Text(message_frame, width=0, height=5)
        self.message_editor.pack(fill=tk.BOTH, side=tk.LEFT,
                                 expand=True, padx=0, pady=0)

        self.entry_editor = tk.Text(editor_frame, width=0, height=5)
        self.entry_editor.tag_configure('entry-right', justify='right')
        self.entry_editor.tag_configure('entry-left', justify='left')
        self.entry_editor.pack(fill=tk.BOTH, side=tk.LEFT,
                               expand=True, padx=0, pady=0)

        entry_editor_scrollbar = tk.Scrollbar(master=scroll_frame,
                                              command=self.entry_editor.yview)
        self.entry_editor['yscrollcommand'] = entry_editor_scrollbar.set
        entry_editor_scrollbar.pack(fill=tk.Y, side=tk.LEFT,
                                    expand=False, padx=0, pady=0)


class Footer(tk.Frame):
    def __init__(self, root, send_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._send_callback = send_callback
        self._draw()

    def send_click(self):
        if self._send_callback is not None:
            try:
                if len(file_path1) > 0:
                    self._send_callback()
            except (NameError, TypeError):
                try:
                    if len(dsu_file) > 0:
                        self._send_callback()
                except (NameError, TypeError):
                    
                    profile_load_error()

    def _draw(self):
        save_button = tk.Button(master=self, text="Send", width=20, command=self.send_click)
        save_button.pack(fill=tk.BOTH, side=tk.RIGHT, padx=5, pady=5)

        self.footer_label = tk.Label(master=self, text="Ready.")
        self.footer_label.pack(fill=tk.BOTH, side=tk.LEFT, padx=5)


class NewContactDialog(tk.simpledialog.Dialog):
    def __init__(self, root, title=None, user=None, pwd=None, server=None, files_pp=None):
        self.root = root
        self.server = server
        self.user = user
        self.pwd = pwd
        self.file_p = files_pp
        super().__init__(root, title)

    def body(self, frame):
        self.server_label = tk.Label(frame, width=30, text="DS Server Address")
        self.server_label.pack()
        self.server_entry = tk.Entry(frame, width=30)
        self.server_entry.insert(tk.END, self.server)
        self.server_entry.pack()
        serv = self.server_entry.get()

        self.username_label = tk.Label(frame, width=30, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(frame, width=30)
        self.username_entry.insert(tk.END, self.user)
        self.username_entry.pack()
        
        self.password_label = tk.Label(frame, width=30, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(frame, width=30)
        self.password_entry['show'] = '*'
        self.password_entry.insert(tk.END, self.pwd)
        self.password_entry.pack()


    def apply(self):
        self.user = self.username_entry.get()
        self.pwd = self.password_entry.get()
        self.server = self.server_entry.get()
        assign = Profile()
        assign.load_profile(self.file_p)
        assign.username = self.user
        assign.password = self.pwd
        assign.dsuserver = self.server
        assign.save_profile(self.file_p)

class MainApp(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.username = None
        self.password = None
        self.server = None
        self.file_path = None
        self.recipient = None
        self.t = None
        self.u = None
        self.m = None
        self.after_meth = None
        self._draw()


    def send_message(self):
        msg = self.body.get_text_entry()
        self.body.set_text_entry(msg)
        if len(msg) > 0:
            SaveFilePath(self.file_path)
            self.ds_mess = DirectMessenger(self.server, self.username, self.password)
            self.ds_mess.send(msg, self.recipient)
            assign = Profile()
            assign.load_profile(self.file_path)
            self.body.insert_user_message(msg, self.recipient, str(datetime.datetime.now()))
            pass
        else:
            pass

    def add_contact(self):
        new_cont = tkinter.simpledialog.askstring("New Contact", "Enter a contact.")
        self.body.insert_contact(new_cont, self.file_path)
        assign = Profile()
        if new_cont is None or len(new_cont) == 0:
            return False
        else:
            try:
                if len(self.file_path) > 0:
                    assign.load_profile(self.file_path)
                    try:
                        if new_cont in assign.contacts:
                            new_wind = Toplevel()
                            new_wind.geometry("350x150+460+235")
                            new_wind.title("Reminder!")
                            er_msg = Label(new_wind, text="You have already added that contact.").pack(pady=10)
                            close = Button(new_wind, text="Ok", command=new_wind.destroy).pack(pady=10)
                        elif " " in new_cont:
                            new_wind = Toplevel()
                            new_wind.geometry("350x150+460+235")
                            new_wind.title("Error!")
                            er_msg = Label(new_wind, text="Usernames don't have whitespace.").pack(pady=10)
                            close = Button(new_wind, text="Ok", command=new_wind.destroy).pack(pady=10)
                        else:
                            assign.add_cont1(new_cont)
                            assign.save_profile(self.file_path)
                    except TypeError:
                        pass
            except (NameError, TypeError):
                try:
                    if len(self.file_path) > 0:
                        assign.load_profile(self.file_path)
                        try:
                            if new_cont in assign.contacts:
                                new_wind = Toplevel()
                                new_wind.geometry("350x150+460+235")
                                new_wind.title("Reminder!")
                                er_msg = Label(new_wind, text="You have already added that contact.").pack(pady=10)
                                close = Button(new_wind, text="Ok", command=new_wind.destroy).pack(pady=10)
                            elif " " in new_cont:
                                new_wind = Toplevel()
                                new_wind.geometry("350x150+460+235")
                                new_wind.title("Error!")
                                er_msg = Label(new_wind, text="Usernames don't have whitespace.").pack(pady=10)
                                close = Button(new_wind, text="Ok", command=new_wind.destroy).pack(pady=10)
                            else:
                                assign.add_cont1(new_cont)
                                assign.save_profile(self.file_path)
                        except TypeError:
                            pass
                except (NameError, TypeError):
                    profile_load_error()

    def recipient_selected(self, recipient):
        '''
        Whatever is selected in the treeview should be passed here and made self.recipient. So when a message is sent the code knows that this is the person to send the message to.
        '''
        if recipient != self.recipient:
            self.body.clear_box()
            assign = Profile()
            assign.load_profile(self.file_path)
            #for i in assign.messagees[0]: for the messages right
            
            #for i in assign.messages[1]:  #for messages on the left
            self.recipient = recipient
            ds_client.save_path(self.file_path)
        else:
            pass

    def configure_server(self):
        if self.file_path is not None:
            ud = NewContactDialog(self.root, "Configure Account",
                                  self.username, self.password, self.server, self.file_path)
            x = ds_client.connect(ud.server, 3021, ud.user, ud.pwd, "Testing account...")
            if x is False:
                self.root.after(1000, self.root.after_cancel, self.after_meth)
                assign = Profile()
                assign.load_profile(self.file_path)
                assign.username = self.username
                assign.password = self.password
                assign.dsuserver = self.server
                assign.save_profile(self.file_path)
                user_error2()
            else:
                self.root.after(1000, self.root.after_cancel, self.after_meth)
                self.username = ud.user
                self.password = ud.pwd
                self.server = ud.server
                self.check_new()
        else:
            pass

    def publish(self, message:str):
        pass


    def check_new(self):
        '''
        This method checks for new posts and checks if the user that sent the message is in the contact list of the user that's logged in. This method is triggered when the user opens a new file.
        This method also alerts the new when they've gotten a new message and displays a notification. The user must click on the contact in the treeview to see the full message though. The notification can pop up from any point in the gui though since this check_new is triggered once the file is open so it runs the entire time.
        '''
        try:
            if self.username is not None:
                assign = Profile()
                assign.load_profile(self.file_path)
                ds_client.save_path(self.file_path)
                ds_messenger.save_p(self.file_path)
                ds_mess = DirectMessenger(self.server, self.username, self.password)
                assign.new = []
                assign.save_profile(self.file_path)
                ds_mess.retrieve_new()
                ds_mess.retrieve_all()
                try:
                    assign.load_profile(self.file_path)
                    t = assign.new[0]
                    m = assign.new[1]
                    u = assign.new[2]
                    if len(u) > 0:
                        try:
                            if u in assign.contacts:
                                if u == self.recipient:
                                    self.body.insert_contact_message(m, u, t)
                            else:
                                self.body.insert_contact(u, self.file_path)
                                assign.add_cont1(u)
                                assign.save_profile(self.file_path)
                                if u == self.recipient:
                                    self.body.insert_contact_message(m, u, t)
                        except (NameError, TypeError):
                            pass
                        else:
                            new_wind = Toplevel()
                            new_wind.geometry("250x125+460+235")
                            new_wind.title("Notification!")
                            er_msg = Label(new_wind, text=f"{u} just sent you a message!").pack(pady=10)
                            close = Button(new_wind, text="Ok", command=new_wind.destroy).pack(pady=10)
                            self.body.insert_contact(u, self.file_path)
                except (NameError, TypeError, IndexError):
                    pass
                self.after_meth = self.root.after(800, self.check_new)
        except NameError:
            pass

    def _draw(self):
        menu_bar = tk.Menu(self.root)
        self.root['menu'] = menu_bar
        menu_file = tk.Menu(menu_bar)

        menu_bar.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label='New', command=self.create_new_file)
        menu_file.add_command(label='Open...', command=self.open_filee)
        menu_file.add_command(label='Close', command=self.close_code)

        settings_file = tk.Menu(menu_bar)
        menu_bar.add_cascade(menu=settings_file, label='Settings')
        settings_file.add_command(label='Add Contact',
                                  command=self.add_contact)
        settings_file.add_command(label='Configure DS Server',
                                  command=self.configure_server)

        self.body = Body(self.root,
                         recipient_selected_callback=self.recipient_selected)
        self.body.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.footer = Footer(self.root, send_callback=self.send_message)
        self.footer.pack(fill=tk.BOTH, side=tk.BOTTOM)


    def open_filee(self):
        global file_path1
        file_path1 = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("DSU files", ".dsu"), ("allfiles", "*.*")))
        if len(file_path1) > 0:
            assign = Profile()
            assign.load_profile(file_path1)
            self.username = assign.username
            self.password = assign.password
            self.server = assign.dsuserver
            self.file_path = file_path1
            x = ds_client.connect("168.235.86.101", 3021, self.username, self.password, "Testing account...")
            if x is False:
                user_error2()
            else:
                ds_client.save_path(file_path1)
                contact_lst = assign.contacts
                ds_mess = DirectMessenger(assign.dsuserver, assign.username, assign.password)
                ds_mess.retrieve_all()
                new_list = []
                self.body.del_conts()
                for i in contact_lst:
                    new_list.append(i)
                for new_cont in new_list:
                    self.body.insert_contact2(new_cont)
                self.body.clear_box()
                self.check_new()
        else:
            pass

    def close_code(self):
        main.destroy()

    def create_new_file(self):
        global dsu_file
        dsu_file = filedialog.asksaveasfilename(defaultextension=".dsu", title = "Create New DSU File", filetypes=(("DSU files", ".dsu"), ("All Files", "*.*")))
        if len(dsu_file) > 1:
            main = tk.Tk()
            main.withdraw()
            global input_user
            global input_password
            global input_server
            global save_info
            global root2
            root2 = tk.Tk()
            root2.geometry("325x130+485+200")
            root2.title("Enter your user information.")
            descrip = tk.Label(root2, text="Username:")
            descrip2 = tk.Label(root2, text="Password:")
            descrip3 = tk.Label(root2, text="Server Number:")
            input_user = tk.Entry(root2)
            input_password = tk.Entry(root2)
            input_server = tk.Entry(root2)
            save_info = tk.Button(root2, text="Save", command=self.save_data)
            descrip.grid(row=0, column=0)
            descrip2.grid(row=1, column=0)
            descrip3.grid(row=2, column=0)
            input_user.grid(row=0, column=20)
            input_password.grid(row=1, column=20)
            input_server.grid(row=2, column=20)
            save_info.grid(row=3, column=20)
        else:
            pass


    def save_data(self):
        u = input_user.get()
        p = input_password.get()
        s = input_server.get()
        match = re.search(r' ', u)
        if not match and len(u) > 0:
            match = re.search(r' ', p)
            if not match and len(p) > 0:
                x = ds_client.connect(s, 3021, u, p, "Testing account...")
                if x is False:
                    invalid_server()
                else:
                    x = ds_client.connect("168.235.86.101", 3021, u, p, "Testing account...")
                    if x is False:
                        user_error()
                    else:
                        user.user_asker(dsu_file, u, p, s)
                        self.username = u
                        self.password = p
                        self.server = s
                        self.file_path = dsu_file
                        ds_client.save_path(self.file_path)
                        self.body.clear_box()
                        self.body.del_conts()
                        self.close_q()
                        self.check_new()
            else:
                self.new_window()
        else:
            self.new_window()


    def new_window(self):
        new_wind = Toplevel()
        new_wind.geometry("350x150+460+235")
        new_wind.title("Error")
        er_msg = Label(new_wind, text="Username/password must not contain whitespace.").pack(pady=10)
        close = Button(new_wind, text="Ok", command=new_wind.destroy).pack(pady=10)


    def close_q(self):
        root2.destroy()


if __name__ == "__main__":
    # All Tkinter programs start with a root window. We will name ours 'main'.
    main = tk.Tk()

    # 'title' assigns a text value to the Title Bar area of a window.
    main.title("ICS 32 Distributed Social Messenger")

    # This is just an arbitrary starting point. You can change the value
    # around to see how the starting size of the window changes.
    main.geometry("950x700+188+60")

    # adding this option removes some legacy behavior with menus that
    # some modern OSes don't support. If you're curious, feel free to comment
    # out and see how the menu changes.
    main.option_add('*tearOff', False)

    # Initialize the MainApp class, which is the starting point for the
    # widgets used in the program. All of the classes that we use,
    # subclass Tk.Frame, since our root frame is main, we initialize
    # the class with it.
    app = MainApp(main)

    # When update is called, we finalize the states of all widgets that
    # have been configured within the root frame. Here, update ensures that
    # we get an accurate width and height reading based on the types of widgets
    # we have used. minsize prevents the root window from resizing too small.
    # Feel free to comment it out and see how the resizing
    # behavior of the window changes.
    main.update()
    main.minsize(main.winfo_width(), main.winfo_height())
    #id = main.after(8000, app.check_new)
    #print(id)
    # And finally, start up the event loop for the program (you can find
    # more on this in lectures of week 9 and 10).
    main.mainloop()
