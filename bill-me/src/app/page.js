"use client";
import React, { useState } from "react";
import Image from "next/image";
import BillUpload from "./components/BillUpload";
import BillDetails from "./components/BillDetails";

export default function HomePage() {
  const [billDetails, setBillDetails] = useState(null);

  const handleBillRecognition = (data) => {
    setBillDetails(data);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      {/* Add your logo */}
      <Image
        src="/logo.png" // Referencing the image placed in the public folder
        alt="Bill Me Logo"
        width={300} // Adjust width as per your design needs
        height={150} // Adjust height as per your design needs
      />

      <h1>Bill Recognition App</h1>

      <BillUpload onRecognition={handleBillRecognition} />

      {billDetails && <BillDetails details={billDetails} />}
    </div>
  );
}
