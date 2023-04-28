import React from 'react'
import { Table } from 'react-bootstrap'

function LoanApplicationOutcomeComponent(props) {
  return (
    <Table className='table-borderless'>
      <tbody>
        <tr>
          <td>Loan Approval Rate:</td>
          <td><b>{props.data.loanApprovalRate}%</b></td>
        </tr>
        <tr>
          <td>Approved Amount:</td>
          <td><b> ${props.data.loanAmountApproved.toLocaleString("en-US")}</b></td>
        </tr>
      </tbody>
    </Table>
  )
}

export default LoanApplicationOutcomeComponent