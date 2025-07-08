import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
import webbrowser

def get_random_wiki():

    url="https://en.wikipedia.org/api/rest_v1/page/random/summary"

    try:
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()

        title=data.get("title","n/a")
        extract=data.get("extract","no summary available")
        page_url=data.get("content_urls",{}).get("desktop",{}).get("page","url not available")
        imagewiki=data.get("originalimage",{}).get('source',None)
        '''print(f"Title:{title}\n")
        print(f"summary:{extract}\n")
        print(f"Read more:{page_url}")'''
    except requests.RequestException as e:
        print("failed to fetch data",e)

    return title,extract,imagewiki,page_url

def update_image(label, image_url):
    if image_url:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 11.0; Win64; x64)"
            }
            img_response = requests.get(image_url, headers=headers)
            img_response.raise_for_status()

            if "image" in img_response.headers.get("Content-Type", ""):
                img_data = Image.open(BytesIO(img_response.content)).resize((300, 300))
                tk_img = ImageTk.PhotoImage(img_data)
                label.config(image=tk_img, text='')
                label.image = tk_img  # prevent garbage collection
            else:
                raise ValueError("Not an image")
        except Exception as e:
            label.config(image='', text="Image could not be loaded")
            label.image = None
    else:
        label.config(image='', text="No image available")
        label.image = None

def get_random_wiki_refresh():
        global page_url
        title,extract,image_url,page_url=get_random_wiki()
        titlewiki_label.config(text=title)
        summarywiki_label.config(text=extract)
        
        #image refresh
        update_image(wikiimage_label,image_url)

def open_article():
    webbrowser.open(page_url)

root=tk.Tk()        #creates the main window


root.title("Wiki Fact Collection")


root.state("zoomed")

#data from api
titledata,summarydata,image_url,page_url=get_random_wiki()

print(image_url)
head_label=tk.Label(root,text="Wiki Fact Collection ",font=('helvetica',40,'bold'))
head_label.place(relx=.38,rely=.1)

titlewiki_label=tk.Label(root,text=titledata,font=('helvetica',20,'bold'))
titlewiki_label.place(relx=.43,rely=.3)

if image_url:

    try:
        headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 11.0; win64, x64)"
        }
        img_response = requests.get(image_url,headers=headers)
        img_response.raise_for_status()
        if "image" in img_response.headers.get("Content-Type",""):
            img_data = Image.open(BytesIO(img_response.content)).resize((300, 300))
            tk_img = ImageTk.PhotoImage(img_data)

            wikiimage_label = tk.Label(root, image=tk_img)
            wikiimage_label.image = tk_img  # keep reference to avoid garbage collection
            wikiimage_label.place(relx=0.7, rely=0.4)
        else:
            raise ValueError("Not an image")

    except Exception as e:
        wikiimage_label = tk.Label(root, text="Image could not be loaded")
        wikiimage_label.place(relx=0.6, rely=0.2)
else:
    wikiimage_label = tk.Label(root, text="No image available")
    wikiimage_label.place(relx=0.6, rely=0.2)


summarywiki_label=tk.Message(root,text=summarydata,font=('helvetica',20),width=500)
summarywiki_label.place(relx=.2,rely=.4)

new_artice_button=tk.Button(root,text="New Article",font=("helvetica",30),command=get_random_wiki_refresh)
new_artice_button.place(relx=0.45,rely=.8)

new_article_button=tk.Button(root,text="Read More",font=("helvetica",30),command=open_article)
new_article_button.place(relx=0.2,rely=.8)

root.mainloop()     #starts the gui event loop



