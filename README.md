## Virtual Assistant

A hybrid AI-powered virtual assistant built using Python, FastAPI, LangChain, FAISS, and Neo4j.
The system combines semantic vector search with graph-based knowledge retrieval to handle complex multi-hop queries efficiently.

## Features
Hybrid Retrieval Pipeline
Integrated FAISS for semantic vector search.
Used Neo4j graph database for relationship-aware query execution.
Combined structured and unstructured data retrieval for improved response accuracy.
Agent-Based Query Orchestration
Built using LangChain agents.
Dynamically routes queries between:
Semantic similarity search
Graph traversal operations
Supports intelligent multi-step reasoning workflows.
Scalable Backend Architecture
Developed backend using FastAPI.


## Followed a modular architecture:


services/
models/
tools/
Improved maintainability, scalability, and code organization.
Optimized Retrieval Efficiency
Combined vector embeddings with graph relationships.
Reduced query latency while improving contextual relevance.


## Tech Stack
Technology	                Purpose
Python                    	Core backend development
FastAPI	                    API framework
LangChain	                  Agent orchestration and LLM workflows
FAISS	Vector                similarity search
Neo4j	Graph                 database and relationship queries
