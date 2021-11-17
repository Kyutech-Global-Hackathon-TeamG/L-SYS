from janome.tokenizer import Tokenizer
# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
import pandas as pd
import sys

def talk2phrase(input_path, output_path):
    df_talk = pd.read_csv(input_path, encoding="shift-jis")
        
    t = Tokenizer()
    df_phrase = []
    for i in range(len(df_talk)):
        sj = df_talk["JP"][i]
        se = df_talk["EN"][i]
        sj_split = "/".join(list(t.tokenize(sj, wakati=True)))
        se_split = se.replace(" ","/")[:-1]+"/"+se.replace(" ","/")[-1]
        df_phrase.append([sj_split, se_split])

    df_phrase  = pd.DataFrame(df_phrase ,columns=["JP","EN"])
    #df_phrase = pd.concat([df_save,df_phrase])
    df_phrase = df_phrase.drop_duplicates()
    df_phrase.to_csv(output_path, index=None, sep="\t")

    return


