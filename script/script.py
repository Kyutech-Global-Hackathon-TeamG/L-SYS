import os
import csv
import tkinter as tk
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


    ##//  Main Frame  //##
    main_frm = tk.Frame()
    main_frm.grid(row=0, column=0, sticky="nsew")
    main_btn_go2vocab = tk.Button(main_frm, text="Vocabulary Learning", command = lambda:changeFrm(vocab_frm))
    main_btn_go2vocab.pack()
    main_btn_go2gram = tk.Button(main_frm, text="Grammar Learning", command = lambda:changeFrm(gram_frm))
    main_btn_go2gram.pack()


    ##//  Vocabulary Learning Frame  //##
    vocab_frm = tk.Frame()
    vocab_frm.grid(row=0, column=0, sticky="nsew")
    vocab_btn_back2main = tk.Button(vocab_frm, text="Home", command = lambda:changeFrm(main_frm))
    vocab_btn_back2main.pack()


    ##//  Grammar Learning Frame  //##
    gram_frm = tk.Frame()
    gram_frm.grid(row=0, column=0, sticky="nsew")
    gram_btn_back2main = tk.Button(gram_frm, text="Home", command = lambda:changeFrm(main_frm))
    gram_btn_back2main.pack()


    ##//  Output GUI Window  //##
    main_frm.tkraise()
    win.mainloop()