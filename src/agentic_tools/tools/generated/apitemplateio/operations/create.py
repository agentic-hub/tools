from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ApitemplateioCredentials

class ApitemplateioCreateToolInput(BaseModel):
    image_template_id: Optional[str] = Field(None, description="ID of the image template to use. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    download: Optional[bool] = Field(None, description="Name of the binary property to which to write the data of the read file")
    resource: Optional[str] = Field(None, description="Resource")
    properties_json: Optional[str] = Field(None, description="Properties (JSON)")
    properties_ui: Optional[Dict[str, Any]] = Field(None, description="Properties")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    pdf_template_id: Optional[str] = Field(None, description="ID of the PDF template to use. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    binary_property: Optional[str] = Field(None, description="Put Output File in Field")
    overrides_json: Optional[str] = Field(None, description="Overrides (JSON)")
    operation: Optional[str] = Field(None, description="Operation")
    overrides_ui: Optional[Dict[str, Any]] = Field(None, description="Overrides")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")


class ApitemplateioCreateTool(BaseTool):
    name: str = "apitemplateio_create"
    description: str = "Tool for apiTemplateIo create operation - create operation"
    args_schema: type[BaseModel] | None = ApitemplateioCreateToolInput
    credentials: Optional[ApitemplateioCredentials] = None
