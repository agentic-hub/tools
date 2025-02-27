from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ThehiveCredentials

class ThehiveExecuteresponderToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    flag: Optional[bool] = Field(None, description="Flag of the case default=false")
    description: Optional[str] = Field(None, description="Description of the alert")
    analyzers: Optional[str] = Field(None, description="analyzers")
    tlp: Optional[str] = Field(None, description="Traffict Light Protocol (TLP). Default=Amber.")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    case_id: Optional[str] = Field(None, description="Case ID")
    tags: Optional[str] = Field(None, description="Case Tags")
    id: Optional[str] = Field(None, description="Title of the alert")
    operation: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="Description of the observable in the context of the case")
    severity: Optional[str] = Field(None, description="Severity of the alert. Default=Medium.")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    status: Optional[str] = Field(None, description="Status of the alert")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    responder: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    start_date: Optional[str] = Field(None, description="Date and time of the begin of the case default=now")
    title: Optional[str] = Field(None, description="Title of the alert")


class ThehiveExecuteresponderTool(BaseTool):
    name: str = "thehive_executeresponder"
    connector_id: str = "nodes-base.theHive"
    description: str = "Tool for theHive executeResponder operation - executeResponder operation"
    args_schema: type[BaseModel] | None = ThehiveExecuteresponderToolInput
    credentials: Optional[ThehiveCredentials] = None
