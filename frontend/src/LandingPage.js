// LandingPage.js
import React from 'react';
import { Link } from 'react-router-dom';

function LandingPage() {
  return (
    <div className="landing-container">
      <h1>Welcome to the Financial Analysis Platform</h1>
      <Link to="/dashboard" className="enter-link">Enter Dashboard</Link>
    </div>
  );
}

export default LandingPage;
