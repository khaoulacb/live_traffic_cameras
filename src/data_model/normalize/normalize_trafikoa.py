from .normalize_source import NormalizeSource
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import logging as log
import requests


class NormalizeTrafikoa(NormalizeSource):

    def __init__(self):
       NormalizeSource.__init__(self, "trafikoa")

    def _getRawData(self, url):
        """Loads the data in JSON format from a source URL"""
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
        try:
            response = requests.get(url, headers=headers)
            data = response.json()          
            return data
        except Exception:
            log.error(f"Problem fetching data from URL {url}")
            return None


    def _getRawDataframe(self):
        """Transforms the RAW data in JSON format (from the url) into a tabular one by returning a Dataframe"""
        url = self.source.url
        data = self._getRawData(url)
        if data is None:
            log.warning("Raw JSON data is None")
            return None
        else:
            try:
                list_cameras = []
                range_pages = data["totalPages"] + 1
                for i in range(1, range_pages):
                    current_url = url[:-1]+str(i)
                    current_data = self._getRawData(current_url)
                    current_data = current_data["cameras"]
                    list_cameras.extend(current_data)
                data = list_cameras
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
                fields = ["cameraId", "cameraName", "urlImage", "road", "kilometer", "address", "latitude", "longitude"]
                df = data[fields]
                df.rename(columns = {"cameraId": "camera_id", "cameraName": "name", "urlImage": "url_image", "kilometer": "km", "address": "location_info"}, inplace=True)
                return df
                
            except Exception:
                log.error("Problem with dataframe format.")
                return None