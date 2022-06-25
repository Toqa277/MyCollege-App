from tkinter import *#library used for gui
from tkinter import ttk,messagebox,filedialog#function we called form tkinter
import googletrans        #the library used to drive the languages used in the translator by the free api of google translate
import json#the library that used to load the data from api in jason format
import requests#the library that used to request the data from api
#from convertor import *#python file contain all the unit convertor functions
import textblob#library that used to translate the words
import math
import cmath
from datetime import datetime

#functions
def translator(): # the function that translate the languages
    try:
        for key,value in languages.items(): # here we loop over two things in the dictionary the key and value
            if value == translate1_box.get():# if the value = the language i choosed from the combo box
                used_language = key # we but the key of this lang. in varibale
        for key,value in languages.items():
            if value == translate2_box.get():
                wanted_language_to_translate = key
        sentences =textblob.TextBlob(translate1_area.get(1.0,END)) # here we took the words that we want to translate and add it to varibale
        sentences = sentences.translate(from_lang=used_language,to=wanted_language_to_translate) #then we we used textblob to translate the words
        translate2_area.insert(1.0,sentences)# here we show the words after translation
    except Exception as error:
        messagebox.showerror('translator',error)

def read_file():
    try:
        file = filedialog.askopenfilename(initialdir="E:/",title='open',filetypes=(("text files","*.txt"),("all files","*.*"),))
        file = open(file,"r")
        note_area.insert(1.0,file.read())
        file.close()
    except Exception as read_error:
        messagebox.showerror('',read_error)
def write_file():
    try:
        file = filedialog.askopenfilename(initialdir="E:/",title='open',filetypes=(("text files","*.txt"),("all files","*.*"),))
        file = open(file,"a")
        dictionary_content = text_area.get(1.0,END)
        notes_content = note_area.get(1.0,END)
        if len(dictionary_content) == 0 and len(notes_content) > 0:
            file.write(notes_content)
        elif len(dictionary_content) > 0 and len(notes_content) == 0:
            file.write(dictionary_content)
        elif len(dictionary_content) > 0 and len(notes_content) > 0:
            file.write(f'{dictionary_content}\n\n {notes_content}')
        file.close()
    except Exception as write_error:
        messagebox.showerror('',write_error)

#interface-----------------------------------------------------------------------------------------------------------------------
my_college_app =Tk()
my_college_app.title('MY COLLEGE')
menu = Menu(my_college_app)
my_college_app.config(menu=menu)
#creating a menu
file_menu = Menu(menu)
#creating a menu items
menu.add_cascade(label='file',menu=file_menu)
file_menu.add_command(label='open',command= read_file)
file_menu.add_command(label='save as..',command=write_file)
my_college_app.resizable(0, 0)
note = ttk.Notebook(my_college_app)
tab1 = Frame(my_college_app,bg='#15133C') #the area that contain calculator
tab2 = Frame(my_college_app,bg='white') #the area that contain translator
tab3 = Frame(my_college_app,bg='black') #the area that contain web blocker
tab4 = Frame(my_college_app) #the area of the to do list
tab5 = Frame(my_college_app)
tab6 = Frame(my_college_app)
tab7 = Frame(my_college_app)
x='#EC994B' #calc button color
#-----------------------------------------------------------------------------------------------------------------------
#start of the calculator
e = Entry(tab1,width=45,borderwidth=5)
e.grid(row=0,column=0,padx=10,pady=10,columnspan=4)
global mood
def insert(number): # this the function that will display the numbers i clicked on the entry bar
    e.insert(END,number)
def button_add():#function that get the first number i will use to add to other number and set the mood = addition so the equal function know that we are going to add
    try:
     first_number = e.get()
     global f_num
     global mood
     mood = 'addition'
     f_num = float(first_number)
     e.delete(0,END)
    except Exception as error_add:
        messagebox.showerror('calculator',error_add)
def button_sub():#function that get the first number i will use to subtract to other number and set the mood = subtract so the equal function know that we are going to subtract
    try:
     first_number = e.get()
     global f_num
     global mood
     mood = 'sub'
     f_num = float(first_number)
     e.delete(0,END)
    except Exception as error_sub:
        messagebox.showerror('calculator',error_add)
