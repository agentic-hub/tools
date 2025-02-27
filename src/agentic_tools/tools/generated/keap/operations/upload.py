from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import KeapCredentials

class KeapUploadToolInput(BaseModel):
    tag_ids: Optional[str] = Field(None, description="tagIds")
    user_id: Optional[str] = Field(None, description="The infusionsoft user to create the note on behalf of. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    addresses_ui: Optional[Dict[str, Any]] = Field(None, description="Addresses")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    operation: Optional[str] = Field(None, description="Operation")
    binary_data: Optional[bool] = Field(None, description="Whether the data to upload should be taken from binary field")
    phones_ui: Optional[Dict[str, Any]] = Field(None, description="Phones")
    is_public: Optional[bool] = Field(None, description="Is Public")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    order_id: Optional[str] = Field(None, description="Order ID")
    file_association: Optional[str] = Field(None, description="File Association")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    file_data: Optional[str] = Field(None, description="The content of the attachment, encoded in Base64")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    note_id: Optional[str] = Field(None, description="Note ID")
    file_name: Optional[str] = Field(None, description="The filename of the attached file, including extension")
    faxes_ui: Optional[Dict[str, Any]] = Field(None, description="Faxes")
    product_id: Optional[str] = Field(None, description="Product ID")


class KeapUploadTool(BaseTool):
    name: str = "keap_upload"
    connector_id: str = "nodes-base.keap"
    description: str = "Tool for keap upload operation - upload operation"
    args_schema: type[BaseModel] | None = KeapUploadToolInput
    credentials: Optional[KeapCredentials] = None
