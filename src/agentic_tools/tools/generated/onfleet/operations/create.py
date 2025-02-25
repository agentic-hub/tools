from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class OnfleetCreateToolInput(BaseModel):
    updateFields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    addressNumber: Optional[str] = Field(None, description="The number component of this address, it may also contain letters")
    address: Optional[str] = Field(None, description="The destination's street address details")
    addressCity: Optional[str] = Field(None, description="The name of the municipality")
    teams: Optional[str] = Field(None, description="teams")
    workers: Optional[str] = Field(None, description="workers")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    recipientName: Optional[str] = Field(None, description="The recipient's complete name")
    email: Optional[str] = Field(None, description="The administrator's email address")
    addressCountry: Optional[str] = Field(None, description="The name of the country")
    id: Optional[str] = Field(None, description="The ID of the admin object for lookup")
    phone: Optional[str] = Field(None, description="A list of worker’s phone numbers")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The administrator's name")
    managers: Optional[str] = Field(None, description="managers")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    addressStreet: Optional[str] = Field(None, description="The name of the street")
    destination: Optional[Dict[str, Any]] = Field(None, description="Destination")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="The resource to perform operations on")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    unparsed: Optional[bool] = Field(None, description="Whether or not the address is specified in a single unparsed string")
    recipientPhone: Optional[str] = Field(None, description="A unique, valid phone number as per the organization's country if there's no leading + sign. If a phone number has a leading + sign, it will disregard the organization's country setting.")


class OnfleetCreateTool(BaseTool):
    name = "onfleet_create"
    description = "Tool for onfleet create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the onfleet create operation."""
        # Implement the tool logic here
        return f"Running onfleet create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the onfleet create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
