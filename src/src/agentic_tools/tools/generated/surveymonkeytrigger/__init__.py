# surveyMonkeyTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_surveymonkeytrigger_tools() -> List[BaseTool]:
    """Get all surveyMonkeyTrigger tools."""
    from . import operations
    return operations.get_tools()
