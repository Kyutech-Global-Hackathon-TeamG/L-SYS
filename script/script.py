import os
import csv
import tkinter as tk
import tkinter.font as font
import webbrowser as web
from PIL import Image, ImageTk
#import talk2word


###////                //###
###///   Parameters   ///###
###//                ////###

q_num = 10
csv_dict ={'talk':['../csv/talk.csv', 0],
           'wordbook':['../csv/wordbook.csv', 0],
           'phrasebook':['../csv/phrasebook.csv', 0]}



###////               //###
###///   Functions   ///###
###//               ////###

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



###///   Update GUI Frame Function   ///###
def updateFrm(lrn, lng, frame, num):
    frame.destroy()
    num += -1
    if lrn == "vcb":
        vcbExam(lng, num)
    elif lrn == "grm":
        grmExam(lng, num)
    return



###///   Vocabulary Learning Function   ///###
def vcbExam(lng, num):
    ##//  Question Frame  //##
    #global vcbex_qst_frm
    vcbex_qst_frm = tk.Frame()
    vcbex_qst_frm.grid(row=0, column=0, sticky="nsew")
    #/ Label /#
    vcbex_qst_lbl_title = tk.Label(vcbex_qst_frm, text = lng + " Vocabulary Learning " + str(num), font = font_1)
    vcbex_qst_lbl_title.pack(expand = True)
    #/ Button /#
    vcbex_qst_btn_go2exam = tk.Button(vcbex_qst_frm, text = "Next", command = lambda:updateFrm("vcb", lng, vcbex_qst_frm, num))
    vcbex_qst_btn_go2exam.pack()
    vcbex_qst_btn_back2main = tk.Button(vcbex_qst_frm, text = "Cancel", command = lambda:changeFrm(main_frm))
    vcbex_qst_btn_back2main.pack()

    ##//  Score Frame  //##
    if num == 0:
        vcbex_scr_frm = tk.Frame()
        vcbex_scr_frm.grid(row=0, column=0, sticky="nsew")
        #/ Button /#
        vcbex_scr_btn_back2main = tk.Button(vcbex_scr_frm, text = "Finish", command = lambda:changeFrm(main_frm))
        vcbex_scr_btn_back2main.pack()

    return
    


###///   Grammar Learning Function   ///###
def grmExam(lng, num):
    ##//  Question Frame  //##
    #global vcbex_qst_frm
    vcbex_qst_frm = tk.Frame()
    vcbex_qst_frm.grid(row=0, column=0, sticky="nsew")
    #/ Label /#
    vcbex_qst_lbl_title = tk.Label(vcbex_qst_frm, text= lng + " Grammer Learning " + str(num), font = font_1)
    vcbex_qst_lbl_title.pack(expand = True)
    #/ Button /#
    vcbex_qst_btn_go2exam = tk.Button(vcbex_qst_frm, text = "Next", command = lambda:updateFrm("grm", lng, vcbex_qst_frm, num))
    vcbex_qst_btn_go2exam.pack()
    vcbex_qst_btn_back2main = tk.Button(vcbex_qst_frm, text = "Cancel", command = lambda:changeFrm(main_frm))
    vcbex_qst_btn_back2main.pack()

    ##//  Score Frame  //##
    if num == 0:
        vcbex_scr_frm = tk.Frame()
        vcbex_scr_frm.grid(row=0, column=0, sticky="nsew")
        #/ Button /#
        vcbex_scr_btn_back2main = tk.Button(vcbex_scr_frm, text = "Finish", command = lambda:changeFrm(main_frm))
        vcbex_scr_btn_back2main.pack()

    return



