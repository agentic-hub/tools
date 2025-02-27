from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import OnfleetCredentials

class OnfleetCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    address_number: Optional[str] = Field(None, description="The number component of this address, it may also contain letters")
    address: Optional[str] = Field(None, description="The destination's street address details")
    address_city: Optional[str] = Field(None, description="The name of the municipality")
    teams: Optional[str] = Field(None, description="teams")
    workers: Optional[str] = Field(None, description="workers")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    recipient_name: Optional[str] = Field(None, description="The recipient's complete name")
    email: Optional[str] = Field(None, description="The administrator's email address")
    address_country: Optional[str] = Field(None, description="The name of the country")
    id: Optional[str] = Field(None, description="The ID of the admin object for lookup")
    phone: Optional[str] = Field(None, description="A list of worker’s phone numbers")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The administrator's name")
    managers: Optional[str] = Field(None, description="managers")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    address_street: Optional[str] = Field(None, description="The name of the street")
    destination: Optional[Dict[str, Any]] = Field(None, description="Destination")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="The resource to perform operations on")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    unparsed: Optional[bool] = Field(None, description="Whether or not the address is specified in a single unparsed string")
    recipient_phone: Optional[str] = Field(None, description="A unique, valid phone number as per the organization's country if there's no leading + sign. If a phone number has a leading + sign, it will disregard the organization's country setting.")


class OnfleetCreateTool(BaseTool):
    name: str = "onfleet_create"
    description: str = "Tool for onfleet create operation - create operation"
    args_schema: type[BaseModel] | None = OnfleetCreateToolInput
    credentials: Optional[OnfleetCredentials] = None
