# Conversational Agent MLOps

This project contains the structure for a Conversational Agent MLOps pipeline, including agents, RAG, evaluation, and MLOps steps.

# 🤖 Conversational Agent MLOps (Agentic RAG)

[![ZenML](https://img.shields.io/badge/Orchestration-ZenML-blueviolet)](https://zenml.io/)
[![LangGraph](https://img.shields.io/badge/Agent-LangGraph-blue)](https://python.langchain.com/docs/langgraph)
[![MLOps](https://img.shields.io/badge/Category-MLOps-green)](#)

A production-grade Agentic RAG pipeline designed for reliability and scalability. This project uses **ZenML** to orchestrate the lifecycle of an AI agent capable of routing between real-time API tools and a vector-based knowledge base.

## 🏗️ Technical Architecture


The system is split into two primary ZenML pipelines:
1. **Ingestion Pipeline:** Automates PDF loading, Recursive Character Splitting, and Qdrant upserts with built-in caching.
2. **Inference Pipeline:** Orchestrates a LangGraph-powered state machine that intelligently decides whether to query the **Weather API** or the **Vector DB**.

## 🌟 Key Features
- **Deterministic Routing:** LangGraph prevents infinite loops and ensures the agent stays on task.
- **Reproducible Data Lineage:** Every document ingested is tracked as a ZenML artifact.
- **Observability:** Integrated with LangSmith for deep tracing and performance monitoring.
