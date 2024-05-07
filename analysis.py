import pandas as pd
from io import BytesIO

def analyze_financial_data(contents):
    excel_data = BytesIO(contents)
    df = pd.read_excel(excel_data, sheet_name=None)

    target_sheets = {
        'Condensed Consolidated Statemen': 'Condensed Consolidated Statements of Income',
        'Condensed Consolidated Balance ': 'Condensed Consolidated Balance Sheets',
        'Condensed Consolidated Financia': 'Condensed Consolidated Financial Statements'
    }

    subtitulos_por_hoja = {}

    for sheet_name, sheet_data in df.items():
        for key_substring, target_name in target_sheets.items():
            if key_substring in sheet_name:
                subtitles_list = sheet_data.iloc[:, 0].dropna().tolist()
                # Clean subtitles list from NaNs and infinite values
                clean_subtitles = [subtitle if not pd.isna(subtitle) else 'N/A' for subtitle in subtitles_list]
                subtitulos_por_hoja[target_name] = clean_subtitles

    return subtitulos_por_hoja
