from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import JenkinsCredentials

class JenkinsTriggerparamsToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    instance_notice: Optional[str] = Field(None, description="Instance operation can shutdown Jenkins instance and make it unresponsive. Some commands may not be available depending on instance implementation.")
    job: Optional[str] = Field(None, description="Name of the job. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    param: Optional[Dict[str, Any]] = Field(None, description="Parameters for Jenkins job")
    trigger_params_notice: Optional[str] = Field(None, description="Make sure the job is setup to support triggering with parameters. <a href=\"https://wiki.jenkins.io/display/JENKINS/Parameterized+Build\" target=\"_blank\">More info</a>")
    operation: Optional[str] = Field(None, description="Possible operations")


class JenkinsTriggerparamsTool(BaseTool):
    name: str = "jenkins_triggerparams"
    connector_id: str = "nodes-base.jenkins"
    description: str = "Tool for jenkins triggerParams operation - triggerParams operation"
    args_schema: type[BaseModel] | None = JenkinsTriggerparamsToolInput
    credentials: Optional[JenkinsCredentials] = None
