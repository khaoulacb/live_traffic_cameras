from .normalize_source import NormalizeSource
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import logging as log
import requests


class NormalizeAndorra(NormalizeSource):

    def __init__(self):
       NormalizeSource.__init__(self, "andorra")

    def _getRawData(self):
        """Loads the data in JSON format from a source URL"""
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
        url = self.source.url
        try:
            response = requests.get(url, headers=headers)
            data = response.json()
            return data
        except Exception:
            log.error(f"Problem fetching data from URL {url}")
            return None

    def _getRawDataframe(self):
        """Transforms the RAW data in JSON format (from the url) into a tabular one by returning a Dataframe"""
        data = self._getRawData()

        if data is None:
            log.warning("Raw JSON data is None")
            return None
        else:
            try:
                data = data["result"]
                df = pd.json_normalize(data)
                return df
            except Exception:
                log.error("Problem with data format.")
                return None
    
    def getNormalizedDataframe(self):
        """Normalization of the RAW Dataframe in order to be ready to be inserted in the Database"""
        data = self._getRawDataframe()

        if data is None:
            log.warning("Raw Dataframe is None")
            return None
        else:
            try:
                fields = ["id", "url_gif", "title", "lat", "lng"]
                df = data[fields]
                df.rename(columns= {"id": "camera_id", "url_gif": "url_image", "title": "location_info", "lat": "latitude", "lng": "longitude"}, inplace=True)

                return df
                
            except Exception:
                log.error("Problem with dataframe format.")
                return None