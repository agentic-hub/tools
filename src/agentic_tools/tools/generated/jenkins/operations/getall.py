from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import JenkinsCredentials

class JenkinsGetallToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    instance_notice: Optional[str] = Field(None, description="Instance operation can shutdown Jenkins instance and make it unresponsive. Some commands may not be available depending on instance implementation.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    job: Optional[str] = Field(None, description="Name of the job. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Possible operations")


class JenkinsGetallTool(BaseTool):
    name: str = "jenkins_getall"
    description: str = "Tool for jenkins getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = JenkinsGetallToolInput
    credentials: Optional[JenkinsCredentials] = None
