from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ThehiveprojectCredentials

class Thehiveproject__custom_api_call__ToolInput(BaseModel):
    sort: Optional[Dict[str, Any]] = Field(None, description="Sort")
    content: Optional[str] = Field(None, description="Content")
    location: Optional[str] = Field(None, description="Create in")
    observable_fields: Optional[str] = Field(None, description="observableFields")
    page_id: Optional[Dict[str, Any]] = Field(None, description="Page")
    comment_id: Optional[Dict[str, Any]] = Field(None, description="Comment")
    analyzers: Optional[str] = Field(None, description="analyzers")
    alert_id: Optional[Dict[str, Any]] = Field(None, description="Alert")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    observable_id: Optional[Dict[str, Any]] = Field(None, description="Observable")
    case_id: Optional[Dict[str, Any]] = Field(None, description="Case")
    task_update_fields: Optional[str] = Field(None, description="taskUpdateFields")
    alert_fields: Optional[str] = Field(None, description="alertFields")
    id: Optional[Dict[str, Any]] = Field(None, description="Alert")
    operation: Optional[str] = Field(None, description="Operation")
    task_id: Optional[Dict[str, Any]] = Field(None, description="Task")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    task_fields: Optional[str] = Field(None, description="taskFields")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="Message")
    alert_update_fields: Optional[str] = Field(None, description="alertUpdateFields")
    data_type: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    search_in: Optional[str] = Field(None, description="Whether to search for comments in all alerts and cases or in a specific case or alert")
    resource: Optional[str] = Field(None, description="Resource")
    case_update_fields: Optional[str] = Field(None, description="caseUpdateFields")
    responder: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    attachments_ui: Optional[Dict[str, Any]] = Field(None, description="Array of supported attachments to add to the message")
    case_fields: Optional[str] = Field(None, description="caseFields")
    log_id: Optional[Dict[str, Any]] = Field(None, description="Task Log")
    observable_update_fields: Optional[str] = Field(None, description="observableUpdateFields")
    log_fields: Optional[str] = Field(None, description="logFields")
    attachment_id: Optional[str] = Field(None, description="ID of the attachment. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class Thehiveproject__custom_api_call__Tool(BaseTool):
    name: str = "thehiveproject___custom_api_call__"
    connector_id: str = "nodes-base.theHiveProject"
    description: str = "Tool for theHiveProject __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Thehiveproject__custom_api_call__ToolInput
    credentials: Optional[ThehiveprojectCredentials] = None
