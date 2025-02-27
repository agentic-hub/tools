from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AgilecrmCredentials

class AgilecrmGetToolInput(BaseModel):
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    json_notice: Optional[str] = Field(None, description="See <a href=\"https://github.com/agilecrm/rest-api#121-get-contacts-by-dynamic-filter\" target=\"_blank\">Agile CRM guide</a> to creating filters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    additional_fields_json: Optional[str] = Field(None, description="Object of values to set as described <a href=\"https://github.com/agilecrm/rest-api#1-contacts---companies-api\">here</a>")
    company_id: Optional[str] = Field(None, description="Unique identifier for a particular company")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filter_json: Optional[str] = Field(None, description="Filters (JSON)")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    deal_id: Optional[str] = Field(None, description="Unique identifier for a particular deal")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contact_id: Optional[str] = Field(None, description="Unique identifier for a particular contact")
    filter_type: Optional[str] = Field(None, description="Filter")
    match_type: Optional[str] = Field(None, description="Must Match")


class AgilecrmGetTool(BaseTool):
    name: str = "agilecrm_get"
    description: str = "Tool for agileCrm get operation - get operation"
    args_schema: type[BaseModel] | None = AgilecrmGetToolInput
    credentials: Optional[AgilecrmCredentials] = None
