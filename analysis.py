import pandas as pd

def analyze_financial_data(contents):
    # Leer archivo Excel desde bytes
    df = pd.read_excel(contents, sheet_name=None)
    hojas = [
        'Condensed Consolidated Statements of Income',
        'Condensed Consolidated Balance Sheets',
        'Condensed Consolidated Financial Statements'
    ]
    subtitulos_por_hoja = {}
    for hoja in hojas:
        if hoja in df:
            subtitulos_por_hoja[hoja] = list(df[hoja].iloc[:, 0].dropna())
    return subtitulos_por_hoja