def button_multi():#function that get the first number i will use to multiplay to other number and set the mood = multiplay so the equal function know that we are going to multiplay
    try:
     first_number = e.get()
     global f_num
     global mood
     mood = 'multi'
     f_num = float(first_number)
     e.delete(0,END)
    except Exception as error_multi:
        messagebox.showerror('calculator',error_multi)
def button_divide():#function that get the first number i will use to divide to other number and set the mood = dividion so the equal function know that we are going to divide
    try:
     first_number = e.get()
     global f_num
     global mood
     mood = 'divide'
     f_num = float(first_number)
     e.delete(0,END)
    except Exception as error_divide:
        messagebox.showerror('calculator',error_divide)
def button_root():#function that get the first number and set the mood = root
    try:
     number = e.get()
     global f_num
     global mood
     mood = 'root'
     f_num = float(number)
     e.delete(0,END)
    except Exception as error_root:
        messagebox.showerror('calculator',error_root)
def button_power():#function that get the first number set mood = power
    try:
     number = e.get()
     global f_num
     global mood
     mood = 'power'
     f_num = float(number)
     e.delete(0,END)
    except Exception as error_power:
        messagebox.showerror('calculator',error_power)
def button_3root():#function that get the first number and set mood to qubic root
    try:
     number = e.get()
     global f_num
     global mood
     mood = '3root'
     f_num = float(number)
     e.delete(0,END)
    except Exception as error_3root:
        messagebox.showerror('calculator',error_3root)
def button_reminder():#function that get the first number and set mood = reminder to get the reminder of this number reltive to other number
    try:
     number = e.get()
     global f_num
     global mood
     mood = 'reminder'
     f_num = float(number)
     e.delete(0,END)
    except Exception as error_reminder:
        messagebox.showerror('calculator',error_reminder)
def button_round():#function that get the first number set mood = round so we can round the number to the seginfacnt figeres we want
    try:
        number = e.get()
        global f_num
        global mood
        mood = 'round'
        f_num = float(number)
        e.delete(0,END)
    except Exception as error_round:
        messagebox.showerror('calcultor',error_round)
def button_average():#function that get many number splited by comma and set mood = average
    try:
        global set
        set = e.get().split(',')
        global mood
        mood = 'average'
        e.delete(0,END)
    except Exception as error_average:
        messagebox.showerror('calculator',error_average)
def button_shift():#function that get the mood of the unit convertor and the number that we will convert and set the mood = convert
    try:
        global spinbox
        global f_num
        global mood
        mood = 'convertor'
        f_num = e.get()
        spinbox = convert_box.get()
        e.delete(0,END)
    except Exception as error_convert:
        messagebox.showerror('calculator',error_convert)
def angle_convertor():#function that get the angle to convert
    try:
        global spinbox
        global f_num
        global mood
        mood = 'angle convertor'
        f_num = e.get()
        spinbox = convert_box.get()
        e.delete(0,END)
    except Exception as error:
        messagebox.showerror('calculator',error)
