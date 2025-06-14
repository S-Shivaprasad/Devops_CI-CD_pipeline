from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import json
import re

# Load environment variables
load_dotenv()
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

if not HF_API_TOKEN:
    raise EnvironmentError("Please set the HF_API_TOKEN environment variable.")

# Initialize Hugging Face endpoint with Mistral
llm = HuggingFaceEndpoint(
    endpoint_url="https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3",
    huggingfacehub_api_token=HF_API_TOKEN,
    task="text-generation",
    temperature=0.5,
    max_new_tokens=1024,
)

# Multitool/multilang prompt template
template = r"""
You are a CI/CD DevOps assistant.

Your task is to analyze a CI/CD pipeline configuration (in YAML or JSON), detect inefficiencies or issues, and suggest improvements. Return a structured response in valid JSON format using the schema below:

{{
  "tool": "GitHub Actions" or "GitLab CI" or "Jenkins" or "CircleCI" or others (detected from input),
  "language": "Node.js" or "Python" or "Java" or other (detected from the pipeline),
  "issues": [
    {{
      "job": "name of the job or stage",
      "issue": "brief explanation of the problem",
      "rule_based_suggestion": "basic DevOps fix",
      "llm_suggestion": "detailed suggestion to optimize performance, maintainability, or clarity"
    }}
  ],
  "suggestions": [
    "Short bullet list of improvements"
  ],
  "optimized_pipeline": "Optimized CI/CD pipeline as a valid YAML string with separate jobs for parallel execution. If the input has a single long 'build' job, break it into smaller jobs (e.g., build-part-1, build-part-2, etc.) to enable parallelism. Each job should contain a logically grouped subset of steps. Keep the optimized YAML clean and executable."
}}

⚠️ Output Rules:

- Respond with only a valid JSON object.
- Do NOT include markdown, comments, or extra text.
- optimized_pipeline must be a valid YAML string inside the JSON.
- Use the appropriate syntax for the detected CI/CD tool.
- Preserve the logic of the original pipeline but optimize for clarity, speed, and modularity.

Input pipeline:
{issue}
"""




# Create LangChain chain
prompt = PromptTemplate(input_variables=["issue"], template=template)
chain = prompt | llm

# Main callable
def ask_llm(issue: str) -> dict:
    try:
        response = chain.invoke({"issue": issue})
        print("\n🔍 Raw LLM Response:", response)

        # Extract generated text
        if isinstance(response, list) and isinstance(response[0], dict):
            text = response[0].get("generated_text", "")
        elif isinstance(response, dict):
            text = response.get("generated_text", "")
        elif isinstance(response, str):
            text = response
        else:
            text = str(response)

        # Remove markdown formatting
        cleaned = re.sub(r"```(json|yaml)?", "", text, flags=re.IGNORECASE).strip()
        print("\n🧹 Cleaned LLM Output:\n", cleaned)

        # Try to extract JSON block
        json_match = re.search(r"\{.*\}", cleaned, re.DOTALL)
        if not json_match:
            return {"error": "No JSON object found in LLM response.", "raw": cleaned}

        json_str = json_match.group(0)
        parsed = json.loads(json_str)
        return parsed

    except json.JSONDecodeError as e:
        return {"error": f"JSON parse error: {str(e)}", "raw": text}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}
