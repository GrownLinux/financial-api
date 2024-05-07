# analysis.py

import spacy
import pandas as pd
from io import BytesIO
from spacy.pipeline import EntityRuler

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Add custom entity patterns to the NER pipeline
def add_custom_entities(nlp):
    ruler = EntityRuler(nlp)
    patterns = [
        {"label": "Income", "pattern": [{"LOWER": "income"}, {"LOWER": "statement"}]},
        {"label": "Balance", "pattern": [{"LOWER": "balance"}, {"LOWER": "sheet"}]},
        {"label": "Financial", "pattern": [{"LOWER": "financial"}, {"LOWER": "statement"}]},
    ]
    ruler.add_patterns(patterns)
    nlp.add_pipe(ruler, before="ner")

add_custom_entities(nlp)

# Function to apply NER and extract named entities from text
def extract_named_entities(text):
    entities = {
        "Income Statement [Abstract]": [],
        "Balance Sheets": [],
        "Financial Statements": []
    }
    doc = nlp(text)
    for ent in doc.ents:
        # Add entities if not already in the list to avoid duplicates
        if ent.label_ in ["Income", "MONEY", "ORG"] or any(keyword in ent.text.lower() for keyword in ["income", "revenue", "cost", "expense"]):
            if (ent.text, ent.label_) not in entities["Income Statement [Abstract]"]:
                entities["Income Statement [Abstract]"].append((ent.text, ent.label_))
        elif ent.label_ in ["Balance", "MONEY", "ORG"] or any(keyword in ent.text.lower() for keyword in ["balance", "equity", "asset", "liability"]):
            if (ent.text, ent.label_) not in entities["Balance Sheets"]:
                entities["Balance Sheets"].append((ent.text, ent.label_))
        elif ent.label_ in ["Financial", "ORG", "DATE"] or any(keyword in ent.text.lower() for keyword in ["financial", "statement", "cash"]):
            if (ent.text, ent.label_) not in entities["Financial Statements"]:
                entities["Financial Statements"].append((ent.text, ent.label_))
    return entities

# Function to analyze financial data from Excel file
def analyze_financial_data(contents):
    excel_data = BytesIO(contents)
    df = pd.read_excel(excel_data, sheet_name=None)

    target_sheets = {
        'Condensed Consolidated Statemen': 'Income Statement [Abstract]',
        'Condensed Consolidated Balance ': 'Balance Sheets',
        'Condensed Consolidated Financia': 'Financial Statements'
    }

    subtitulos_por_hoja = {}

    for sheet_name, sheet_data in df.items():
        for key_substring, target_name in target_sheets.items():
            if key_substring in sheet_name:
                subtitles_list = sheet_data.iloc[:, 0].dropna().tolist()
                # Remove duplicates from subtitles
                clean_subtitles = list(set(subtitle if not pd.isna(subtitle) else 'N/A' for subtitle in subtitles_list))
                
                # Apply NER extraction
                categorized_entities = []
                for subtitle in clean_subtitles:
                    entities = extract_named_entities(subtitle)
                    categorized_entities.append(entities)

                subtitulos_por_hoja[target_name] = {
                    "subtitles": clean_subtitles,
                    "categorized_entities": categorized_entities
                }

    return subtitulos_por_hoja
