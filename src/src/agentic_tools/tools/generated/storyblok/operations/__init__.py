# storyblok operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all storyblok operation tools."""
    tools = []
    from .get import StoryblokGetTool
    tools.append(StoryblokGetTool())
    from .getall import StoryblokGetallTool
    tools.append(StoryblokGetallTool())
    from .delete import StoryblokDeleteTool
    tools.append(StoryblokDeleteTool())
    from .get import StoryblokGetTool
    tools.append(StoryblokGetTool())
    from .getall import StoryblokGetallTool
    tools.append(StoryblokGetallTool())
    from .publish import StoryblokPublishTool
    tools.append(StoryblokPublishTool())
    from .unpublish import StoryblokUnpublishTool
    tools.append(StoryblokUnpublishTool())
    return tools
