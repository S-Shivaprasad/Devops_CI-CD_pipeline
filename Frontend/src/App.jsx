import React from "react";
import PipelineAnalyzer from "./components/PipelineAnalyzer";
import logo from "/devops.png"

function App() {
  return (
    <div className="min-h-screen bg-gray-900 text-white p-10">
      {/* Header Section with Logo + Title */}
      <div className="flex items-center justify-center mb-8">
        <img
          src={logo}
          alt="DevOps Logo"
          className="h-16 w-16 mr-4 rounded-full shadow-lg"
        />
        <h1 className="text-4xl font-extrabold text-center">
          DevOps Pipeline Analyzer
        </h1>
      </div>

      {/* Main Analyzer Component */}
      <PipelineAnalyzer />
    </div>
  );
}

export default App;
