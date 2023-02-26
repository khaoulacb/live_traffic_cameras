import yaml
import logging as log


def check_source(source_name: str) -> bool:
    """Function that checks if a source is registered and exists in the sources_info.yaml file"""
    source_exists = False
    yaml_path = "config/sources_info.yaml"
    try:
        with open(yaml_path, "r") as f:
            data = yaml.safe_load(f)
        sources = data["sources"]
    except:
        log.error("<Function check_source> Problem opening file 'sources_info.yaml'")
    try:
        for source in sources:
            if source["source"] == source_name:
                source_exists = True
                break
        return source_exists
    except:
        log.error("<Function check_source> Error while accessing sources information in 'sources_info.yaml'")


class SourceInfo:
    def __init__(self, source_name: str):
        if check_source(source_name=source_name):
            yaml_path = "config/sources_info.yaml"
            with open(yaml_path, "r") as f:
                data = yaml.safe_load(f)
            sources = data["sources"]
            source_index = next((index for (index, s) in enumerate(sources) if s["source"] == source_name), None)
            source_info = sources[source_index]

            self.name = source_info["source"]
            self.complete_name = source_info["sourceName"]
            self.url = source_info["url"]
            self.format = source_info["format"]
            self.class_name = source_info["class"]
            self.module_name = source_info["module"]
            self.csv_name = source_info["fileName"]

        else:
            log.error("Invalid Source Name")


def get_sources() -> list:
    """Function that generates SourceInfo() object for every source in sources_info.yaml and outputs a list of them"""
    yaml_path = "config/sources_info.yaml"
    sources_list = []

    try:
        with open(yaml_path, "r") as f:
            data = yaml.safe_load(f)
        sources = data["sources"]
    except:
        log.error("<Function get_sources> Problem opening file 'sources_info.yaml'")

    try:
        for source in sources:
            current_object = SourceInfo(source["source"])
            sources_list.append(current_object)
        
        return sources_list
    except:
        log.error("<Function get_sources> Error while accessing sources information in 'sources_info.yaml'")