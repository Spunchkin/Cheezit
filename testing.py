import os
import shutil
import tempfile
import unittest
from search import search_files, search_files_by_name, search_files_by_size, get_unique_file_extensions

class TestFileSearchFunctions(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()

        # Create some test files in the temporary directory
        test_file_paths = [
            os.path.join(self.test_dir, 'file1.txt'),
            os.path.join(self.test_dir, 'file2.txt'),
            os.path.join(self.test_dir, 'image1.jpg'),
            os.path.join(self.test_dir, 'document.docx'),
            os.path.join(self.test_dir, 'subdir', 'file3.txt'),
        ]

        for path in test_file_paths:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w') as f:
                f.write("Test content")

    def test_search_files(self):
        result = search_files(self.test_dir, '.txt')
        expected_result = [
            os.path.join(self.test_dir, 'file1.txt'),
            os.path.join(self.test_dir, 'file2.txt'),
            os.path.join(self.test_dir, 'subdir', 'file3.txt'),
        ]
        self.assertCountEqual(result, expected_result)

    def test_search_files_by_name(self):
        result = search_files_by_name(self.test_dir, 'file')
        expected_result = [
            os.path.join(self.test_dir, 'file1.txt'),
            os.path.join(self.test_dir, 'file2.txt'),
            os.path.join(self.test_dir, 'subdir', 'file3.txt'),
        ]
        self.assertCountEqual(result, expected_result)

    def search_files_by_size(self):
        result = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                try:
                    size = os.stat(os.path.join(root, file)).st_size
                    if size > size_greaterthan and size < size_lessthan:
                        result.append(os.path.join(root, file))
                except FileNotFoundError:
                    # Handle the case where the file is not found
                    pass
        return result


    def test_get_unique_file_extensions(self):
        result = get_unique_file_extensions(self.test_dir)
        expected_result = {'.txt', '.jpg', '.docx'}
        self.assertEqual(result, expected_result)

    def tearDown(self):
        # Remove the temporary directory and its contents
        shutil.rmtree(self.test_dir)

if __name__ == '__main__':
    unittest.main()
