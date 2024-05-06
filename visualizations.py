import matplotlib.pyplot as plt
from io import BytesIO

def generate_visualizations(analysis_results):
    figures = {}
    for sheet, subtitles in analysis_results.items():
        plt.figure(figsize=(10, 5))
        plt.bar(range(len(subtitles)), [1]*len(subtitles))
        plt.xticks(range(len(subtitles)), subtitles, rotation=45, ha="right")
        plt.title(sheet)
        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        figures[sheet] = buffer.read()
    return figures
