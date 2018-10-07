import logging
import os
import time

class KassertObject(object):

    def is_of_types(self, obj, the_types):
        '''
        :param obj: object to assert
        :param the_types: iterable of types, or a signle type
        :raise: an exception if obj is not an instance of types
        '''
        if not isinstance(obj, the_types):
            raise Exception('object type (%s) is not one of (%s)' % (type(obj), the_types))

    def is_int(self, obj):
        '''
        :param obj: object to assert
        :raise: an exception if obj is not an int type
        '''
        self.is_of_types(obj, int)

    def is_in(self, obj, it):
        '''
        :param obj: object to assert
        :param it: iterable of elements we assert obj is in
        :raise: an exception if obj is in an iterable
        '''
        if obj not in it:
            raise Exception('(%s) is not in %s' % (obj, it))


    def not_none(self, obj):
        '''
        :param obj: object to assert
        :raise: an exception if obj is not None
        '''
        if obj is None:
            raise Exception('object is None')

def kassert():
    return KassertObject()

def khash(*args):
    '''
    hash arguments. khash handles None in the same way accross runs (which is good :))
    '''
    ksum = sum([hash(arg if arg is not None else -13371337) for arg in args])
    return hash(str(ksum))


class KittyObject(object):
    '''
    Basic class to ease logging and description of objects.
    '''

    _logger = None
    log_file_name = './kittylogs/kitty_%s.log' % (time.strftime("%Y%m%d-%H%M%S"),)

    @classmethod
    def get_logger(cls):
        '''
        :return: the class logger
        '''
        if KittyObject._logger is None:
            logger = logging.getLogger('kitty')
            logger.setLevel(logging.INFO)
            consolehandler = logging.StreamHandler()
            console_format = logging.Formatter('[%(levelname)-8s][%(module)s.%(funcName)s] %(message)s')
            consolehandler.setFormatter(console_format)
            logger.addHandler(consolehandler)
            if not os.path.exists('./kittylogs'):
                os.mkdir('./kittylogs')
            filehandler = logging.FileHandler(KittyObject.log_file_name)
            file_format = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(module)s.%(funcName)s] -> %(message)s')
            filehandler.setFormatter(file_format)
            logger.addHandler(filehandler)
            KittyObject._logger = logger
        return KittyObject._logger

    @classmethod
    def get_log_file_name(cls):
        '''
        :return: log file name
        '''
        return KittyObject.log_file_name

    @classmethod
    def set_verbosity(cls, verbosity):
        '''
        Set verbosity of logger

        :param verbosity: verbosity level. currently, we only support 1 (logging.DEBUG)
        '''
        if verbosity > 0:
            # currently, we only toggle between INFO, DEBUG
            logger = KittyObject.get_logger()
            levels = [logging.DEBUG]
            verbosity = min(verbosity, len(levels)) - 1
            logger.setLevel(levels[verbosity])

    def __init__(self, name, logger=None):
        '''
        :param name: name of the object
        '''
        self.name = name
        if logger:
            self.logger = logger
        else:
            self.logger = KittyObject.get_logger()

    def not_implemented(self, func_name):
        '''
        log access to unimplemented method and raise error

        :param func_name: name of unimplemented function.
        :raise: NotImplementedError detailing the function the is not implemented.
        '''
        msg = '%s is not overridden by %s' % (func_name, type(self).__name__)
        self.logger.error(msg)
        raise NotImplementedError(msg)

    def get_description(self):
        '''
        :rtype: str
        :return: the description of the object. by default only prints the object type.
        '''
        return type(self).__name__

    def get_name(self):
        '''
        :rtype: str
        :return: object's name
        '''
        return self.name
