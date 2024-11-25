from tkinter import *
import speedtest

def speedcheck():
    sp_test = speedtest.Speedtest()
    sp_test.get_servers()  # Get list of servers
    down_speed = str(round(sp_test.download() / (10**6), 3)) + " Mbps"  # Convert to Mbps
    up_speed = str(round(sp_test.upload() / (10**6), 3)) + " Mbps"  # Convert to Mbps
    lab_down.config(text=down_speed)  # Update download speed label
    lab_up.config(text=up_speed)  # Update upload speed label

# Set up the main window
sp = Tk()
sp.title("Internet Speedtest")
sp.geometry("500x650")
sp.config(bg="skyblue")

# Title label
lab = Label(sp, text="Internet Speedtest", font=("Times New Roman", 20, "bold"), bg="skyblue", fg="blue")
lab.place(x=60, y=20, height=50, width=380)

# Download speed label
lab_down_title = Label(sp, text="Download Speed", font=("Times New Roman", 15, "bold"), bg="skyblue")
lab_down_title.place(x=60, y=130, height=50, width=380)

lab_down = Label(sp, text="00 Mbps", font=("Times New Roman", 15, "bold"), bg="white")
lab_down.place(x=60, y=200, height=50, width=380)

# Upload speed label
lab_up_title = Label(sp, text="Upload Speed", font=("Times New Roman", 15, "bold"), bg="skyblue")
lab_up_title.place(x=60, y=290, height=50, width=380)

lab_up = Label(sp, text="00 Mbps", font=("Times New Roman", 15, "bold"), bg="white")
lab_up.place(x=60, y=360, height=50, width=380)

# Speed check button
button = Button(sp, text="Check Speed", font=("Times New Roman", 15, "bold"), relief=RAISED, bg="lightgreen", command=speedcheck)
button.place(x=60, y=460, height=50, width=380)

sp.mainloop()
