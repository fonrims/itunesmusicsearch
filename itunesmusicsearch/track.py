from itunesmusicsearch import result_item

class Track(result_item.ResultItem):

    def __init__(self, json):
        """
        Initializes the ResultItem class from the JSON provided
        :param json: String. Raw JSON data to fetch information from
        """
        result_item.ResultItem.__init__(self, json)