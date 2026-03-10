import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_sql(user_prompt):

    schema = """
    Table: campaigns

    Columns:
    Campaign_ID
    Campaign_Type
    Target_Audience
    Duration
    Channel_Used
    Impressions
    Clicks
    Leads
    Conversions
    Revenue
    Acquisition_Cost
    ROI
    Language
    Engagement_Score
    Customer_Segment
    Date
    """

    prompt = f"""
Convert the following request into a valid SQLite SQL query.

Schema:
{schema}

Rules:
- Return ONLY SQL
- Use aliases for aggregated columns
Example: SUM(Revenue) AS Total_Revenue

User request:
{user_prompt}
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "HTTP-Referer": "http://localhost:5173",
            "X-Title": "Conversational BI Dashboard"
        },
        json={
            "model": "deepseek/deepseek-chat",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )

    result = response.json()

    print("OPENROUTER RESPONSE:", result)

    if "choices" not in result:
        raise Exception(f"OpenRouter API error: {result}")

    sql = result["choices"][0]["message"]["content"].strip()

    sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql