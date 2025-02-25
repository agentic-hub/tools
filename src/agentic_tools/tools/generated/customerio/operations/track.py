from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CustomerioTrackToolInput(BaseModel):
    eventName: Optional[str] = Field(None, description="Name of the event to track")
    resource: Optional[str] = Field(None, description="Resource")
    campaignId: Optional[float] = Field(None, description="The unique identifier for the campaign")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    customerId: Optional[str] = Field(None, description="The unique identifier for the customer")
    additionalFieldsJson: Optional[str] = Field(None, description="Object of values to set as described <a href=\"https://customer.io/docs/api-triggered-data-format#basic-data-formatting\">here</a>")
    operation: Optional[str] = Field(None, description="Operation")
    id: Optional[str] = Field(None, description="The unique identifier for the customer")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")


class CustomerioTrackTool(BaseTool):
    name = "customerio_track"
    description = "Tool for customerIo track operation - track operation"
    
    def _run(self, **kwargs):
        """Run the customerIo track operation."""
        # Implement the tool logic here
        return f"Running customerIo track operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the customerIo track operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
