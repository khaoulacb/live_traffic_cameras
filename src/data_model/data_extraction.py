import importlib
from utils.entities.source_info import get_sources
import logging as log
import os


def extract_data():
    sources = get_sources()
    dir = "temp_files/"
    try:
        for source in sources:
            
            class_ = getattr(importlib.import_module(source.module_name), source.class_name)
            instance = class_()
            df = instance.getNormalizedDataframe()
            destination = dir + source.csv_name

            if os.path.exists(destination):
                os.remove(destination)

            df.to_csv(destination, index=False)
    except:
        log.error("<Function extract_data> Error while extracting data from sources")