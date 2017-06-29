from Tkinter import * 
import tkFont
import time
import pdb

green_color="#6B8E23"

def get_value(player):
	return(player.get())
#def reset(player)
#	player.set(20)


def assign_modifyer_peter(stamina):
	temp=int(stamina)
	string_color="black"
	if ( temp > 14 and temp < 21 ) :
		newlabel="Normal"
		string_color='green'
	elif ( temp > 9 and temp < 15 ) : 
		newlabel="Puffed (-1)"
		string_color=green_color
	elif ( temp > 4 and temp < 10 ) :
		newlabel="Tired (-2)"
		string_color='orange'
	else: 
		newlabel="Exhaused (-3)"
		string_color='red'
	label_text=newlabel
	peter_status.config(text=newlabel)
	peter_status.configure(foreground=string_color)	
def assign_modifyer_blake(stamina):
        temp=int(stamina)
        string_color="black"
        if ( temp > 14 and temp < 21 ) :
                newlabel="Normal"
                string_color='green'
        elif ( temp > 9 and temp < 15 ) :
                newlabel="Puffed (-1)"
                string_color=green_color
        elif ( temp > 4 and temp < 10 ) :
                newlabel="Tired (-2)"
                string_color='orange'
        else:
                newlabel="Exhaused (-3)"
                string_color='red'
        label_text=newlabel
        blake_status.config(text=newlabel)
        blake_status.configure(foreground=string_color)
def assign_modifyer_charlie(stamina):
        temp=int(stamina)
        string_color="black"
        if ( temp > 14 and temp < 21 ) :
                newlabel="Normal"
                string_color='green'
        elif ( temp > 9 and temp < 15 ) :
                newlabel="Puffed (-1)"
                string_color=green_color
        elif ( temp > 4 and temp < 10 ) :
                newlabel="Tired (-2)"
                string_color='orange'
        else:
                newlabel="Exhaused (-3)"
                string_color='red'
        label_text=newlabel
        charlie_status.config(text=newlabel)
        charlie_status.configure(foreground=string_color)
#def rerender():
#        peter_stamina.pack()
#	peter_status=Label(master,textvariable=assign_modifyer(peter_stamina)).pack()
#	blake_stamina.pack()
#	charlie_stamina.pack()
#	master.update()


peter="Atlas"
blake="Vis"
charlie="Oak"
puffed_threshold=15
tired_threshold=10
exhausted_threshold=5
global label_text
label_text="normal"



master=Tk()
master.configure(background='white')
################ CODE FOR PETER'S STAMINA ###############
label=Label(master, text=peter)
label.configure(background='white')

f = tkFont.Font(font=label['font'])
f['weight'] = 'bold'
f['size'] = 16


x = tkFont.Font(font=label['font'])
x['weight'] = 'bold'
x['size'] = 14


label['font'] = f.name
label.pack()
#status=Label(master,text=label_text).pack()
peter_stamina=Scale(master,from_=0, to=20, orient=HORIZONTAL,command=assign_modifyer_peter)
peter_stamina.set(20)
peter_stamina.configure(background='white')
#peter_status=Label(master,textvariable=assign_modifyer(peter_stamina)).pack()
peter_stamina.pack()
#ame=Text(master)
#name.insert(END, peter)
#name.pack()
#Button(master, text='reset', command=reset(peter_stamina)).pack()
peter_status=Label(master, text=label_text)
peter_status['font'] = x.name
peter_status.configure(background='white')
peter_status.config(highlightbackground='white')
peter_status.pack()


#################### CODE FOR BLAKE'S STAMINA #####################
label=Label(master, text=blake)
label['font'] = f.name
label.configure(background='white')
label.pack()
blake_stamina=Scale(master, from_=0, to=20, orient=HORIZONTAL, command=assign_modifyer_blake)
blake_stamina.set(20)
blake_stamina.configure(background='white')
blake_stamina.pack()
blake_status=Label(master, text=label_text)
blake_status['font'] = x.name
blake_status.configure(background='white')
blake_status.pack()


###############CODE FOR CHARLIE'S STAMINA################

label=Label(master, text=charlie)
label.configure(background='white')
label['font'] = f.name
label.pack()
charlie_stamina=Scale(master, from_=0, to=20, orient=HORIZONTAL, command=assign_modifyer_charlie)
charlie_stamina.set(20)
charlie_stamina.configure(background='white')
charlie_stamina.pack()
charlie_status=Label(master, text=label_text)
charlie_status['font'] = x.name
charlie_status.configure(background='white')
charlie_status.pack()
#Button(master, text='reset', command=reset(charlie_stamina)).pack()

mainloop()

#while 1:
#	rerender()
#	time.sleep(0.02)	
