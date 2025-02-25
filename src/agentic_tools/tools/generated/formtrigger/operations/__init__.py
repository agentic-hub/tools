# formTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all formTrigger operation tools."""
    tools = []
    from .default import FormtriggerDefaultTool
    tools.append(FormtriggerDefaultTool())
    return tools
