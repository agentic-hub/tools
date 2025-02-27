from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PhantombusterCredentials

class PhantombusterGetoutputToolInput(BaseModel):
    resolve_data: Optional[bool] = Field(None, description="By default the outpout is presented as string. If this option gets activated, it will resolve the data automatically.")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    agent_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class PhantombusterGetoutputTool(BaseTool):
    name: str = "phantombuster_getoutput"
    description: str = "Tool for phantombuster getOutput operation - getOutput operation"
    args_schema: type[BaseModel] | None = PhantombusterGetoutputToolInput
    credentials: Optional[PhantombusterCredentials] = None
