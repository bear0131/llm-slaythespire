def logTitle(message: str) -> None:
    totalLength = 80
    paddingL = (totalLength - len(message) - 2) // 2
    paddingR = (totalLength - len(message) - 2 + 1) // 2
    paddedMessage = ('=' * paddingL) + ' ' + message + ' ' + ('=' * paddingR)
    print(paddedMessage)
