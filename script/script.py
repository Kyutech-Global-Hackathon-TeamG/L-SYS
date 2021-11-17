# -*- coding: utf-8 -*-
import os
import csv
import tkinter as tk
import tkinter.font as font
import webbrowser as web
import random
import chardet
from PIL import Image, ImageTk
from talk2word import T2P


###////                //###
###///   Parameters   ///###
###//                ////###

q_num = 10
a_num = 0
csv_dict ={'talk':['../csv/talk.csv', 0],
           'wordbook_j2e':['../csv/wordbook_j2e.csv', 0],
           'wordbook_e2j':['../csv/wordbook_e2j.csv', 0],
           'phrasebook':['../csv/phrasebook.csv', 0]}



###////               //###
###///   Functions   ///###
###//               ////###

###///   Edit File Path Function   ///###
def editPath(file_path):
    path = os.path.join(os.path.dirname(__file__), file_path)
    path = os.path.normpath(path)
    return path



###///   Generate Wordbook Files Function   ///###
def genWordbook():
    #T2W.talk2word(csv_dict['talk'][0], csv_dict['wordbook_j2e'][0])
    #T2W.talk2word(csv_dict['talk'][0], csv_dict['wordbook_e2j'][0])
    return



###///   Generate Phrasebook Files Function   ///###
def genPhrasebook():
    T2P.talk2phrase(csv_dict['talk'][0], csv_dict['phrasebook'][0])
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


###///   Read Files Function   ///###
def readFiles():
    ##//  Read Files  //##
    csv_keys = csv_dict.keys()
    for csv_key in csv_keys:
        value = []
        print(csv_key)
        #/ Detect Encoding /#
        with open(editPath(csv_dict[csv_key][0]), 'rb') as f:
            b = f.read()
            enc = chardet.detect(b)
        #/ Open CSV File /#
        with open(editPath(csv_dict[csv_key][0]), encoding=enc['encoding']) as f:
            reader = csv.reader(f) # Read CSV
            header = next(reader)
            for row in reader:
                value.append(row)
            csv_dict[csv_key].append(value)
    print(csv_dict)
    return 



###///   Change GUI Frame Function   ///###
def changeFrm(frame, a_n):
    a_n = 0
    frame.tkraise()
    return



###///   Update GUI Frame Function   ///###
def updateFrm(lrn, lng, frame, q_n, a_n):
    frame.destroy()
    q_n -= 1
    if lrn == "vcb":
        vcbExam(lng, q_n, a_n)
    elif lrn == "grm":
        grmExam(lng, q_n, a_n)
    return


###///   Check Answer Function   ///###
def checkAns(lrn, lng, frm, q_n, a_n, pf_n):
    if pf_n == 1:
        a_n += 1
    updateFrm(lrn, lng, frm, q_n, a_n)
    return


###///   Vocabulary Learning Function   ///###
def vcbExam(lng, q_n, a_n):
    ##//  Question Frame  //##
    vcbex_qst_frm = tk.Frame()
    vcbex_qst_frm.grid(row=0, column=0, sticky="nsew")
    #/ Label /#
    vcbex_qst_lbl_title = tk.Label(vcbex_qst_frm, text= "Vocabulary Learning(" + lng + ")", font = font_1)
    vcbex_qst_lbl_title.place(x=230, y=10)
    if q_n != 1:
        s = "s"
    else:
        s = ""
    vcbex_qst_lbl_quest = tk.Label(vcbex_qst_frm, text=  str(q_n) + " Question"+ s +" Left", font = font_1)
    vcbex_qst_lbl_quest.place(x=100, y=50)
    vcbex_qst_lbl_score = tk.Label(vcbex_qst_frm, text= "Score Result: " + str(a_n) + "/10", font = font_1)
    vcbex_qst_lbl_score.place(x=100, y=300)
    #/ Checkbutton /#
    bln = []
    c_n = random.randint(0, 3)
    for i in range(4):
        bln.append(tk.BooleanVar())
        bln[-1].set(False)
        if i == c_n:
            chk = tk.Checkbutton(vcbex_qst_frm, variable=bln[-1], text='Correct', command = lambda:checkAns("vcb", lng, vcbex_qst_frm, q_n, a_n, 1))
            chk.place(x=100, y=150 + i * 20)
        elif i != c_n:
            chk = tk.Checkbutton(vcbex_qst_frm, variable=bln[-1], text='Incorrect', command = lambda:checkAns("vcb", lng, vcbex_qst_frm, q_n, a_n, 0))
            chk.place(x=100, y=150 + i * 20)
    #/ Button /#
    vcbex_qst_btn_back2main = tk.Button(vcbex_qst_frm, text = "Cancel", command = lambda:changeFrm(main_frm, a_n))
    vcbex_qst_btn_back2main.place(x=350, y=400)


    ##//  Score Frame  //##
    if q_n == 0:
        vcbex_scr_frm = tk.Frame()
        vcbex_scr_frm.grid(row=0, column=0, sticky="nsew")
        #/ Label /#
        vcbex_scr_lbl_title = tk.Label(vcbex_scr_frm, text= "Vocabulary Learning(" + lng + ")", font = font_1)
        vcbex_scr_lbl_title.pack(expand = True)
        vcbex_scr_lbl_score = tk.Label(vcbex_scr_frm, text= "Score Result: " + str(a_n) + "/10", font = font_1)
        vcbex_scr_lbl_score.pack(expand = True)
        #/ Button /#
        vcbex_scr_btn_back2main = tk.Button(vcbex_scr_frm, text = "Finish", command = lambda:changeFrm(main_frm, a_n))
        vcbex_scr_btn_back2main.pack()

    return
    


