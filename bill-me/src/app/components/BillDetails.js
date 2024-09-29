import React from "react";

const BillDetails = ({ details }) => (
  <div>
    <h2>Bill Details</h2>
    <p>
      <strong>Amount:</strong> {details.amount}
    </p>
    <p>
      <strong>Due Date:</strong> {details.dueDate}
    </p>
    <p>
      <strong>Biller:</strong> {details.biller}
    </p>
  </div>
);

export default BillDetails;
