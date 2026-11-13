"""HW11 Question 2: Iterable and Iterator

Your task is to implement the EmailsInStringIterator so that an instance of EmailsInString
can be iterated over (like it is in main() below).

The _set_next_email() method should set the instance variable called self._next_email.
If there are no more email addresses left in the string, self._next_email should be set to None.

The __next__() method should return the next email address (stored in self._next_email) and
call _set_next_email() to prepare self._next_email for the next time __next__() is called.
If self._next_email is None, __next__() should raise StopIteration.

Make sure to write tests in the tests directory.
"""

from typing import Iterable, Iterator

class EmailsInString(Iterable[str]):
    """Iterable over email addresses in a string."""
    def __init__(self, content: str) -> None:
        self._content = content

    def __iter__(self) -> Iterator[str]:
        return EmailsInStringIterator(self._content)

class EmailsInStringIterator(Iterator[str]):
    """Iterator over email addresses in a string."""
    def __init__(self, content: str) -> None:
        self._contents = content.split()
        self._set_next_email()

    def _set_next_email(self) -> None:
        # TODO: Set the next email address from the remaining contents
        # If there are no more email addresses, set self._next_email to None
        # A word is an email address if it contains the '@' character
        pass

    def __next__(self) -> str:
        # TODO: Return the next email address and prepare the next one
        # If there are no more email addresses, raise StopIteration
        pass

def main() -> None:
    """Main function to demonstrate EmailsInString iterable."""
    emails = EmailsInString('Emails: puff@example.com fluff@example.org floof@example.net')
    for email in emails:
        print(email)

if __name__ == '__main__':
    main()
