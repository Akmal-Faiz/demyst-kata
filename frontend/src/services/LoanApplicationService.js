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
    "business_details": {
      "business_name": businessName,
      "year_established": establishedYear
    },
    "accounting_software": accountingService
  }
  const response = await axios.post(BASE_URL + "/balance-sheet", payload)
  return response
}

async function submitLoanApplication(payload) {
  const response = await axios.post(BASE_URL + "/submit", payload)
}

export { getAccountingServices, getBalanceSheet, submitLoanApplication,  }