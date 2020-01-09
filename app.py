import tkinter as tk
from tkinter import filedialog, Text
import os

# App Structure
root = tk.Tk()
apps = []

if os.path.isfile("save.txt"):
    with open("save.txt", "r") as f:
        tempApps = f.read()
        tempApps = tempApps.split(",")
        # Get rid of empty spaces
        apps = [x for x in tempApps if x.strip()]

# Add Apps to queue


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    fileName = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(fileName)
    print(fileName)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


# Run Apps
def runApps():
    for app in apps:
        os.startfile(app)


# Set canvas specifications
canvas = tk.Canvas(root, height=700, width=700, bg="#2D4F78")
canvas.pack()

# Kind of adding a div
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.7, relheight=0.7, relx=0.15, rely=0.15)

# Add buttons
openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#2D4F78", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="white", bg="#2D4F78", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

# Whenever we close the app, generate a save.txt file with our previously added apps
with open('save.txt', "w") as f:
    for app in apps:
        f.write(app + ",")
