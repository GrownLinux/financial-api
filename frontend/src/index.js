import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import ErrorBoundary from './ErrorBoundary'; // Assuming you have an ErrorBoundary component

const root = ReactDOM.createRoot(document.getElementById('root'));

// Using React.lazy for code splitting
const LazyApp = React.lazy(() => import('./App'));

root.render(
  <React.Suspense fallback={<div>Loading...</div>}>  // Providing a fallback while components are lazily loaded
    <ErrorBoundary>
      <LazyApp />
    </ErrorBoundary>
  </React.Suspense>
);

// Enhanced usage of reportWebVitals
if (process.env.NODE_ENV === 'production') {
  reportWebVitals(console.log);  // or use a more sophisticated handler
}