###///   Grammar Learning Function   ///###
def grmExam(lng, q_n, a_n):
    ##//  Question Frame  //##
    grmex_qst_frm = tk.Frame()
    grmex_qst_frm.grid(row=0, column=0, sticky="nsew")
    #/ Label /#
    grmex_qst_lbl_title = tk.Label(grmex_qst_frm, text= "Grammer Learning(" + lng + ")", font = font_1)
    grmex_qst_lbl_title.place(x=230, y=10)
    if q_n != 1:
        s = "s"
    else:
        s = ""
    grmex_qst_lbl_quest = tk.Label(grmex_qst_frm, text=  str(q_n) + " Question"+ s +" Left", font = font_1)
    grmex_qst_lbl_quest.place(x=100, y=50)
    grmex_qst_lbl_score = tk.Label(grmex_qst_frm, text= "Score Result: " + str(a_n) + "/10", font = font_1)
    grmex_qst_lbl_score.place(x=100, y=300)
    #/ Checkbutton /#
    bln = []
    c_n = random.randint(0, 3)
    for i in range(4):
        bln.append(tk.BooleanVar())
        bln[-1].set(False)
        if i == c_n:
            chk = tk.Checkbutton(grmex_qst_frm, variable=bln[-1], text='Correct', command = lambda:checkAns("grm", lng, grmex_qst_frm, q_n, a_n, 1))
            chk.place(x=100, y=150 + i * 20)
        elif i != c_n:
            chk = tk.Checkbutton(grmex_qst_frm, variable=bln[-1], text='Incorrect', command = lambda:checkAns("grm", lng, grmex_qst_frm, q_n, a_n, 0))
            chk.place(x=100, y=150 + i * 20)
    #/ Button /#
    grmex_qst_btn_back2main = tk.Button(grmex_qst_frm, text = "Cancel", command = lambda:changeFrm(main_frm, a_n))
    grmex_qst_btn_back2main.place(x=350, y=400)

    ##//  Score Frame  //##
    if q_n == 0:
        grmex_scr_frm = tk.Frame()
        grmex_scr_frm.grid(row=0, column=0, sticky="nsew")
        #/ Label /#
        grmex_scr_lbl_title = tk.Label(grmex_scr_frm, text= "Grammer Learning(" + lng + ")", font = font_1)
        grmex_scr_lbl_title.pack(expand = True)
        grmex_scr_lbl_score = tk.Label(grmex_scr_frm, text= "Score Result: " + str(a_n) + "/10", font = font_1)
        grmex_scr_lbl_score.pack(expand = True)
        #/ Button /#
        grmex_scr_btn_back2main = tk.Button(grmex_scr_frm, text = "Finish", command = lambda:changeFrm(main_frm, a_n))
        grmex_scr_btn_back2main.pack()

    return



