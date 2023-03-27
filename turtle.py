class PostOffice:
    """A Post Office class. Allows users to message each other.

    Args:
        usernames (list): Users for which we should create PO Boxes.

    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}
        self.read = 0

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            message_body (str): The body of the message.
            urgent (bool, optional): The urgency of the message.
                                    Urgent messages appear first.

        Returns:
            int: The message ID, auto incremented number.

        Raises:
            KeyError: If the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'read': False,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, n=-1):
        """Read n messages from user username PO box.

         Args:
             username (str): The username whose box to read.
             n (int): The number of messages to read. If nothing is received all
                    the messages will be returned.

         Returns:
             int: The messages that were requested for reading.

         Raises:
             KeyError: If the recipient does not exist.
         """
        if n < 0 or len(msgs := self.boxes[username]) < self.read + n:
            for msg in msgs:
                msg['read'] = True
            self.read = len(msgs)
            return msgs
        else:
            it = iter(msgs)
            msg = next(it)
            ret = []
            while msg['read']:
                msg = next(it)
            for i in range(n):
                msg['read'] = True
                ret.append(msg)
                msg = next(it)
            return ret

    def search_inbox(self, username, string):
        """Read n messages from user username PO box.

         Args:
             username (str): The username whose box to search.
             string (str): The string to be searched.

         Returns:
             int: The messages in which the string appeared.

         Raises:
             KeyError: If the recipient does not exist.
         """
        res = []
        for msg in self.boxes[username]:
            if string in msg['body']:
                res.append(msg)
        return res

    def print_read(self, username):
        """Help function that prints the number of messages the username read."""
        count = 0
        it = iter(self.boxes[username])
        msg = next(it)
        while msg['read']:
            msg = next(it)
            count += 1
        print(count)


def show_example():
    """Show example of using the PostOffice class."""
    users = ('Newman', 'Mr. Peanutbutter')
    post_office = PostOffice(users)
    for i in range(5):
        message_id = post_office.send_message(
            sender='Mr. Peanutbutter',
            recipient='Newman',
            message_body='Hello, Newman.' + str(i),
        )
        print(f"Successfully sent message number {message_id}.")
    print(post_office.boxes['Newman'])
    return post_office


def main():
    post_office = show_example()
    ans = post_office.search_inbox('Newman', "1")
    print(ans)
    msgs = post_office.read_inbox('Newman', 2)
    post_office.print_read('Newman')
    print(msgs)
    msgs = post_office.read_inbox('Newman', 1)
    post_office.print_read('Newman')
    print(msgs)


if __name__ == '__main__':
    main()
