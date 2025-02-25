from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CustomerioUpsertToolInput(BaseModel):
    eventName: Optional[str] = Field(None, description="Name of the event to track")
    resource: Optional[str] = Field(None, description="Resource")
    campaignId: Optional[float] = Field(None, description="The unique identifier for the campaign")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    additionalFieldsJson: Optional[str] = Field(None, description="Object of values to set as described <a href=\"https://github.com/agilecrm/rest-api#1-companys---companies-api\">here</a>")
    operation: Optional[str] = Field(None, description="Operation")
    id: Optional[str] = Field(None, description="The unique identifier for the customer")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")


class CustomerioUpsertTool(BaseTool):
    name = "customerio_upsert"
    description = "Tool for customerIo upsert operation - upsert operation"
    
    def _run(self, **kwargs):
        """Run the customerIo upsert operation."""
        # Implement the tool logic here
        return f"Running customerIo upsert operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the customerIo upsert operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
