"""
ADK Helper Functions for State Management

This module provides helper functions for managing state in ADK agents,
specifically for the RAG corpus management use case.
"""

from google.adk.tools import ToolContext, FunctionTool
from typing import Dict, Optional, Any
from ..config import PROJECT_ID, LOCATION

def store_corpus_id(tool_context: ToolContext, corpus_id: str) -> dict:
    """
    Store a corpus ID in the agent's state.
    
    Args:
        tool_context: The tool context containing state
        corpus_id: The corpus ID to store
        
    Returns:
        A status message
    """
    if hasattr(tool_context, 'state'):
        # Store the corpus ID in the session state
        tool_context.state['last_corpus_id'] = corpus_id
        return {
            "status": "success",
            "message": f"Stored corpus ID '{corpus_id}' in state"
        }
    return {
        "status": "warning",
        "message": "State not available in this context"
    }

def get_last_corpus_id(tool_context: ToolContext) -> dict:
    """
    Retrieve the last stored corpus ID from the agent's state.
    
    Args:
        tool_context: The tool context containing state
        
    Returns:
        A dictionary with the corpus ID or an error message
    """
    if hasattr(tool_context, 'state') and 'last_corpus_id' in tool_context.state:
        return {
            "status": "success",
            "corpus_id": tool_context.state['last_corpus_id'],
            "message": f"Retrieved corpus ID: {tool_context.state['last_corpus_id']}"
        }
    return {
        "status": "error",
        "message": "No corpus ID found in state"
    }

# Create FunctionTools from the functions
store_corpus_id_tool = FunctionTool(store_corpus_id)
get_last_corpus_id_tool = FunctionTool(get_last_corpus_id) 