
# This is a project for Ohjelmisto 1 -course in Metropolia University of Applied Sciences.

# Authors: Abdur Abou Ramadan, Ahmed Ezzaroui, Juan Rosales and Sami Abo Ramadan.

# Project started on 28.9.2022 13.30.

# Project finished on NA.

import mysql.connector

# connecting to our airport database
connection = mysql.connector.connect(host='localhost', port=3306, database='flight_game', user='juanito',
                                    password='password1', autocommit=True)


# function to check if the chosen country is in the formerly selected continent
def check_country(ctry, cont):
   sql_code = "SELECT iso_country FROM country WHERE name = '" + ctry + "' and continent = '" + cont + "'"
   cursor = connection.cursor()
   cursor.execute(sql_code)
   cursor.fetchall()
   return cursor.rowcount


# function to check if the chosen airport is in the formerly selected country
def check_airport_name(name, ctry):
   sql_code = "SELECT * FROM airport, country WHERE airport.name" \
              " = '" + name + "' and airport.iso_country = country.iso_country and country.name = '" + ctry + "'"
   cursor = connection.cursor()
   cursor.execute(sql_code)
   cursor.fetchall()
   return cursor.rowcount


# function to get all airport names from selected country
def get_airport_names(ctry):
   sql_code = "SELECT airport.name FROM airport, country WHERE country.iso_country = airport.iso_country" \
              " and country.name = '" + ctry + "' ORDER BY country.name asc"
   cursor = connection.cursor()
   cursor.execute(sql_code)
   sql_print = cursor.fetchall()
   if cursor.rowcount > 0:
       for row in sql_print:
           print(f"{row[0]}")
       print("")
   else:
       print("Error!")
   return


# function to get the amount of different airports in the chosen country
def get_airports_amount(ctry):
   sql_code = "SELECT type, count(*) FROM airport, country WHERE country.iso_country = airport.iso_country " \
              " and country.name = '" + ctry + "' GROUP BY type ORDER BY count(*) desc"
   cursor = connection.cursor()
   cursor.execute(sql_code)
   sql_print = cursor.fetchall()
   if cursor.rowcount > 0:
       for row in sql_print:
           print(f"{row[0].capitalize()}: {row[1]}")
       print("")
   return


# function to get the total amount of airports in the chosen country
def get_airports_total(ctry):
   sql_code = "SELECT count(*) FROM airport, country WHERE country.iso_country = airport.iso_country" \
              " and country.name = '" + ctry + "'"
   cursor = connection.cursor()
   cursor.execute(sql_code)
   sql_print = cursor.fetchall()
   if cursor.rowcount > 0:
       run_function = True
       for row in sql_print:
           print(f"Airports in total: {row[0]}")
       print("")
   return


# function to get wanted data from a certain airport
def get_airport_data(name, ctry):
   sql_code = "SELECT * FROM airport, country WHERE airport.name" \
              " = '" + name + "' and airport.iso_country = country.iso_country and country.name = '" + ctry + "'"
   cursor = connection.cursor()
   cursor.execute(sql_code)
   sql_print = cursor.fetchall()
   if cursor.rowcount > 0:
       for row in sql_print:
           print(f"Type: {row[2]}\nName: {row[3]}\nLatitude: {row[4]}\nLongitude: {row[5]}"
                 f"\nElevation: {row[6]} ft\nMunicipality: {row[10]}")
   return


# start of the program
print("\nWelcome to Airport Simulator! \nStart by choosing a continent you want airport data from:"
     "\n(AF) (AN) (AS) (EU) (NA) (SA) (OC)\n")

# asking the user to choose a continent and checking for errors
while True:
   user_continent = input("Insert continent code: ")
   if (user_continent == "AF" or user_continent == "AN" or user_continent == "AS" or user_continent == "EU" or
           user_continent == "NA" or user_continent == "SA" or user_continent == "OC"):
       print(user_continent + " chosen!\n")
       break
   else:
       print("Error, try again!\n")


# asking the user to choose a country that's in the chosen continent and checking for errors
while True:
   user_country = input("Choose a country that's in " + user_continent + ": ").capitalize()
   if check_country(user_country, user_continent) == 1:
       print("All airports in " + user_country + ":\n")
       break
   else:
       print(user_country + " is not in " + user_continent + ", try again!\n")

get_airport_names(user_country)
get_airports_amount(user_country)
get_airports_total(user_country)

# asking the user to choose an airport from the formerly selected country and checking for errors then showing data
while True:
   user_airport_name = input("Choose an airport that's in " + user_country + ": ").title()
   if check_airport_name(user_airport_name, user_country) == 1:
       print("Data from " + user_airport_name + ":\n")
       get_airport_data(user_airport_name, user_country)
       print("")
   else:
       print(user_airport_name + " is not in " + user_country + "!\n")





from tkinter import *
from PIL import ImageTk, Image

# install tkinter and pil/pillow in order to use this code

window = Tk()

# POSITION .PACK() AFTER EVERY NEW ELEMENT

window.title("Airport Data Simulator")
width = 700
height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

window.geometry('%dx%d+%d+%d' % (width, height, x, y))

canvas = Canvas(window, width=170, height=170)

img = (Image.open("/Users/abdur/Downloads/earth-icon.png"))
resized_image = img.resize((150, 150), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)

#test_image = ImageTk.PhotoImage(Image.open("/Users/abdur/Downloads/earth-icon.png"))

canvas.create_image(10, 10, anchor=NW, image=new_image)

#window.config(bg='white')

instruction_text = Text(window, width=40, height=2, foreground='green', background='black', borderwidth=5, font=('Courier', 14))
instruction_text.insert('1.0', 'Choose a continent (non-interactable)')
instruction_text.config(state='disabled')

text = Text(window, width=45, height=5, foreground='green', background='black', borderwidth=5, font=('Courier', 14))
text.insert('1.0', 'Type here then press Enter')


def fill_text():
   filled_text = text.get('1.0', 'end')
   text2.delete('1.0', END)
   text2.insert('1.0', filled_text)
   return


text2 = Text(window, width=45, height=10, foreground='red', background='black', borderwidth=5, font=('Courier', 14))
text2.insert('1.0', 'Answer here...')

button1 = Button(window, text='Enter', command=lambda: fill_text(), fg='black', bg='blue')
button2 = Button(window, text='Exit', command=window.destroy, fg='black', bg='black')


list_box = Listbox(window)
scrollbar = Scrollbar(window)

test_list = ["sheesh", "dlkfjs", "kjsdhfds", "sdkjfhs", "dskfjsdfs", "ds",
            "sdjf", "sdjf", "sdjf", "sdjf", "sdjf", "sdjf", "sdkjfhsd", "jksdhf", "jkdshf", "jkds", "1", "2", "3"]

for i in test_list:
   list_box.insert(END, i)

list_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list_box.yview)

# text.grid()
instruction_text.pack(anchor='w')
text.pack(anchor='w')
text2.pack(anchor='w')

list_box.pack(side=LEFT, fill=BOTH)
scrollbar.pack(side=LEFT, fill=BOTH)

canvas.pack()

button1.pack(anchor='s', side=LEFT)
button2.pack(anchor='s', side=RIGHT)

window.mainloop()






