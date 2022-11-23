import math
import numpy as np
import pandas as pd
import emoji
import utils
from utils import dates, stop_words, dates_aux, docs_aux
import re
import matplotlib.pyplot as plt
import PyPDF2


def clean_tweet(tweet):
    tweet_limpio = emoji.replace_emoji(tweet, replace="", version=-1)

    # Limpieza puntuacion
    regex = '[\\!\\"\\#\\$\\%\\&\\\'\\(\\)\\*\\+\\,\\-\\.\\/\\:\\;\\<\\=\\>\\?\\@\\[\\\\\\]\\^_\\`\\{\\|\\}\\~]'
    tweet_limpio = re.sub(regex, ' ', tweet_limpio)
    # elimina los numeros
    tweet_limpio = re.sub("\d+", ' ', tweet_limpio)
    # elimina espacion en blanco
    tweet_limpio = re.sub("\\s+", ' ', tweet_limpio)
    # separa por palabras
    tweet_limpio = tweet_limpio.split(sep=' ')
    # elimina palabras con tamaño < 2
    tweet_limpio = [term for term in tweet_limpio if term.lower() not in stop_words]
    tweet_limpio = [term for term in tweet_limpio if len(term) > 2]

    return tweet_limpio

def calcular_tf(top_10_palabras, lista_palabras):
    filtered_list = []
    for palabra in lista_palabras:
        for top in top_10_palabras:
            if top.lower() == palabra.lower():
                filtered_list.append(top.lower())
    # initialize dict with 0
    tf_dict = {}
    for top in top_10_palabras:
        tf_dict[top] = 0
    # populate dict with ocurrencies
    for word in filtered_list:
        if word in tf_dict.keys():
            tf_dict[word] += 1
        else:
            tf_dict[word] = 1
    # return normalized with Euclide
    values = list(tf_dict.values())
    power_temp = []
    for x in values:
        power_temp.append(x*x)
    module = np.sqrt(sum(power_temp))
    for key,value in tf_dict.items():
        if module != 0:
            tf_dict[key] = tf_dict[key]/module

    return tf_dict

def calcular_df(top_10_palabras, df_aux):
    df_dict = {}
    idf_dict = {}
    for top in top_10_palabras:
        df_dict[top] = 0
    # calculo df
    for doc in df_aux.keys():
        for palabra in top_10_palabras:
            if palabra in df_aux[doc]:
                df_dict[palabra] += 1
    # calculo idf
    for palabra in top_10_palabras:
        idf_dict[palabra] = math.log(13/df_dict[palabra],10)


    df_dict = {'df':df_dict, 'idf':idf_dict}

    return df_dict

def calcular_tf_idf(tf, idf, top_10_palabras):
    tf_idf = {}
    for doc in tf.keys():
        temp = {}
        for p in tf[doc]:
            temp[p] = (tf[doc][p])*idf['idf'][p]
        tf_idf[doc] = temp

    return tf_idf

def tabla(top_10_palabras, candidato):
    tweets = pd.read_csv('files/livetweets_data_no_json.csv', dtype='unicode')
    candidato_tweets = tweets['tweet_screen_name'].isin([candidato])
    filtro = tweets[candidato_tweets]
    count = 1

    tf = {}
    df_aux = {}
    for date in dates:
        start_date = date[0]
        end_date = date[1]
        after_start_date = filtro["tweet_date"] >= start_date
        before_end_date = filtro["tweet_date"] <= end_date
        between_two_dates = after_start_date & before_end_date
        filtered_dates = filtro.loc[between_two_dates]
        # tiene lista de tweets de la semana (DOCUMENTO)
        lista_tweets = filtered_dates.tweet_text.values
        # documentos.append(lista_tweets)
        palabras_semana = []
        for tweet in lista_tweets:
            tweet_limpio = clean_tweet(tweet)
            for palabra in tweet_limpio:
                palabras_semana.append(palabra.lower())
        # calcular tf
        tf_response = calcular_tf(top_10_palabras,  palabras_semana)
        tf['Doc '+str(count)] = tf_response
        count +=1
        df_aux[date] = palabras_semana
    print('------------- tf Table ----------------')
    tf_table = pd.DataFrame(tf, index=top_10_palabras)
    pd.set_option('display.max_columns', None)
    print(tf_table)

    print('------------- df | idf Table ----------------')
    df = calcular_df(top_10_palabras, df_aux)
    df_table = pd.DataFrame(df, index=top_10_palabras)
    pd.set_option('display.max_columns', None)
    print(df_table)

    print('------------- tf-idf Table ----------------')
    idf = {'idf':df['idf']}
    tf_idf = calcular_tf_idf(tf, idf, top_10_palabras)
    tf_idf_table = pd.DataFrame(tf_idf, index=top_10_palabras)
    pd.set_option('display.max_columns', None)
    print(tf_idf_table)

    print('------------- Linea de tiempo ----------------')
    linea_tiempo(tf, top_10_palabras)

    print('------------- Query ----------------')
    query_vector(top_10_palabras,df,tf)

    print('------------- Similaridad Tweets ----------------')
    similaridad_tweets(tf)

    print('------------- Similaridad Manifiestos ----------------')
    similaridad_manifiestos(df,candidato,top_10_palabras)

