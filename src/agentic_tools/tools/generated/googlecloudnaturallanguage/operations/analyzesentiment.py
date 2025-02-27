from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglecloudnaturallanguageCredentials

class GooglecloudnaturallanguageAnalyzesentimentToolInput(BaseModel):
    content: Optional[str] = Field(None, description="The content of the input in string format. Cloud audit logging exempt since it is based on user data.")
    source: Optional[str] = Field(None, description="The source of the document: a string containing the content or a Google Cloud Storage URI")
    resource: Optional[str] = Field(None, description="Resource")
    gcs_content_uri: Optional[str] = Field(None, description="The Google Cloud Storage URI where the file content is located. This URI must be of the form: <code>gs://bucket_name/object_name</code>. For more details, see <a href=\"https://cloud.google.com/storage/docs/reference-uris.\">reference</a>.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GooglecloudnaturallanguageAnalyzesentimentTool(BaseTool):
    name: str = "googlecloudnaturallanguage_analyzesentiment"
    connector_id: str = "nodes-base.googleCloudNaturalLanguage"
    description: str = "Tool for googleCloudNaturalLanguage analyzeSentiment operation - analyzeSentiment operation"
    args_schema: type[BaseModel] | None = GooglecloudnaturallanguageAnalyzesentimentToolInput
    credentials: Optional[GooglecloudnaturallanguageCredentials] = None
