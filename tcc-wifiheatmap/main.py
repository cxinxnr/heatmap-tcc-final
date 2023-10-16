import subprocess
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageDraw, ImageGrab
from tkinter import filedialog
from tkinter import Toplevel


def importsite():
    apps = []
    filename = filedialog.askopenfilename(initialdir='C:', title='Select Files')
    filetypes = ("all files", "*.*")
    apps.append(filename)

    global canvas6
    global photo6
    global item6

    # Define o tamanho máximo para a imagem exibida
    max_width = 700
    max_height = 450

    # Carrega a imagem original
    original_image = Image.open(apps[0])

    # Redimensiona a imagem para ajustar ao tamanho máximo
    resized_image = original_image.copy()
    resized_image.thumbnail((max_width, max_height))

    # Cria a PhotoImage a partir da imagem redimensionada
    photo6 = ImageTk.PhotoImage(resized_image)

    # Cria o item de imagem no canvas6
    canvas6 = Canvas(main_canvas, width=max_width, height=max_height, bg='white')
    item6 = canvas6.create_image(0, 0, image=photo6, anchor="nw")
    canvas6.place(relx=0, rely=0)

    # Atualiza o tamanho do main_canvas de acordo com o tamanho máximo
    main_canvas.configure(width=max_width, height=max_height)



def donothing(event):
    pass


def open_frequency_window():
    frequency_net_button.pack_forget()
    legend_frame2.pack_forget()
    frequency_window = Toplevel(root)
    frequency_window.title('Inserir nível do sinal')

    def confirm():
        frequency = frequency_entry.get()
        canvas6.bind("<Button-1>", lambda event, freq=frequency: on_canvas_click(event, freq))
        frequency_window.destroy()

    def cancel():
        frequency_window.destroy()

    def on_canvas_click(event, freq):
        print("Clique detectado!")
        x, y = event.x, event.y
        radius = 60  # Define o raio do círculo
        freq = int(freq)
        # Carrega a imagem
        if freq > -40:
            photo = Image.open("images/red.png")
        elif freq > -50:
            photo = Image.open("images/orange.png")
        elif freq > -60:
            photo = Image.open("images/weakorange.png")
        elif freq > -70:
            photo = Image.open("images/yellow.png")
        elif freq > -80:
            photo = Image.open("images/green.png")
        elif freq > -90:
            photo = Image.open("images/darkgreen.png")
        else:
            photo = Image.open("images/darkgreen.png")

        # Redimensiona a imagem para o tamanho desejado
        resized_photo = photo.resize((radius * 2, radius * 2))

        # Cria uma nova instância de PhotoImage com a imagem redimensionada
        circle_image = ImageTk.PhotoImage(resized_photo)

        # Adiciona a nova imagem ao dicionário com as coordenadas correspondentes
        image_dict[circle_image] = (x - radius, y - radius)

        # Desenha a imagem no canvas
        image_item = canvas6.create_image(x - radius, y - radius, image=circle_image, anchor="nw")
        canvas6.tag_lower(item6)
        # Desenha uma borda vermelha ao redor da imagem
        # canvas6.create_rectangle(x - radius, y - radius, x + radius, y + radius, outline="red", width=2)

        # Cria um botão para deletar a imagem
        delete_button = Button(canvas6, text=str(freq)+' dBm', command=lambda: delete_image(circle_image, delete_button))

        # Posiciona o botão no meio da imagem
        offset_x = 48  # Deslocamento para a esquerda
        offset_y = 48  # Deslocamento para cima
        button_x = x - radius + offset_x
        button_y = y - radius + offset_y
        delete_button.place(x=button_x, y=button_y)

        # Armazena a referência da imagem e do botão
        image_button_dict[image_item] = delete_button

    def delete_image(image, button):
        canvas6.delete(image)
        button.destroy()
        del image_dict[image]

    frequency_label = Label(frequency_window, text='Nível do sinal:')
    frequency_label.pack()

    frequency_entry = Entry(frequency_window)
    frequency_entry.pack()

    confirm_button = Button(frequency_window, text='Confirmar', command=confirm)
    confirm_button.pack()

    cancel_button = Button(frequency_window, text='Cancelar', command=cancel)
    cancel_button.pack()

