from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import JenkinsCredentials

class JenkinsCreateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    instance_notice: Optional[str] = Field(None, description="Instance operation can shutdown Jenkins instance and make it unresponsive. Some commands may not be available depending on instance implementation.")
    xml: Optional[str] = Field(None, description="XML of Jenkins config")
    job: Optional[str] = Field(None, description="Name of the job. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    new_job: Optional[str] = Field(None, description="Name of the new Jenkins job")
    create_notice: Optional[str] = Field(None, description="To get the XML of an existing job, add ‘config.xml’ to the end of the job URL")
    operation: Optional[str] = Field(None, description="Possible operations")


class JenkinsCreateTool(BaseTool):
    name: str = "jenkins_create"
    description: str = "Tool for jenkins create operation - create operation"
    args_schema: type[BaseModel] | None = JenkinsCreateToolInput
    credentials: Optional[JenkinsCredentials] = None
