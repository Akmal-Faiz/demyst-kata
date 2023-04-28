import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import LandingPageComponent from './components/LandingPageComponent';
import LoanApplicationFormComponent from './components/LoanApplicationFormComponent';
import ErrorAlertComponent from './components/ErrorAlertComponent';
import { useState } from 'react';

function App() {
  const [showLandingPage, setShowLandingPage] = useState(true)
  const [showLoanApplication, setShowLoanApplication] = useState(false)
  const [accountingServices, setAccountingServices] = useState([])

  const [error, setError] = useState(null);


  const togglePage = () => {
    setShowLandingPage(!showLandingPage)
    setShowLoanApplication(!showLoanApplication)
  }

  return (
    <>
      {showLandingPage ? <LandingPageComponent togglePage={togglePage} setAccountingServices={setAccountingServices} setError={setError} /> : <></>}
      {showLoanApplication ? <LoanApplicationFormComponent togglePage={togglePage} accountingServices={accountingServices} setError={setError} /> : <></>}

      {error && <ErrorAlertComponent message={error}  setError={setError}/>}
    </>
  )
}

export default App
