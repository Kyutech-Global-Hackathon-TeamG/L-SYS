import os
import csv
import tkinter as tk
import tkinter.font as font
from PIL import Image, ImageTk
from janome.tokenizer import Tokenizer



###///   CSV Files   ///###
csv_dict ={'talk':['../csv/talk.csv', 0],
           'wordbook':['../csv/wordbook.csv', 0],
           'phrasebook':['../csv/phrasebook.csv', 0]}



###///   Edit File Path Function   ///###
def editPath(file_path):
    path = os.path.join(os.path.dirname(__file__), '../' + file_path)
    path = os.path.normpath(path)
    return path



###///   Generate Wordbook Files Function   ///###
def genWordbook():
    ##//  Road File  //##
    #with open(editPath(csv_dict['talk'][0])) as f:
    #    reader = csv.reader(f) # Read CSV
    #    header = next(reader)
    ##//  Morphological Analysis  //##
    ##//  Translate  //##
    ##//  Generate File  //##    
    return



###///   Generate Phrasebook Files Function   ///###
def genPhrasebook():
    ##//  Road File  //##
    #with open(editPath(csv_dict['talk'][0])) as f:
    #    reader = csv.reader(f) # Read CSV
    #    header = next(reader)
    ##//  Morphological Analysis  //##
    ##//  Translate  //##
    ##//  Generate File  //##
    return



###///   Check Files Function   ///###
def checkFiles():
    ##//  Check Files  //##
    csv_keys = csv_dict.keys()
    for csv_key in csv_keys:
        tf = os.path.isfile(editPath(csv_dict[csv_key][0]))
        csv_dict[csv_key][1] = 1 if tf == True else 0


    ##//  Update Files  //##
    if csv_dict['talk'][1] == 1:
        genWordbook()   # Generate Wordbook
        genPhrasebook() # Generate Phrasebook

    return



###///   Change GUI Frame Function   ///###
def changeFrm(frame):
    frame.tkraise()
    return


###///   Main Function   ///###
if __name__ == "__main__":
    ##//  Check Files  //##
    checkFiles()


    ##//  Window  //##
    win = tk.Tk()
    win.title("L-SYS (Kyutech Global Hackathon)")
    win.geometry("800x600")
    

    ##//  Fonts  //##
    font_1 = font.Font(family='Helvetica', size=20, weight='bold')


    ##//  Menubar  //##
    menu_bar = tk.Menu(win)
    win.config(menu=menu_bar)
    #/ File Menu /#
    menu_fle = tk.Menu(menu_bar, tearoff=0)
    menu_fle.add_command(label='Vocabulary', command=lambda:changeFrm(vocab_frm))
    menu_fle.add_command(label='Grammar', command=lambda:changeFrm(gram_frm))
    menu_fle.add_command(label='Exit', command=quit)
    menu_bar.add_cascade(label = 'File', menu = menu_fle)
    #/ About Menu /#
    menu_abt = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label = 'About', menu = menu_abt)


    ##//  Main Frame  //##
    main_frm = tk.Frame()
    main_frm.grid(row=0, column=0, sticky="nsew")
    #/ Logo /#
    main_img_lg = Image.open("../image/logo.png")
    main_img_w = main_img_lg.width
    main_img_h = main_img_lg.height
    main_img_lg = main_img_lg.resize((int(main_img_w * (500/main_img_h)), int(main_img_h * (500/main_img_h))))
    main_img_lg = ImageTk.PhotoImage(main_img_lg)
    canvas = tk.Canvas(main_frm, bg="white", width=800, height=500)
    canvas.pack()
    canvas.create_image((800 - (main_img_w * (500/main_img_h)))/2, 0, image=main_img_lg, anchor=tk.NW)
    #main_lbl_title = tk.Label(main_frm, text="L-SYS", font = font_title)
    #main_lbl_title.pack(expand = True)
    #/ Button /#
    main_btn_go2vocab = tk.Button(main_frm, text="Vocabulary Learning", command = lambda:changeFrm(vocab_frm))
    main_btn_go2vocab.pack()
    main_btn_go2gram = tk.Button(main_frm, text="Grammar Learning", command = lambda:changeFrm(gram_frm))
    main_btn_go2gram.pack()


    ##//  Vocabulary Learning Frame  //##
    vocab_frm = tk.Frame()
    vocab_frm.grid(row=0, column=0, sticky="nsew")
    #/ Button /#
    vocab_btn_back2main = tk.Button(vocab_frm, text="Home", command = lambda:changeFrm(main_frm))
    vocab_btn_back2main.pack()


    ##//  Grammar Learning Frame  //##
    gram_frm = tk.Frame()
    gram_frm.grid(row=0, column=0, sticky="nsew")
    #/ Button /#
    gram_btn_back2main = tk.Button(gram_frm, text="Home", command = lambda:changeFrm(main_frm))
    gram_btn_back2main.pack()


    ##//  Output GUI Window  //##
    main_frm.tkraise()
    win.mainloop()