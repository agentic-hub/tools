from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SalesforceCredentials

class SalesforceUploadToolInput(BaseModel):
    external_id: Optional[str] = Field(None, description="The field to check to see if the lead already exists. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    campaign_id: Optional[str] = Field(None, description="ID of the campaign that needs to be fetched. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    case_id: Optional[str] = Field(None, description="ID of case that needs to be fetched")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[str] = Field(None, description="ID of account that needs to be fetched")
    custom_fields_ui: Optional[Dict[str, Any]] = Field(None, description="Filter by custom fields")
    task_id: Optional[str] = Field(None, description="ID of task that needs to be fetched")
    lastname: Optional[str] = Field(None, description="Required. Last name of the lead. Limited to 80 characters.")
    name: Optional[str] = Field(None, description="Required. Last name of the opportunity. Limited to 80 characters.")
    opportunity_id: Optional[str] = Field(None, description="ID of opportunity that needs to be fetched")
    external_id_value: Optional[str] = Field(None, description="If this value exists in the 'match against' field, update the lead. Otherwise create a new one.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    custom_object: Optional[str] = Field(None, description="Name of the custom object. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    authentication: Optional[str] = Field(None, description="OAuth Authorization Flow")
    contact_id: Optional[str] = Field(None, description="ID of contact that needs to be fetched")
    title: Optional[str] = Field(None, description="Name of the file")
    lead_id: Optional[str] = Field(None, description="ID of Lead that needs to be fetched")
    attachment_id: Optional[str] = Field(None, description="ID of attachment that needs to be fetched")
    record_id: Optional[str] = Field(None, description="Record ID to be updated")


class SalesforceUploadTool(BaseTool):
    name: str = "salesforce_upload"
    connector_id: str = "nodes-base.salesforce"
    description: str = "Tool for salesforce upload operation - upload operation"
    args_schema: type[BaseModel] | None = SalesforceUploadToolInput
    credentials: Optional[SalesforceCredentials] = None
