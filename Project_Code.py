#TYPING SPEED TEST WITH GUI USING TKINTER AND RANDOM
#PYTHON PROJECT-4CP50
#20CP018-VEDANT DHAMECHA
#20CP003-SRUSHTI MALAVIYA

# Import necessary modules from tkinter and random.
from tkinter import *
from random import randint

# Create a Tkinter window.
windows = Tk()
windows.title('Typing Speed Test 20CP003|20CP018')

# Set the minimum size for the window.
windows.minsize(width='1200', height='800')

# Load a background image.
background = PhotoImage(file="py1.png")

# Create a label and place the background image on the window.
label1 = Label(windows, image=background)
label1.place(x=0, y=0)

# Initialize variables for the typing speed test.
running = False  # Flag to track whether the test is running.
seconds = 60      # Total time for the test (in seconds).

errors = 0         # Initialize the error count.
tychar = 1         # Initialize the typed character count.
char = 0           # Initialize the total character count.
read = 0           # Initialize the read character count.
str = ''           # Initialize the text string.

# Create a function to draw a rectangle on the window.
def rectangle():
    canvas = Canvas(windows, width=1000, height=300)
    canvas.place(x=100, y=80)
    canvas.create_rectangle(0, 0, 1100, 400, fill="#edc7b7")



# Create a function to calculate typing statistics.
def calculator():
    global errors
    global tychar
    global char
    global accuracy
    global netwpm
    netwpm = char
    if read != 0:
        accuracy = (tychar / read) * 100



# Create a function to generate random text for the test.
def random_text_generate():
    rectangle()
    #list
    names = ["We", "I", "They", "He", "She", "Jack", "Jim", "Rose"]
    verbs = ["is", "was", "are", "were"]
    nouns = ["reading", "playing", "watching TV", "talking", "dancing", "speaking"]
    l = 23 #how many sentences want to generate
    global str
    str = ''
    #generating sentences
    for i in range(1, l + 1):
        str += names[randint(0, len(names) - 1)] + " " + verbs[randint(0, len(verbs) - 1)] + " " + nouns[randint(0, len(nouns) - 1)]
        str += '. '

    #showing the generated text
    global main_text
    main_text = Label(windows, text=str, font=('Times New Roman', 20, 'bold'), bg="#edc7b7", bd=0, foreground='#123c69', wraplength=950)
    main_text.place(x=140, y=150)

    #shows "Type:"
    global typch
    typch = Label(windows, text='Type: ', font=('Times New Roman', 20, 'bold'), bg="#edc7b7", bd=0, foreground='#123c69')
    typch.place(x=500, y=100)
    
    #shows the first character from the string
    global typdis
    typdis = Label(windows, text=str[0], font=('Times New Roman', '20', 'bold'), bg="#edc7b7")
    typdis.place(x=570, y=100)

    #length of generated text.
    global lens
    lens = len(str)



# Create a function to enable typing input.
def write():
    if seconds <= 60:
        global writeAble
        writeAble = True
        #when key pressed keypress function called
        windows.bind('<Key>', keyPress)




# Define a function to handle keypress events.
def keyPress(event=None):
    global errors
    global tychar
    global char
    global spot
    global typdis
    global err_dis
    global read
    global running
    global lens

    # Check if the spot has reached the end of the text.
    if spot == lens - 1:
        # Update the main text, cancel the timer, and display a completion message.
        main_text.configure(text=main_text.cget('text')[1:])
        timer.after_cancel(update_time)
        running = False
        global timeup
        #congratulation
        timeup = Label(windows, text="Congratulations", font=('Times New Roman', 50, 'bold'), bg="#A0E4CB", bd=0, foreground='Red')
        timeup.place(x=350, y=200)
        typdis.config(text='Completed')
        return
    elif event.char == main_text.cget('text')[0] and seconds >= 0 and seconds < 60:
        # If the typed character matches the expected character, update the main text and statistics.
        main_text.configure(text=main_text.cget('text')[1:])
        tychar += 1
        spot += 1
        if str[spot] == ' ' and spot != lens:
            typdis.config(text='Space')
        else:
            typdis.config(text=main_text.cget('text')[0])
        if main_text.cget('text')[0] == ' ':
            char += 1
        if (event.char >= 'a' and event.char <= 'z') or (event.char >= 'A' and event.char <= 'Z') or (event.char == ' ') or (event.char == ',') or (event.char == '.'):
            read += 1
    else:
        # If there's a typing error, update the error count.
        if ((event.char >= 'a' and event.char <= 'z') or (event.char >= 'A' and event.char <= 'Z') or (event.char == ' ') or (event.char == ',') or (event.char == '.')) and seconds > 0 and seconds < 60:
            errors += 1
            err_dis.config(text=errors)
            read += 1



    # Update typing accuracy and speed.
    global accu_dis
    global speed_dis
    calculator() #calculates the accuracy by calling function
    global accuracy
    global netwpm
    # Display the calculated accuracy and speed.
    if read != 0:
        #printing accuracy in below format
        accu_dis.config(text="{:.2f} %".format(accuracy))
    speed_dis.config(text=f'{netwpm} WPM')



