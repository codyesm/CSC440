import pypandoc
from config import CONTENT_DIR


output = pypandoc.convert_file(CONTENT_DIR + '/rules.md', 'docx', outputfile=CONTENT_DIR + '/convertTest.docx')
assert output == ""