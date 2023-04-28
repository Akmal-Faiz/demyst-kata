import React from 'react';
import { useState } from 'react';
import { Container, Form, Button } from 'react-bootstrap';
import { getBalanceSheet, submitLoanApplication } from '../services/LoanApplicationService'
import BalanceSheetComponent from './BalanceSheetComponent'
import LoanApplicationOutcomeComponent from './LoanApplicationOutcomeComponent'

function LoanApplicationFormComponent(props) {
  const [validated, setValidated] = useState(false);
  const [businessName, setBusinessName] = useState('');
  const [establishedYear, setEstablishedYear] = useState('');
  const [accountingService, setAccountingService] = useState('');
  const [loanAmount, setLoanAmount] = useState('');
  const [loanApplicationOutCome, setLoanApplicationOutcome] = useState({})

  const [balanceSheet, setBalanceSheet] = useState([])

  const currentYear = new Date().getFullYear();

  const handleSubmit = async (event) => {
    event.preventDefault();
    const form = event.currentTarget;

    if (form.checkValidity() === false) {
      event.stopPropagation();
    } else {
      try {
        let response = await submitLoanApplication(
          businessName,
          establishedYear,
          accountingService,
          loanAmount
        );

        setLoanApplicationOutcome(response.data)
      } catch (error) {
        props.setError("Error: Something went wrong..")
      }
    }

    setValidated(true);
  };

  const clearForm = () => {
    return () => {
      setBusinessName('');
      setEstablishedYear('');
      setAccountingService('');
      setLoanAmount('');
      setValidated(false);
      setBalanceSheet([]);
      setLoanApplicationOutcome({});
    };
  }

  const handleGetBalanceSheet = async (event) => {
    event.preventDefault();
    const form = event.currentTarget;

    if (form.checkValidity() === false) {
      event.stopPropagation();
    } else {
      try {
        let response = await getBalanceSheet(
          businessName,
          establishedYear,
          accountingService
        )
        setBalanceSheet(response.data)
        setLoanApplicationOutcome({});
      } catch (error) {
        props.setError("Error: Something went wrong..")
      }
    }

    setValidated(true);
  };

  return (
    <Container className='d-grid gap-3'>
      <h1>Loan Application Form</h1>
      <Form className='d-grid gap-3' noValidate validated={validated} onSubmit={handleSubmit}>
        <Form.Group controlId="businessName">
          <Form.Label>Business Name</Form.Label>
          <Form.Control
            required
            type="text"
            value={businessName}
            onChange={(event) => setBusinessName(event.target.value)}
          />
        </Form.Group>

        <Form.Group controlId="establishedYear">
          <Form.Label>Established Year</Form.Label>
          <Form.Control
            required
            type="number"
            value={establishedYear}
            onChange={(event) => setEstablishedYear(event.target.value)}
            min={0}
            max={currentYear}
          />
          <Form.Control.Feedback type="invalid">Please enter a valid year</Form.Control.Feedback>
        </Form.Group>

        <Form.Group controlId="loanAmount">
          <Form.Label>Loan Amount</Form.Label>
          <Form.Control
            required
            type="number"
            value={loanAmount}
            min={0}
            onChange={(event) => setLoanAmount(event.target.value)}
          />
          <Form.Control.Feedback type="invalid">Please enter a valid loan amount</Form.Control.Feedback>
        </Form.Group>

        <Form.Group controlId="accountingService">
          <Form.Label>AccountingService</Form.Label>
          <Form.Select
            required
            value={accountingService}
            onChange={(event) => setAccountingService(event.target.value)}
          >
            <option disabled value=""></option>
            {props.accountingServices.map(ac => (
              <option value={ac}>{ac}</option>
            ))}
          </Form.Select>
        </Form.Group>

        {balanceSheet.length > 0 ? <BalanceSheetComponent data={balanceSheet} /> : <></>}

        <div className="d-flex justify-content-between">
          <Button variant="primary" type="submit" className="m-3">
            Submit Application
          </Button>

          <Button variant="primary" onClick={handleGetBalanceSheet} className="m-3">
            Get Balance Sheet
          </Button>

          <Button variant="secondary" onClick={clearForm()} className="m-3">
            Clear Form
          </Button>
        </div>
        <div className='d-flex justify-content-end'>
          <Button variant="secondary" onClick={() => props.togglePage()} className="m-3">Back</Button>
        </div>
      </Form>
      {Object.keys(loanApplicationOutCome).length > 0 ? <LoanApplicationOutcomeComponent data={loanApplicationOutCome}></LoanApplicationOutcomeComponent> : <></>}
    </Container>
  )


}

export default LoanApplicationFormComponent