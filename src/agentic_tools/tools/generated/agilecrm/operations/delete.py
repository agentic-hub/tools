from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AgilecrmCredentials

class AgilecrmDeleteToolInput(BaseModel):
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    json_notice: Optional[str] = Field(None, description="See <a href=\"https://github.com/agilecrm/rest-api#121-get-contacts-by-dynamic-filter\" target=\"_blank\">Agile CRM guide</a> to creating filters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    additional_fields_json: Optional[str] = Field(None, description="Object of values to set as described <a href=\"https://github.com/agilecrm/rest-api#1-contacts---companies-api\">here</a>")
    company_id: Optional[str] = Field(None, description="ID of company to delete")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filter_json: Optional[str] = Field(None, description="Filters (JSON)")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    deal_id: Optional[str] = Field(None, description="ID of deal to delete")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contact_id: Optional[str] = Field(None, description="ID of contact to delete")
    filter_type: Optional[str] = Field(None, description="Filter")
    match_type: Optional[str] = Field(None, description="Must Match")


class AgilecrmDeleteTool(BaseTool):
    name: str = "agilecrm_delete"
    connector_id: str = "nodes-base.agileCrm"
    description: str = "Tool for agileCrm delete operation - delete operation"
    args_schema: type[BaseModel] | None = AgilecrmDeleteToolInput
    credentials: Optional[AgilecrmCredentials] = None
