#installed PySimeGUI from pip
#command is--------->>>pip install pysimplegui

#------------imported libraries------

import sqlite3
from sqlite3 import Error
import PySimpleGUI as sg
import os

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'pythonsqlite1.db')


#--------code that finds error if not connected to python
 
try:
    conn=sqlite3.connect(DEFAULT_PATH)
    cur=conn.cursor()
    print('Successfully Connected')

except Error as e:
    print(e)

#--------a function that takes value in python and insert data in sql

def insert(i,v):
    if(i==1):
        while v[i]!='None':
            code="insert into products (s_no,product_name,price) values ({},'{}',{})"
            cur.execute(code.format(len(items()),v[0],v[i+1]))
            conn.commit()
            break
    else:
        while v[i]!='None':
            code="insert into entery (id,name,fathers_name,mobile_no,city,age) values ({},'{}','{}',{},'{}',{})"
            cur.execute(code.format(len(entery()),v[0],v[1],v[2],v[3],v[4]))
            conn.commit()
            break

#-------functions which gies data from sql to python

def items():
    cur.execute('select * from products')
    a=cur.fetchall()
    b=[]
    for i in range(len(a)):
        b.append(a[i][1])
    return b

def prices():
    cur.execute('select * from products')
    a=cur.fetchall()
    b=[]
    for i in range(len(a)):
        b.append(a[i][2])
    return b

def entery():
    cur.execute('select * from entery')
    a=cur.fetchall()
    b=[]
    for i in range(len(a)):
        b.append(a[i])
    return b

#------------changing our window colour-------
 
sg.ChangeLookAndFeel('GreenTan')
sg.SetOptions(window_location=(0,0))


#-------------there are many one i tried them as follows--------

'''NeutralBlue,lightyellow,LightGreen4,lightbrown1,Topanga,GreenTan,TanBlue:'''

#----------string for Developer Information----

i=["***Why it is created:-",'This is the man who creates this application for the use of billing management',
   'So you can use it as it was started to provide best details of billing',
   'as many retailers give lend to customers and they forgot it','And Ultimatly they go in loss',
   '***Creaters:-','1:-Deepak Choudhary (Main Coder)','2:-Vikram Singh (Code Helper)',
   '***Bibliography:-','1:-Navneet sir (give approach to us)','2:-Best Freind circle( who motivated us )']

#----------Layout for Developer Information----

p_i=[
                                [sg.T(i[0],font='normal 26',size=(50,2),text_color='red',justification='center')],
                                [sg.T('',size=(2,1)),sg.T(i[1],size=(100,1))],
                                [sg.T('',size=(2,1)),sg.T(i[2],size=(100,1))],
                                [sg.T('',size=(2,1)),sg.T(i[3],size=(100,1))],
                                [sg.T('',size=(2,1)),sg.T(i[4],size=(100,1))],
                                [sg.T('',size=(4,1)),sg.T(i[5],font='normal 16',text_color='red',size=(98,1))],
                                [sg.T('',size=(2,1)),sg.T(i[6],size=(97+3,1))],
                                [sg.T('',size=(2,1)),sg.T(i[7],size=(97+3,1))],
                                [sg.T('',size=(4,1)),sg.T(i[8],font='normal 16',text_color='red',size=(98,1))],
                                [sg.T('',size=(2,1)),sg.T(i[9],size=(97,1))],
                                [sg.T('',size=(2,1)),sg.T(i[10],size=(97,1))],
                                [sg.T('',size=(30,1)),sg.Button('Ok',size=(9,1))]
                                ]

#-------------string for privacy policy---------

p_policy=['What information is collected and how can we use it?',
          '*Types of information collected:-',
          '1.In order to provide our services to you, we will ask you to provide personal information that is necessary to provide those services to you.',
          '2.If you do not provide your personal information, we may not be able to provide you with our products or services.',
          '3.We will only collect the information that is necessary for its specified, explicit and legitimate purposes and not further',
          'processed in a manner that is incompatible with those purposes. ',
          '*How the personal information can be used:-',
          'Personal information is collected for providing services and / or products to you,and legal compliance on our part under applicable laws.',
          '*We may use your personal information for the following purposes:',
          '>Providing, processing, maintaining, improving and developing our goods and/or services to you,',
          'including after-sales and customer support and for services on your device or through our websites.',
          '>Communicating with you about your service or any general queries, such as updates,',
          ' customer inquiry support, information about our events, notices.',
          'NOTE:-We Will Not Sell Your DATA to Other Companies',
          '................This our Privcy Policy..............']

#-----------string for rules and regulation----
 
