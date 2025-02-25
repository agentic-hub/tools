# elasticsearch operations
from typing import List
from langchain.tools import BaseTool
from .. import ElasticsearchCredentials

def get_tools() -> List[BaseTool]:
    """Get all elasticsearch operation tools."""
    tools = []
    from .create import ElasticsearchCreateTool
    tools.append(ElasticsearchCreateTool())
    from .delete import ElasticsearchDeleteTool
    tools.append(ElasticsearchDeleteTool())
    from .get import ElasticsearchGetTool
    tools.append(ElasticsearchGetTool())
    from .getall import ElasticsearchGetallTool
    tools.append(ElasticsearchGetallTool())
    from .update import ElasticsearchUpdateTool
    tools.append(ElasticsearchUpdateTool())
    from .__custom_api_call__ import Elasticsearch__custom_api_call__Tool
    tools.append(Elasticsearch__custom_api_call__Tool())
    from .create import ElasticsearchCreateTool
    tools.append(ElasticsearchCreateTool())
    from .delete import ElasticsearchDeleteTool
    tools.append(ElasticsearchDeleteTool())
    from .get import ElasticsearchGetTool
    tools.append(ElasticsearchGetTool())
    from .getall import ElasticsearchGetallTool
    tools.append(ElasticsearchGetallTool())
    from .__custom_api_call__ import Elasticsearch__custom_api_call__Tool
    tools.append(Elasticsearch__custom_api_call__Tool())
    return tools
