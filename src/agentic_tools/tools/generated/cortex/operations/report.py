from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CortexCredentials

class CortexReportToolInput(BaseModel):
    json_object: Optional[bool] = Field(None, description="Choose between providing JSON object or seperated attributes")
    object_data: Optional[str] = Field(None, description="Entity Object (JSON)")
    resource: Optional[str] = Field(None, description="Choose a resource")
    entity_type: Optional[str] = Field(None, description="Choose the Data type. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    responder: Optional[str] = Field(None, description="Choose the responder. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    parameters: Optional[Dict[str, Any]] = Field(None, description="Parameters")
    job_id: Optional[str] = Field(None, description="ID of the job")
    operation: Optional[str] = Field(None, description="Choose an operation")


class CortexReportTool(BaseTool):
    name: str = "cortex_report"
    description: str = "Tool for cortex report operation - report operation"
    args_schema: type[BaseModel] | None = CortexReportToolInput
    credentials: Optional[CortexCredentials] = None
