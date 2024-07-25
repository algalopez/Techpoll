from src.poll.domain.poll_model import Poll
from src.poll.infrastructure import poll_dao
from uuid import UUID


def run(poll: UUID, key: str) -> Poll:
    """
    Get score for a poll and a user

    :param poll: The poll uuid
    :param key: The user key
    :return: The list
    """
    return poll_dao.get_poll(poll_uuid=poll)
    # return PollResults(poll_uuid=poll, key=key)
