#  Файл нужно положить именно в тот каталог где  лежат файлы. Скрипт создаст папку OUT  и  все файлы будут там.
# Обрабатывает только файлы из  file_dict  плюс rusplt,novorus,cnews
#
import glob 
import pandas as pd 
import os
import shutil
FileList = glob.glob('*.csv') 
#print(FileList) 
err_log=[]
#Work_list=list(set(FileList)-set(end_work))
if os.path.exists('OUT'): shutil.rmtree('OUT', ignore_errors=False, onerror=None)
os.mkdir('OUT')

file_dict={'ria.ru.csv': 3, 'sobesednik.ru.csv': 3, 'lookat.me.csv': 4, 'grani.ru.csv': 4,
           'interfax.ru.csv': 3, 'novayagazeta.ru.csv': 3, 'ura.ru.csv': 4, 'vedomosti.ru.csv': 3,
           'inosmi.ru.csv': 3, 'podrobnosti.com.ua.csv': 3, 'gazeta.ru.csv': 3, 'vogue.ua.csv': 3,
           'planet.su.csv': 3, 'belaruspartisan.org.csv': 3, 'newsru.com.csv': 3, 'buro247.ru.csv': 3,
           'news.su.csv': 3, 'km.ru.csv': 3, 'rus.tvnet.lv.csv': 4, 'rus.newsru.ua.csv': 3, 
           'svpressa.ru.csv': 3, 'rbc.ru.csv': 3, 'tass.com.csv': 3}
#kom_dict={}

def split_novorus(s):
    l=[]
    #novorus  
    l=s.split('/')
    if len(l)>5:return l[4]
    else:return 'NaN'
    #------
    #ruspult
def split_rusplt(s):
    l=[]
    t=[]
    l=s.split('/')
    if l[2]=='rusplt.ru':
        return l[3]
        print(l[3])
    else:
        t=l[2].split('.')
       # print (t[0])
        return t[0]
    #---------
    #cnews
def split_cnews(s):
    l=[]
    t=[]
    l=s.split('/')
    if l[2]=='cnews.ru':return 'NaN'
    else:
        t=l[2].split('.')
        return t[0]
    

for fname in FileList: 
    fname_split=fname.split('-')[-1]
    if fname_split in file_dict.keys():
        fname_split=fname.split('-')[-1]
        df = pd.read_csv(fname) 
        df[['date','URL']]=df[['URL','date']]
        try:
            df['topics'] = df['URL'].map(lambda x: x.split('/')[file_dict[fname_split]])
            df.to_csv('OUT/'+fname, encoding='utf-8',index=False)
        
       
        except:
            
            err_log.append(fname)
      
    elif fname_split == 'novorus.info.csv':
        
        df = pd.read_csv(fname) 
        df[['date','URL']]=df[['URL','date']]
        df['topics'] = df.URL.apply(split_novorus)
        df.to_csv('OUT/'+fname, encoding='utf-8',index=False)
    elif fname_split == 'rusplt.ru.csv':
        df = pd.read_csv(fname) 
        df[['date','URL']]=df[['URL','date']]
        
        df['topics'] = df.URL.apply(split_rusplt)
        df.to_csv('OUT/'+fname, encoding='utf-8',index=False) 
    elif fname_split == 'cnews.ru.csv':
        df = pd.read_csv(fname) 
        df[['date','URL']]=df[['URL','date']]
        df['topics'] = df.URL.apply(split_cnews)
        df.to_csv('OUT/'+fname, encoding='utf-8',index=False)  
                                         
with open('OUT/result.txt','w') as result:

    result.write('ошибки: '+str(err_log)+'\n\n')

   

