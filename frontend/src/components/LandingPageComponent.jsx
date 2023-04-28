import React from 'react'
import { Container, Button } from 'react-bootstrap';
import { getAccountingServices } from '../services/LoanApplicationService';

function LandingPageComponent(props) {
  const handleClick = async ()=>{
    let response = await getAccountingServices()
    if (response.status===200){
      props.setAccountingServices(response.data)
      props.togglePage()
    }else{
      console.log(response.detail)
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