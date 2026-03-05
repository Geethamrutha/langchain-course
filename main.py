from dotenv import load_dotenv
import os
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv(".venv/.env")

@tool
def search(query: str) -> str:
    """Tool that searchesthe web for information
    
    Args:
        query: The query to search the web for

    Returns:
        The information found on the web
    """
   

    return "I found this information: " + query

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print(os.getenv("OPENAI_API_KEY"))
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="I want to search for 3 job postings for ai engineer in liknked in in bay area")]})
    print(result)
if __name__ == "__main__":
    main()