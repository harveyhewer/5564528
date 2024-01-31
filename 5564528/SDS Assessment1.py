
#Importing libraries

from guizero import *
import numpy as np


def mainMenu():

    #Generates screen for main menu

    def hidemainmenu():

        #Hides main menu and opens login screen

        mainmenu.hide()
        login()

    def exitsystem():
        
        #Subroutine to exit the system
        
        mainmenu.hide()
        exit()

    def login():

        def hidelogin():

            #Hides login screen to allow for user to return to main menu

            login.hide()
            mainMenu()
            
            

        def verify_Login():

            def hidemainforadmin():

                login.hide()
                admin_Menu()

            def admin_Menu():

                def hideadminformain():

                    adminmenu.hide()
                    mainMenu()

                def doctorviewtransition():

                    adminmenu.hide()
                    doctorview()

                def patientviewtransition():

                    adminmenu.hide()
                    patientview()

                def patientview():

                    def hidepatientdataforadmin():

                        #Hides the patient data screen and returns to admin menu

                        patientdata.hide()
                        admin_Menu()

                    def freezepatientdataforremove():

                        patientdata.disable()
                        patient_Remove()

                    def patient_Remove():

                        #Subroutine to remove patient records

                        def hidepatientremoveforpatientdata():
                        
                            #Subroutine to hide the remove window and then run the remove subroutine

                            remove.hide()
                            patientdata.hide()
                            Remove()

                        def returntopatientdata():

                            #Subroutine to return to patient data from remove

                            remove.hide()
                            patientdata.enable()


                        def Remove():
                            
                            #Subroutine to remove the doctor record accosiated with the username the user provided

                            search = username.value

                            current_Array = np.genfromtxt('User_Database.txt', dtype=str, encoding=None)
                            
                            num_rows, num_cols = current_Array.shape

                            search_Criteria = False

                            for x in np.nditer(current_Array):
                                if x == search:
                                    search_Criteria = True
                                    for i in range(0,num_rows):
                                        if current_Array[i][0] == search:
                                            oldrecord = [current_Array[i][0], current_Array[i][1], 'p', current_Array[i][3], current_Array[i][4], current_Array[i][5]]
                                            np.savetxt("Old_Records.txt", oldrecord,fmt='%s')
                                            current_Array = np.delete(current_Array, i, axis=0)
                                            np.savetxt("User_Database.txt", current_Array,fmt='%s')
                                            patientview()
                            if search_Criteria == False:
                                remove.warn('Error', 'Search criteria not found')

                        #patient_Remove
                        #Creating the window where the user inputs the username of the patient record they want to remove from the database

                        remove = Window(patientdata, title='REMOVE', height=150, width=400, bg='white')
                        message = Text(remove, text='REMOVE')
                        
                        searchbox = Box(remove)
                        searchtext = Text(searchbox, text='Enter the username of patient you want to remove')
                        username = TextBox(searchbox, width = 30)

                        back = PushButton(remove, align = 'right', text='Back', command=returntopatientdata)
                        button = PushButton(remove, text='Enter', align='right', command=hidepatientremoveforpatientdata)
                

                    def hidedataforapplications():

                        #Hides the patient screen to allow user to view applications to the medical center

                        patientdata.hide()
                        applications()
                        
                    #View/manage the doctors within the organisation

                    patientdata = Window(adminmenu, title='PATIENT DATA', layout='grid', height=200, width=1050, bg='white')
                
                    usercolumn = Box(patientdata, grid=[0,0], height=200, width=100, border = 1)
                    usercolumntxt = Text(usercolumn, text='Username')

                    passcolumn = Box(patientdata, grid=[1,0], height=200, width=100, border = 1)
                    passcolumntxt = Text(passcolumn, text='Password')

                    namecolumn = Box(patientdata, grid=[3,0], height=200, width=100, border = 1)
                    namecolumntxt = Text(namecolumn, text='Name')

                    surnamecolumn = Box(patientdata, grid=[4,0], height=200, width=100, border = 1)
                    surnamecolumntxt = Text(surnamecolumn, text='Surname')

                    addresscolumn = Box(patientdata, grid=[5,0], height=200, width=100, border = 1)
                    addresscolumntxt = Text(addresscolumn, text='Address')

                    #Recovering staff data from text file to present in table

                    current_Array = np.genfromtxt('User_Database.txt', dtype=str, encoding=None)

                    num_rows, num_cols = current_Array.shape

                    for i in range(0,num_rows):


                        #Checking each record for doctors

                        if current_Array[i][2] == 'p':
                            
                            #Populating the doctor data table with every doctor record
                        
                            useraddition = Text(usercolumn, text=current_Array[i][0])

                            passaddition = Text(passcolumn, text=current_Array[i][1])

                            nameaddition = Text(namecolumn, text=current_Array[i][3])

                            surnameaddition = Text(surnamecolumn, text=current_Array[i][4])

                            addressaddition = Text(addresscolumn, text=current_Array[i][5])

                    buttons = Box(patientdata, grid=[8,0])
                    button2 = PushButton(buttons, text='View Applications', width=30, command=hidedataforapplications)
                    button3 = PushButton(buttons, text='Remove Patient', width=30, command=freezepatientdataforremove)
                    back = PushButton(buttons, text='Back', width=30, command=hidepatientdataforadmin)

                def oldrecordstransition():

                    #Transitioning to old record screen

                    adminmenu.hide()
                    oldrecord()
                    

                def changepersonalrecord():

                    def append():

                        def returntoadminscreen():

                            #Subroutine to return to admin menu from append screen

                            appendscreen.hide()
                            admin_Menu()


                        def final_Append():

                            #Newly appended staff data is recombined with the staff database and stored in a text file
                                    
                            newentry = np.array([username.value.replace(" ", ""), password.value.replace(" ", ""), 'a', name.value.replace(" ", ""), surname.value.replace(" ", ""), address.value.replace(" ", "")])
                            
                            new_Array = np.vstack((replacement_Array, newentry))
                            np.savetxt("User_Database.txt", new_Array,fmt='%s')
                                
    
                            appendscreen.hide()
                            admin_Menu()

                        #Generates the screen where the user is able to change their data
                        
                        appendscreen = Window(adminmenu, title='APPEND')
                        message = Text(appendscreen, text='APPEND')
                                
                        userbox = Box(appendscreen, border = 1, height = 30, width = 'fill')
                        usertext = Text(userbox, align='left', text='Username:')
                        username = TextBox(userbox, width = 30, align='right', text=append_Array[0])

                        passbox = Box(appendscreen, border = 1, height = 30, width = 'fill')
                        passtext = Text(passbox, align='left', text='Password:')
                        password = TextBox(passbox, width = 30, align='right', text=append_Array[1])
                                    
                        namebox = Box(appendscreen, border = 1, height = 30, width = 'fill')
                        nametext = Text(namebox, align='left', text='First Name:')
                        name = TextBox(namebox, width = 30, align='right', text=append_Array[3])
                                    
                        surbox = Box(appendscreen, border = 1, height = 30, width = 'fill')
                        surtext = Text(surbox,align='left', text='Second Name:')
                        surname = TextBox(surbox, width = 30, align='right', text=append_Array[4])
                                    
                        addressbox = Box(appendscreen, border = 1, height = 30, width = 'fill')
                        addresstext = Text(addressbox, align='left', text='Address:')
                        address = TextBox(addressbox, width = 30, align='right', text=append_Array[5])

                                    
                        back = PushButton(appendscreen, align = 'right', text='Back', command=returntoadminscreen)
                        button = PushButton(appendscreen, align = 'right', text='Append Data', command=final_Append)
                        
                    #Subroutine to allow admin to change personal detailw

    

                    current_Array = np.genfromtxt('User_Database.txt', dtype=str, encoding=None)
                        
                    num_rows, num_cols = current_Array.shape

                    username = 'admin'

                  
                    
                    for x in np.nditer(current_Array):
                        if x == username:
                            for i in range(0,num_rows):
                                if current_Array[i][0] == username:
                                    row = i
                                    append_Array = [current_Array[row][0], current_Array[row][1], 'a', current_Array[row][3], current_Array[row][4], current_Array[row][5]]
                                    replacement_Array = np.delete(current_Array, i, axis=0)
                                    append()
                                 

                                    
                def personaltransition():

                    #Subroutine to return
                    
                    
                    adminmenu.hide()
                    changepersonalrecord()
                    
                def oldrecord():


                    def backtoadmin():

                        #Subroutine that takes you from old records back to admin menu

                        olddata.hide()
                        admin_Menu()

                    #View old records

                    olddata = Window(adminmenu, title='OLD DATA', layout='grid', height=200, width=1050, bg='white')
                
                    usercolumn = Box(olddata, grid=[0,0], height=200, width=100, border = 1)
                    usercolumntxt = Text(usercolumn, text='Username')

                    passcolumn = Box(olddata, grid=[1,0], height=200, width=100, border = 1)
                    passcolumntxt = Text(passcolumn, text='Password')

                    namecolumn = Box(olddata, grid=[3,0], height=200, width=100, border = 1)
                    namecolumntxt = Text(namecolumn, text='Name')

                    surnamecolumn = Box(olddata, grid=[4,0], height=200, width=100, border = 1)
                    surnamecolumntxt = Text(surnamecolumn, text='Surname')

                    addresscolumn = Box(olddata, grid=[5,0], height=200, width=100, border = 1)
                    addresscolumntxt = Text(addresscolumn, text='Address')

                    back = PushButton(olddata, align = 'right', text='Back', command=backtoadmin)
                                

                    #Recovering staff data from text file to present in table

                    current_Array = np.genfromtxt('Old_Records.txt', dtype=str, encoding=None)

                    num_rows, num_cols = current_Array.shape

                    for i in range(0,num_rows):

                    #Populating the doctor data table with every doctor record
                        
                        useraddition = Text(usercolumn, text=current_Array[i][0])

                        passaddition = Text(passcolumn, text=current_Array[i][1])

                        nameaddition = Text(namecolumn, text=current_Array[i][3])

                        surnameaddition = Text(surnamecolumn, text=current_Array[i][4])

                        addressaddition = Text(addresscolumn, text=current_Array[i][5])

                def Report():

                    #Subroutine that generates report
                    

                    def reportgenerator():

                        def backtoadmin():

                            #Subroutine to return to admin menu

                            report.hide()
                            admin_Menu()

                        report = Window(adminmenu, title='REPORT', layout='grid', height='200', width=1050, bg='white')

                        numofdocs = Box(report, grid=[0,0], height=200, width=200, border = 1)
                        numberofdoctors = Text(numofdocs, text='Number of Doctors: ')
                        numberofd = Text(numofdocs, text=p)
                       

                        back = PushButton(numofdocs, align = 'right', text='Back', command=backtoadmin)
                        
                        

                    current_Array = np.genfromtxt('User_Database.txt', dtype=str, encoding=None)
                        
                    num_rows, num_cols = current_Array.shape

                    username = 'admin'
                    
                    p = 0
                    
                    for x in np.nditer(current_Array):
                        if x == username:
                            for i in range(0,num_rows):
                                if current_Array[i][2] == 'd':
                                    p = p + 1
                                    row = i
                                    append_Array = [current_Array[row][0], current_Array[row][1], 'a', current_Array[row][3], current_Array[row][4], current_Array[row][5]]
                                    replacement_Array = np.delete(current_Array, i, axis=0)
                    reportgenerator()

                def reporttransition():

                    #Subroutine for opening the management report

                    adminmenu.hide()
                    Report()

                    
                def doctorview():


                    def hidedoctordataforadmin():

                        doctordata.hide()
                        adminmenu()

                    def hidedoctordataforadd():

                        doctordata.hide()
                        add()

                    def freezedoctordataforremove():

                        doctordata.hide()
                        doctor_Remove()

                    def freezedoctordataforappend():

                        doctordata.disable()
                        doctor_append()

                    def doctor_append():


                        def hideappendforappend():

                            #Subroutine to hide staff append and then run the append subrotuine

                            append.hide()
                            doctordata.hide()
                            Append()

                        def returntodoctordata():

                            #Subroutine to return to staff data from append screen

                            append.hide()
                            doctordata.enable()

                        def Append():
                            
                            def append_Screen():

                                def returntodoctordata():

                                    #Subroutine to return to staff data from append screen

                                    appendscreen.hide()
                                    doctorview()

                                def final_Append():

                                    #Newly appended staff data is recombined with the staff database and stored in a text file
                                    
                                    newentry = np.array([username.value.replace(" ", ""), password.value.replace(" ", ""), 'd', name.value.replace(" ", ""), surname.value.replace(" ", ""), address.value.replace(" ", "")])
                            
                                    new_Array = np.vstack((replacement_Array, newentry))
                                    np.savetxt("User_Database.txt", new_Array,fmt='%s')
                                
    
                                    appendscreen.hide()
                                    doctorview()
                                
                                #append_Screen
                                #Generating the screen where the user is able to input the amended staff data

                                appendscreen = Window(append, title='APPEND')
                                message = Text(appendscreen, text='APPEND')
                                
                                userbox = Box(appendscreen, border = 1, height = 30, width = 'fill')
                                usertext = Text(userbox, align='left', text='Username:')
                                username = TextBox(userbox, width = 30, align='right', text=append_Array[0])

                                passbox = Box(appendscreen, border = 1, height = 30, width = 'fill')
                                passtext = Text(passbox, align='left', text='Password:')
                                password = TextBox(passbox, width = 30, align='right', text=append_Array[1])
                                
                                namebox = Box(appendscreen, border = 1, height = 30, width = 'fill')
                                nametext = Text(namebox, align='left', text='First Name:')
                                name = TextBox(namebox, width = 30, align='right', text=append_Array[3])
                                
                                surbox = Box(appendscreen, border = 1, height = 30, width = 'fill')
                                surtext = Text(surbox,align='left', text='Second Name:')
                                surname = TextBox(surbox, width = 30, align='right', text=append_Array[4])
                                
                                addressbox = Box(appendscreen, border = 1, height = 30, width = 'fill')
                                addresstext = Text(addressbox, align='left', text='Address:')
                                address = TextBox(addressbox, width = 30, align='right', text=append_Array[5])

                                
                                back = PushButton(appendscreen, align = 'right', text='Back', command=returntodoctordata)
                                button = PushButton(appendscreen, align = 'right', text='Append Data', command=final_Append)

                        
                            #def append()
                            #Finding row accosiated with staffID the user inputted and then removing it from the main array
                            
                            
                            search = username.value

                            current_Array = np.genfromtxt('User_Database.txt', dtype=str, encoding=None)
                            
                            num_rows, num_cols = current_Array.shape

                            search_Criteria = False

                            for x in np.nditer(current_Array):
                                if x == search:
                                    search_Criteria = True
                                    for i in range(0,num_rows):
                                        if current_Array[i][0] == search:
                                            row = i

                                            append_Array = [current_Array[row][0], current_Array[row][1], 'd', current_Array[row][3], current_Array[row][4], current_Array[row][5]]
                                            replacement_Array = np.delete(current_Array, i, axis=0)
                        
                                            append_Screen()
                                            
                                            
                            if search_Criteria == False:
                                append.warn('Error', 'Search criteria not found')
                        
                        #staff_Append
                        #Creating the screen where the user inputs the ID of the staff record they want to append
                        
                        append = Window(doctordata, title='APPEND', height=150, width=400, bg='white')
                        message = Text(append, text='APPEND')
                        
                        searchbox = Box(append)
                        searchtext = Text(searchbox, text='Enter the username of the doctor you want to append')
                        username = TextBox(searchbox, width = 30)

                        back = PushButton(append, align = 'right', text='Back', command=returntodoctordata)
                        button = PushButton(append, text='Enter', align='right', command=hideappendforappend)

                    def doctor_Remove():
                    
                        def hidestaffremoveforstaffdata():
                        
                            #Subroutine to hide the remove window and then run the remove subroutine

                            remove.hide()
                            doctordata.hide()
                            remove()

                        def returntostaffdata():

                            #Subroutine to return to doctor data from remove

                            remove.hide()
                            doctordata.enable()


                        def remove():
                            
                            #Subroutine to remove the doctor record accosiated with the username the user provided

                            search = username.value

                            current_Array = np.genfromtxt('User_Database.txt', dtype=str, encoding=None)
                            
                            num_rows, num_cols = current_Array.shape

                            search_Criteria = False

                            for x in np.nditer(current_Array):
                                if x == search:
                                    search_Criteria = True
                                    for i in range(0,num_rows):
                                        if current_Array[i][0] == search:
                                            current_Array = np.delete(current_Array, i, axis=0)
                                            np.savetxt("User_Database.txt", current_Array,fmt='%s')
                                            staff_Data()
                            if search_Criteria == False:
                                staffremove.warn('Error', 'Search criteria not found')

                        #staff_Remove
                        #Creating the window where the user inputs the staffID of the staff record they want to remove from the database

                        remove = Window(doctordata, title='REMOVE', height=150, width=400, bg='white')
                        message = Text(remove, text='REMOVE')
                        
                        searchbox = Box(remove)
                        searchtext = Text(searchbox, text='Enter the username of doctor you want to remove')
                        username = TextBox(searchbox, width = 30)

                        back = PushButton(remove, align = 'right', text='Back', command=returntostaffdata)
                        button = PushButton(remove, text='Enter', align='right', command=hidestaffremoveforstaffdata)

                    def hidedoctordataforadmin():

                        #Returns to admin menu from doctor data

                        doctordata.hide()
                        admin_Menu()

                    def add():

                        def hideaddfordata():

                            doctoradd.hide()
                            doctorview()

                        def save():

                            #Subroutine that stores new data into file

                            newentry = np.array([username.value.replace(" ", ""), password.value.replace(" ", ""), 'd', name.value.replace(" ", ""), surname.value.replace(" ", ""), address.value.replace(" ", "")])
    
                            current_Array = np.genfromtxt('User_Database.txt', dtype=str, encoding=None)
                            new_Array = np.vstack((current_Array, newentry))
                            np.savetxt("User_Database.txt", new_Array,fmt='%s')
                            
                            doctorview()
            
                        #Subroutine for adding new doctor to system

                        doctoradd = Window(doctordata, title='ADD')
                        text = Text(doctoradd, text='ADD')
                        
                        userbox = Box(doctoradd, border = 1, height = 30, width = 'fill')
                        usertext = Text(userbox, align='left', text='Username:')
                        username = TextBox(userbox, width = 30, align='right')

                        passbox = Box(doctoradd, border = 1, height = 30, width = 'fill')
                        passtext = Text(passbox, align='left', text='Password:')
                        password = TextBox(passbox, width = 30, align='right')
                        
                        namebox = Box(doctoradd, border = 1, height = 30, width = 'fill')
                        nametext = Text(namebox, align='left', text='First Name:')
                        name = TextBox(namebox, width = 30, align='right')
                        
                        surbox = Box(doctoradd, border = 1, height = 30, width = 'fill')
                        surtext = Text(surbox,align='left', text='Second Name:')
                        surname = TextBox(surbox, width = 30, align='right')
                        
                        addressbox = Box(doctoradd, border = 1, height = 30, width = 'fill')
                        addresstext = Text(addressbox, align='left', text='Address:')
                        address = TextBox(addressbox, width = 30, align='right')
                        
                        buttons = Box(doctoradd, align='right')
                        back = PushButton(buttons, align = 'right', text='Back', command=hideaddfordata)
                        button = PushButton(buttons, align = 'right', text='Add data', command=save)
                        
                    #View/manage the doctors within the organisation

                    doctordata = Window(adminmenu, title='DOCTOR DATA', layout='grid', height=200, width=1050, bg='white')
                
                    usercolumn = Box(doctordata, grid=[0,0], height=200, width=100, border = 1)
                    usercolumntxt = Text(usercolumn, text='Username')

                    passcolumn = Box(doctordata, grid=[1,0], height=200, width=100, border = 1)
                    passcolumntxt = Text(passcolumn, text='Password')

                    namecolumn = Box(doctordata, grid=[3,0], height=200, width=100, border = 1)
                    namecolumntxt = Text(namecolumn, text='Name')

                    surnamecolumn = Box(doctordata, grid=[4,0], height=200, width=100, border = 1)
                    surnamecolumntxt = Text(surnamecolumn, text='Surname')

                    addresscolumn = Box(doctordata, grid=[5,0], height=200, width=100, border = 1)
                    addresscolumntxt = Text(addresscolumn, text='Address')
                    
                    #Recovering staff data from text file to present in table

                    current_Array = np.genfromtxt('User_Database.txt', dtype=str, encoding=None)

                    num_rows, num_cols = current_Array.shape

                    for i in range(0,num_rows):


                        #Checking each record for doctors

                        if current_Array[i][2] == 'd':
                            
                            #Populating the doctor data table with every doctor record
                        
                            useraddition = Text(usercolumn, text=current_Array[i][0])

                            passaddition = Text(passcolumn, text=current_Array[i][1])

                            nameaddition = Text(namecolumn, text=current_Array[i][3])

                            surnameaddition = Text(surnamecolumn, text=current_Array[i][4])

                            addressaddition = Text(addresscolumn, text=current_Array[i][5])

                    buttons = Box(doctordata, grid=[8,0])
                    button2 = PushButton(buttons, text='Add doctor', width=30, command=hidedoctordataforadd)
                    button3 = PushButton(buttons, text='Remove doctor', width=30, command=freezedoctordataforremove)
                    button4 = PushButton(buttons, text='Append doctor data', width=30, command=freezedoctordataforappend)
                    back = PushButton(buttons, text='Back', width=30, command=hidedoctordataforadmin)
                    
                def hidemainforapplicant():

                    #Hides adminmenu to view applicant data

                    adminmenu.hide()
                    applicant()

                def applicant():

                    def applicanttoadmin():

                        #Subroutine that goes from applicant screen to admin menu

                        applicantdata.hide()
                        admin_Menu()

                    #Subroutine that allows admin to view applicant data

                    applicantdata = Window(adminmenu, title='Applications', layout='grid', height=200, width=1050, bg='white')
                
                    usercolumn = Box(applicantdata, grid=[0,0], height=200, width=100, border = 1)
                    usercolumntxt = Text(usercolumn, text='Username')

                    passcolumn = Box(applicantdata, grid=[1,0], height=200, width=100, border = 1)
                    passcolumntxt = Text(passcolumn, text='Password')

                    namecolumn = Box(applicantdata, grid=[3,0], height=200, width=100, border = 1)
                    namecolumntxt = Text(namecolumn, text='Name')

                    surnamecolumn = Box(applicantdata, grid=[4,0], height=200, width=100, border = 1)
                    surnamecolumntxt = Text(surnamecolumn, text='Surname')

                    addresscolumn = Box(applicantdata, grid=[5,0], height=200, width=100, border = 1)
                    addresscolumntxt = Text(addresscolumn, text='Address')
                    
                    #Recovering staff data from text file to present in table

                    current_Array = np.genfromtxt('Applications.txt', dtype=str, encoding=None)

                    num_rows, num_cols = current_Array.shape

                    for i in range(0,num_rows):
        
                    #Populating the doctor data table with every doctor record
                        
                        useraddition = Text(usercolumn, text=current_Array[i][0])

                        passaddition = Text(passcolumn, text=current_Array[i][1])

                        nameaddition = Text(namecolumn, text=current_Array[i][3])
    
                        surnameaddition = Text(surnamecolumn, text=current_Array[i][4])

                        addressaddition = Text(addresscolumn, text=current_Array[i][5])
                    
                    buttons = Box(applicantdata, grid=[8,0])
                    button2 = PushButton(buttons, text='Back', width=30, command=applicanttoadmin)                    
                    

                #Generates the admin menu

                adminmenu = Window(mainmenu,title='ADMIN MENU', bg = 'white')
                message = Text(adminmenu, text='ADMIN MENU')
                #picture2 = Picture(adminmenu, image='Safetyform.png', width= 500, height= 200)
                button = PushButton(adminmenu, text='View/Manage Doctors', width= 30, command=doctorviewtransition)
                button5 = PushButton(adminmenu, text='View/Manage Patient Record', width=30, command=patientviewtransition)
                button2 = PushButton(adminmenu, text='View Old Records', width=30, command=oldrecordstransition)
                button8 = PushButton(adminmenu, text='Update personal information', width= 30, command=personaltransition)
                button3 = PushButton(adminmenu, text='Management Report', width= 30, command=reporttransition)
                button6 = PushButton(adminmenu, text='Applications', width= 30, command=hidemainforapplicant)
                button4 = PushButton(adminmenu, text='Exit to Main Menu', width= 30, command=hideadminformain)


            def hidemainfordoctor():

                    #Subroutine that takes user to doctor menu

                    login.hide()
                    doctor_Menu()
                    
            def doctor_Menu():
               

                def hidedoctorformain():

                    #Subroutine that allows user to go from doctor menu to main menu

                    doctormenu.hide()
                    mainMenu()

                def hidedoctorforpatient():

                    #Subroutine to go from doctor menu to patient records

                    doctormenu.hide()
                    patientrecords()

                def patientrecords():

                    def patienttodoctor():

                        #Subroutine to return to doctor menu

                        patientdata.hide()
                        doctor_Menu()

                    #View/manage the doctors within the organisation

                    patientdata = Window(doctormenu, title='PATIENT DATA', layout='grid', height=200, width=1050, bg='white')
                
                    usercolumn = Box(patientdata, grid=[0,0], height=200, width=100, border = 1)
                    usercolumntxt = Text(usercolumn, text='Username')

                    passcolumn = Box(patientdata, grid=[1,0], height=200, width=100, border = 1)
                    passcolumntxt = Text(passcolumn, text='Password')

                    namecolumn = Box(patientdata, grid=[3,0], height=200, width=100, border = 1)
                    namecolumntxt = Text(namecolumn, text='Name')

                    surnamecolumn = Box(patientdata, grid=[4,0], height=200, width=100, border = 1)
                    surnamecolumntxt = Text(surnamecolumn, text='Surname')

                    addresscolumn = Box(patientdata, grid=[5,0], height=200, width=100, border = 1)
                    addresscolumntxt = Text(addresscolumn, text='Address')

                    #Recovering staff data from text file to present in table

                    current_Array = np.genfromtxt('User_Database.txt', dtype=str, encoding=None)

                    num_rows, num_cols = current_Array.shape

                    for i in range(0,num_rows):


                        #Checking each record for doctors

                        if current_Array[i][2] == 'p':
                            
                            #Populating the doctor data table with every doctor record
                        
                            useraddition = Text(usercolumn, text=current_Array[i][0])

                            passaddition = Text(passcolumn, text=current_Array[i][1])

                            nameaddition = Text(namecolumn, text=current_Array[i][3])

                            surnameaddition = Text(surnamecolumn, text=current_Array[i][4])

                            addressaddition = Text(addresscolumn, text=current_Array[i][5])

                    buttons = Box(patientdata, grid=[8,0])
                    back = PushButton(buttons, text='Back', width=30, command=patienttodoctor)

                    #Subroutine that allows doctor to view patient records

                    

                #Generates the doctor menu

                doctormenu = Window(login,title='DOCTOR MENU', bg = 'white')

                button = PushButton(doctormenu, text='View Appointments', width= 30,) #command=hidemainfordoctor)
                button5 = PushButton(doctormenu, text='View/Manage Patient Record', width=30, command=hidedoctorforpatient)
                button4 = PushButton(doctormenu, text='Exit to Main Menu', width= 30, command=hidedoctorformain)

                
            def hidemainforpatient():

                #Subroutine to allow for user to go from main menu to patient menu

                login.hide()
                patient_Menu()
                
            def patient_Menu():


                def hidepatientforappointment():

                    #Subroutine to hide patient screen for appointment screen

                    patientmenu.hide()
                    appointment()

                def hidepatientformain():

                    #Subroutine to hide patient screen for main menu

                    patientmenu.hide()
                    mainMenu()

                

                def appointment():

                    def hideappointmentforpatient():

                        #Subroutine to allow for user to go from appointment to patient screen

                        appointmentmenu.hide()
                        patient_Menu()

                    def hideappointmentformain():

                        #Subroutine to allow user to go from appointment to patient screen

                        appointmentmenu.hide()
                        patient_Menu()

                    def save():

                        newentry = np.array([username.value, date.value])

                        np.savetxt('Appointments.txt', newentry,fmt='%s')

                        appointmentmenu.hide()
                        patient_Menu()

                    #Subroutine to allow user to make appointments

                    appointmentmenu = Window(login,title='APPOINTMENT MENU', bg = 'white')
                            
                    userbox = Box(appointmentmenu, border = 1, height = 30, width = 'fill')
                    usertext = Text(userbox, align='left', text='Username:')
                    username = TextBox(userbox, width = 30, align='right')

                    datebox = Box(appointmentmenu, border = 1, height = 30, width = 'fill')
                    datetext = Text(datebox, align='left', text='Date:')
                    date = TextBox(datebox, width = 30, align='right')                    

                    button = PushButton(appointmentmenu, text='Book Appointment', width= 30, command=save)
                    button4 = PushButton(appointmentmenu, text='Exit', width= 30, command=hideappointmentforpatient)

                    

                #Generates the patient menu

                patientmenu = Window(login,title='PATIENT MENU', bg = 'white')

                button = PushButton(patientmenu, text='Book Appointment', width= 30, command=hidepatientforappointment)
                button4 = PushButton(patientmenu, text='Exit to Main Menu', width= 30, command=hidepatientformain)
            
                
            
            #Verifying the login information that the user inputted with the preexisiting copy of the username and the password
                        
            current_Array = np.genfromtxt('User_Database.txt', dtype=str, encoding=None)
                        
            num_rows, num_cols = current_Array.shape

            username_Present = False
            
            for x in np.nditer(current_Array):
                    if x == username.value:
                        username_Present = True
                        for i in range(0,num_rows):
                            if current_Array[i][0] == username.value:
                                row = i
                                append_Array = [username.value, current_Array[row][1], current_Array[row][2], current_Array[row][3], current_Array[row][4], current_Array[row][5]]
                                comparevalue = current_Array[row][1]
                                
                                #Sending user to relevant role menu
                                
                                if password.value == comparevalue:
                                    if append_Array[2] == 'a':
                                        
                                        hidemainforadmin()
                                        
                                    elif append_Array[2] == 'd':
                                        hidemainfordoctor()
                            
                                    else:
                                        hidemainforpatient()
                                
                                else:
                                    login.warn('Error', 'Incorrect password')
                                    
            if username_Present == False:
                login.warn('Error','Username not found in database')

        def showpassword():
            
            #Subroutine to allow the user to reveal the password
            
            login.info('Show Password','Password: ' + password.value)

        #Subroutine to generate the login screen


        login = Window(mainmenu, title=" LOGIN", bg='white')
        message = Text(login, text=" LOGIN")
        loginbox = Box(login)
        usernamebox = Box(loginbox)
        message2 = Text(usernamebox, align= 'left', text="Username:")
        username = TextBox(usernamebox, align='right',width = 30)
        passwordbox = Box(loginbox)
        message3 = Text(passwordbox, align= 'left', text='Password: ')
        password = TextBox(passwordbox, align='right', width = 30, hide_text=True)
        buttons = Box(loginbox)
        show = PushButton(buttons, align = 'left', width = 10, height = 1, text='Show password', command=showpassword)
        back = PushButton(buttons, align= 'right', width = 10, height = 1, text='Back',command=hidelogin)
        enter = PushButton(buttons, align = 'right', width = 10, height = 1, text='Enter', command=verify_Login)

    def hidemenu():

        #Subroutine to show the application screen

        mainmenu.hide()
        application()

    def application():

        def hideapplicationformain():

            #Subroutine to allow user to hide applicatn screen for main menu

            applicant.hide()
            mainMenu()

        def save():

            #Saves applicant data to applicant file

           

            newentry = np.array([username.value.replace(" ", ""), password.value.replace(" ", ""), 'p', name.value.replace(" ", ""), surname.value.replace(" ", ""), address.value.replace(" ", "")])
    
            current_Array = np.genfromtxt('Applications.txt', dtype=str, encoding=None)
            new_Array = np.vstack((current_Array, newentry))
            np.savetxt("Applications.txt", new_Array,fmt='%s')
                            
            mainMenu()

        #Subroutine to allow user to apply to medical centre

        applicant = Window(mainmenu, title='APPLY')
        text = Text(applicant, text='APPLY')
                        
        userbox = Box(applicant, border = 1, height = 30, width = 'fill')
        usertext = Text(userbox, align='left', text='Username:')
        username = TextBox(userbox, width = 30, align='right')

        passbox = Box(applicant, border = 1, height = 30, width = 'fill')
        passtext = Text(passbox, align='left', text='Password:')
        password = TextBox(passbox, width = 30, align='right')

        namebox = Box(applicant, border = 1, height = 30, width = 'fill')                
        nametext = Text(namebox, align='left', text='First Name:')
        name = TextBox(namebox, width = 30, align='right')
                        
        surbox = Box(applicant, border = 1, height = 30, width = 'fill')
        surtext = Text(surbox,align='left', text='Second Name:')
        surname = TextBox(surbox, width = 30, align='right')
                        
        addressbox = Box(applicant, border = 1, height = 30, width = 'fill')
        addresstext = Text(addressbox, align='left', text='Address:')
        address = TextBox(addressbox, width = 30, align='right')
                        
        buttons = Box(applicant, align='right')
        back = PushButton(buttons, align = 'right', text='Back', command=hideapplicationformain)
        button = PushButton(buttons, align = 'right', text='Add data', command=save)

        
        
        

    mainmenu = App(title="MAIN MENU", bg = 'white')
    message = Text(mainmenu, text="MAIN MENU")
    #picture = Picture(mainmenu, image='Healthcenterlogo.png', width= 500, height= 300)
    
    #Button to access login protal
    
    button = PushButton(mainmenu, text="Login", width= 25, command=hidemainmenu)

    #Button to apply for medical center

    button = PushButton(mainmenu, text="Apply to Medical Centre", width= 25, command=hidemenu)

    #Button to exit the system
    button3 = PushButton(mainmenu, text="Exit", width= 25, command=exitsystem)
    mainmenu.display()


mainMenu()
