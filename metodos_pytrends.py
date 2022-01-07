# pip install pytrends
import pandas as pd
from pytrends.request import TrendReq
import json
pytrends = TrendReq(hl='sp-MX', tz=360)


def tendencias_mex():
    df = pytrends.trending_searches(pn="mexico")
    df.rename(columns={0:'tendencias_mx'},inplace=True)
    trends_mx_json=df.to_json()
    return trends_mx_json


#datos de single_q y comparison_q 
def tendencias_i(inicio,fin,single_q,comparison_q=None):
    periodo=inicio+' '+fin
    words=list()
    words.append(single_q)
    if(comparison_q != None):
        words.append(comparison_q)
    pytrends.build_payload(words,timeframe=periodo,geo='MX')
    df_tendencias=pytrends.interest_over_time()
    df_tendencias.drop(columns='isPartial', inplace=True)
    json_tendencias=df_tendencias.to_json(orient='index')
    return json_tendencias


def tendencias_region(inicio,fin,single_q,comparison_q=None):
    periodo=inicio+' '+fin
    words=list()
    words.append(single_q)
    if(comparison_q != None):
        words.append(comparison_q)
    pytrends.build_payload(words,timeframe=periodo,geo='MX')
    df_tendencias_region=pytrends.interest_by_region(resolution='COUNTRY',inc_low_vol=True)
    json_tendencias_region=df_tendencias_region.to_json()
    json_utf=str(json_tendencias_region).encode('utf-8','strict')
    return json_utf


def suggestions_word(single_q,comparison_q=None):
    single_q_sugg = pytrends.suggestions(single_q)
    i=0
    single_q_json={}
    for elem in single_q_sugg:
        single_q_json[str(i)]=single_q_sugg[i]['title']
        i+=1
    if(comparison_q != None):
        comparison_q_sugg = pytrends.suggestions(comparison_q)
        comparison_q_json = {}
        i=0
        for elem in comparison_q_sugg:
            comparison_q_json[str(i)]=comparison_q_sugg[i]['title']
            i+=1
        json_c={'single_q_sugg':single_q_json,'comparison_q_sugg':comparison_q_json}
    else: 
        json_c={'single_q_sugg':single_q_json}
    return json_c


#máximo 5 palabras
def _related_queries(single_q,comparison_q=None):
    words=list()
    words.append(single_q)
    if(comparison_q!=None):
        words.append(comparison_q)
    else: 
        pass
    pytrends.build_payload(words)
    related_queries_dict=pytrends.related_queries()
    single_q_rising=related_queries_dict[single_q]['rising']
    single_q_top=related_queries_dict[single_q]['top']
    single_q_r_json=single_q_rising.to_json(orient='index')
    single_q_t_json=single_q_top.to_json(orient='index')
    json_c={
        'temas_relacionados_single_query': {'top':single_q_t_json,'rising': single_q_r_json}
    }
    if (comparison_q != None):
        comparison_q_rising=related_queries_dict[comparison_q]['rising']
        comparison_q_top=related_queries_dict[comparison_q]['top']
        comparison_q_r_json=comparison_q_rising.to_json(orient='index')
        comparison_q_t_json=comparison_q_top.to_json(orient='index')
        json_c=json_c={
        'temas_relacionados_single_query': {'top':single_q_t_json,'rising': single_q_r_json},
            'temas_relacionados_comparison_query':{'top': comparison_q_t_json,
                                                   'rising':comparison_q_r_json
                                                  }}
    else: 
        json_c={
        'temas_relacionados_single_query': {'top':single_q_t_json,'rising': single_q_r_json}}
    return json_c


#Solo podemos extraer por año (se quitó el soporte para hacer consultas mensuales) hasta 2020
def data_top_chart(periodo=2020,ubicacion='MX'):
    top_charts_df = pytrends.top_charts(periodo, hl='sp-MX', tz=300, geo=ubicacion)
    return top_charts_df


def all_trends(inicio,fin,single_q,comparison_q=None):
    periodo=inicio+' '+fin
    json_tendencias=tendencias_i(inicio,fin,single_q,comparison_q)
    json_tendencias_reg=tendencias_region(inicio,fin,single_q,comparison_q)
    json_sugerencias=suggestions_word(single_q,comparison_q)
    json_related=_related_queries(single_q,comparison_q)
    json_completo={
        'tendencias':json_tendencias,'tendencias region':json_tendencias_reg,\
        'sugerencias':json_sugerencias,'relacionados':json_related
    }
    return json_completo