def top_10():
    candidatos = pd.read_csv('files/account_info.csv', dtype='unicode')
    tweets = pd.read_csv('files/livetweets_data_no_json.csv', dtype='unicode')

    username_candidatos = candidatos['twitter_screen_name'].values.tolist()
    username_general = tweets['tweet_screen_name'].values.tolist()
    candidatos = {}


    username_candidatos = utils.username_candidatos
    for candidato in username_candidatos:
        candidatos.update({candidato: 0})
    for x in username_general:

        if x in candidatos:
            candidatos[x] += 1

    candidatos_sorted = sorted(candidatos.items(), key=lambda i: i[1], reverse=True)
    lista_cantidados = []
    print('TOP 10 Candidatos')
    for i in range(10):
        print(candidatos_sorted[i])
        lista_cantidados.append(candidatos_sorted[i][0])
    print('----------------------------------')
    return lista_cantidados

def palabras_mas_usadas(lista_cantidatos):
    tweets = pd.read_csv('files/livetweets_data_no_json.csv', dtype='unicode')
    dic_general = {}
    # m representa un candidato del top 10 de candidatos
    for m in lista_cantidatos:
        temp_tweets = tweets['tweet_screen_name'].isin([str(m)])
        filtro = tweets[temp_tweets]
        lista_tweets = filtro['tweet_text'].values
        dic_frecuencias = {}
        for x in lista_tweets:
            #Limpieza de emojis y creacion de lista
            tweet_limpio = clean_tweet(x)
            for y in tweet_limpio:
                if y.lower() != m.lower() and y.lower() not in m.lower():
                    y = y.lower()
                    if y in dic_frecuencias:
                        dic_frecuencias[y] +=1
                    else:
                        dic_frecuencias.update({y: 0})
        dic_general[m] = dic_frecuencias
        top_10_words = sorted(dic_general[m].items(), key=lambda i: i[1], reverse=True)
        temp_top_10 = []
        print('TOP 10 Palabras - candidato ',m)
        for i in range(10):
            print(top_10_words[i])
            temp_top_10.append(top_10_words[i][0])
        tabla(temp_top_10, m)
        print('---------------------------------')

def linea_tiempo(tf, top_10_palabras):

    valores = []
    for palabra in top_10_palabras:
        temp = []
        for key, value in tf.items():
            temp.append(value[palabra])
        valores.append(temp)

    data = {}
    for i in range(10):
        data['palabra'+str(i)] = dates_aux
        data[top_10_palabras[i]] = valores[i]

    print(data)
    df = pd.DataFrame(data)
    ax = plt.gca()
    for i in range(10):
        df.plot(kind='line', x= 'palabra'+str(i), y=top_10_palabras[i], ax=ax)
    plt.show()

def query_vector(top_10_palabras, df, tf):
    query = input('Ingrese un query: ')
    dic_temp={}
    for palabra in top_10_palabras:
        dic_temp[palabra] = 0
    lista = query.split(' ')
    for n in lista:
        if n in dic_temp:
            dic_temp[n] +=1

    df['tf'] = dic_temp
    idf_temp= df['idf']

    wtq_temp={}
    vector_wtq = []
    for k,v in idf_temp.items():
        wtq_temp[k] = v*dic_temp[k]
        vector_wtq.append(v*dic_temp[k])
    df['wtq'] = wtq_temp

    wtd_temp={}
    vectores_doc = []
    for k,v in tf.items():
        temp_doc = []
        for n in v.values():
            temp_doc.append(n)
        vectores_doc.append(temp_doc)
    ranking=[]
    wtd_vector=[]
    for n in vectores_doc:
        temp_wtd = []
        for y in range(10):
            temp_wtd.append(n[y]*vector_wtq[y])
        suma =0
        for g in range(10):
            suma= suma+temp_wtd[g]
        ranking.append(suma)
        wtd_vector.append(temp_wtd)
    for j in range(13):
        wtd_temp['doc'+str(j+1)] = wtd_vector[j]

    ranking_dict = {}
    for i in range(13):
        ranking_dict['doc'+str(i+1)] = ranking[i]
    ranking_dict = {'Ranking':ranking_dict}

    print('------------- Tabla con w_tq de Query ----------------')
    df_table = pd.DataFrame(df, index=top_10_palabras)
    pd.set_option('display.max_columns', None)
    print(df_table)

    print('------------- Tabla Producto por Documento ----------------')
    df_table = pd.DataFrame(wtd_temp, index=top_10_palabras)
    pd.set_option('display.max_columns', None)
    print(df_table)

    print('------------- Tabla de Ranking para el Query  ----------------')
    # imprime los rankings
    df_table = pd.DataFrame(ranking_dict,index=docs_aux)
    pd.set_option('display.max_columns', None)
    print(df_table)

