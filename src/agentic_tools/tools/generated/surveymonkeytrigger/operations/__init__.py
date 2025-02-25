# surveyMonkeyTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all surveyMonkeyTrigger operation tools."""
    tools = []
    from .default import SurveymonkeytriggerDefaultTool
    tools.append(SurveymonkeytriggerDefaultTool())
    return tools
