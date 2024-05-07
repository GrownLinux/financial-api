// FinancialDataDisplay.js
import React from 'react';

function FinancialDataDisplay({ type }) {
  return (
    <div>
      <h2>{type}</h2>
      {/* Display content based on the type */}
      <div>Content for {type} will be displayed here...</div>
    </div>
  );
}

export default FinancialDataDisplay;