def similaridad_tweets(tf):
    vectores_doc=[]
    for k,v in tf.items():
        temp_doc = []
        for n in v.values():
            temp_doc.append(n)
        vectores_doc.append(temp_doc)
    count = 1
    for f in vectores_doc:
        temp_ranking={}
        for i in range(13):
            temp_ranking['doc'+str(i+1)] = np.dot(f,vectores_doc[i])

        tf_table = pd.DataFrame(temp_ranking, index=['doc'+str(count)])
        pd.set_option('display.max_columns', None)
        print(tf_table)
        count+=1
        print('---------------------------------')

def manifiesto_query(df,top_10_twitter, top_10_manifiesto, tf,candidato):
    query = top_10_manifiesto
    dic_temp = {}
    for palabra in top_10_twitter:
        dic_temp[palabra] = 0
    lista = query
    for n in lista:
        if n in dic_temp:
            dic_temp[n] += 1

    df['tf'] = dic_temp
    idf_temp = df['idf']

    wtq_temp = {}
    vector_wtq = []
    for k, v in idf_temp.items():
        wtq_temp[k] = v * dic_temp[k]
        vector_wtq.append(v * dic_temp[k])
    df['wtq'] = wtq_temp

    wtd_temp = {}
    vectores_doc = []
    for k, v in tf.items():
        temp_doc = []
        for n in v.values():
            temp_doc.append(n)
        vectores_doc.append(temp_doc)
    ranking = []
    wtd_vector = []

    for n in vectores_doc:
        temp_wtd = []
        for y in range(10):
            temp_wtd.append(n[y] * vector_wtq[y])
        suma = 0
        for g in range(10):
            suma = suma + temp_wtd[g]
        ranking.append(suma)
        wtd_vector.append(temp_wtd)
    for j in range(1):
        wtd_temp['Manifiesto'] = wtd_vector[j]

    ranking_dict = {}
    for i in range(1):
        ranking_dict['Score(twitter,manifiesto): '] = ranking[i]
        dic_ranking_manifiesto[candidato] = ranking[i]
    ranking_dict = {'Ranking': ranking_dict}

    print('------------- Tabla con w_tq de Query Manifiesto ----------------')
    df_table = pd.DataFrame(df, index=top_10_twitter)
    pd.set_option('display.max_columns', None)
    print(df_table)

    print('------------- Tabla Producto por Query x Manifiesto ----------------')
    df_table = pd.DataFrame(wtd_temp, index=top_10_twitter)
    pd.set_option('display.max_columns', None)
    print(df_table)

    print('------------- Tabla de Ranking para el Query  ----------------')
    # imprime los rankings
    df_table = pd.DataFrame(ranking_dict, index=['Score(twitter,manifiesto): '])
    pd.set_option('display.max_columns', None)
    print(df_table)

def similaridad_manifiestos(df, candidato, top_10_twitter):
    paths = utils.paths_manifiestos

    tf_manifiestos = {}
    df_candidatos = df

    pdfFileObj = open('00_Quito/'+paths[candidato], 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    text = []
    exclude = utils.exclude


    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(i)
        lineas_por_documento = pageObj.extractText().split('\n')
        for f in lineas_por_documento:
            text.append(f.strip())
    dic_frecuencias = {}
    palabras = []
    for x in text:
        # Limpieza de emojis y creacion de lista
        tweet_limpio = clean_tweet(x)
        for y in tweet_limpio:
            y = y.lower()
            if y not in exclude:
                if y in dic_frecuencias:
                    palabras.append(y)
                    dic_frecuencias[y] += 1
                else:
                    palabras.append(y)
                    dic_frecuencias.update({y: 1})

    top_10_words = sorted(dic_frecuencias.items(), key=lambda i: i[1], reverse=True)
    temp_top_10 = []
    print('TOP 10 Palabras Manifiestos - Candidato ',candidato)
    for i in range(10):
        print(top_10_words[i])
        temp_top_10.append(top_10_words[i][0])
    print('-------------------------')

    tf_response = calcular_tf(temp_top_10, palabras)
    tf_manifiestos[paths[candidato]] = tf_response

    manifiesto_query(df_candidatos, top_10_twitter, temp_top_10, tf_manifiestos,candidato)

def pastel(dic_ranking_manifiesto):
    for k,v in dic_ranking_manifiesto.items():
        ranking = [v,1-v]
        candidatos = ['similaridad','no_similaridad']
        plt.pie(ranking, labels=candidatos, autopct="%0.1f %%")
        plt.title(k)
        plt.axis("equal")
        plt.show()

if __name__ == '__main__':
    dic_ranking_manifiesto = {}
    lista_cantidatos = top_10()
    palabras_mas_usadas(lista_cantidatos)
    pastel(dic_ranking_manifiesto)