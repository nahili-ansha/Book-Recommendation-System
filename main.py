import tkinter  # importing tkinter
from tkinter import *  # From tkinter import everything
from tkinter import messagebox  # From tkinter import messagebox
import requests  # import requests to make https request
from PIL import ImageTk, Image  # import ImageTK, Image from pillow (PIL) for image processing
import urllib.parse  # import urllib.parse for URL parsing and manipulation
from io import BytesIO # import for handling byte data

# class to handle HTTP requests
class Request:
    def __init__(self, method, args):
        self.args = args
        self.method = method

inc = 0 # counter for widget naming

# to fetch and display information
def fetch_information(title,poster,date,rating):
    global inc
    inc += 1

    text[f"a{inc}"].config(text=title) # set book title
    
    response = requests.get(poster) # fetch image data
    img_data = response.content 
    img = Image.open(BytesIO(img_data)) # open image
    resized_img = img.resize((140, 200), Image.Resampling.LANCZOS) # resize image
    photo = ImageTk.PhotoImage(resized_img) # convert to PhotoImage
    images[f"b{inc}"].config(image = photo) # display image
    images[f"b{inc}"].image = photo

    if check_var.get(): # display date if checkbox is checked
        text2[f"a{inc}{inc}"].config(text = date)
    else:
        text2[f"a{inc}{inc}"].config(text="")

    if check_var2.get(): # display rating if checkbox is checked
        text3[f"a{inc}{inc}{inc}"].config(text=rating)
    else:
        text3[f"a{inc}{inc}{inc}"].config(text="")

# search books 
def search():
    global inc
    inc = 0
    search_term = Search.get()
    request = Request('GET',{'search': search_term})
    if request.method == 'GET':
        search = urllib.parse.quote(request.args.get('search',''))
        url = f"https://www.googleapis.com/books/v1/volumes?q={search}&maxResults=5"
        response = requests.get(url)
        #print(response.json())

        if response.status_code == 200: # 200 the request was successful
            data = response.json()
            #print(data)
            for item in data.get('items',[]):
                volume_info = item.get('volumeInfo',{})
                title = volume_info.get('title','N/A')
                publisher = volume_info.get('publisher','N/A')
                published_date = volume_info.get('publishedDate','N/A')
                rating = volume_info.get('averageRating','N/A')
                author = volume_info.get('authors',['N/A'])
                image_links = volume_info.get('imageLinks',{}) 
                image = image_links.get('thumbnail') if 'thumbnail' in image_links else 'N/A'

                print(title)
                print(publisher)
                print(published_date)
                print(author)
                print(rating)
                print(image)

                fetch_information(title,image,published_date,rating)

                # display or hide frames based on checkbox states
                if check_var.get() or check_var2.get():
                    frame11.grid(row=2, column=0, padx=20, pady=10)
                    frame22.grid(row=2, column=1, padx=20, pady=10)
                    frame33.grid(row=2, column=2, padx=20, pady=10)
                    frame44.grid(row=2, column=3, padx=20, pady=10)
                    frame55.grid(row=2, column=4, padx=20, pady=10)
                else:
                    frame11.grid_forget()
                    frame22.grid_forget()
                    frame33.grid_forget()
                    frame44.grid_forget()
                    frame55.grid_forget()
        else:
            print("Failed to fetch data from Google Books API")
            messagebox.showinfo("info","Failed to fetch data from Google Books API")

# to show menu       
def show_menu(event):
    # display the menu at the mouse position
    menu.post(event.x_root, event.y_root)

root = tkinter.Tk()
root.title("Book Recommendation System")
root.geometry("1250x700+200+100")
root.configure(bg="#111119")
#root.resizable(False, False)

# Create a canvas and a scrollbar
canvas = Canvas(root, bg="#111119", width=1250, height=700)
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollable_frame = Frame(canvas, bg="#111119")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

# icon
icon_path = r"images\icon.png"
image = Image.open(icon_path)
icon_image = ImageTk.PhotoImage(image)
# Set the window icon
root.iconphoto(False, icon_image)

# background image
background_path = r"images\background.png"
image2 = Image.open(background_path)
background_image = ImageTk.PhotoImage(image2)
# Set the background image
Label(scrollable_frame, image=background_image, bg="#111119").grid(row=0, column=0, columnspan=5, sticky="nsew")

# Logo
logo_path = r"images\logo.png"
image3 = Image.open(logo_path)
logo_image = ImageTk.PhotoImage(image3)
# Set the Logo
Label(scrollable_frame, image=logo_image, bg="#0099ff").place(x=380, y=80)

# heading
heading = Label(scrollable_frame, text="BOOK RECOMMENDATION", font=("Lato", 30, "bold"), fg="white", bg="#0099ff")
heading.place(x=550, y=90)

# search Background image
search_box_path = r"images\Rectangle.png"
image4 = Image.open(search_box_path)
search_box = ImageTk.PhotoImage(image4)
# Set the search box image
Label(scrollable_frame, image=search_box, bg="#0099ff").place(x=380, y=175)

# entry box
Search = StringVar()
search_entry = Entry(scrollable_frame, textvariable=Search, width=20, font=("Lato", 25), bg="white", fg="black", bd=0)
search_entry.place(x=480, y=190)

