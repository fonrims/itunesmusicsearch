from itunesmusicsearch import result_item

class Track(result_item.ResultItem):

    def __init__(self, json):
        """
        Initializes the ResultItem class from the JSON provided
        :param json: String. Raw JSON data to fetch information from
        """
        result_item.ResultItem.__init__(self, json)

    def get_track_url(self):
        """
        Retrieves the track's length and converts it to minutes
        :return: Int. Track length in minutes
        """
        return self.trackViewUrl