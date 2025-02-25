from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CustomerioAddToolInput(BaseModel):
    eventName: Optional[str] = Field(None, description="Name of the event to track")
    customerIds: Optional[str] = Field(None, description="A list of customer IDs to add to the segment")
    segmentId: Optional[float] = Field(None, description="The unique identifier of the segment")
    resource: Optional[str] = Field(None, description="Resource")
    campaignId: Optional[float] = Field(None, description="The unique identifier for the campaign")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    additionalFieldsJson: Optional[str] = Field(None, description="Object of values to set as described <a href=\"https://github.com/agilecrm/rest-api#1-companys---companies-api\">here</a>")
    operation: Optional[str] = Field(None, description="Operation")
    id: Optional[str] = Field(None, description="The unique identifier for the customer")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")


class CustomerioAddTool(BaseTool):
    name = "customerio_add"
    description = "Tool for customerIo add operation - add operation"
    
    def _run(self, **kwargs):
        """Run the customerIo add operation."""
        # Implement the tool logic here
        return f"Running customerIo add operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the customerIo add operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
