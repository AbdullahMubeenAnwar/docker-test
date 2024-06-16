import sparknlp
from sparknlp.pretrained import PretrainedPipeline

spark = sparknlp.start()

testDoc = '''
Peter is a very good persn.
My life in Russia is very intersting.
John and Peter are brthers. However they don't support each other that much.
Lucas Dunbercker is no longer happy. He has a good car though.
Europe is very culture rich. There are huge churches! and big houses!
'''

pipeline = PretrainedPipeline('explain_document_ml', lang='en')


result = pipeline.annotate(testDoc)
print(result['sentence'])