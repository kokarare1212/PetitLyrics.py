import xml.etree.ElementTree as ET
import requests

class PetitLyrics:
  
  @classmethod
  def getNewLyricsList(cls, maxCount: int = 10, raw: bool = False):
    resp = requests.post("https://p1.petitlyrics.com/api/GetNewLyricsList.php",{
      "clientAppId": "p1427608",
      "maxCount": maxCount
    })
    return resp.text if raw else ET.parse(resp.text)

  @classmethod
  def getRankingData(cls, maxCount: int = 10, term: str = "day", raw: bool = False):
    resp = requests.post("https://p1.petitlyrics.com/api/GetNewLyricsList.php",{
      "clientAppId": "p1427608",
      "term": term,
      "maxCount": maxCount
    })
    return resp.text if raw else ET.parse(resp.text)