# Define a function to start the typing test.
def start():
    global errors
    global tychar
    global running

    # Check if the test is not already running.
    if not running:
        update()  # Start the timer.
        errors = 0  # Reset error count.
        tychar = 0  # Reset typed character count.
        running = True
        timer.config(foreground='black')

# Define a function to reset the typing test.
def reset():
    global running

    # Check if the test is running, and if so, cancel the timer.
    if running:
        timer.after_cancel(update_time)
        running = False

    global seconds
    seconds = 60
    timer.config(text='60')
    timer.config(foreground='black')

    # Reset various statistics and labels.
    global errors
    errors = 0
    err_dis.config(text=errors)

    global accuracy
    global netwpm
    accuracy = 0
    netwpm = 0

    global tychar
    tychar = 0
    accu_dis.config(text='0.0 %')
    speed_dis.config(text='00 WPM')

    global read
    read = 0

    global char
    char = 0

    global spot
    spot = 0

# Define a function to update the timer during the test.
def update():
    global seconds
    seconds -= 1

    # Check if time is up.
    if seconds == -1:
        global timeup
        timeup = Label(windows, text="Time's up", font=('Times New Roman', 50, 'bold'), bg="#A0E4CB", bd=0, foreground='Red')
        timeup.place(x=450, y=200)
        return
    #in last 10 sec shows with red color
    elif seconds < 10:
        timer.config(foreground='red')

    # Format the remaining time as a string. (agad 2 digit banava mate 0 lagadvo if <9 hoy to)
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    timer.config(text=seconds_string)

    global update_time
    # Schedule the update function to run again after 1000 milliseconds (1 second).
    update_time = timer.after(1000, update)


#GUI PART -------------------------------------------------
# Define a function to start the typing test.
def start_type():
    # Remove all existing widgets from the window.
    for widget in windows.winfo_children():
        widget.destroy()

    # Configure the background and set the title label.
    windows.config(bg="#eee2dc")
    title = Label(text='TYPING SPEED TEST  20CP003|20CP018', font=('Rockwell Extra Bold', 25, 'bold'), bg="#eee2dc", foreground='#ac3b61')
    title.place(x=250, y=10)

    # Create and place the timer label.
    global timer
    timer = Label(windows, text='60', font=('Bree serif', '20', 'bold'), bg="#eee2dc")
    timer.place(x=270, y=417)

    # Create labels for time, speed, accuracy, and errors.
    text1 = Label(windows, text='Time: ', font=('Times New Roman', 20, 'bold'), bg="#eee2dc", bd=0, foreground='#123c69')
    text1.place(x=190, y=417)

    speed_tx = Label(windows, text='Speed: ', font=('Times New Roman', 20, 'bold'), bg="#eee2dc", bd=0, foreground='#123c69')
    speed_tx.place(x=440, y=417)

    accu_tx = Label(windows, text='Accuracy: ', font=('Times New Roman', 20, 'bold'), bg="#eee2dc", bd=0, foreground='#123c69')
    accu_tx.place(x=800, y=417)

    err_tx = Label(windows, text='Errors: ', font=('Times New Roman', 20, 'bold'), bg="#eee2dc", bd=0, foreground='#123c69')
    err_tx.place(x=480, y=480)

    # Generate random text for the test and create a "START" button.
    random_text_generate()
    start_btn = Button(windows, text='START', font=('Bree serif', '10', 'bold'), bg='#ea3548', bd=0, fg='#fff', width=20, height=2, command=lambda: [start(), write()])
    start_btn.place(x=200, y=650)

    # Create labels to display typing speed, accuracy, and errors.
    global speed_dis
    speed_dis = Label(windows, text='00 WPM', font=('Bree serif', '20', 'bold'), bg="#eee2dc")
    speed_dis.place(x=525, y=417)

    global accu_dis
    accu_dis = Label(windows, text='0.0%', font=('Bree serif', '20', 'bold'), bg="#eee2dc")
    accu_dis.place(x=930, y=417)

    global err_dis
    err_dis = Label(windows, text='0', font=('Bree serif', '20', 'bold'), bg="#eee2dc")
    err_dis.place(x=580, y=480)

    # Create a "RESET" button.
    reset_btn = Button(windows, text='RESET', font=('Bree serif', '10', 'bold'), bg='#ea3548', bd=0, fg='#fff', width=20, height=2, command=lambda: [reset(), random_text_generate()])
    reset_btn.place(x=800, y=650)

# Load a start button image and create a button to initiate the typing test.
start_img = PhotoImage(file='button_start.png')
button = Button(windows, image=start_img, bg='white', command=start_type)
button.place(x=900, y=250)

# Start the main event loop to display the window and run the application.
windows.mainloop()
