import nltk #形態素解析
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from janome.tokenizer import Tokenizer

import pandas as pd

import requests
import bs4
from bs4 import BeautifulSoup
import urllib.request as req
from urllib.request import urlopen
import os,re,sys
import time

def Morphological_analysis(s):
    t = Tokenizer()
    list_dic = []
    for token in t.tokenize(s):
        #print(token)
        #print(token.surface, token.part_of_speech.split(",")[0], token.base_form)
        if token.part_of_speech.split(",")[0]=="名詞":
            if token.part_of_speech.split(",")[1]!="数" and token.part_of_speech.split(",")[1]!="固有名詞":
                list1 = [token.surface,  token.base_form]
                list_dic.append(list1)
        elif token.part_of_speech.split(",")[0] in ["動詞", "形容詞", "形容動詞"]:
            list1 = [token.surface,  token.base_form]
            list_dic.append(list1)
    return list_dic
            
def get_html(url):
    time.sleep(1.0)
    html=requests.get(url).text
    html=BeautifulSoup(html,"html.parser")
    return html

def get_en(html):
    word_en = html.find_all("td" ,class_="content-explanation je")[0].get_text()
    if ";" in word_en:
        return list(set(word_en.split(";")))
    else:
        return list(set(word_en.split("、")))
    
def get_jp(html):
    word_en = html.find_all("td" ,class_="content-explanation ej")[0].get_text()
    return list(set(word_en.split("、")))

def talk2word_j2e(df_talk_path, df_save_path):
    df_talk = pd.read_csv(df_talk_path, encoding="shift-jis")
    try:
        df_save = pd.read_csv(df_save_path)
    except:
        df_save = pd.DataFrame([],columns=["JP","EN"])

    #形態素解析
    flashcard = []
    for i in range(len(df_talk)):
        flashcard += Morphological_analysis(df_talk["JP"][i])
    flashcard = list(map(list, set(map(tuple, flashcard))))
    df_flashcard = pd.DataFrame(flashcard, columns=["単語", "基本形"])

    #日本語＝＞英単語(スクレイピング)
    df_flashcard_j2e = []
    for i in range(len(df_flashcard)):
        jw = df_flashcard["基本形"][i]
        html = get_html("https://ejje.weblio.jp/content/"+jw)
        for ew in get_en(html):
            df_flashcard_j2e.append([jw, ew])

    #ファイル出力
    df_flashcard_j2e = pd.DataFrame(df_flashcard_j2e,columns=["JP","EN"])
    df_flashcard_j2e = pd.concat([df_save,df_flashcard_j2e])
    df_flashcard_j2e = df_flashcard_j2e.drop_duplicates()
    df_flashcard_j2e.to_csv(df_save_path,index=None)
    
    return 

def talk2word_e2j(df_talk_path, df_save_path):
    df_talk = pd.read_csv(df_talk_path, encoding="shift-jis")
    try:
        df_save = pd.read_csv(df_save_path)
    except:
        df_save = pd.DataFrame([],columns=["JP","EN"])
    
    #形態素解析
    flashcard = []
    part_of_speech = ["NN", "JJ", "JJR","JJS", "NNS", "VB","VBD", "VBG","VBN","VBP","VBZ"]
    for i in range(len(df_talk)):
        #flashcard += Morphological_analysis(df["JP"][i])
        morph = nltk.word_tokenize(df_talk["EN"][i])
        pos = nltk.pos_tag(morph)
        for p in pos:
            if p[1] in part_of_speech:
                flashcard.append(p[0])

    df_flashcard_e2j = []
    for i in range(len(flashcard)):
        ew = flashcard[i]
        html = get_html("https://ejje.weblio.jp/content/"+ew)
        for jw in get_jp(html):
            df_flashcard_e2j.append([ew, jw])

    df_flashcard_e2j = pd.DataFrame(df_flashcard_e2j,columns=["EN", "JP"])
    df_flashcard_e2j = pd.concat([df_save,df_flashcard_e2j])
    df_flashcard_e2j = df_flashcard_e2j.drop_duplicates()
    df_flashcard_e2j.to_csv(df_save_path, index=None)
    
    return 

