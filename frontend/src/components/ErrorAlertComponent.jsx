import { useState, useEffect } from 'react';
import { Alert } from 'react-bootstrap';



function ErrorAlertComponent({ message, setError }) {

  useEffect(() => {
    const timer = setTimeout(() => {
      setError(null)
    }, 5000);
    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="position-fixed bottom-0 start-50 translate-middle-x">
      {<Alert variant="danger" onClose={() => setError(null)} dismissible>{message}</Alert>}
    </div>
  );
};

export default ErrorAlertComponent