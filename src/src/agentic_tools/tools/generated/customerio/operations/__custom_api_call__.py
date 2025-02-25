from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Customerio__custom_api_call__ToolInput(BaseModel):
    eventName: Optional[str] = Field(None, description="Name of the event to track")
    resource: Optional[str] = Field(None, description="Resource")
    campaignId: Optional[float] = Field(None, description="The unique identifier for the campaign")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    additionalFieldsJson: Optional[str] = Field(None, description="Object of values to set as described <a href=\"https://github.com/agilecrm/rest-api#1-companys---companies-api\">here</a>")
    operation: Optional[str] = Field(None, description="Operation")
    id: Optional[str] = Field(None, description="The unique identifier for the customer")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")


class Customerio__custom_api_call__Tool(BaseTool):
    name = "customerio___custom_api_call__"
    description = "Tool for customerIo __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    
    def _run(self, **kwargs):
        """Run the customerIo __CUSTOM_API_CALL__ operation."""
        # Implement the tool logic here
        return f"Running customerIo __CUSTOM_API_CALL__ operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the customerIo __CUSTOM_API_CALL__ operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
