from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import JenkinsCredentials

class JenkinsCopyToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    instance_notice: Optional[str] = Field(None, description="Instance operation can shutdown Jenkins instance and make it unresponsive. Some commands may not be available depending on instance implementation.")
    job: Optional[str] = Field(None, description="Name of the job. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    new_job: Optional[str] = Field(None, description="Name of the new Jenkins job")
    operation: Optional[str] = Field(None, description="Possible operations")


class JenkinsCopyTool(BaseTool):
    name: str = "jenkins_copy"
    description: str = "Tool for jenkins copy operation - copy operation"
    args_schema: type[BaseModel] | None = JenkinsCopyToolInput
    credentials: Optional[JenkinsCredentials] = None