global mood
def button_equal(): #the function the perform the mood that choosed in the functions behind
    try:
     if mood == 'addition':
        x = e.get()
        e.delete(0,END)
        y = f_num + float(x)
        e.insert(0,y)
     elif mood == 'sub':
        x = e.get()
        e.delete(0,END)
        y = f_num - float(x)
        e.insert(0,y)
     elif mood == 'multi':
        x = e.get()
        e.delete(0,END)
        y = f_num * float(x)
        e.insert(0,y)
     elif mood == 'divide':
        x = e.get()
        e.delete(0,END)
        y = f_num / float(x)
        e.insert(0,y)
     elif mood == 'root':
        y = f_num ** (1/2)
        e.insert(0,y)
     elif mood == 'power':
        x = e.get()
        e.delete(0,END)
        y = f_num ** float(x)
        e.insert(0,y)
     elif mood == '3root':
        y = f_num ** (1/3)
        e.insert(0,y)
     elif mood == 'reminder':
        x = e.get()
        e.delete(0,END)
        y = f_num % float(x)
        e.insert(0,y)
     elif mood == 'round':
         x = e.get()
         z = int(x)
         e.delete(0,END)
         y = round(f_num,z)
         e.insert(0,y)
     elif mood == 'average':
         for i in range(len(set)): #here in the average we first float all the number enterd
             set[i] = float(set[i])
         sum = 0
         for j in range(len(set)):#then we made a for loop to calc the sum of this list
             sum = sum + set[j]
         average = sum / len(set) #here we divide the sum on the lentgh of the list to get the average and show it
         e.insert(0,average)
     elif mood == 'convertor':#in the converotr function behind we set the value we choosed fo the spinbox containing the moods
         if spinbox == '1':#this group of if and elif to call the convert function from the file convert and preform it according to the number choosed
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{cmTOm(number)} m')
         elif spinbox == '2':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{mTOcm(number)} cm')
         elif spinbox == '3':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{inTOcm(number)} cm')
         elif spinbox == '4':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{cmTOin(number)} in')
         elif spinbox == '5':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{mTOft(number)} ft')
         elif spinbox == '6':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{ftTOm(number)} m')
         elif spinbox == '7':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{ydTOm(number)} m')
         elif spinbox == '8':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{mTOyd(number)} yd')
         elif spinbox == '9':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{mileTOkm(number)} km')
         elif spinbox == '10':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{kmTOmile(number)} mile')
         elif spinbox == '11':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{mileTOm(number)} m')
         elif spinbox == '12':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{mTOmile(number)} mile')
         elif spinbox == '13':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{nmileTOm(number)} m')
         elif spinbox == '14':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{mTOnmile(number)} nmile')
         elif spinbox == '15':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{acreTOmsq(number)} msq')
         elif spinbox == '16':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{msqTOacre(number)} acre')
         elif spinbox == '16':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{msqTOacre(number)} acre')
         elif spinbox == '16':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{msqTOacre(number)} acre')
         elif spinbox == '16':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{msqTOacre(number)} acre')
         elif spinbox == '16':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{msqTOacre(number)} acre')
         elif spinbox == '17':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{galUStoL(number)} L')
         elif spinbox == '18':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{LtogalUS(number)} galUS')
         elif spinbox == '19':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{galUKtoL(number)} L')
         elif spinbox == '20':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{LtogalUK(number)} galUK')
         elif spinbox == '21':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{gTOKg(number)} Kg')
         elif spinbox == '22':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{kgTOg(number)} g')
         elif spinbox == '23':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{ozTOg(number)} g')
         elif spinbox == '24':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{gTOoz(number)} oz')
         elif spinbox == '25':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{lbTOkg(number)} Kg')
         elif spinbox == '26':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{kgTOlb(number)} lb')
         elif spinbox == '27':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{kmhTOms(number)} m/s')
         elif spinbox == '28':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{msTOkmh(number)} km/h')
         elif spinbox == '29':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{atmTOpascal(number)} pascal')
         elif spinbox == '30':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{pascalTOatm(number)} atm')
         elif spinbox == '31':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{mmHGTOpascal(number)} pascal')
         elif spinbox == '32':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{pascalTOmmHG(number)} mmHG')
         elif spinbox == '33':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{kgfcm2TOpa(number)} pa')
         elif spinbox == '34':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{paTOkgfcm2(number)} kgf/cm^2')
         elif spinbox == '35':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{lbfin2TOkpa(number)} kpa')
         elif spinbox == '36':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{kpaTOlbfin2(number)} lbfin2')
         elif spinbox == '37':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{kgfmTOJ(number)} J')
         elif spinbox == '38':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{JTOkgf(number)} kgf/m')
         elif spinbox == '39':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{jTOcal(number)} cal')
         elif spinbox == '40':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{calTOj(number)} J')
         elif spinbox == '41':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{hpTOkw(number)} kW')
         elif spinbox == '42':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{kwTOhp(number)} Hp')
         elif spinbox == '43':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{FtoC(number)} C')
         elif spinbox == '38':
             number = float(f_num)
             e.delete(0,END)
             e.insert(0,f'{CtoF(number)} F')
     elif mood == 'angle convertor':
         e.delete(0,END)
         if spinbox == '1':
             number = (180*float(f_num))/math.pi
         elif spinbox == '2':
             number = math.radians(float(f_num))
         angle_type = GeneralAngleType(float(f_num))
         e.insert(0,f'{number}\t{angle_type}')

    except Exception as error1:
        messagebox.showerror('calculator',error1)

