# visualizations.py

import base64
import matplotlib.pyplot as plt
from io import BytesIO
import random

def generate_visualizations(analysis_results):
    """
    Generate visualizations for the given analysis results.

    Parameters:
    - analysis_results (dict): A dictionary containing analysis results, where the keys are sheet names and the values are lists of subtitles.

    Returns:
    - figures (dict): A dictionary containing the generated visualizations encoded as base64 strings, where the keys are sheet names and the values are the encoded images.
    """
    figures = {}
    for sheet, data in analysis_results.items():
        subtitles = data['subtitles']
        entity_count = len(subtitles)
        
        # Bar chart if subtitles count is more than 1
        if entity_count > 1:
            plt.figure(figsize=(12, 6))
            plt.bar(range(entity_count), [random.randint(1, 10) for _ in range(entity_count)], color='skyblue')
            plt.xticks(range(entity_count), subtitles, rotation=45, ha="right")
            plt.title(f"{sheet} - Entity Distribution")
            plt.xlabel("Entities")
            plt.ylabel("Counts")
            plt.tight_layout()
        
        # Pie chart if subtitles count is 1
        elif entity_count == 1:
            plt.figure(figsize=(6, 6))
            plt.pie([100], labels=subtitles, autopct='%1.1f%%', startangle=90, colors=['skyblue'])
            plt.title(f"{sheet} - Entity Distribution")
            plt.axis('equal')

        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        figures[sheet] = base64.b64encode(buffer.read()).decode('utf-8')
        plt.close()
        
    return figures
