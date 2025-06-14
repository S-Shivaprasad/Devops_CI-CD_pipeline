import React, { useState } from "react";
import { analyzePipeline } from "../services/api";
import { FaFileAlt } from "react-icons/fa";

const PipelineAnalyzer = () => {
  const [file, setFile] = useState(null);
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setUrl("");
    setResult(null);
    setError("");
  };

  const handleUrlChange = (e) => {
    setUrl(e.target.value);
    setFile(null);
    setResult(null);
    setError("");
  };

  const handleAnalyze = async () => {
    if (!file && !url) {
      setError("Please upload a file or enter a URL.");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const response = await analyzePipeline({ file, url });
      console.log("📦 LLM API response:", response.data);
      setResult(response.data);
    } catch (err) {
      console.error("❌ API Error:", err);
      setError("❌ Failed to analyze pipeline. Please check your input.");
    } finally {
      setLoading(false);
    }
  };

  const renderSection = (title, icon, data) => {
    const isOptimizedPipeline = title.includes("Optimized Pipeline");
    return (
      <div className="bg-white rounded-2xl shadow-xl p-5 border border-gray-200">
        <h3 className="text-lg font-semibold mb-3 flex items-center gap-2 text-gray-800">
          <span>{icon}</span> {title}
        </h3>
        <pre className="bg-gray-50 text-gray-800 p-4 rounded-xl text-sm overflow-x-auto whitespace-pre-wrap break-words">
          {data
            ? isOptimizedPipeline && typeof data === "string"
              ? data.replace(/\n/g, "\n").replace(/\"/g, '"')
              : JSON.stringify(data, null, 2)
            : "No data available."}
        </pre>
      </div>
    );
  };

  return (
    <div className="w-[95%] sm:w-[90%] md:w-[80%] lg:w-[75%] xl:w-[70%] mx-auto p-6 sm:p-8 bg-gradient-to-br from-white to-blue-50 shadow-2xl rounded-3xl border border-gray-200">
      <h2 className="text-3xl font-bold mb-6 text-center text-gray-900">
        🚀 CI/CD Optimizer
      </h2>

      {/* File Upload */}
      <div className="mb-5">
        <input
          type="file"
          accept=".yml,.yaml"
          onChange={handleFileChange}
          className="hidden"
          id="fileUpload"
        />
        <label
          htmlFor="fileUpload"
          className="cursor-pointer bg-white hover:bg-gray-100 text-blue-600 border border-dashed border-blue-400 w-full py-3 px-4 rounded-xl flex items-center justify-center gap-2 transition shadow-inner"
        >
          {file ? (
            <span className="flex items-center gap-2 font-medium">
              <FaFileAlt />
              {file.name}
            </span>
          ) : (
            "📁 Upload a YAML file"
          )}
        </label>
      </div>

      {/* URL Input */}
      <div className="mb-5">
        <textarea
          placeholder="🔗 Paste raw .yaml URL (e.g., GitHub)"
          value={url}
          onChange={handleUrlChange}
          rows={3}
          className="w-full border border-blue-300 px-4 py-3 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-400 text-gray-800 shadow-inner resize-none"
        />
      </div>

      {/* Analyze Button */}
      <button
        onClick={handleAnalyze}
        disabled={loading}
        className="w-full py-3 px-6 rounded-xl bg-blue-600 text-white font-semibold hover:bg-blue-700 transition disabled:opacity-50 shadow-md"
      >
        {loading ? "Analyzing..." : "Analyze Pipeline"}
      </button>

      {/* Error Message */}
      {error && <p className="text-red-500 mt-4 text-center">{error}</p>}

      {/* Output Sections */}
      {result?.llm_response && (
        <div className="mt-8 space-y-8">
          {renderSection("🐞 Issues", "🐞", result.llm_response.issues)}
          {renderSection("💡 Suggestions", "💡", result.llm_response.suggestions)}
          {renderSection("🛠 Optimized Pipeline", "🛠", result.llm_response.optimized_pipeline)}
        </div>
      )}
    </div>
  );
};

export default PipelineAnalyzer;
