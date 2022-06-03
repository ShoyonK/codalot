from Knight import Knight

class KingArthur(Knight):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__name = "King Arthur"
