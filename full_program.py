# Program sends an automated email to an email list of the user's choice
# Fixes Needed: - Run from gui instead of the necessity to return to terminal
#               - Login sequence from database needed
#               - Better User Interface?
#               - 

import customtkinter, webbrowser, time, re, pyautogui, threading

# set default colors of user interface
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

# set default for UI window
root = customtkinter.CTk() # variable for UI window
root.title("Email Automator") # add title to window
root.geometry("500x700") # 500 by 300 pixels by default

# method to send emails after input is received
def send_emails():
    threading._start_new_thread(lambda: None, ()) # necessary to prevent multiple threads from running simultaneously - pycharm IDE shows as an error, but it is functional code

    # call variables from input boxes upon button press
    company_name = initial_input_one.get()
    raw_email_input = initial_input_two.get()
    mass_message = initial_input_three.get()
    # Prompt the user for information
    local_width, local_height = pyautogui.size() # get screen dimensions of local machine
    local_width = local_width * 0.1215 # x dimension of 'send' button
    local_height = local_height * 0.967 # y dimension of 'send' button

    # Find all valid email addresses in the input text
    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b" # regex matching email format
    email_list = re.findall(email_regex, raw_email_input, flags=re.IGNORECASE) # pass 'raw_input' through regex to create list of emails

    # Compose the email message
    general_greeting = "Hello! I hope this email finds you well,\n"
    general_salutation = f"Best,\nThe people at {company_name}"
    body = mass_message
    final_email = f"{general_greeting}{body}\n{general_salutation}"

    # Prompt the user to open the Gmail website and login
    input("Press enter when you have opened Gmail in a new browser window and logged in\nASSURE THE OPEN WINDOW IS IN FULL SCREEN\n>")

    time.sleep(2) # necessary, or subject line won't be capitalized on first iteration

    # Open a new compose email page for each email address in the list
    for email in email_list:
        url = 'https://mail.google.com/mail/u/0/?fs=1&tf=cm&to=' + email # url that will open a draft with email typed into box
        webbrowser.open(url) # open a draft with email typed into box
        time.sleep(7.5)  # Wait for page to load

        # Format final email in preparation to send
        pyautogui.write(company_name) # type subject line
        pyautogui.press('tab') # Pass cursor to start to type body of message
        pyautogui.write(final_email, interval=0.05) # type final email

        # Send the email
        pyautogui.moveTo(local_width, local_height) # place cursor over send button
        pyautogui.click() # click send
        time.sleep(5) # wait 5 seconds for email to send


"""
Below constructs a user interface capable of receiving input and returning said variables
to the send_emails() method.
"""
# construct frame for the window
frame = customtkinter.CTkFrame(master=root) # assign 'root' as master
frame.pack(pady=30, padx=60, fill="both", expand=True) # position frame within root/window

# construct a label to sit within frame
label = customtkinter.CTkLabel(master=frame, text="Welcome to Email Automator", font=("Arial", 20))
label.pack(pady=50, padx=10)

# construct input boxes
company_label = customtkinter.CTkLabel(master=frame, text="Type Your Company Name Here", font=("Arial",10)) # initialize variable for label (company name box)
company_label.pack(pady=10, padx=60) # place label within frame
initial_input_one = customtkinter.StringVar() # empty placeholder for company name
input_company_name = customtkinter.CTkEntry(master=frame, textvariable=initial_input_one) # box to input company_name
input_company_name.pack(pady=5, padx=60) # place within frame

raw_email_label = customtkinter.CTkLabel(master=frame, text="Input Email List Here", font=("Arial",10)) # initialize variable for label (email list box)
raw_email_label.pack(pady=10, padx=60) # place label within frame
initial_input_two = customtkinter.StringVar() # empty placeholder for raw string containing email list
input_raw_email = customtkinter.CTkEntry(master=frame, textvariable=initial_input_two) # box to input a raw list of emails
input_raw_email.pack(pady=5, padx=60) # place within frame

mass_message_label = customtkinter.CTkLabel(master=frame, text="Type Email Body Here", font=("Arial",10)) # initialize variable for label (mass message box)
mass_message_label.pack(pady=10, padx=60) # place label within frame
initial_input_three = customtkinter.StringVar() # empty placeholder for email to be sent
input_mass_message = customtkinter.CTkEntry(master=frame, textvariable=initial_input_three) # box to input the body of email to be mass sent
input_mass_message.pack(pady=5, padx=60) # place within frame

# construct start button to sit within frame
start_button = customtkinter.CTkButton(master=frame, text="Click to Start", command=send_emails)
start_button.pack(pady=40, padx=10)

button_label = customtkinter.CTkLabel(master=frame, text="Return to Terminal After Clicking Start Button", font=("Arial", 10)) # initialize variable for button label
button_label.pack(pady=5, padx=60) # place button label into frame

root.mainloop() # open window