p_rules=['Our Rules and Regulations:-',
         '01-Do not use such Services in a way that distracts you and prevents you from obeying traffic or safety laws.',
         '02-All Data is Safe',
         '03-If You Cancel The Sign in Process Data in this case will not be saved',
         '04-Do not misuse our Services, for example, do not interfere with our Services or try to access them using a method other',
         ' than the interface and the instructions that we provide.',
         '05-You may use our Services only as permitted by law, including applicable export and control laws and regulations.',
         '06-We may suspend or stop providing our Services to you if you do not comply with our terms or policies or if ',
         'we are investigating suspected misconduct.',
         '07-Using our Services does not give you ownership of any intellectual property rights in our Services or the content that you access.',
         '08-You may not use content from our Services unless you obtain permission from its owner or are otherwise permitted by law.',
         '09-To protect your Hotel Management account , keep your password confidential.',
         '10-You are responsible for the activity that happens on or through your Hotel Management Account.']

#-------------layout for privacy policy-----

p_p=[
                                [sg.T(p_policy[14],size=(100,1),text_color='lightblue',justification='center')],
                                [sg.T(p_policy[0],size=(100,1),text_color='red',justification='center')],
                                [sg.T(p_policy[1],size=(100, 1),text_color='green')],
                                [sg.T('',size=(2,1)),sg.T(p_policy[2],size=(97,1))],
                                [sg.T('',size=(2,1)),sg.T(p_policy[3],size=(97,1))],
                                [sg.T('',size=(2,1)),sg.T(p_policy[4],size=(97,1))],
                                [sg.T('',size=(3,1)),sg.T(p_policy[5],size=(96,1))],
                                [sg.T(p_policy[6],size=(100,1),text_color='green')],
                                [sg.T('',size=(3,1)),sg.T(p_policy[7],size=(96,1))],
                                [sg.T(p_policy[8],size=(100,1),text_color='green')],
                                [sg.T('',size=(3,1)),sg.T(p_policy[9],size=(96,1))],
                                [sg.T('',size=(4,1)),sg.T(p_policy[10],size=(95,1))],
                                [sg.T('',size=(3,1)),sg.T(p_policy[11],size=(96,1))],
                                [sg.T('',size=(4,1)),sg.T(p_policy[12],size=(95,1))],
                                [sg.T('',size=(30,1)),sg.T(p_policy[13],size=(69,1),text_color='orange')],
                                [sg.T('',size=(45,1)),sg.Button("ok",size=(10,1))]
                                ]

#-------------layout for rules and regulations---------

rules=[
                                [sg.T(p_policy[0],size=(103,1),text_color='red',justification='center')],
                                [sg.T('',size=(2,1)),sg.T(p_rules[1],size=(100,1))],
                                [sg.T('',size=(2,1)),sg.T(p_rules[2],size=(100,1))],
                                [sg.T('',size=(2,1)),sg.T(p_rules[3],size=(100,1))],
                                [sg.T('',size=(2,1)),sg.T(p_rules[4],size=(100,1))],
                                [sg.T('',size=(4,1)),sg.T(p_rules[5],size=(98,1))],
                                [sg.T('',size=(2,1)),sg.T(p_rules[6],size=(97+3,1))],
                                [sg.T('',size=(2,1)),sg.T(p_rules[7],size=(97+3,1))],
                                [sg.T('',size=(4,1)),sg.T(p_rules[8],size=(98,1))],
                                [sg.T('',size=(2,1)),sg.T(p_rules[9],size=(97+3,1))],
                                [sg.T('',size=(2,1)),sg.T(p_rules[10],size=(97+3,1))],
                                [sg.T('',size=(2,1)),sg.T(p_rules[11],size=(97+3,1))],
                                [sg.T('',size=(2,1)),sg.T(p_rules[12],size=(97+3,1))],
                                [sg.T('',size=(30,1)),sg.Button('Ok',size=(9,1))]
                                ]

#-------layout for outer layout-------
 
L1=[
        [sg.T('',size=(15,1))],
        [sg.T('Best Billing management application all over India......',size=(60,1),font=('Helventica',19))],
        [sg.T('...........The best freind of Retailer',justification='right',size=(60,1),font=('Helventica',19))],
        [sg.T('New Member ?--(click here)---->>>',size=(105,1),justification='right',text_color='#34495E'),sg.RButton('ENTER',size=(8,1))],
        [sg.Button('Read Privacy Policy',size=(17,2)),
         sg.Button('Read Rules',size=(11,2)),
         sg.Button('Developer Information',size=(17,2)),
         sg.T('',size=(36,1)),
         sg.T('want to exit-(click here)-->>>',justification='right',size=(15,1),text_color='#34495E'),
         sg.Button('Exit',size=(8,1))]
        ]

#---------------main working layout---------