b1 = Button(tab1,text='1',width=15,cursor='hand2',bg=x,activebackground=x,command=lambda:insert(1)).grid(row=1,column=0,pady=5,padx=5)
b2 = Button(tab1,text='2',width=15,cursor='hand2',bg=x,activebackground=x,command=lambda:insert(2)).grid(row=1,column=1,pady=5,padx=5)
b3 = Button(tab1,text='3',width=15,cursor='hand2',bg=x,activebackground=x,command=lambda:insert(3)).grid(row=1,column=2,pady=5,padx=5)
b4 = Button(tab1,text='4',width=15,cursor='hand2',bg=x,activebackground=x,command=lambda:insert(4)).grid(row=2,column=0,pady=5,padx=5)
b5 = Button(tab1,text='5',width=15,cursor='hand2',bg=x,activebackground=x,command=lambda:insert(5)).grid(row=2,column=1,pady=5,padx=5)
b6 = Button(tab1,text='6',width=15,cursor='hand2',bg=x,activebackground=x,command=lambda:insert(6)).grid(row=2,column=2,pady=5,padx=5)
b7 = Button(tab1,text='7',width=15,cursor='hand2',bg=x,activebackground=x,command=lambda:insert(7)).grid(row=3,column=0,pady=5,padx=5)
b8 = Button(tab1,text='8',width=15,cursor='hand2',bg=x,activebackground=x,command=lambda:insert(8)).grid(row=3,column=1,pady=5,padx=5)
b9 = Button(tab1,text='9',width=15,cursor='hand2',bg=x,activebackground=x,command=lambda:insert(9)).grid(row=3,column=2,pady=5,padx=5)
b0 = Button(tab1,text='0',width=15,cursor='hand2',bg=x,activebackground=x,command=lambda:insert(0)).grid(row=4,column=0,pady=5,padx=5)
b_dot = Button(tab1,text='.',width=10,cursor='hand2',bg=x,activebackground=x,command=lambda:insert('.')).grid(row=4,column=3,pady=5,padx=5)
b_average = Button(tab1,text='average',width=10,cursor='hand2',command=button_average).grid(row=5,column=3,pady=5,padx=5)
b_comma = Button(tab1,text=',',width=10,cursor='hand2',command=lambda:insert(',')).grid(row=6,column=3,pady=5,padx=5)
b_reminder = Button(tab1,text='reminder',width=10,cursor='hand2',bg=x,activebackground=x,command=button_reminder).grid(row=2,column=3,pady=5,padx=5)
b_plus = Button(tab1,text='+',width=15,cursor='hand2',bg=x,activebackground=x,command=button_add).grid(row=4,column=1,pady=5,padx=5)
b_sub = Button(tab1,text='-',width=15,cursor='hand2',bg=x,activebackground=x,command=button_sub).grid(row=5,column=0,pady=5,padx=5)
b_multi = Button(tab1,text='x',width=15,cursor='hand2',bg=x,activebackground=x,command=button_multi).grid(row=5,column=1,pady=5,padx=5)
b_root = Button(tab1,text='_/--',width=15,cursor='hand2',bg=x,activebackground=x,command=button_root).grid(row=6,column=0,pady=5,padx=5)
b1_power = Button(tab1,text='^',width=15,cursor='hand2',bg=x,activebackground=x,command=button_power).grid(row=6,column=1,pady=5,padx=5)
b1_qubicroot = Button(tab1,text='3root',width=15,cursor='hand2',bg=x,activebackground=x,command=button_3root).grid(row=6,column=2,pady=5,padx=5)
b1_divide = Button(tab1,text='/',width=15,cursor='hand2',bg=x,activebackground=x,command=button_divide).grid(row=5,column=2,pady=5,padx=5)
b_round = Button(tab1,text='round',width=10,cursor='hand2',command=button_round).grid(row=3,column=3,pady=5,padx=5)
b_angle_convertor = Button(tab1,text='angle covertor',width=10,cursor='hand2',command=angle_convertor).grid(row=8,column=3)
b_clear = Button(tab1,text='clear',width=15,cursor='hand2'
                 ,command=lambda: e.delete(0,END)).grid(row=4,column=2,pady=5,padx=5)
b_shift = Button(tab1,text='shift',width=10,cursor='hand2',comman=button_shift).grid(row=7,column=3)
b_equal = Button(tab1,text='=',width=15,cursor='hand2',
                 command=button_equal).grid(row=7,column=2,pady=5,padx=5)
