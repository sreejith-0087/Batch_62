# a destructors is used to destroy the object and perform the final clean up.


class MnM:

    def __init__(self):
        print('Object Creation')

    def __del__(self):
        print('Object Destroy')

b = MnM()
del b
