from django.test import TestCase
from .models import Book

# Create your tests here.
class BookModelTest(TestCase):
    # set up objects that will not change during the test
    def setUpTestData():
        Book.objects.create(name='Pride and Prejudice',
                            author_name='Jane Austen',
                            genre='classic',
                            book_type='hardcover',
                            price='23.71')

    # Test to see if book's name is initialized as expected
    def test_book_name(self):
        # Get book object to test
        book = Book.objects.get(id=1)
        # Get metadata for the name field
        field_label = book._meta.get_field('name').verbose_name
        # Compare the value to the expected result
        self.assertEqual(field_label, 'name')

    # Test to see if author name max length is working
    def test_author_name_max_length(self):
        # Get a book object to test
        book = Book.objects.get(id=1)
        # Get metadata for author_name field and query its max length
        max_length = book._meta.get_field('author_name').max_length
        # Compare the value to the expected result
        self.assertEqual(max_length, 100)

    