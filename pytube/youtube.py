import tkinter as tk
import customtkinter as ctk
from pytube import YouTube

def start_download():
    try:
        yt_link = url_var.get()
        yt_object = YouTube(yt_link,on_progress_callback=on_progress)
        video = yt_object.streams.get_highest_resolution()
        
        title.configure(text=yt_object.title , text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded")
    except Exception as e:
        finishLabel.configure(text=f"Downloaded Eror because {str(e)}", text_color="red")
        

def on_progress(stream,chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded=total_size - bytes_remaining
    percentage_fo_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_fo_completion))
    pPercentsge.configure(text=per + '%')
    pPercentsge.update()
    
    #update progress bar
    progressBar.set(float(percentage_fo_completion) / 100)

# System settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("500x480")
app.title("YouTube Video Downloader")

# Adding UI Elements
title = ctk.CTkLabel(app, text="Youtube link kiriting")
title.pack(padx=10, pady=10)

# Link entry
url_var = tk.StringVar()
link = ctk.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack(padx=10, pady=10)

# Download button
button = ctk.CTkButton(app, text="Yuklab olish", command=start_download)
button.pack(padx=10, pady=10)

#prpgress bar
    
pPercentsge = ctk.CTkLabel(app, text="0%")
pPercentsge.pack()

progressBar = ctk.CTkProgressBar(app,width=400)
progressBar.set(0)
progressBar.pack(padx=10,pady=10)


# Adding UI Elements
title = ctk.CTkLabel(app, text="Author Lochinbek => Telegram:@lochinbek_dev")
title.pack(padx=10, pady=10)

#finish   downloading
finishLabel = ctk.CTkLabel(app,text="")
finishLabel.pack()

# Run app
app.mainloop()
