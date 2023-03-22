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
from ds_messenger import DirectMessenger
from ds_protocol import SaveFilePath
import ds_client


class Body(tk.Frame):
    def __init__(self, root, recipient_selected_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._contacts = [str]
        self._select_callback = recipient_selected_callback
        # After all initialization is complete,
        # call the _draw method to pack the widgets
        # into the Body instance
        self._draw()

    def node_select(self, event):
        index = int(self.posts_tree.selection()[0])
        entry = self._contacts[index]
        if self._select_callback is not None:
            self._select_callback(entry)

    def insert_contact(self, contact: str):
        self._contacts.append(contact)
        id = len(self._contacts) - 1
        self._insert_contact_tree(id, contact)

    def _insert_contact_tree(self, id, contact: str):
        if len(contact) > 25:
            entry = contact[:24] + "..."
        id = self.posts_tree.insert('', id, id, text=contact)

    def insert_user_message(self, message:str):
        self.entry_editor.insert(1.0, message + '\n', 'entry-right')

    def insert_contact_message(self, message:str):
        self.entry_editor.insert(1.0, message + '\n', 'entry-left')

    def get_text_entry(self) -> str:
        return self.message_editor.get('1.0', 'end').rstrip()

    def set_text_entry(self, text:str):
        self.message_editor.delete(1.0, tk.END)
        self.message_editor.insert(1.0, text)

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
            self._send_callback()
            #self.send_message()
            

    def _draw(self):
        save_button = tk.Button(master=self, text="Send", width=20, command=self.send_click)
        # You must implement this.
        # Here you must configure the button to bind its click to
        # the send_click() function.
        save_button.pack(fill=tk.BOTH, side=tk.RIGHT, padx=5, pady=5)

        self.footer_label = tk.Label(master=self, text="Ready.")
        self.footer_label.pack(fill=tk.BOTH, side=tk.LEFT, padx=5)


class NewContactDialog(tk.simpledialog.Dialog):
    def __init__(self, root, title=None, user=None, pwd=None, server=None):
        self.root = root
        self.server = server
        self.user = user
        self.pwd = pwd
        super().__init__(root, title)

    def body(self, frame):
        self.server_label = tk.Label(frame, width=30, text="DS Server Address")
        self.server_label.pack()
        self.server_entry = tk.Entry(frame, width=30)
        self.server_entry.insert(tk.END, self.server)
        self.server_entry.pack()

        self.username_label = tk.Label(frame, width=30, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(frame, width=30)
        self.username_entry.insert(tk.END, self.user)
        self.username_entry.pack()

        # You need to implement also the region for the user to enter
        # the Password. The code is similar to the Username you see above
        # but you will want to add self.password_entry['show'] = '*'
        # such that when the user types, the only thing that appears are
        # * symbols.
        #self.password...


    def apply(self):
        self.user = self.username_entry.get()
        self.pwd = self.password_entry.get()
        self.server = self.server_entry.get()


class MainApp(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.username = None
        self.password = None
        self.server = None
        self.file_path = None
        self.recipient = None
        # You must implement this! You must configure and
        # instantiate your DirectMessenger instance after this line.
        #self.direct_messenger = ... continue!

        # After all initialization is complete,
        # call the _draw method to pack the widgets
        # into the root frame
        self._draw()
        #self.body.insert_contact("studentexw23") # adding one example student.

    def send_message(self):
        msg = self.body.get_text_entry()
        if len(msg) > 0:
            ds_mess = DirectMessenger(self.server, self.username, self.password)
            #p = SaveFilePath(self.file_path)
            result = ds_mess.send(msg, self.recipient)
            pass
        else:
            pass

    def add_contact(self):
        new_cont = tkinter.simpledialog.askstring("New Contact", "Enter a contact.")
        self.body.insert_contact(new_cont)
        pass
    '''
    def ret_fp(self):
        print("test1232")
        return self.file_path
    '''
    def recipient_selected(self, recipient):
        '''
        Whatever is selected in the treeview should be passed here and made self.recipient. So when a message is sent the code knows that this is the person to send the message to.
        '''
        self.recipient = recipient

    def configure_server(self):
        ud = NewContactDialog(self.root, "Configure Account",
                              self.username, self.password, self.server)
        self.username = ud.user
        self.password = ud.pwd
        self.server = ud.server
        # You must implement this!
        # You must configure and instantiate your
        # DirectMessenger instance after this line.

    def publish(self, message:str):
        # You must implement this!
        pass

    def check_new(self):
        # You must implement this!
        pass


    def _draw(self):
        # Build a menu and add it to the root frame.
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

        # The Body and Footer classes must be initialized and
        # packed into the root window.
        self.body = Body(self.root,
                         recipient_selected_callback=self.recipient_selected)
        self.body.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.footer = Footer(self.root, send_callback=self.send_message)
        self.footer.pack(fill=tk.BOTH, side=tk.BOTTOM)


    def open_filee(self):
        file_path1 = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("DSU files", ".dsu"), ("allfiles", "*.*")))
        assign = Profile()
        assign.load_profile(file_path1)
        self.username = assign.username
        self.password = assign.password
        self.server = assign.dsuserver
        self.file_path = file_path1
        ds_client.set_path(self.file_path)


    def close_code(self):
        main.destroy()

    def create_new_file(self):
        global dsu_file
        dsu_file = filedialog.asksaveasfilename(defaultextension=".dsu", title = "Create New DSU File", filetypes=(("DSU files", ".dsu"), ("All Files", "*.*")))
        asks = ["Username:", "Password:", "Server IP:"]
        if len(dsu_file) > 1:
            main = tk.Tk()
            main.withdraw()
            global input_user
            global input_password
            global input_server
            global save_info
            global root2
            root2 = tk.Tk()
            #global input_user
            input_user = tk.Entry(root2)
            #global input_password
            input_password = tk.Entry(root2)
            #global input_server
            input_server = tk.Entry(root2)
            save_info = tk.Button(root2, text="Save", command=self.save_data)
            input_user.grid(row=0, column=0)
            input_password.grid(row=1, column=0)
            input_server.grid(row=2, column=0)
            save_info.grid(row=3, column=0)
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
                user.user_asker(dsu_file, u, p, s)
                self.username = u
                self.password = p
                self.server = s
                self.file_path = dsu_file
                self.close_q()
            else:
                self.new_window()
        else:
            self.new_window()


    def new_window(self):
        new_wind = Toplevel()
        new_wind.geometry("350x150")
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
    main.geometry("720x480")

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
    id = main.after(2000, app.check_new)
    print(id)
    # And finally, start up the event loop for the program (you can find
    # more on this in lectures of week 9 and 10).
    main.mainloop()