b_quit = Button(tab1,text='quit',width=15,cursor='hand2'
                ,command=my_college_app.quit,bg='white',fg='black',activeforeground='black'
                ,activebackground='white').grid(row=8,column=2,pady=5,padx=5)
convert_box = ttk.Spinbox(tab1,from_=1,to=44)
convert_box.grid(row=9,column=0)
#the end of the calculator app -----------------------------------------------------------------------------------------

#start of the translator
def clear():
    translate1_area.delete(1.0,END)
    translate2_area.delete(1.0,END)
translate1_area = Text(tab2,bg='light yellow',fg='navy',width=22,height=10,bd=2)
translate1_area.grid(row=0,column=0,padx=5,pady=5)
translate2_area = Text(tab2,bg='light yellow',fg='navy',width=25,height=10,bd=2)
translate2_area.grid(row=0,column=2,padx=5,pady=5)
translate_button=Button(tab2,text='translate',width=10,bg='black',fg='white',command=translator)
translate_button.grid(row=2,column=0,pady=5)
clear_button = Button(tab2,text='clear',width=10,bg='black',fg='white',command=clear)
clear_button.grid(row=2,column=1,pady=5)
close_button = Button(tab2,text='close',width=10,bg='black',fg='white',command=my_college_app.quit)
close_button.grid(row=2,column=2,pady=5)
#-------->creating the list of languges
languages = googletrans.LANGUAGES#here we used the function from google trans library to get dictiory of all languages and it's key to use them in the translator
languages_list = [] #then we created empty list to add the languges
for x in languages: # we looped for the key in the languges dictionary
    y = languages[x] # we set a varibale y = the languages dictionary[key] to get the value and add them the list
    languages_list.append(y)


translate1_box = ttk.Combobox(tab2)
translate1_box.grid(row=1,column=0,padx=10,pady=5)
translate1_box.config(values=languages_list)#here we added the list of languges to combo box to choose the languages
translate1_box.current(21)


