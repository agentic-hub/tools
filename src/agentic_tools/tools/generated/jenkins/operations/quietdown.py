from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import JenkinsCredentials

class JenkinsQuietdownToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    reason: Optional[str] = Field(None, description="Freeform reason for quiet down mode")
    instance_notice: Optional[str] = Field(None, description="Instance operation can shutdown Jenkins instance and make it unresponsive. Some commands may not be available depending on instance implementation.")
    job: Optional[str] = Field(None, description="Name of the job. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Possible operations")


class JenkinsQuietdownTool(BaseTool):
    name: str = "jenkins_quietdown"
    connector_id: str = "nodes-base.jenkins"
    description: str = "Tool for jenkins quietDown operation - quietDown operation"
    args_schema: type[BaseModel] | None = JenkinsQuietdownToolInput
    credentials: Optional[JenkinsCredentials] = None
