from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CortexReportToolInput(BaseModel):
    jsonObject: Optional[bool] = Field(None, description="Choose between providing JSON object or seperated attributes")
    objectData: Optional[str] = Field(None, description="Entity Object (JSON)")
    resource: Optional[str] = Field(None, description="Choose a resource")
    entityType: Optional[str] = Field(None, description="Choose the Data type. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    responder: Optional[str] = Field(None, description="Choose the responder. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    parameters: Optional[Dict[str, Any]] = Field(None, description="Parameters")
    jobId: Optional[str] = Field(None, description="ID of the job")
    operation: Optional[str] = Field(None, description="Choose an operation")


class CortexReportTool(BaseTool):
    name = "cortex_report"
    description = "Tool for cortex report operation - report operation"
    
    def _run(self, **kwargs):
        """Run the cortex report operation."""
        # Implement the tool logic here
        return f"Running cortex report operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the cortex report operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
