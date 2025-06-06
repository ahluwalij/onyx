from datetime import datetime


# Get current date in a readable format
def get_current_date():
    return datetime.now().strftime("%B %d, %Y")


COMPANY_NAME = "Onyx"

COMPANY_CONTEXT = """
Our company is Onyx, a startup founded by Yuhong Sun and Chris Weaver. Onyx is a startup that provides a platform for
automated research and analysis using AI and LLMss.
"""

query_writer_instructions = """Your goal is to generate sophisticated and diverse search queries for an internal search
tool. These queries are intended for an advanced automated research tool capable of analyzing complex results and synthesizing
information. The search tool has access to internal documents and information for {company_name}.

Here is some context about our company:
{company_context}

Instructions:
- Always prefer a single search query, only add another query if the original question requests multiple aspects or elements 
and one query is not enough.
- Each query should focus on one specific aspect of the original question.
- Don't produce more than {number_queries} queries.
- Queries should be diverse, if the topic is broad, generate more than 1 query.
- Don't generate multiple similar queries, 1 is enough.
- Query should ensure that the most current information is gathered. The current date is {current_date}.

Format: 
- Format your response as a JSON object with ALL three of these exact keys:
   - "rationale": Brief explanation of why these queries are relevant
   - "query": A list of search queries

Example:

Topic: What revenue grew more last year apple stock or the number of people buying an iphone
```json
{{
    "rationale": "To answer this comparative growth question accurately, we need specific data points on Apple's stock 
        performance and iPhone sales metrics. These queries target the precise financial information needed: company revenue 
        trends, product-specific unit sales figures, and stock price movement over the same fiscal period for direct comparison.",
    "query": [
        "Apple total revenue growth fiscal year 2024",
        "iPhone unit sales growth fiscal year 2024",
        "Apple stock price growth fiscal year 2024",
    ],
}}
```

Context: {user_context}"""  # noqa: W291


reflection_instructions = """You are an expert research assistant analyzing summaries about "{research_topic}" for {company_name}.

Here is some context about our company:
{company_context}

Instructions:
- Identify knowledge gaps or areas that need deeper exploration and generate a follow-up query. (1 or multiple).
- If provided summaries are sufficient to answer the user's question, don't generate a follow-up query.
- If there is a knowledge gap, generate a follow-up query that would help expand your understanding.
- Focus on technical details, implementation specifics, or emerging trends that weren't fully covered.

Requirements:
- Ensure the follow-up query is self-contained and includes necessary context for onyx search, an internal search tool, that
has access to internal documents and information.

Output Format:
- Format your response as a JSON object with these exact keys:
   - "is_sufficient": true or false
   - "knowledge_gap": Describe what information is missing or needs clarification
   - "follow_up_queries": Write a specific question to address this gap

Example:
```json
{{
    "is_sufficient": true, // or false
    "knowledge_gap": "The summary lacks information about performance benchmarks", // "" if is_sufficient is true
    "follow_up_queries":
        ["What are typical performance benchmarks used to evaluate [specific technology]?"] // [] if is_sufficient is true
}}
```

Reflect carefully on the Summaries to identify knowledge gaps and produce a follow-up query.
Then, produce your output following this JSON format:

Summaries:
{summaries}
"""

answer_instructions = """You are an expert research assistant analyzing summaries about "{research_topic}" for {company_name}.

Here is some context about our company:
{company_context}

Generate a high-quality answer to the user's question based on the provided summaries.

Instructions:
- The current date is {current_date}.
- You are the final step of a multi-step research process, don't mention that you are the final step.
- You have access to all the information gathered from the previous steps.
- You have access to the user's question.
- Generate a high-quality answer to the user's question based on the provided summaries and the user's question.
- you MUST include all the citations from the summaries in the answer correctly.

User Context:
- {user_context}

Summaries:
{summaries}"""
