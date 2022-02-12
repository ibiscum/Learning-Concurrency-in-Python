from threading import Lock


def lock_class(_method_names, _lock_factory):
    return lambda cls: make_threadsafe(cls, _method_names, _lock_factory)


def lock_method(method):
    if getattr(method, '__is_locked', False):
        raise TypeError("Method %r is already locked!" % method)

    def locked_method(self, *arg, **kwarg):
        with self._lock:
            return method(self, *arg, **kwarg)

    locked_method.__name__ = '%s(%s)' % ('lock_method', method.__name__)
    locked_method.__is_locked = True
    return locked_method


def make_threadsafe(cls, method_names, lock_factory):
    init = cls.__init__

    def new_init(self, *arg, **kwarg):
        init(self, *arg, **kwarg)
        self._lock = lock_factory()

    cls.__init__ = new_init

    for method_name in method_names:
        old_method = getattr(cls, method_name)
        new_method = lock_method(old_method)
        setattr(cls, method_name, new_method)

    return cls


@lock_class(['add', 'remove'], Lock)
class ClassDecoratorLockedSet(set):

    @lock_method  # if you double-lock a method, a TypeError is raised
    def locked_method(self):
        print("This section of our code would be thread safe")
        pass
