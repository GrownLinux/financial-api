from fastapi import FastAPI, UploadFile, File
from analysis import analyze_financial_data
from visualizations import generate_visualizations

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    analysis_results = analyze_financial_data(contents)
    visualizations = generate_visualizations(analysis_results)
    return {
        "analysis_results": analysis_results,
        "visualizations": visualizations,
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
