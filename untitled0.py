from functools import partial
import tkinter as tk
root = tk.Tk()
# instanciation partielle de classe :
MonBouton = partial(tk.Button, root, fg="purple", bg="green")
MonBouton(text= "Boutton1" ).pack()
MonBouton(text= "Boutton2" ).pack()
MonBouton(text= "QUITTER" , bg="red", fg="black",
command=root.quit).pack(fill=tk.X, expand=True)
root.title( "PFA!" )
root.mainloop()
