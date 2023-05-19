from pika.exceptions import (
    AMQPChannelError,
    AMQPConnectionError,
    AMQPError,
    AuthenticationError,
    ChannelClosed,
    ChannelClosedByBroker,
    ChannelClosedByClient,
    ChannelError,
    ChannelWrongStateError,
    ConnectionBlockedTimeout,
    ConnectionClosed,
    ConnectionClosedByBroker,
    ConnectionClosedByClient,
    ConnectionOpenAborted,
    ConnectionWrongStateError,
    ProbableAccessDeniedError,
    ProbableAuthenticationError,
    StreamLostError,
)

AMQP_CHANNEL_AND_CONNECTION_ERRORS = [
    AMQPError,
    AMQPChannelError,
    AMQPConnectionError,
    ChannelClosed(reply_code=0, reply_text=""),
    AuthenticationError,
    ChannelClosedByBroker(reply_code=0, reply_text=""),
    ChannelClosedByClient(reply_code=0, reply_text=""),
    ChannelError(),
    ChannelWrongStateError,
    ConnectionBlockedTimeout,
    ConnectionClosed(reply_code=0, reply_text=""),
    ConnectionClosedByBroker(reply_code=0, reply_text=""),
    ConnectionClosedByClient(reply_code=0, reply_text=""),
    ConnectionOpenAborted,
    ConnectionWrongStateError,
    ProbableAccessDeniedError,
    ProbableAuthenticationError,
    StreamLostError,
]