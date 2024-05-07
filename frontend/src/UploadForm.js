// src/UploadForm.js
import React, { useState } from "react";
import "./App.css";

const UploadForm = () => {
    const [file, setFile] = useState(null);
    const [response, setResponse] = useState(null);

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData();
        formData.append("file", file);

        const res = await fetch("http://127.0.0.1:8000/upload/", {
            method: "POST",
            body: formData,
        });

        const data = await res.json();
        setResponse(data);
    };

    return (
        <div className="upload-container">
            <h2 className="upload-title">Upload Financial Data</h2>
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleFileChange} className="upload-input" />
                <button type="submit" className="upload-button">Upload</button>
            </form>
            {response && (
                <div className="response-container">
                    {response.visualizations && Object.keys(response.visualizations).map((key) => (
                        <div key={key}>
                            <h3>{key}</h3>
                            <img src={`data:image/png;base64,${response.visualizations[key]}`} alt={key} />
                        </div>
                    ))}
                    <pre>{JSON.stringify(response.analysis_results, null, 2)}</pre>
                </div>
            )}
        </div>
    );
};

export default UploadForm;
