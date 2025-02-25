from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Cortex__custom_api_call__ToolInput(BaseModel):
    jsonObject: Optional[bool] = Field(None, description="Choose between providing JSON object or seperated attributes")
    objectData: Optional[str] = Field(None, description="Entity Object (JSON)")
    resource: Optional[str] = Field(None, description="Choose a resource")
    entityType: Optional[str] = Field(None, description="Choose the Data type. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    responder: Optional[str] = Field(None, description="Choose the responder. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    parameters: Optional[Dict[str, Any]] = Field(None, description="Parameters")
    operation: Optional[str] = Field(None, description="Choose an operation")


class Cortex__custom_api_call__Tool(BaseTool):
    name = "cortex___custom_api_call__"
    description = "Tool for cortex __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    
    def _run(self, **kwargs):
        """Run the cortex __CUSTOM_API_CALL__ operation."""
        # Implement the tool logic here
        return f"Running cortex __CUSTOM_API_CALL__ operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the cortex __CUSTOM_API_CALL__ operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