translate2_box = ttk.Combobox(tab2)
translate2_box.grid(row=1,column=2,padx=10,pady=5)
translate2_box.config(values=languages_list)#here we added the list of languges to combo box to choose the languages
translate2_box.current(30)
#end of the translator app
#start of dictionary
def search():# function that we search for the data in the oxford dictionary API
    try:
        text_area.delete(1.0,END)
        app_id = 'd810243b' #the api id i requsted from oxford
        app_key = '019a1fb51670afbde444e8d815f20429'#the key
        language = 'en-gb'#the languages of the dictionary
        word_id = word_entry.get() #here we get the entered word
        url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/'  + word_id.lower()
        r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})#we used the function get from the library request to get the data
        content = json.loads(r.content)#here we used loads from json to load the data
        start_key = 0 #counter we will use to make conditions
        for i in content: #here i looped in the whoele data
            if i == 'error': #if it contain the key error this mean the user enter miss spilled word so we add 1 to the start_key
                start_key = start_key + 1
        if start_key > 0: # if the start_key >0 this mean there is error
            text_area.delete(1.0,END)
            text_area.insert(1.0,'there is no data to show you have entered a wrong word') #so will show the user that he may enterd a miss spilled word
        elif start_key == 0: #else
            y = content["results"] #the data is to large so we must reduce it the most common index so we can search
            provider = 'Oxford University Press' #this coomon for all words
            the_word = content['id'] #first the=is varibale stantd for the word we entered second this index is common for all words
            definition = y[0]["lexicalEntries"][0]["entries"][0]['senses'][0]["definitions"][0]#the index of the defintion of the word is common for all words
            common_content = y[0]["lexicalEntries"]#the data that i will loop in to get the synyoms this index is common in all words and this index is common in the first part of the whole synonymes index
            common_content_hitory = y[0]["lexicalEntries"][0]["entries"][0]#the same for the history of the word
            history = [] #these empty list to append the data i found
            synonyms_list=[]
            for i in range(len(common_content)): #i started to make many nested loop to reduce the search data so i can iterate easily
                x = common_content[i]['entries'][0]['senses']# i found the some word the place of synonyms took index [0] or [1] after the common synonyms content
                                                             #so i started to loop in to find
                for j in range(len(x)): #there is word get index after the the varibale x 0,1,2
                    #so i looped i to drive all the data and it returns from 1 to 5 dictionaries of data depend on the word some of them have the key synonyms
                    s = x[j]

                    for key in s:#so i made this loop with condtion if the key = synonyms
                        if key == 'synonyms':
                            synonyms = s[key]#finally we got the synonyms

                            for n in range(len(synonyms)):#this last loop for formatting the synonyms is a list of dictionries with two key and we need value of one key of them
                                word = synonyms[n]['text'] #so this loop to get the needed data and append them in the synonyms list
                                synonyms_list.append(word)

            for keys in common_content_hitory:#the same here with history some words does not have history but it is much easier than synonyms so it need on loop only
                if keys =='etymologies':
                    history.append(common_content_hitory[keys][0])
            if len(synonyms_list) > 0 and len(history) > 0:#here the if and elif to show the data based on the reasult i got
                text_area.delete(1.0,END) # if len synonyms_list and the hitory_list > = this mean that they contain a data
                text_area.insert(1.0,f'the source: {provider}\n\nthe word: {the_word}\n\nthe history {history[0]}\n\ndefintion1: {definition}\n\n'
                                 f'the synonyms:\n\n{synonyms_list}')
            elif len(synonyms_list) > 0 and len(history) == 0:#here no history so i do not show it
                text_area.delete(1.0,END)
                text_area.insert(1.0,f'the source: {provider}\n\nthe word: {the_word}\n\ndefintion1: {definition}\n\n'
                                 f'the synonyms:\n\n {synonyms_list}')
            elif len(history) > 0 and len(synonyms_list) == 0: #here no synonyms so i showed to the user all data excpet i write there is no synonyms for this word
                text_area.delete(1.0,END)
                text_area.insert(1.0,f'the source: {provider}\n\nthe word: {the_word}\n\nthe history {history[0]}\n\ndefintion1: {definition}\n\n'
                                 f'the synonyms:\n\n there is no synonyms for the word {the_word}')
            elif len(history) == 0 and len(synonyms_list) == 0: #here no synonyms no history
                text_area.delete(1.0,END)
                text_area.insert(1.0,f'the source: {provider}\n\nthe word: {the_word}\n\ndefintion1: {definition}\n\n'
                                 f'the synonyms:\n\n there is no synonyms for the word {the_word}')
    except Exception as errorr:
        messagebox.showerror('dictionary',errorr)
search_button = Button(tab4,text='lookup',command=search).grid(row=0,column=0)
word_entry = Entry(tab4,width=10)
word_entry.grid(row=0,column=1)
text_area = Text(tab4,width=60,height=25)
text_area.grid(row=1,column=0,columnspan=2)
#-----------------------------------------------------------------------------------------------------------------------
#start of website blocker
info_label = Label(tab3,text='enter the end time in year,month,day,hour,minute seprated by comma',width=45,bg='black',fg='white')
info_label.place(x=10,y=5)
time_entry = Entry(tab3,width=45)
time_entry.place(x=5,y=25)
site_label = Label(tab3,text='enter the urls you want to block seprated by comma',bg='black',fg='white').place(x=5,y=50)
site_entry = Entry(tab3,width=45)
site_entry.place(x=5,y=75)
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
def block():
    time = time_entry.get().split(',')
    year = int(time[0])
    month =int(time[1])
    day = int(time[2])
    hour = int(time[3])
    minute =int(time[4])
    end_time = datetime(year,month,day,hour,minute)
    sites =site_entry.get().split()
    if datetime.now() < end_time:
        messagebox.showinfo('web blocker',"blocked succefully")
        with open(hosts_path, 'r+') as hostfile:
            hosts_content = hostfile.read()
            for i in sites:
                if i not in hosts_content:
                   hostfile.write(redirect + ' ' + i + '\n')
                    #adding the desired site to block in the host file

    else:
        messagebox.showinfo('web blocker',"error in time re enter the time")
        with open(hosts_path, 'r+') as hostfile:
            lines= hostfile.readline()
            hostfile.seek(0)
            hostfile.truncate()
block_button = Button(tab3,text='block',width=15,command=block).place(x=25,y=100)