def open_frequency_net_window():
    frequency_button.pack_forget()
    legend_frame1.pack_forget()
    frequency_net_window = Toplevel(root)
    frequency_net_window.title('Inserir nível da velocidade da internet')

    def confirm():
        speed = frequency_net_entry.get()
        canvas6.bind("<Button-1>", lambda event, speed=speed: on_canvas_click(event, speed))
        frequency_net_window.destroy()

    def cancel():
        frequency_net_window.destroy()

    def on_canvas_click(event, speed):
        print("Clique detectado!")
        x, y = event.x, event.y
        radius = 60  # Define o raio do círculo
        speed = int(speed)
        # Carrega a imagem
        if speed >= 200:
            photo = Image.open("images/darkblue.png")
        elif speed >= 100:
            photo = Image.open("images/bluesky.png")
        elif speed >= 50:
            photo = Image.open("images/blue.png")
        else:
            photo = Image.open("images/purple.png")

        # Redimensiona a imagem para o tamanho desejado
        resized_photo = photo.resize((radius * 2, radius * 2))

        # Cria uma nova instância de PhotoImage com a imagem redimensionada
        circle_image = ImageTk.PhotoImage(resized_photo)

        # Adiciona a nova imagem ao dicionário com as coordenadas correspondentes
        image_dict[circle_image] = (x - radius, y - radius)

        # Desenha a imagem no canvas
        image_item = canvas6.create_image(x - radius, y - radius, image=circle_image, anchor="nw")
        canvas6.tag_lower(item6)
        # Desenha uma borda vermelha ao redor da imagem
        # canvas6.create_rectangle(x - radius, y - radius, x + radius, y + radius, outline="red", width=2)

        # Cria um botão para deletar a imagem
        delete_button = Button(canvas6, text=str(speed)+' Mbps', command=lambda: delete_image(circle_image, delete_button))

        # Posiciona o botão no meio da imagem
        offset_x = 48  # Deslocamento para a esquerda
        offset_y = 48  # Deslocamento para cima
        button_x = x - radius + offset_x
        button_y = y - radius + offset_y
        delete_button.place(x=button_x, y=button_y)

        # Armazena a referência da imagem e do botão
        image_button_dict[image_item] = delete_button

    def delete_image(image, button):
        canvas6.delete(image)
        button.destroy()
        del image_dict[image]

    frequency_net_label = Label(frequency_net_window, text='Velocidade da Internet:')
    frequency_net_label.pack()

    frequency_net_entry = Entry(frequency_net_window)
    frequency_net_entry.pack()

    confirm_button = Button(frequency_net_window, text='Confirmar', command=confirm)
    confirm_button.pack()

    cancel_button = Button(frequency_net_window, text='Cancelar', command=cancel)
    cancel_button.pack()

def open_ap_window():

    ap_window = Toplevel(root)
    ap_window.title('Inserir roteador(AP)')

    def confirm():
        speed = frequency_net_entry.get()
        canvas6.bind("<Button-1>", lambda event, speed=speed: on_canvas_click(event, speed))
        ap_window.destroy()

    def cancel():
        ap_window.destroy()

    def on_canvas_click(event, model):
        print("Clique detectado!")
        x, y = event.x, event.y
        radius = 60  # Define o raio do círculo
        model = str(model)
        # Carrega a imagem
        photo = Image.open("images/wallpro.png")

        # Redimensiona a imagem para o tamanho desejado
        resized_photo = photo.resize((radius * 2, radius * 2))

        # Cria uma nova instância de PhotoImage com a imagem redimensionada
        circle_image = ImageTk.PhotoImage(resized_photo)

        # Adiciona a nova imagem ao dicionário com as coordenadas correspondentes
        image_dict[circle_image] = (x - radius, y - radius)

        # Desenha a imagem no canvas
        image_item = canvas6.create_image(x - radius, y - radius, image=circle_image, anchor="nw")
        canvas6.tag_lower(item6)
        # Desenha uma borda vermelha ao redor da imagem
        # canvas6.create_rectangle(x - radius, y - radius, x + radius, y + radius, outline="red", width=2)

        # Cria um botão para deletar a imagem
        delete_button = Button(canvas6, text=str(model), command=lambda: delete_image(circle_image, delete_button))

        # Posiciona o botão no meio da imagem
        offset_x = 48  # Deslocamento para a esquerda
        offset_y = 48  # Deslocamento para cima
        button_x = x - radius + offset_x
        button_y = y - radius + offset_y
        delete_button.place(x=button_x, y=button_y)

        # Armazena a referência da imagem e do botão
        image_button_dict[image_item] = delete_button

    def delete_image(image, button):
        canvas6.delete(image)
        button.destroy()
        del image_dict[image]

    frequency_net_label = Label(ap_window, text='Modelo do roteador:')
    frequency_net_label.pack()

    frequency_net_entry = Entry(ap_window)
    frequency_net_entry.pack()

    confirm_button = Button(ap_window, text='Confirmar', command=confirm)
    confirm_button.pack()

    cancel_button = Button(ap_window, text='Cancelar', command=cancel)
    cancel_button.pack()


