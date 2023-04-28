import axios from 'axios'

const BASE_URL = import.meta.env.VITE_BASE_URL + "/loan-application"

async function getAccountingServices(){
  return await axios.get(BASE_URL + "/accounting-services")
}

async function getBalanceSheet(
  businessName,
  establishedYear,
  accountingService
) {
  const payload = {
    "businessDetails": {
      "businessName": businessName,
      "yearEstablished": establishedYear
    },
    "accountingSoftware": accountingService
  }
  const response = await axios.post(BASE_URL + "/balance-sheet", payload)
  return response
}

async function submitLoanApplication(
  businessName,
  establishedYear,
  accountingService,
  loanAmount
  ) {
    const payload = {
      "businessDetails": {
        "businessName": businessName,
        "yearEstablished": establishedYear
      },
      "accountingSoftware": accountingService,
      "loanAmount": loanAmount
    }
  const response = await axios.post(BASE_URL + "/submit", payload)
  return response
}

export { getAccountingServices, getBalanceSheet, submitLoanApplication,  }