#-----------------------------------------------------------------------------------------------------------------------
#start of notes
note_area = Text(tab5,width=60,height=25)
note_area.pack()
#----------------------------------------------------------------------------------------------------------------------
#numrical
types_of_functions = ['polinmial','trig','log']
types_label = Label(tab6,text='choose type of the function',fg='red').grid(row=0,column=0)
types_box = ttk.Combobox(tab6)
types_box.grid(row=1,column=0)
types_box.config(values=types_of_functions)
note_label = Label(tab6,text='!if you choosed trig choose the trig function fromthe trig list',fg='red').grid(row=2,column=0)
trig_function_list = ['sin', 'cos', 'tan', 'csc', 'sec', 'cot']
trig_label=Label(tab6,text='trig function list',fg='red').grid(row=0,column=1)
trig_types_box = ttk.Combobox(tab6)
trig_types_box.grid(row=1,column=1)
trig_types_box.config(values=trig_function_list)
note2_label = Label(tab6,text='but if you choosed polynmial complete the following',fg='red').grid(row=3,column=0)
the_degree_label = Label(tab6,text='type the degree').grid(row=4,column=0)
the_degree_entry = Entry(tab6)
the_degree_entry.grid(row=4,column=1)
the_coff_label = Label(tab6,text='type the coff').grid(row=5,column=0)
the_coff_entry = Entry(tab6)
the_coff_entry.grid(row=5,column=1)
lower_limit = Label(tab6,text='enter the lower limit').grid(row=6,column=0)
lower_limit_E =Entry(tab6)
lower_limit_E.grid(row=6,column=1)
upper_limit = Label(tab6,text='enter the upper limit').grid(row=7,column=0)
upper_limit_E =Entry(tab6)
upper_limit_E.grid(row=7,column=1)
answer_label = Label(tab6,text='the answer').grid(row=8,column=0)
answer_entry = Entry(tab6)
answer_entry.grid(row=8,column=1)
global a
global answer
o = []
def integeration():
	global answer
	global g
	g= 0
	answer =[]
	def function(num):
		global g
		if types_box.get()=='log':
			g=math.log(num).real
		elif types_box.get()=='trig' and trig_types_box.get()=='sin':
			g= cmath.sin(num).real
		elif types_box.get()=='trig' and trig_types_box.get()=='cos':
			g= cmath.cos(num).real
		elif types_box.get()=='trig' and trig_types_box.get()=='tan':
			g= cmath.tan(num).real
		elif types_box.get()=='trig' and trig_types_box.get()=='csc':
			g= 1/(cmath.sin(num)).real
		elif types_box.get()=='trig' and trig_types_box.get()=='sec':
			g= 1/(cmath.cos(num)).real
		elif types_box.get()=='trig' and trig_types_box.get()=='cot':
			g= 1/(cmath.tan(num)).real


	a= int(lower_limit_E.get())
	b= int(upper_limit_E.get())
	for i in range(a,b+1,2):
		if types_box.get()== 'log' or types_box.get()=='trig':
			f=function(i)
			o.append(f)
		elif types_box.get()=='polinmial':
			coff = int(the_coff_entry.get())

			f= coff*(i**int(the_degree_entry.get()))
			o.append(f)
	sum=o[0]+o[len(o)-1]
	for j in range(len(o)):
		if o[j]!= o[0] and o[j]!=o[len(o)-1]:
			sum=sum+(2*o[j])
	diff= (b-a)/3
	answer_entry.delete(0,END)
	answer.append((diff/2)*sum) ; answer_entry.insert(0,answer[0])
answer_button = Button(tab6,text='show answer',command=integeration).grid(row=9,column=0)
#----------------------------------------------------------------------------------------------------------------------
#the manual
manual_label = Label(tab7,text='application manual',font=14).place(x=150,y=5)
note1 = '1.to use the dictionary or the translator you must be connected to the wifi'
not1_label = Label(tab7,text=note1).place(x=10,y=40)
note2 = '2.to use the unit convertor choose the mood you need from the spinbox\ntype the number then click shift then equal'
note2_label = Label(tab7,text=note2).place(x=10,y=75)
# forbidden space
note.add(tab1,text='py.calculator')
note.add(tab2,text='translator')
note.add(tab3,text='web blocker')
note.add(tab4,text='dictionary')
note.add(tab5,text='notes')
note.add(tab6,text='numrical')
note.add(tab7,text='manual')
note.pack()
my_college_app.mainloop()

