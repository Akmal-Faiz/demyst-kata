import { Table } from "react-bootstrap"

function BalanceSheetComponent(props) {
  function generateRow() {
    return (item, index) => (
      <tr key={index}>
        <td>{item.year}-{item.month}</td>
        <td>{item.profitOrLoss.toLocaleString("en-US")}</td>
        <td>{item.assetsValue.toLocaleString("en-US")}</td>
      </tr>
    )
  }

  return (
    <>
      <h3 className="mt-5">Balance Sheet</h3>
      <div className="overflow-scroll mh-100" style={{ height: "200px" }}>

        <Table className="table-striped">
          <tbody>
            <tr key="labels" style={{ position: "sticky", top: 0, background: "white" }}>
              <td><b>Month</b></td>
              <td><b>Profit</b></td>
              <td><b>Assets</b></td>
            </tr>
            {props.data.map(generateRow())}
          </tbody>

        </Table>

      </div>
    </>

  )


}

export default BalanceSheetComponent