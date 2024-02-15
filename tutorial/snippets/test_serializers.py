from django.test import TestCase
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

class SnippetSerializerTestCase(TestCase):
    def setUp(self):
        self.snippet_data = {
            'title': 'Test Snippet',
            'code': 'print("Hello, World!")',
            'linenos': True,
            'language': 'python',
            'style': 'friendly'
        }
        self.serializer = SnippetSerializer()

    def test_create_snippet(self):
        serializer = SnippetSerializer(data=self.snippet_data)
        self.assertTrue(serializer.is_valid())
        snippet = serializer.save()
        self.assertIsInstance(snippet, Snippet)
        self.assertEqual(snippet.title, self.snippet_data['title'])
        self.assertEqual(snippet.code, self.snippet_data['code'])
        self.assertEqual(snippet.linenos, self.snippet_data['linenos'])
        self.assertEqual(snippet.language, self.snippet_data['language'])
        self.assertEqual(snippet.style, self.snippet_data['style'])

    def test_update_snippet(self):
        snippet = Snippet.objects.create(**self.snippet_data)
        updated_data = {
            'title': 'Updated Snippet',
            'code': 'print("Updated Hello, World!")',
            'linenos': False,
            'language': 'python',
            'style': 'friendly'
        }
        serializer = SnippetSerializer(instance=snippet, data=updated_data)
        self.assertTrue(serializer.is_valid())
        updated_snippet = serializer.save()
        self.assertEqual(updated_snippet.title, updated_data['title'])
        self.assertEqual(updated_snippet.code, updated_data['code'])
        self.assertEqual(updated_snippet.linenos, updated_data['linenos'])
        self.assertEqual(updated_snippet.language, updated_data['language'])
        self.assertEqual(updated_snippet.style, updated_data['style'])