from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwscertificatemanagerCredentials

class AwscertificatemanagerGetmetadataToolInput(BaseModel):
    certificate_arn: Optional[str] = Field(None, description="String that contains the ARN of the ACM certificate to be renewed. This must be of the form: arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012.")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class AwscertificatemanagerGetmetadataTool(BaseTool):
    name: str = "awscertificatemanager_getmetadata"
    description: str = "Tool for awsCertificateManager getMetadata operation - getMetadata operation"
    args_schema: type[BaseModel] | None = AwscertificatemanagerGetmetadataToolInput
    credentials: Optional[AwscertificatemanagerCredentials] = None
