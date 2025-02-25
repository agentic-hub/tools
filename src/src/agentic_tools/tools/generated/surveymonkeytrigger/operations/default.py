from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SurveymonkeytriggerDefaultToolInput(BaseModel):
    resolveData: Optional[bool] = Field(None, description="By default the webhook-data only contain the IDs. If this option gets activated, it will resolve the data automatically.")
    collectorIds: Optional[str] = Field(None, description="collectorIds")
    event: Optional[str] = Field(None, description="Event")
    authentication: Optional[str] = Field(None, description="Authentication")
    onlyAnswers: Optional[bool] = Field(None, description="Whether to return only the answers of the form and not any of the other data")
    objectType: Optional[str] = Field(None, description="Type")
    surveyIds: Optional[str] = Field(None, description="surveyIds")
    surveyId: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")


class SurveymonkeytriggerDefaultTool(BaseTool):
    name = "surveymonkeytrigger_default"
    description = "Tool for surveyMonkeyTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the surveyMonkeyTrigger default operation."""
        # Implement the tool logic here
        return f"Running surveyMonkeyTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the surveyMonkeyTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
