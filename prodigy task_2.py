from tkinter import*
root=Tk()
root.title("to do list")
root.geometry("400x400")
#create frame
my_frame=Frame(root)
my_frame.pack(pady=10)
#create listbox
my_list=Listbox(my_frame, width=25, height=5, bg="SystemButtonFace", bd=0, highlightthickness=0, selectbackground="#a6a6a6", activestyle="none")
my_list.pack(side=LEFT,fill=BOTH)#the list will be ont he left and scrollbar on right
#now create a list which has something defined in it
things=["buy eggs","go to swim","bake a cake","study"]
#now put things in the listbox
for item in things:
    my_list.insert(END,item) #insert at the end 
#create a scrollbar
my_scrollbar=Scrollbar(my_frame)#it will be in my_frame
my_scrollbar.pack(side=RIGHT,fill=BOTH)#we want it in the right hand side
#add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)
#create an entry box to add items to the listbox
my_entry=Entry(root, font=("Ariel",20))
my_entry.pack(pady=20)
#create a button frame
button_frame=Frame(root)
button_frame.pack(pady=20)
#define functions
def delete_item():
    my_list.delete(ANCHOR)#will delete whatever that has been highlighted

def add_item():
    my_list.insert(END, my_entry.get())#we will insert in the listbox at the end and whatever is there in the entry box will get inserted
    my_entry.delete(0,END)#after we wrote what to insert we need this to be deleted from the entry box

def update_item():
    selected_index=my_list.curselection()
    if selected_index:
        my_list.delete(selected_index)
        my_list.insert(selected_index, my_entry.get())
        my_entry.delete(0,END)

#add some buttons
delete_button=Button(button_frame, text="Delete Item", command=delete_item)
add_button=Button(button_frame, text="Add Item", command=add_item)
update_button=Button(button_frame, text="Update Item", command=update_item)
delete_button.grid(row=0,column=0,padx=20)#padx to separate the buttons
add_button.grid(row=0,column=1)
update_button.grid(row=0,column=3,padx=20)

root.mainloop()