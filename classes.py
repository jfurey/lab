class Television:
    '''
    A class representing details for a television object.
    '''
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        '''
        Constructor to set the default state of the TV.
        '''
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__status: bool = False

    def power(self) -> None:
        '''
        Method to turn the TV on/off.
        '''
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def channel_up(self) -> None:
        '''
        Method to turn the TV channel up.
        '''
        if self.__status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        '''
        Method to turn the TV channel down.
        '''
        if self.__status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        '''
        Method to turn the TV volume up.
        '''
        if self.__status == True:
            if self.__volume != Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        Method to turn the TV volume down.
        '''
        if self.__status == True:
            if self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        Method to return the TV status in regard to on/off, channel, and volume.
        '''
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'