###////                   //###
###///   Main Function   ///###
###//                   ////###
if __name__ == "__main__":
    ##///               /##
    ##//  Check Files  //##
    ##/               ///##
    checkFiles()


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
    menu_fle.add_command(label = 'Vocabulary', command  =lambda:changeFrm(vcbmn_frm))
    menu_fle.add_command(label = 'Grammar', command = lambda:changeFrm(grmmn_frm))
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
    main_btn_go2vocab = tk.Button(main_frm, text = "Vocabulary Learning", command = lambda:changeFrm(vcbmn_frm))
    main_btn_go2vocab.pack()
    main_btn_go2gram = tk.Button(main_frm, text = "Grammar Learning", command = lambda:changeFrm(grmmn_frm))
    main_btn_go2gram.pack()


    ##///                                  /##
    ##//  Vocabulary Learning Main Frame  //##
    ##/                                  ///##
    vcbmn_frm = tk.Frame()
    vcbmn_frm.grid(row=0, column=0, sticky="nsew")
    #/ Button /#
    vcbmn_btn_jp = tk.Button(vcbmn_frm, text = "Japanese", command = lambda:changeFrm(vcbjp_frm))
    vcbmn_btn_jp.pack()
    vcbmn_btn_en = tk.Button(vcbmn_frm, text = "English", command = lambda:changeFrm(vcben_frm))
    vcbmn_btn_en.pack()
    vcbmn_btn_back2main = tk.Button(vcbmn_frm, text = "Home", command = lambda:changeFrm(main_frm))
    vcbmn_btn_back2main.pack()


    ##//  Vocabulary Learning for Japanese Frame  //##
    vcbjp_frm = tk.Frame()
    vcbjp_frm.grid(row=0, column=0, sticky="nsew")
    #/ Button /#
    vcbjp_btn_back2exam = tk.Button(vcbjp_frm, text = "Start", command = lambda:vcbExam("jp", q_num))
    vcbjp_btn_back2exam.pack()
    vcbjp_btn_back2main = tk.Button(vcbjp_frm, text = "Home", command = lambda:changeFrm(main_frm))
    vcbjp_btn_back2main.pack()
    

    ##//  Vocabulary Learning for English Frame  //##
    vcben_frm = tk.Frame()
    vcben_frm.grid(row=0, column=0, sticky="nsew")
    #/ Button /#
    vcben_btn_back2exam = tk.Button(vcben_frm, text = "Start", command = lambda:vcbExam("en", q_num))
    vcben_btn_back2exam.pack()
    vcben_btn_back2main = tk.Button(vcben_frm, text = "Home", command = lambda:changeFrm(main_frm))
    vcben_btn_back2main.pack()


    ##///                               /##
    ##//  Grammar Learning Main Frame  //##
    ##/                               ///##
    grmmn_frm = tk.Frame()
    grmmn_frm.grid(row=0, column=0, sticky="nsew")
    #/ Button /#
    grmmn_btn_jp = tk.Button(grmmn_frm, text = "Japanese", command = lambda:changeFrm(grmjp_frm))
    grmmn_btn_jp.pack()
    grmmn_btn_en = tk.Button(grmmn_frm, text = "English", command = lambda:changeFrm(grmen_frm))
    grmmn_btn_en.pack()
    grmmn_btn_back2main = tk.Button(grmmn_frm, text = "Home", command = lambda:changeFrm(main_frm))
    grmmn_btn_back2main.pack()


    ##//  Grammar Learning for Japanese Frame  //##
    grmjp_frm = tk.Frame()
    grmjp_frm.grid(row=0, column=0, sticky="nsew")
    #/ Button /#
    grmjp_btn_back2exam = tk.Button(grmjp_frm, text = "Start", command = lambda:grmExam("jp", q_num))
    grmjp_btn_back2exam.pack()
    grmjp_btn_back2main = tk.Button(grmjp_frm, text = "Home", command = lambda:changeFrm(main_frm))
    grmjp_btn_back2main.pack()


    ##//  Grammar Learning for English Frame  //##
    grmen_frm = tk.Frame()
    grmen_frm.grid(row=0, column=0, sticky="nsew")
    #/ Button /#
    grmen_btn_back2exam = tk.Button(grmen_frm, text = "Start", command = lambda:grmExam("en", q_num))
    grmen_btn_back2exam.pack()
    grmen_btn_back2main = tk.Button(grmen_frm, text = "Home", command = lambda:changeFrm(main_frm))
    grmen_btn_back2main.pack()


    ##///                     /##
    ##//  Output GUI Window  //##
    ##/                     ///##
    main_frm.tkraise()
    win.mainloop()