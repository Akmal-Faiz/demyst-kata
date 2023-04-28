import React from 'react'
import { Container, Button } from 'react-bootstrap';
import { getAccountingServices } from '../services/LoanApplicationService';

function LandingPageComponent(props) {
  const handleClick = async ()=>{
    try{
      let response = await getAccountingServices()
      props.setAccountingServices(response.data)
      props.togglePage()
    } catch (error){
      props.setError("Error: Something went wrong..")
    }   
  }

  return (
    <Container className='d-grid'>
      <h1>Demyst Loan Application</h1>
      <div className='d-flex justify-content-around mt-3'>
        <Button onClick={handleClick}>Get Started</Button>
      </div>
    </Container>
  )
}

export default LandingPageComponent