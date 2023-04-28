import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import LandingPageComponent from './components/LandingPageComponent';
import LoanApplicationFormComponent from './components/LoanApplicationFormComponent';
import { useState } from 'react';

function App() {
  const [showLandingPage, setShowLandingPage] = useState(true)
  const [showLoanApplication, setShowLoanApplication] = useState(false)
  const [accountingServices, setAccountingServices] = useState([])
  
  const togglePage = () => {
    setShowLandingPage(!showLandingPage)
    setShowLoanApplication(!showLoanApplication)
  }

  return (
    <>
      {showLandingPage ? <LandingPageComponent togglePage={togglePage} setAccountingServices={setAccountingServices} /> : <></>}
      {showLoanApplication ? <LoanApplicationFormComponent togglePage={togglePage} accountingServices={accountingServices}/> : <></>}
    </>
  )
}

export default App
