# Adding a model

Add a model thing:
It's mostly copy-paste

1. Create a model in `models.py`
2. Run migrations
3. Create a serializer in `serializers.py`. Only put in fields that should be available in frontend (i.e: dont send password to frontend)
4. Create a viewset in `views.py`
5. Register in `urls.py`
