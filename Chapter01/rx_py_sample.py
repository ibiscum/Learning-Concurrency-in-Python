""" Learning Concurrency in Python - Chapter 01 - rx Python sample """
# from rx import Observable


# Here we define our custom observer which
# contains an on_next method, an on_error method
# and an on_completed method
from rx import Observable


class TemperatureObserver(Observable):
    """ Observing temperature. """

    # Every time we receive a temperature reading
    # this method is called
    @classmethod
    def on_next(cls, x_v):
        """ Next temperature. """
        print("Temperature is: %s degrees centigrade" % x_v)
        if x_v > 6:
            print("Warning: Temperate Is Exceeding Recommended Limit")
        if x_v == 9:
            print("DataCenter is shutting down. Temperature is too high")

    @classmethod
    def on_error(cls, e_v):
        """ If we were to receive an error message, we would handle it here """
        print("Error: %s" % e_v)

    @classmethod
    def on_completed(cls):
        """ This is called when the stream is finished """
        print("All Temps Read")


# Publish some fake temperature readings
# xs = Observable.from_iterable(range(10))
# xs = Observable.pipe(range(10))

# subscribe to these temperature readings
# d = xs.subscribe(TemperatureObserver())
