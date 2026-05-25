from langchain.llms import LlamaCpp
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from rag_store import add_to_index, search_index
from tools.web_search import web_search
from langchain.agents import Tool

# Load local model
llm = LlamaCpp(model_path="./models/gpt4all-j-v1.3-groovy.bin", n_threads=4, n_ctx=512)

def web_search_with_rag(query: str) -> str:
    """
    Check RAG first, else use web search
    """
    results = search_index(query, k=3)
    if results:
        # If we have stored results, return them
        combined = "\n".join([r["text"] for r in results])
        return f"From Knowledge Base:\n{combined}"
    else:
        # If not found, fetch from web, store it, and return
        summary = web_search(query)
        add_to_index(summary, source="web")
        return f"From Web Search:\n{summary}"



# Example tool: simple calculator
def calculator_tool(query: str) -> str:
    try:
        return str(eval(query))
    except:
        return "Could not calculate"

tools = [
    Tool(
        name="Calculator",
        func=calculator_tool,
        description="Use this tool to perform simple math operations"
    ),
   Tool(
        name="Web Search + RAG",
        func=web_search_with_rag,
        description="Search the web or Knowledge Base and summarize results"
    )
]

# Initialize agent
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

# Function to handle user query
def handle_query(query: str) -> str:
    response = agent.run(query)
    return response