import React from 'react';
import { useState } from 'react';
import { Container, Form, Button } from 'react-bootstrap';
import { getBalanceSheet, submitLoanApplication } from '../services/LoanApplicationService'

function LoanApplicationForm() {
  const [validated, setValidated] = useState(false);
  const [businessName, setBusinessName] = useState('');
  const [establishedYear, setEstablishedYear] = useState('');
  const [accountingService, setAccountingService] = useState('');
  const [loanAmount, setLoanAmount] = useState('');

  const currentYear = new Date().getFullYear();

  const handleSubmit = (event) => {
    event.preventDefault();
    const form = event.currentTarget;

    if (form.checkValidity() === false) {
      event.stopPropagation();
    } else {
      const loanApplicationData = {
        businessName,
        establishedYear,
        accountingService,
        loanAmount
      };
      submitLoanApplication(loanApplicationData);
    }

    setValidated(true);
  };

  const handleGetBalanceSheet = async (event) => {
    event.preventDefault();
    const form = event.currentTarget;

    if (form.checkValidity() === false) {
      event.stopPropagation();
    } else {
      const response = await getBalanceSheet(
        businessName,
        establishedYear,
        accountingService
        )
        console.log(response)
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
            <option value="Xero">Xero</option>
            <option value="MYOB">MYOB</option>
          </Form.Select>
        </Form.Group>

        <div className="d-flex justify-content-around">
          <Button variant="primary" type="submit">
            Submit Application
          </Button>
          <Button variant="primary" onClick={handleGetBalanceSheet}>
            Get Balance Sheet
          </Button>
          <Button variant="secondary" onClick={() => {
            setBusinessName('');
            setEstablishedYear('');
            setAccountingService('');
            setLoanAmount('');
            setValidated(false);
          }}>
            Clear Form
          </Button>
        </div>

      </Form>
    </Container>
  )
}

export default LoanApplicationForm