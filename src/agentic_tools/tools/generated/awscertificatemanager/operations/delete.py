from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwscertificatemanagerCredentials

class AwscertificatemanagerDeleteToolInput(BaseModel):
    certificate_arn: Optional[str] = Field(None, description="String that contains the ARN of the ACM certificate to be renewed. This must be of the form: arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012.")
    resource: Optional[str] = Field(None, description="Resource")
    bucket_name: Optional[str] = Field(None, description="Bucket Name")
    operation: Optional[str] = Field(None, description="Operation")
    certificate_key: Optional[str] = Field(None, description="Certificate Key")


class AwscertificatemanagerDeleteTool(BaseTool):
    name: str = "awscertificatemanager_delete"
    description: str = "Tool for awsCertificateManager delete operation - delete operation"
    args_schema: type[BaseModel] | None = AwscertificatemanagerDeleteToolInput
    credentials: Optional[AwscertificatemanagerCredentials] = None
