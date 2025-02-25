from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Highlevel__custom_api_call__ToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email or Phone are required to create contact")
    phone: Optional[str] = Field(None, description="Phone or Email are required to create contact. Phone number has to start with a valid <a href=\"https://en.wikipedia.org/wiki/List_of_country_calling_codes\">country code</a> leading with + sign.")
    operation: Optional[str] = Field(None, description="Operation")
    taskId: Optional[str] = Field(None, description="Task ID")
    opportunityId: Optional[str] = Field(None, description="Opportunity ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contactId: Optional[str] = Field(None, description="Contact ID")
    title: Optional[str] = Field(None, description="Title")


class Highlevel__custom_api_call__Tool(BaseTool):
    name = "highlevel___custom_api_call__"
    description = "Tool for highLevel __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    
    def _run(self, **kwargs):
        """Run the highLevel __CUSTOM_API_CALL__ operation."""
        # Implement the tool logic here
        return f"Running highLevel __CUSTOM_API_CALL__ operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the highLevel __CUSTOM_API_CALL__ operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