# search button
search_button_path = r"images\Search.png"
image5 = Image.open(search_button_path)
search_button = ImageTk.PhotoImage(image5)
# Set the search button
Button(scrollable_frame, image=search_button, bg="#0099ff", bd=0, activebackground="#252532", cursor="hand1", command = search).place(x=949, y=187)

# setting button
setting_path = r"images\setting.png"
image6 = Image.open(setting_path)
setting_image = ImageTk.PhotoImage(image6)
# Set the setting image
setting_button = Button(scrollable_frame, image=setting_image, bd=0, cursor="hand2", activebackground="#0099ff", bg="#0099ff")
setting_button.place(x=1150, y=190)
setting_button.bind('<Button-1>', show_menu)

# Menu for search button
menu = Menu(root, tearoff=0)
check_var = BooleanVar()
menu.add_checkbutton(label="Published Date", variable=check_var, command=lambda: print(f"check option is{' checked' if check_var.get() else 'unchecked'}"))

check_var2 = BooleanVar()
menu.add_checkbutton(label="Rating", variable=check_var2, command=lambda: print(f"rating check option is{' checked' if check_var2.get() else 'unchecked'}"))

# logout button
logout_path = r"images/logout.png"
image6 = Image.open(logout_path)
logout_image = ImageTk.PhotoImage(image6)
# Set the logout image
logout_button = Button(scrollable_frame, image=logout_image, bg="#0099ff", cursor="hand1", command=lambda: root.destroy())
logout_button.place(x=1100, y=60)

# main frames
frame1 = Frame(scrollable_frame, width=150, height=240, bg="white")
frame2 = Frame(scrollable_frame, width=150, height=240, bg="white")
frame3 = Frame(scrollable_frame, width=150, height=240, bg="white")
frame4 = Frame(scrollable_frame, width=150, height=240, bg="white")
frame5 = Frame(scrollable_frame, width=150, height=240, bg="white")

frame1.grid(row=1, column=0, padx=20, pady=10)
frame2.grid(row=1, column=1, padx=20, pady=10)
frame3.grid(row=1, column=2, padx=20, pady=10)
frame4.grid(row=1, column=3, padx=20, pady=10)
frame5.grid(row=1, column=4, padx=20, pady=10)

# book titles
text = {'a1': Label(frame1, text="Book Title", fg="blue", font=("arial", 10)),
        'a2': Label(frame2, text="Book Title", fg="blue", font=("arial", 10)),
        'a3': Label(frame3, text="Book Title", fg="blue", font=("arial", 10)),
        'a4': Label(frame4, text="Book Title", fg="blue", font=("arial", 10)),
        'a5': Label(frame5, text="Book Title", fg="blue", font=("arial", 10))}
text['a1'].place(x=10, y=5)
text['a2'].place(x=10, y=5)
text['a3'].place(x=10, y=5)
text['a4'].place(x=10, y=5)
text['a5'].place(x=10, y=5)

# book images
images = {'b1': Label(frame1), 'b2': Label(frame2), 'b3': Label(frame3), 'b4': Label(frame4), 'b5': Label(frame5)}
images['b1'].place(x=3, y=30)
images['b2'].place(x=3, y=30)
images['b3'].place(x=3, y=30)
images['b4'].place(x=3, y=30)
images['b5'].place(x=3, y=30)

# second frames
frame11 = Frame(scrollable_frame, width=150, height=50, bg="#e6e6e6")
frame22 = Frame(scrollable_frame, width=150, height=50, bg="#e6e6e6")
frame33 = Frame(scrollable_frame, width=150, height=50, bg="#e6e6e6")
frame44 = Frame(scrollable_frame, width=150, height=50, bg="#e6e6e6")
frame55 = Frame(scrollable_frame, width=150, height=50, bg="#e6e6e6")

# published dates
text2 = {'a11': Label(frame11, text="date", font=("arial", 10), fg="green", bg="#e6e6e6"),
         'a22': Label(frame22, text="date", font=("arial", 10), fg="green", bg="#e6e6e6"),
         'a33': Label(frame33, text="date", font=("arial", 10), fg="green", bg="#e6e6e6"),
         'a44': Label(frame44, text="date", font=("arial", 10), fg="green", bg="#e6e6e6"),
         'a55': Label(frame55, text="date", font=("arial", 10), fg="green", bg="#e6e6e6")}
text2['a11'].place(x=10, y=5)
text2['a22'].place(x=10, y=5)
text2['a33'].place(x=10, y=5)
text2['a44'].place(x=10, y=5)
text2['a55'].place(x=10, y=5)

# ratings
text3 = {'a111': Label(frame11, text="rating", font=("arial", 10), bg="#e6e6e6"),
         'a222': Label(frame22, text="rating", font=("arial", 10), bg="#e6e6e6"),
         'a333': Label(frame33, text="rating", font=("arial", 10), bg="#e6e6e6"),
         'a444': Label(frame44, text="rating", font=("arial", 10), bg="#e6e6e6"),
         'a555': Label(frame55, text="rating", font=("arial", 10), bg="#e6e6e6")}
text3['a111'].place(x=20, y=30)
text3['a222'].place(x=20, y=30)
text3['a333'].place(x=20, y=30)
text3['a444'].place(x=20, y=30)
text3['a555'].place(x=20, y=30)

root.mainloop()

