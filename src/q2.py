"""HW11 Question 2: Iterable and Iterator

Your task is to implement the EmailsInStringIterator so that an instance of EmailsInString
can be iterated over (like it is in main() below).

The _set_next_email() method and the `__next__()` method should work together to allow iterating 
over email addresses. A word is an email address if it contains the '@' character

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
        pass

    def __next__(self) -> str:
        pass

def main() -> None:
    """Main function to demonstrate EmailsInString iterable."""
    emails = EmailsInString('Emails: puff@example.com fluff@example.org floof@example.net')
    for email in emails:
        print(email)

if __name__ == '__main__':
    main()
