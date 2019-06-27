import tkinter as tk
import csv

girls = []

with open('girls.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    for r in reader:
        girls.append((r))

if __name__ == '__main__':

    w, h = 1200, 600
    root = tk.Tk()
    root.geometry('+0+0')
    canvas = tk.Canvas(root, width=w, height=h, borderwidth=1, relief='solid', bg='white')
    canvas.pack()
    canvas.create_line((w*0.1, h*0.1), (w*0.9, h*0.1), dash=(1,1))
    canvas.create_line((w*0.1, h*0.9), (w*0.9, h*0.9), dash=(1,1))
    canvas.create_line((w*0.1, h*0.1), (w*0.1, h*0.9), dash=(1,1))
    canvas.create_line((w*0.9, h*0.1), (w*0.9, h*0.9), dash=(1,1))
    axes = ('Height', 'Weight')
    canvas.create_text((w/2, 0), text=axes[0], font=('Courier', 20), anchor='n')
    canvas.create_text((0, h/2), text=axes[1], font=('Courier', 20), anchor='w')
    max_v1 = max([int(g[axes[0]]) for g in girls])
    min_v1 = min([int(g[axes[0]]) for g in girls])
    dv1 = max_v1 - min_v1
    canvas.create_text((w*0.1, 0), text=str(min_v1), font=('Courier', 16), anchor='n')
    canvas.create_text((w*0.9, 0), text=str(max_v1), font=('Courier', 16), anchor='n')
    max_v2 = max([int(g[axes[1]]) for g in girls])
    min_v2 = min([int(g[axes[1]]) for g in girls])
    dv2 = max_v2 - min_v2
    canvas.create_text((0, h*0.1), text=str(max_v2), font=('Courier', 16), anchor='w')
    canvas.create_text((0, h*0.9), text=str(min_v2), font=('Courier', 16), anchor='w')
    ovals = []
    nums = [7, 507, 67, 79, 173, 241, 97, 65]

    for i in range(len(girls)):
        girl = girls[i]
        v1, v2 = int(girl[axes[0]]), int(girl[axes[1]])
        x, y = w/10 + (v1 - min_v1)/ dv1 * w * 0.8, h - (h/10 + (v2 - min_v2) / dv2 * h *0.8)
        oval = canvas.create_oval((x-15, y-15), (x+15, y+15), fill='white')
        ovals.append(oval)
        canvas.create_text((x, y), text=str(i), font=('Courier', 7))
        if i in nums:
            canvas.create_text((x, y+20), text=(girls[i]['Month']+girls[i]['Year']), font=('Courier', 10), fill='red')
            canvas.itemconfig(ovals[-1], fill='yellow')

    root.mainloop()
