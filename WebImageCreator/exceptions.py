def ExceptionFactory(exception_name: str):

  class BusinessException(Exception):
    def __init__(self, message: str):
      self.__class__.__name__ = exception_name
      super().__init__(message)
    
  return BusinessException


ComponentPathException = ExceptionFactory('ComponentPathException')
ComponentDirectoryException = ExceptionFactory('ComponentDirectoryException')
ComponentFileException = ExceptionFactory('ComponentFiles')


