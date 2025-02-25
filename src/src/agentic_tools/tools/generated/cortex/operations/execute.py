from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CortexExecuteToolInput(BaseModel):
    jsonObject: Optional[bool] = Field(None, description="Choose between providing JSON object or seperated attributes")
    objectData: Optional[str] = Field(None, description="Entity Object (JSON)")
    resource: Optional[str] = Field(None, description="Choose a resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    observableValue: Optional[str] = Field(None, description="Enter the observable value")
    binaryPropertyName: Optional[str] = Field(None, description="Put Output File in Field")
    entityType: Optional[str] = Field(None, description="Choose the Data type. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    responder: Optional[str] = Field(None, description="Choose the responder. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    analyzer: Optional[str] = Field(None, description="Choose the analyzer. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    observableType: Optional[str] = Field(None, description="Choose the observable type. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    parameters: Optional[Dict[str, Any]] = Field(None, description="Parameters")
    tlp: Optional[str] = Field(None, description="The TLP of the analyzed observable")
    operation: Optional[str] = Field(None, description="Choose an operation")


class CortexExecuteTool(BaseTool):
    name = "cortex_execute"
    description = "Tool for cortex execute operation - execute operation"
    
    def _run(self, **kwargs):
        """Run the cortex execute operation."""
        # Implement the tool logic here
        return f"Running cortex execute operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the cortex execute operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
