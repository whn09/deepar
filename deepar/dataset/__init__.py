# from abc import ABC
#
#
# class Dataset(ABC):
#     def __init__(self):
#         super().__init__()
#
#     def next_batch(self, **kwargs):
#         pass

# TODO python2
from abc import ABCMeta


class Dataset(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        super(Dataset, self).__init__()

    def next_batch(self, **kwargs):
        pass
