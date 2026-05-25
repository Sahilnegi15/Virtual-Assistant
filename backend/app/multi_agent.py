from langchain.llms import LlamaCpp
from rag_store import add_long_term_memory

# Load same local model
llm = LlamaCpp(
    model_path="./models/gpt4all-j-v1.3-groovy.bin",
    n_ctx=512,
    n_threads=4
)

# -----------------------------
# 1. Research Agent
# -----------------------------
from agents import web_search_with_rag

def research_agent(query: str) -> str:
    print("[Research Agent] Running...")
    data = web_search_with_rag(query)
    return data


# -----------------------------
# 2. Summarizer Agent
# -----------------------------
def summarizer_agent(text: str) -> str:
    print("[Summarizer Agent] Running...")
    
    prompt = f"""
    Summarize the following information clearly and concisely:

    {text}
    """
    
    return llm(prompt)


# -----------------------------
# 3. Decision Agent
# -----------------------------
def decision_agent(summary: str) -> str:
    print("[Decision Agent] Running...")
    
    prompt = f"""
    Based on the following summary, generate a clear and structured final answer:

    {summary}

    Provide:
    - Key Insights
    - Important Trends
    - Final Conclusion
    """
    
    return llm(prompt)


# -----------------------------
# Orchestrator (MAIN SYSTEM)
# -----------------------------
def multi_agent_pipeline(query: str) -> str:
    print("\n=== Multi-Agent Pipeline Started ===")

    # Step 1: Research
    research_data = research_agent(query)

    # Step 2: Summarize
    summary = summarizer_agent(research_data)

    # Step 3: Decision
    final_output = decision_agent(summary)

    print("=== Pipeline Completed ===\n")
    return final_output



def multi_agent_pipeline(query: str) -> str:
    print("\n=== Multi-Agent Pipeline Started ===")

    context = get_context()

    research_data = research_agent(query + "\nContext:\n" + context)
    summary = summarizer_agent(research_data)
    final_output = decision_agent(summary)

    # Save short-term
    update_memory(query, final_output)

    # Save long-term knowledge
    add_long_term_memory(final_output)

    print("=== Pipeline Completed ===\n")
    return final_output