L_M=[
    [sg.T('',size=(15,1))],
    [sg.T('Best Billing management application all over India',size=(40,1),text_color='red',font=('Helventica',19))],
    [sg.T('.......Quality Matters',justification='right',size=(40,1),font=('Helventica',19))],
    [sg.T("",key='k1')],
    [sg.T('',key='k2')],
    [sg.Frame('',layout=[[sg.T('----Product Name'),sg.T('',size=(8,1)),sg.T('----Quantity')],
                         [sg.Checkbox('Parle-G'),sg.T('',size=(17,1)),sg.In('',size=(5,1))],
                         [sg.Checkbox('Parle-G Bheem'),sg.T('',size=(9+3,1)),sg.In('',size=(5,1))],
                         [sg.Checkbox('20-20 Butter'),sg.T('',size=(9+5,1)),sg.In('',size=(5,1))],
                         [sg.Checkbox('20-20 Cashew'),sg.T('',size=(9+3,1)),sg.In('',size=(5,1))],
                         [sg.Checkbox('Good-Day'),sg.T('',size=(9+7,1)),sg.In('',size=(5,1))],
                         [sg.Checkbox('Uncle Chips'),sg.T('',size=(9+5,1)),sg.In('',size=(5,1))],
                         [sg.Checkbox('Kurkure'),sg.T('',size=(9+8,1)),sg.In('',size=(5,1))],
                         [sg.Checkbox('Pepsi'),sg.T('',size=(9+10,1)),sg.In('',size=(5,1))],
                         [sg.Checkbox('Sprite'),sg.T('',size=(9+10,1)),sg.In('',size=(5,1))],
                         [sg.Checkbox('Bikanari Bhujia'),sg.T('',size=(9+3,1)),sg.In('',size=(5,1))],
                         [sg.Checkbox('Moong Daal'),sg.T('',size=(9+6,1)),sg.In('',size=(5,1))],
                         [sg.Checkbox('Kuch-Kuch'),sg.T('',size=(9+6,1)),sg.In('',size=(5,1))]])],
    [sg.Ok()]
    ]
Rup5=['Parle-G','Parle-G Bheem','20-20 Butter','20-20 Cashew']
#-------------------layout for Enter -------
 
L2=[
        [sg.T('Welcome to our',size=(30,1),font=('Courier',32))],
        [sg.T('',size=(15,1))],
        [sg.T('Hotel Management System',size=(30,1),font=('Helventica',37),text_color='#F39C12',justification='center')],
        [sg.T('Please Fill Mandatory Details :-',size=(30,1),font=('Helventica',21))],
        [sg.T('Enter your Name:-',size=(25,1),font=('Courier',20)),sg.In(background_color='lightblue')],
        [sg.T("Enter your Father's Name:-",size=(25,1),font=('Courier',20)),sg.In(background_color='lightblue')],
        [sg.T('Enter your Mobile Number:-',size=(25,1),font=('Courier',20)),sg.In(background_color='lightblue')],
        [sg.T('Enter your City:-',size=(25,1),font=('Courier',20)),sg.In(background_color='lightblue')],
        [sg.T('Enter your Age:-',size=(25,1),font=('Courier',20)),sg.Spin(values=('15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50'), initial_value='17',size=(3,1))],
        [sg.T('',size=(6,1)),sg.Button('Submit',size=(7,1)),sg.Button('Cancel',size=(7,1)),sg.Button('Home',size=(7,1))]
        ]

#----------------status of windows (Also known as Flag mechanism )---------
 
s_enter=False
s_submit_signin=False

#-------------window for application--------

w1=sg.Window('Hotel Management App - main window').Layout(L1)

#-------------event loop(as many times loop have to be iterated )-----
w2=sg.Window('Information').Layout(L2)

def bill(v):
    j=0
    k=0
    for i in range(len(v)):
        if (v[i]=="True"):
            if(v[i+1] in Rup5):
                j+=1
            else:
                k+=1
    value=j*5+k*10
    return value



while True:
    e1,v1=w1.Read()
    if(not s_enter and e1=='ENTER'):
        s_enter=True
        w1.Hide()
        while True:
            e2,v2=w2.Read()
            if(e2=='Home'):
                s_enter=False
                w1.UnHide()
                w2.Hide()
                break
            elif (e2 in (None,'Cancel')):
                w2.Close()
                w1.UnHide()
                break
            elif(e2=='Submit' and not s_submit_signin):
                s_submit_signin=True
                w2.Hide()
                insert(2,v2)
                w3=sg.Window('Main').Layout(L_M)
                while True:
                    e3,v3=w3.Read()
                    if (e3=='Ok'):
                        w3.FindElement('k1').Update('Your Bill Value is:-')
                        w3.FindElement('k2').Update(bill(v3))
                        break
                    
                break
    elif(e1=='Read Privacy Policy'):
        w=sg.Window('').Layout(p_p)
        e,v=w.Read()
        w.Close()
    elif(e1=='Developer Information'):
        w=sg.Window('').Layout(p_i)
        e,v=w.Read()
        w.Close()
    elif(e1=='Read Rules'):
        w=sg.Window('').Layout(rules)
        e,v=w.Read()
        w.Close()
    elif(e1 in (None,'Exit')):
        w1.Close()
        break


#unpack coomit at line 24 &31
