import React, { useState } from 'react';
import UploadForm from './UploadForm';
import FinancialDataDisplay from './FinancialDataDisplay';

// Define the fetchFinancialData function
const fetchFinancialData = async (formData) => {
    try {
        const response = await fetch("http://127.0.0.1:8000/upload/", {
            method: "POST",
            body: formData,
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json(); // This returns the JSON response from your backend
    } catch (error) {
        console.error("Fetching financial data failed:", error);
        throw error; // Rethrow to handle it further up the call chain
    }
};

function FinancialDashboard() {
  const [activeMenu, setActiveMenu] = useState('');
  const [financialData, setFinancialData] = useState({});

  const handleFileUpload = async (file) => {
    const formData = new FormData();
    formData.append("file", file);

    try {
      const data = await fetchFinancialData(formData); // Call the function with formData
      setFinancialData(data); // Update state with the response data
    } catch (error) {
      console.error("Error in file upload:", error);
    }
  };

  const handleMenuChange = (event) => {
    setActiveMenu(event.target.value);
  };

  return (
    <div>
      <UploadForm onFileUpload={handleFileUpload} />
      <select onChange={handleMenuChange} value={activeMenu} className="menu-select">
        <option value="">Select Data Type</option>
        <option value="Income Statement [Abstract]">Income Statement</option>
        <option value="Balance Sheets">Balance Sheets</option>
        <option value="Financial Statements">Financial Statements</option>
      </select>
      {activeMenu && <FinancialDataDisplay data={financialData[activeMenu]} />}
    </div>
  );
}

export default FinancialDashboard;

