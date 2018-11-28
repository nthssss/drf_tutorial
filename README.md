# drf_tutorial
## [Serialization](https://www.django-rest-framework.org/tutorial/1-serialization/)
### [Setting up a new environment](https://www.django-rest-framework.org/tutorial/1-serialization/#setting-up-a-new-environment)
### [Getting started](https://www.django-rest-framework.org/tutorial/1-serialization/#getting-started)
```
python manage.py makemigrations snippets
python manage.py migrate
```
### [Creating a model to work with](https://www.django-rest-framework.org/tutorial/1-serialization/#creating-a-model-to-work-with)
### [Creating a Serializer class](https://www.django-rest-framework.org/tutorial/1-serialization/#creating-a-serializer-class)
### [Working with Serializers](https://www.django-rest-framework.org/tutorial/1-serialization/#working-with-serializers)
```
# ipython shell可以自动补全
pip install ipython 
pip freeze > req.txt
```
```
python manage.py shell
```
```
In [1]: from snippets.models import Snippet                                                                                          

In [2]: from snippets.serializers import SnippetSerializer                                                                           

In [3]: from rest_framework.renderers import JSONRenderer                                                                            

In [4]: from rest_framework.parsers import JSONParser                                                                                

In [5]:                                                                                                                              

In [5]: snippet = Snippet(code='foo = "bar"\n')                                                                                      

In [6]: snippet.save()                                                                                                               

In [7]:                                                                                                                              

In [7]: snippet = Snippet(code='print "hello, world"\n')                                                                             

In [8]: snippet.save()                                                                                                               

In [9]: serializer = SnippetSerializer(snippet)                                                                                      

In [10]: serializer.data                                                                                                             
Out[10]: {'id': 2, 'title': '', 'code': 'print "hello, world"\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}

In [11]: content = JSONRenderer().render(serializer.data)                                                                            

In [12]: content                                                                                                                     
Out[12]: b'{"id":2,"title":"","code":"print \\"hello, world\\"\\n","linenos":false,"language":"python","style":"friendly"}'

In [13]: import io                                                                                                                   

In [14]: stream = io.BytesIO(content)                                                                                                

In [15]: data = JSONParser().parse(stream)                                                                                           

In [16]: serializer = SnippetSerializer(data=data)                                                                                   

In [17]: serializer.is_valid()                                                                                                       
Out[17]: True

In [18]: serializer.validated_data                                                                                                   
Out[18]: 
OrderedDict([('title', ''),
             ('code', 'print "hello, world"'),
             ('linenos', False),
             ('language', 'python'),
             ('style', 'friendly')])

In [19]: serializer.save()                                                                                                           
Out[19]: <Snippet: Snippet object (3)>

In [20]: serializer = SnippetSerializer(Snippet.objects.all(),many=True)                                                             

In [21]: serializer.data                                                                                                             
Out[21]: [OrderedDict([('id', 1), ('title', ''), ('code', 'foo = "bar"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 2), ('title', ''), ('code', 'print "hello, world"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 3), ('title', ''), ('code', 'print "hello, world"'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])]
```
