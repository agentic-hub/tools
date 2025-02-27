from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import JenkinsCredentials

class JenkinsTriggerToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    instance_notice: Optional[str] = Field(None, description="Instance operation can shutdown Jenkins instance and make it unresponsive. Some commands may not be available depending on instance implementation.")
    job: Optional[str] = Field(None, description="Name of the job. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Possible operations")


class JenkinsTriggerTool(BaseTool):
    name: str = "jenkins_trigger"
    description: str = "Tool for jenkins trigger operation - trigger operation"
    args_schema: type[BaseModel] | None = JenkinsTriggerToolInput
    credentials: Optional[JenkinsCredentials] = None
