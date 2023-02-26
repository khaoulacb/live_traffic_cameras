from utils.entities.source_info import SourceInfo

class NormalizeSource:

    def __init__(self, source_name: str):
        self.source = SourceInfo(source_name)

    def _getRawData(self):
        """Loads the data in JSON format from a source URL"""
        pass

    def _getRawDataframe(self):
        """Transforms the RAW data in JSON format (from the url) into a tabular one by returning a Dataframe"""
        pass
    
    def getNormalizedDataframe(self):
        """Normalization of the RAW Dataframe in order to be ready to be inserted in the Database"""
        pass