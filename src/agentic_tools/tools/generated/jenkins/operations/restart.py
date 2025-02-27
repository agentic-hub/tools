from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import JenkinsCredentials

class JenkinsRestartToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    instance_notice: Optional[str] = Field(None, description="Instance operation can shutdown Jenkins instance and make it unresponsive. Some commands may not be available depending on instance implementation.")
    job: Optional[str] = Field(None, description="Name of the job. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Possible operations")


class JenkinsRestartTool(BaseTool):
    name: str = "jenkins_restart"
    connector_id: str = "nodes-base.jenkins"
    description: str = "Tool for jenkins restart operation - restart operation"
    args_schema: type[BaseModel] | None = JenkinsRestartToolInput
    credentials: Optional[JenkinsCredentials] = None
