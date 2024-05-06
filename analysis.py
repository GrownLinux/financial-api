import pandas as pd
from io import BytesIO

def analyze_financial_data(contents):
    # Load the Excel data from bytes
    excel_data = BytesIO(contents)
    df = pd.read_excel(excel_data, sheet_name=None)

    # Specific sheets to look for, with a substring for fuzzy matching
    target_sheets = {
        'Condensed Consolidated Statemen': 'Condensed Consolidated Statements of Income',
        'Condensed Consolidated Balance ': 'Condensed Consolidated Balance Sheets',
        'Condensed Consolidated Financia': 'Condensed Consolidated Financial Statements'
    }

    # Initialize the result dictionary
    subtitulos_por_hoja = {}

    # Iterate through the sheets in the Excel file
    for sheet_name, sheet_data in df.items():
        for key_substring, target_name in target_sheets.items():
            if key_substring in sheet_name:
                subtitulos_por_hoja[target_name] = list(sheet_data.iloc[:, 0].dropna())

    return subtitulos_por_hoja
