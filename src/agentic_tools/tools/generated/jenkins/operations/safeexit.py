from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import JenkinsCredentials

class JenkinsSafeexitToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    instance_notice: Optional[str] = Field(None, description="Instance operation can shutdown Jenkins instance and make it unresponsive. Some commands may not be available depending on instance implementation.")
    job: Optional[str] = Field(None, description="Name of the job. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Possible operations")


class JenkinsSafeexitTool(BaseTool):
    name: str = "jenkins_safeexit"
    connector_id: str = "nodes-base.jenkins"
    description: str = "Tool for jenkins safeExit operation - safeExit operation"
    args_schema: type[BaseModel] | None = JenkinsSafeexitToolInput
    credentials: Optional[JenkinsCredentials] = None