def export_image():
    save_filename = filedialog.asksaveasfilename(initialdir='C:', title='Save Image', defaultextension=".png",
                                                filetypes=(("PNG Files", "*.png"), ("All Files", "*.*")))
    if save_filename:
        # Captura de tela do canvas6
        x = root.winfo_rootx() + main_canvas.winfo_x()
        y = root.winfo_rooty() + main_canvas.winfo_y()
        x1 = x + main_canvas.winfo_width()
        y1 = y + main_canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(save_filename)
        
def save_canvas():
    subprocess.Popen('C:\\Windows\\System32\\SnippingTool.exe')


root = Tk()
root.title('Wifi Heatmap')
root.geometry('1200x800')
root.resizable(False, False)
root.config(bg='#292929')


main_canvas = Canvas(root, width=700, height=450, bg='white')
main_canvas.pack(pady=10)

bottom_canvas = Canvas(root, width=600, height=120, bg='#383838')
bottom_canvas.place(relx=0, rely=1, anchor="sw", relwidth=1, relheight=0.4)

frequency_button = Button(bottom_canvas, text='Inserir nível do sinal', command=open_frequency_window)
frequency_button.pack(side=LEFT, padx=30, pady=30)

legend_frame1 = Frame(bottom_canvas, bg='#383838')
legend_frame1.pack(side=LEFT, padx=(10, 30), pady=10)

legend_label1 = Label(legend_frame1, text="Legenda:", font=("Arial", 12), fg="white", bg="#383838")
legend_label1.grid(row=0, column=0, sticky="w", padx=10)

legend_colors1 = {
    "-40 dBm": ("red", "forte"),
    "-50 dBm": ("orange red", "forte"),
    "-60 dBm": ("dark orange", "médio"),
    "-70 dBm": ("yellow", "médio"),
    "-80 dBm": ("pale green", "fraco"),
    "-90 dBm": ("dark green", "fraco")
}

row = 1
for freq, (color, strength) in legend_colors1.items():
    legend_item = Frame(legend_frame1, bg=color, width=20, height=20)
    legend_item.grid(row=row, column=0, padx=5, pady=5)

    legend_label = Label(legend_item, text=freq, font=("Arial", 10), fg="black", bg=color)
    legend_label.pack()

    legend_desc = Label(legend_frame1, text=f"nível do sinal {strength}", font=("Arial", 10), fg="white", bg="#383838")
    legend_desc.grid(row=row, column=1, sticky="w")

    row += 1


frequency_net_button = Button(bottom_canvas, text='Inserir velocidade da internet', command=open_frequency_net_window)
frequency_net_button.pack(side=LEFT, padx=30, pady=30)

legend_frame2 = Frame(bottom_canvas, bg='#383838')
legend_frame2.pack(side=LEFT, padx=(30, 10), pady=10)

legend_label2 = Label(legend_frame2, text="Legenda:", font=("Arial", 12), fg="white", bg="#383838")
legend_label2.grid(row=0, column=0, sticky="w", padx=10)

legend_colors2 = {
    "200 Mbps": ("blue", "rápida"),
    "100 Mbps": ("sky blue", "média"),
    "50 Mbps": ("dark blue", "lenta"),
    "1 Mbps": ("purple", "muito lenta"),
}

row = 1
for speed, (color, desc) in legend_colors2.items():
    legend_item = Frame(legend_frame2, bg=color, width=20, height=20)
    legend_item.grid(row=row, column=0, padx=5, pady=5)

    legend_label = Label(legend_item, text=speed, font=("Arial", 10), fg="black", bg=color)
    legend_label.pack()

    legend_desc = Label(legend_frame2, text=f"velocidade {desc}", font=("Arial", 10), fg="white", bg="#383838")
    legend_desc.grid(row=row, column=1, sticky="w")

    row += 1

ap_button = Button(bottom_canvas, text='Inserir modelo do roteador', command=open_ap_window)
ap_button.pack(side=LEFT, padx=30, pady=30)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Import', command=importsite)
filemenu.add_separator()

filemenu.add_command(label='Export', command=export_image)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
menubar.add_cascade(label='File', menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='Info', command=donothing)
menubar.add_cascade(label='Help', menu=helpmenu)

root.config(menu=menubar)

# Dicionário para armazenar as imagens e suas coordenadas
image_dict = {}

# Dicionário para armazenar as referências da imagem e do botão
image_button_dict = {}

root.mainloop()
