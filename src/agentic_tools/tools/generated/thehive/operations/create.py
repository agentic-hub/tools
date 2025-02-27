from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ThehiveCredentials

class ThehiveCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    data: Optional[str] = Field(None, description="Data")
    sighted: Optional[bool] = Field(None, description="Whether sighted previously")
    flag: Optional[bool] = Field(None, description="Flag of the case default=false")
    description: Optional[str] = Field(None, description="Description of the alert")
    analyzers: Optional[str] = Field(None, description="analyzers")
    tlp: Optional[str] = Field(None, description="Traffict Light Protocol (TLP). Default=Amber.")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    type: Optional[str] = Field(None, description="Type of the alert")
    date: Optional[str] = Field(None, description="Date and time when the alert was raised default=now")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    case_id: Optional[str] = Field(None, description="ID of the case")
    tags: Optional[str] = Field(None, description="Case Tags")
    binary_property: Optional[str] = Field(None, description="The name of the input binary field that represent the attachment file")
    id: Optional[str] = Field(None, description="Title of the alert")
    operation: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    task_id: Optional[str] = Field(None, description="ID of the task")
    artifact_ui: Optional[Dict[str, Any]] = Field(None, description="Artifact attributes")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="Description of the observable in the context of the case")
    severity: Optional[str] = Field(None, description="Severity of the alert. Default=Medium.")
    data_type: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    source: Optional[str] = Field(None, description="Source of the alert")
    resource: Optional[str] = Field(None, description="Resource")
    follow: Optional[bool] = Field(None, description="Whether the alert becomes active when updated default=true")
    status: Optional[str] = Field(None, description="Status of the alert")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    ioc: Optional[bool] = Field(None, description="Whether the observable is an IOC (Indicator of compromise)")
    source_ref: Optional[str] = Field(None, description="Source reference of the alert")
    responder: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    start_date: Optional[str] = Field(None, description="Date and time of the begin of the case default=now")
    title: Optional[str] = Field(None, description="Title of the alert")
    owner: Optional[str] = Field(None, description="Owner")


class ThehiveCreateTool(BaseTool):
    name: str = "thehive_create"
    connector_id: str = "nodes-base.theHive"
    description: str = "Tool for theHive create operation - create operation"
    args_schema: type[BaseModel] | None = ThehiveCreateToolInput
    credentials: Optional[ThehiveCredentials] = None
