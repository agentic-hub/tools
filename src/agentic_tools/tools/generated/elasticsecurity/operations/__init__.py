# elasticSecurity operations
from typing import List
from langchain.tools import BaseTool
from .. import ElasticsecurityCredentials

def get_tools() -> List[BaseTool]:
    """Get all elasticSecurity operation tools."""
    tools = []
    from .create import ElasticsecurityCreateTool
    tools.append(ElasticsecurityCreateTool())
    from .delete import ElasticsecurityDeleteTool
    tools.append(ElasticsecurityDeleteTool())
    from .get import ElasticsecurityGetTool
    tools.append(ElasticsecurityGetTool())
    from .getall import ElasticsecurityGetallTool
    tools.append(ElasticsecurityGetallTool())
    from .getstatus import ElasticsecurityGetstatusTool
    tools.append(ElasticsecurityGetstatusTool())
    from .update import ElasticsecurityUpdateTool
    tools.append(ElasticsecurityUpdateTool())
    from .add import ElasticsecurityAddTool
    tools.append(ElasticsecurityAddTool())
    from .get import ElasticsecurityGetTool
    tools.append(ElasticsecurityGetTool())
    from .getall import ElasticsecurityGetallTool
    tools.append(ElasticsecurityGetallTool())
    from .remove import ElasticsecurityRemoveTool
    tools.append(ElasticsecurityRemoveTool())
    from .update import ElasticsecurityUpdateTool
    tools.append(ElasticsecurityUpdateTool())
    from .add import ElasticsecurityAddTool
    tools.append(ElasticsecurityAddTool())
    from .remove import ElasticsecurityRemoveTool
    tools.append(ElasticsecurityRemoveTool())
    from .create import ElasticsecurityCreateTool
    tools.append(ElasticsecurityCreateTool())
    return tools
