from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ServicenowCredentials

class ServicenowGetToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    short_description: Optional[str] = Field(None, description="Short description of the incident")
    get_option: Optional[str] = Field(None, description="Unique identifier of the user")
    output_field: Optional[str] = Field(None, description="Field name where downloaded data will be placed")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    inputs_to_ignore: Optional[str] = Field(None, description="List of input properties to avoid sending, separated by commas. Leave empty to send all inputs.")
    id: Optional[str] = Field(None, description="Unique identifier of the incident")
    fields_to_send: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")
    operation: Optional[str] = Field(None, description="Operation")
    download: Optional[bool] = Field(None, description="Download Attachments")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    data_to_send: Optional[str] = Field(None, description="Data to Send")
    user_name: Optional[str] = Field(None, description="Unique identifier of the user")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication method to use")
    attachment_id: Optional[str] = Field(None, description="Sys_id value of the attachment to delete")
    table_name: Optional[str] = Field(None, description="Name of the table in which the record exists. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class ServicenowGetTool(BaseTool):
    name: str = "servicenow_get"
    connector_id: str = "nodes-base.serviceNow"
    description: str = "Tool for serviceNow get operation - get operation"
    args_schema: type[BaseModel] | None = ServicenowGetToolInput
    credentials: Optional[ServicenowCredentials] = None
