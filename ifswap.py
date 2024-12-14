import os
from tkinter import *
from tkinter import ttk

#Заносим в переменную все интерфейсы, которые у нас есть
interfaces = (os.listdir(r'/sys/class/net'))

#пустой словарь для создания кнопок в будущем
ifbuttons = {}

def main():
    #создаем корневой объект окно, с параметрами
    root = Tk() 
    root.title("IFSWAP") 
    root.geometry("500x300+700+350")
    root.resizable(True, True)  
    root.attributes('-alpha', 1)

    #создаем фрейм, для того чтобы кнопки были в отдельном блоке интерфейса
    frame_ifaces = ttk.Frame()
    frame_ifaces.pack()
    
    #цикл, который создает столько кнопок, сколько существует у нас интерфейсов (занося в словарь, видом 'ifbutton1 : *значение*')
    for x, interface in zip(range(1, len(interfaces)+1), interfaces):
        
        #лямбда функция для правильного переноса названия интерфейса в функцию click
        action = lambda h=interface: click(h)

        ifbuttons["ifbutton{0}".format(x)] = ttk.Button(master=frame_ifaces, text=interface, width=9, command=action)
        
    #конфигурация для того чтобы кнопки двигались, в случаи расстягивании окна
    for c in range(5): frame_ifaces.columnconfigure(c, weight=1)

    r=0; c=0

    #цикл, размещающий кнопки в окне, после 5 столбца переход на следующий ряд
    for key in ifbuttons.keys():
        if c == 5:
            c = 0
            r += 1    
        ifbuttons[key].grid(row=r, column=c, padx=5, pady=5)
        c += 1

    #добавляем кнопку перезагрузки сетевых интерфейсов и фрейм под нее
    frame_reboot = ttk.Frame(master=root, width=456, height=200)
    frame_reboot.pack()
    frame_reboot.propagate(False)

    reboot_all = ttk.Button(master=frame_reboot, text='reboot all', command=reboot, width=9)
    reboot_all.pack(side=BOTTOM, anchor=SE)

    #начать отображение окна программы
    root.mainloop() 

def click(iface):
    window = Tk()
    window.title('Новое окно')
    window.geometry('250x250')
   
    labeltest = Label(master=window, text=f'{iface}')
    labeltest.pack()

    ttk.Entry(master=window).pack()

def reboot():
    pass

if __name__ == '__main__':
    main()