from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class Servicenow__custom_api_call__ToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    short_description: Optional[str] = Field(None, description="Short description of the incident")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    inputsToIgnore: Optional[str] = Field(None, description="List of input properties to avoid sending, separated by commas. Leave empty to send all inputs.")
    id: Optional[str] = Field(None, description="Sys_id of the record in the table specified in Table Name that you want to attach the file to")
    fieldsToSend: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    dataToSend: Optional[str] = Field(None, description="Data to Send")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication method to use")
    attachmentId: Optional[str] = Field(None, description="Sys_id value of the attachment to delete")
    tableName: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")


class Servicenow__custom_api_call__Tool(BaseTool):
    name = "servicenow___custom_api_call__"
    description = "Tool for serviceNow __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    
    def _run(self, **kwargs):
        """Run the serviceNow __CUSTOM_API_CALL__ operation."""
        # Implement the tool logic here
        return f"Running serviceNow __CUSTOM_API_CALL__ operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the serviceNow __CUSTOM_API_CALL__ operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
