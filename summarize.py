# summarizer.py

import os
from dotenv import load_dotenv
import openai

# Step 1: Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Step 2: Define the function to summarize CVE content
def summarize_cves(cve_text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", # You can change to gpt-4 if available   
            messages=[
                {"role": "system", "content": "You are a cybersecurity analyst who summarizes CVEs."},
                {"role": "user", "content": f"Summarize the following CVE:\n\n{cve_text}"}
            ],
            temperature=0.5,
            max_tokens=300
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

# Step 3: Sample CVE text for testing
sample_cves = """
CVE-2023-27524: Apache Superset before 2.1.1 allowed unauthorized access due to insecure default SECRET_KEY configuration.
Attackers could bypass authentication and gain admin access on exposed servers with default keys.
"""

# Step 4: Print the summary
summary = summarize_cves(sample_cves)
print("\n📌 GPT Summary:\n", summary)