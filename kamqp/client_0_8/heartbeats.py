from .exceptions import AMQPRecoverableError


class Heartbeat(object):
    prev_sent = None
    prev_recv = None
    missed = 0

    def __init__(self, connection):
        self.connection = connection
        self.reader = self.connection.method_reader
        self.writer = self.connection.method_writer
        self.setup_timer()

    def close(self):
        self.cancel_timer()

    def setup_timer(self):
        pass

    def cancel_timer(self):
        pass

    def tick(self):
        if self.prev_sent == self.writer.bytes_sent:
            self.writer.send_heartbeat()

        if self.prev_recv == self.reader.bytes_recv:
            self.missed += 1
        else:
            self.missed = 0

        self.prev_sent, self.prev_recv = (self.writer.bytes_sent,
                                          self.reader.bytes_recv)

        if self.missed >= 2:
            raise AMQPRecoverableError("Too many heartbeats missed")

        if connection.heartbeat_checker != self:
            self.close()
