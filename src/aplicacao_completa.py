import pandas as pd
import streamlit as st
from datetime import datetime
from pydantic import ValidationError
from validador import PlanilhaVendas

def validar_linha(dados: dict) -> tuple[bool, str]:
    try:
        PlanilhaVendas(
            organizador=dados['Organizador'],
            ano_mes=dados['Ano_Mes'],
            dia_da_semana=dados['Dia_da_Semana'],
            tipo_dia=dados['Tipo_Dia'],
            objetivo=dados['Objetivo'],
            date=dados['Date'],
            adset_name=dados['AdSet_name'],
            amount_spent=dados['Amount_spent'],
            link_clicks=dados['Link_clicks'] if pd.notna(dados['Link_clicks']) else 0,
            impressions=dados['Impressions'] if pd.notna(dados['Impressions']) else 0,
            conversions=dados['Conversions'] if pd.notna(dados['Conversions']) else 0,
            segmentacao=dados['Segmentação'],
            tipo_de_anuncio=dados['Tipo_de_Anúncio'],
            fase=dados['Fase']
        )
        return True, ""
    except ValidationError as e:
        return False, str(e)

def main():
    st.title('Validador de Dados de Campanhas')
    
    # Upload do arquivo
    uploaded_file = st.file_uploader("Escolha o arquivo CSV", type=['csv'])
    
    if uploaded_file is not None:
        try:
            # Lê o CSV
            df = pd.read_csv(uploaded_file)
            st.success('Arquivo carregado com sucesso!')
            
            # Lista para armazenar erros
            erros = []
            
            # Barra de progresso
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Percorre as linhas do DataFrame
            total_rows = len(df)
            for index, row in df.iterrows():
                # Atualiza barra de progresso
                progress = (index + 1) / total_rows
                progress_bar.progress(progress)
                status_text.text(f'Processando linha {index + 1} de {total_rows}')
                
                # Validação usando Pydantic
                valido, mensagem_erro = validar_linha(row.to_dict())
                if not valido:
                    erros.append(f"Linha {index + 1}: {mensagem_erro}")
            
            # Remove a barra de progresso e o texto de status
            progress_bar.empty()
            status_text.empty()
            
            # Exibe resultados
            st.subheader('Resultado da Validação')
            
            if not erros:
                st.success('Nenhum erro encontrado! Todos os dados são válidos.')
            else:
                st.error('Erros encontrados:')
                for erro in erros:
                    st.write(erro)
                        
            # Exibe DataFrame
            st.subheader('Visualização dos Dados')
            st.dataframe(df)
            
        except Exception as e:
            st.error(f'Erro ao processar o arquivo: {str(e)}')
    
    # Adiciona informações de uso
    st.sidebar.title('Informações')
    st.sidebar.write("""
    ### Como usar:
    1. Faça upload de um arquivo CSV
    2. O sistema validará todos os campos conforme o modelo:
        - Organizador (número)
        - Ano_Mes (YYYY | Mês)
        - Dia_da_Semana
        - Tipo_Dia
        - Objetivo
        - Date (YYYY-MM-DD)
        - AdSet_name
        - Amount_spent (número)
        - Link_clicks (número)
        - Impressions (número)
        - Conversions (número)
        - Segmentação
        - Tipo_de_Anúncio
        - Fase
    3. Os resultados serão exibidos na tela
    """)

if __name__ == '__main__':
    main()
