# Copyright (C) 2007-2008 Barry Pederson <bp@barryp.org>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301

from __future__ import absolute_import


from .serialization import GenericContent

__all__ = ["Message"]


class Message(GenericContent):
    """A Message for use with the ``Channnel.basic_*`` methods.

    :param body: string
    :param children: (not supported)

    Keyword properties may include:

    :keyword content_type: shortstr
        MIME content type

    :keyword content_encoding: shortstr
        MIME content encoding

    :keyword application_headers: table
        Message header field table, a dict with string keys,
        and string | int | Decimal | datetime | dict values.

    :keyword delivery_mode: octet
        Non-persistent (1) or persistent (2)

    :keyword priority: octet
        The message priority, 0 to 9

    :keyword correlation_id: shortstr
        The application correlation identifier

    :keyword reply_to: shortstr
        The destination to reply to

    :keyword expiration: shortstr
        Message expiration specification

    :keyword message_id: shortstr
        The application message identifier

    :keyword timestamp: datetime.datetime
        The message timestamp

    :keyword type: shortstr
        The message type name

    :keyword user_id: shortstr
        The creating user id

    :keyword app_id: shortstr
        The creating application id

    :keyword cluster_id: shortstr
        Intra-cluster routing identifier

    Unicode bodies are encoded according to the ``content_encoding``
    argument. If that's None, it's set to 'UTF-8' automatically.

    *Example*:

    .. code-block:: python

        msg = Message('hello world',
                        content_type='text/plain',
                        application_headers={'foo': 7})

    """

    #: Instances of this class have these attributes, which
    #: are passed back and forth as message properties between
    #: client and server
    PROPERTIES = [
        ("content_type", "shortstr"),
        ("content_encoding", "shortstr"),
        ("application_headers", "table"),
        ("delivery_mode", "octet"),
        ("priority", "octet"),
        ("correlation_id", "shortstr"),
        ("reply_to", "shortstr"),
        ("expiration", "shortstr"),
        ("message_id", "shortstr"),
        ("timestamp", "timestamp"),
        ("type", "shortstr"),
        ("user_id", "shortstr"),
        ("app_id", "shortstr"),
        ("cluster_id", "shortstr")]

    def __init__(self, body='', children=None, **properties):
        super(Message, self).__init__(**properties)
        self.body = body

    def __eq__(self, other):
        """Check if the properties and bodies of this message and another
        message are the same.

        Received messages may contain a :attr:`delivery_info` attribute,
        which isn't compared.

        """
        return (super(Message, self).__eq__(other) and
                hasattr(other, 'body') and
                self.body == other.body)
