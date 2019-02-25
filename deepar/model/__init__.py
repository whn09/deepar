# from abc import ABC
#
#
# class NNModel(ABC):
#     def __init__(self):
#         super().__init__()
#
#     def net_structure(self, **kwargs):
#         pass
#
#     def instantiate_and_fit(self, **kwargs):
#         pass

# TODO python2
from abc import ABCMeta


class NNModel(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        super(NNModel, self).__init__()

    def net_structure(self, **kwargs):
        pass

    def instantiate_and_fit(self, **kwargs):
        pass