###////                   //###
###///   Main Function   ///###
###//                   ////###
if __name__ == "__main__":
    ##///               /##
    ##//  Input Files  //##
    ##/               ///##
    checkFiles()
    readFiles()


    ##///          /##
    ##//  Window  //##
    ##/          ///##
    win = tk.Tk()
    win.title("L-SYS (Kyutech Global Hackathon)")
    win.geometry("800x600")
    

    ##//  Fonts  //##
    font_1 = font.Font(family = 'Helvetica', size = 20, weight = 'bold')


    ##///           /##
    ##//  Menubar  //##
    ##/           ///##
    menu_bar = tk.Menu(win)
    win.config(menu=menu_bar)
    #/ File Menu /#
    menu_fle = tk.Menu(menu_bar, tearoff=0)
    menu_fle.add_command(label = 'Vocabulary', command  =lambda:changeFrm(vcbmn_frm, a_num))
    menu_fle.add_command(label = 'Grammar', command = lambda:changeFrm(grmmn_frm, a_num))
    menu_fle.add_command(label = 'Exit', command = quit)
    menu_bar.add_cascade(label = 'Learn', menu = menu_fle)
    #/ About Menu /#
    menu_abt = tk.Menu(menu_bar, tearoff=0)
    menu_abt.add_command(label = 'About Us', command = lambda:web.open("https://github.com/Kyutech-Global-Hackathon-TeamG"))    #Open GitHub Organization Website 
    menu_bar.add_cascade(label = 'Help', menu = menu_abt)


    ##///              /##
    ##//  Main Frame  //##
    ##/              ///##
    main_frm = tk.Frame()
    main_frm.grid(row=0, column=0, sticky="nsew")
    #/ Logo /#
    main_img_lg = Image.open("../image/logo.png")
    main_img_w = main_img_lg.width
    main_img_h = main_img_lg.height
    main_img_lg = main_img_lg.resize((int(main_img_w * (500/main_img_h)), int(main_img_h * (500/main_img_h))))
    main_img_lg = ImageTk.PhotoImage(main_img_lg)
    canvas = tk.Canvas(main_frm, bg = "white", width = 800, height = 500)
    canvas.pack()
    canvas.create_image((800 - (main_img_w * (500/main_img_h)))/2, 0, image=main_img_lg, anchor=tk.NW)
    #/ Button /#
    main_btn_go2vocab = tk.Button(main_frm, text = "Vocabulary Learning", command = lambda:changeFrm(vcbmn_frm, a_num))
    main_btn_go2vocab.pack()
    main_btn_go2gram = tk.Button(main_frm, text = "Grammar Learning", command = lambda:changeFrm(grmmn_frm, a_num))
    main_btn_go2gram.pack()


    ##///                                  /##
    ##//  Vocabulary Learning Main Frame  //##
    ##/                                  ///##
    vcbmn_frm = tk.Frame()
    vcbmn_frm.grid(row=0, column=0, sticky="nsew")
    #/ Button /#
    vcbmn_btn_jp = tk.Button(vcbmn_frm, text = "Japanese", command = lambda:changeFrm(vcbjp_frm, a_num))
    vcbmn_btn_jp.pack()
    vcbmn_btn_en = tk.Button(vcbmn_frm, text = "English", command = lambda:changeFrm(vcben_frm, a_num))
    vcbmn_btn_en.pack()
    vcbmn_btn_back2main = tk.Button(vcbmn_frm, text = "Home", command = lambda:changeFrm(main_frm, a_num))
    vcbmn_btn_back2main.pack()


    ##//  Vocabulary Learning for Japanese Frame  //##
    vcbjp_frm = tk.Frame()
    vcbjp_frm.grid(row=0, column=0, sticky="nsew")
    #/ Button /#
    vcbjp_btn_back2exam = tk.Button(vcbjp_frm, text = "Start", command = lambda:vcbExam("jp", q_num, a_num))
    vcbjp_btn_back2exam.pack()
    vcbjp_btn_back2main = tk.Button(vcbjp_frm, text = "Home", command = lambda:changeFrm(main_frm, a_num))
    vcbjp_btn_back2main.pack()
    

    ##//  Vocabulary Learning for English Frame  //##
    vcben_frm = tk.Frame()
    vcben_frm.grid(row=0, column=0, sticky="nsew")
    #/ Button /#
    vcben_btn_back2exam = tk.Button(vcben_frm, text = "Start", command = lambda:vcbExam("en", q_num, a_num))
    vcben_btn_back2exam.pack()
    vcben_btn_back2main = tk.Button(vcben_frm, text = "Home", command = lambda:changeFrm(main_frm, a_num))
    vcben_btn_back2main.pack()


    ##///                               /##
    ##//  Grammar Learning Main Frame  //##
    ##/                               ///##
    grmmn_frm = tk.Frame()
    grmmn_frm.grid(row=0, column=0, sticky="nsew")
    #/ Button /#
    grmmn_btn_jp = tk.Button(grmmn_frm, text = "Japanese", command = lambda:changeFrm(grmjp_frm, a_num))
    grmmn_btn_jp.pack()
    grmmn_btn_en = tk.Button(grmmn_frm, text = "English", command = lambda:changeFrm(grmen_frm, a_num))
    grmmn_btn_en.pack()
    grmmn_btn_back2main = tk.Button(grmmn_frm, text = "Home", command = lambda:changeFrm(main_frm, a_num))
    grmmn_btn_back2main.pack()


    ##//  Grammar Learning for Japanese Frame  //##
    grmjp_frm = tk.Frame()
    grmjp_frm.grid(row=0, column=0, sticky="nsew")
    #/ Button /#
    grmjp_btn_back2exam = tk.Button(grmjp_frm, text = "Start", command = lambda:grmExam("jp", q_num, a_num))
    grmjp_btn_back2exam.pack()
    grmjp_btn_back2main = tk.Button(grmjp_frm, text = "Home", command = lambda:changeFrm(main_frm, a_num))
    grmjp_btn_back2main.pack()


    ##//  Grammar Learning for English Frame  //##
    grmen_frm = tk.Frame()
    grmen_frm.grid(row=0, column=0, sticky="nsew")
    #/ Button /#
    grmen_btn_back2exam = tk.Button(grmen_frm, text = "Start", command = lambda:grmExam("en", q_num, a_num))
    grmen_btn_back2exam.pack()
    grmen_btn_back2main = tk.Button(grmen_frm, text = "Home", command = lambda:changeFrm(main_frm, a_num))
    grmen_btn_back2main.pack()


    ##///                     /##
    ##//  Output GUI Window  //##
    ##/                     ///##
    main_frm.tkraise()
    win.mainloop()