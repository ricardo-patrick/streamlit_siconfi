import streamlit as st
import pandas as pd
import requests
import json

st.set_page_config(layout='wide')

st.title('Página com informações da API - Siconfi')

df_anexos = requests.get("https://apidatalake.tesouro.gov.br/ords/siconfi/tt/anexos-relatorios")
df_anexos = df_anexos.json()
if df_anexos['count'] != 0:
    st.subheader('anexos')
    df_anexos_tab = pd.DataFrame(df_anexos['items'])
    df_anexos_tab
else:
    st.subheader('anexos')
    st.write('Não tem')


df_entes = requests.get("https://apidatalake.tesouro.gov.br/ords/siconfi/tt/entes")
df_entes = df_entes.json()
if df_entes['count'] != 0:
    st.subheader('antes')
    df_entes_tab = pd.DataFrame(df_entes['items'])
    df_entes_tab
else:
    st.subheader('antes')
    st.write('Não tem')


df_extratos = requests.get("https://apidatalake.tesouro.gov.br/ords/siconfi/tt/extrato_entregas")
df_extratos = df_extratos.json()
if df_extratos['count'] != 0:
    st.subheader('extratos')
    df_extratos_tab = pd.DataFrame(df_extratos['items'])
    df_extratos_tab
else:
    st.subheader('extratos')
    st.write('Não tem')


df_rreo = requests.get("https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rreo")
df_rreo = df_rreo.json()
if df_rreo['count'] != 0:
    st.subheader('rreo')
    df_rreo_tab = pd.DataFrame(df_rreo['items'])
    df_rreo_tab
else:
    st.subheader('rreo')
    st.write('Não tem')


df_rgf = requests.get("https://apidatalake.tesouro.gov.br/ords/siconfi/tt/rgf")
df_rgf = df_rgf.json()
if df_rgf['count'] != 0:
    st.subheader('rgf')
    df_rgf_tab = pd.DataFrame(df_rgf['items'])
    df_rgf_tab
else:
    st.subheader('rgf')
    st.write('Não tem')


df_dca = requests.get("https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca")
df_dca = df_dca.json()
if df_dca['count'] != 0:
    st.subheader('dca')
    df_dca_tab = pd.DataFrame(df_dca['items'])
    df_dca_tab
else:
    st.subheader('dca')
    st.write('Não tem')


df_msc_patrimonial = requests.get("https://apidatalake.tesouro.gov.br/ords/siconfi/tt/msc_patrimonial")
df_msc_patrimonial = df_msc_patrimonial.json()
if df_msc_patrimonial['count'] != 0:
    st.title('msc_patrimonial')
    df_msc_patrimonial_tab = pd.DataFrame(df_msc_patrimonial['items'])
    df_msc_patrimonial_tab
else:
    st.title('msc_patrimonial')
    st.write('Não tem')


df_msc_orcamentaria = requests.get("https://apidatalake.tesouro.gov.br/ords/siconfi/tt/msc_orcamentaria")
df_msc_orcamentaria = df_msc_orcamentaria.json()
if df_msc_orcamentaria['count'] != 0:
    st.title('msc_orcamentaria')
    df_msc_orcamentaria_tab = pd.DataFrame(df_msc_orcamentaria['items'])
    df_msc_orcamentaria_tab
else:
    st.title('msc_orcamentaria')
    st.write('Não tem')


df_msc_controle = requests.get("https://apidatalake.tesouro.gov.br/ords/siconfi/tt/msc_controle")
df_msc_controle = df_msc_controle.json()
if df_msc_controle['count'] != 0:
    st.title('msc_controle')
    df_msc_controle_tab = pd.DataFrame(df_msc_controle['items'])
    df_msc_controle_tab
else:
    st.title('msc_controle')
    st.write('Não tem')



