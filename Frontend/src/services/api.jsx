import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || "http://localhost:8000",
});

/**
 * Analyze a CI/CD pipeline from a file OR a URL
 * @param {Object} input - Either { file: File } or { url: string }
 */
export const analyzePipeline = (input) => {
  const formData = new FormData();

  if (input.file) {
    formData.append("file", input.file);
  } else if (input.url) {
    formData.append("url", input.url);
  } else {
    throw new Error("Either file or url must be provided.");
  }

  return api.post("/upload/", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
};
