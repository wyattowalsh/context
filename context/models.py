"""context/models.py -- data models module
"""

from logging.config import fileConfig
from pathlib import Path
from typing import Annotated

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from pydantic import BaseModel, Field, HttpUrl

from context.enums import FileGroup, FileType, OutputFileExtension, OutputType
from context.utils import BLACKLIST_ROUTE_GLOBS


class Config(BaseModel): 
    """Configuration for the context module"""
    urls            : Annotated[list[HttpUrl|Path], Field(default=None, description="input urls or file paths to compile as context")]                                          = None
    output_types    : Annotated[list[OutputType|OutputFileExtension], Field(default=[OutputType.TEXT], description="output types (as either type or extension enums)")] = None
    max_file_size_mb: Annotated[int, Field(default=10, description="maximum file size to process in MB")]                                                               = None
    web             : Annotated[WebConfig, Field(default=WebConfig(), description="configuration for the web data processor")]                                          = None
    file            : Annotated[fileConfig, Field(default=FileConfig(), description="configuration for the file data processor")]                                       = None
    gh              : Annotated[GithubConfig, Field(default=GithubConfig(), description="configuration for the github data processor")]                                 = None
    
    
class WebConfig(BaseModel): 
    """Configuration for the web data processor"""
    max_num_pages      : Annotated[int, Field(default=None, description="maximum number of pages to process")] = None
    max_depth          : Annotated[int, Field(default=None, description="maximum depth of the crawl")] = None
    reverse_crawl      : Annotated[bool, Field(default=False, description="reverse the crawl direction")] = False
    limit_to_domain    : Annotated[bool, Field(default=True, description="whether to limit the crawl to the domain")] = True
    process_sitemaps   : Annotated[bool, Field(default=True, description="whether to process sitemaps")] = True
    include_summary    : Annotated[bool, Field(default=True, description="whether to include the summary")] = True
    include_tree       : Annotated[bool, Field(default=True, description="whether to include the tree")] = True
    include_frontmatter: Annotated[bool, Field(default=True, description="whether to include the frontmatter")] = True
    download_files     : Annotated[bool, Field(default=True, description="whether to download files")] = True
    process_files      : Annotated[bool, Field(default=True, description="whether to process files")] = True
    include_files      : Annotated[bool, Field(default=True, description="whether to include files")] = True
    include            : Annotated[list[str], Field(default=[], description="list of URL route glob patterns urls to include")] = []
    exclude            : Annotated[list[str], Field(default=[], description="list of URL route glob patterns urls to exclude")] = BLACKLIST_ROUTE_GLOBS
    include_files      : Annotated[list[str], Field(default=[], description="list of file glob patterns to include")] = []
    exclude_files      : Annotated[list[str], Field(default=[], description="list of file glob patterns to exclude")] = []
    include_file_types : Annotated[list[FileType], Field(default=[], description="list of file types to include")] = []
    exclude_file_types : Annotated[list[FileType], Field(default=[], description="list of file types to exclude")] = []
    include_file_groups: Annotated[list[FileGroup], Field(default=[], description="list of file groups to include")] = []
    exclude_file_groups: Annotated[list[FileGroup], Field(default=[], description="list of file groups to exclude")] =[
                                                                                                                        FileGroup.ARCHIVE,
                                                                                                                        FileGroup.DISK_IMAGE,
                                                                                                                        FileGroup.INSTALLER,
                                                                                                                        FileGroup.EXECUTABLE,
                                                                                                                        FileGroup.BITTORRENT,
                                                                                                                        FileGroup.THREE_D,
                                                                                                                        FileGroup.SCIENTIFIC,
                                                                                                                        FileGroup.SHORTCUT,
                                                                                                                        FileGroup.FONT_ICON,
                                                                                                                    ]
    browser_config     : Annotated[BrowserConfig, Field(default=BrowserConfig(), description="crawl4ai browser configuration")] = BrowserConfig()
    crawler_run_config : Annotated[CrawlerRunConfig, Field(default=CrawlerRunConfig(), description="crawl4ai crawler run configuration")] = CrawlerRunConfig()
    proxy_config       : Annotated[ProxyConfig, Field(default=ProxyConfig(), description="proxy configuration")] = ProxyConfig()
    
    
class ProxyConfig(BaseModel): 
    """Configuration for the proxy"""
    enabled: Annotated[bool, Field(default=False, description="whether to use a proxy")] = False
    url: Annotated[str, Field(default="", description="proxy url")] = ""
        url: Annotated[str, Field(default="", description="proxy url")] = ""
    