# import os

# os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_app.settings')

# import django
# django.setup()

# # Fake pop scripts
# import random

# from django_app.models import AcceessRecord,Topic,Webpage
# from faker import Faker

# faker=Faker()

# topics=['Search','Social','Marketplace','News','Games']

# def add_topic():
#     t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t

# def populate(N=5):
#     for entry in range(N):
#         top=add_topic()

#         fake_url=faker.url()
#         fake_date=faker.date()
#         fake_name=faker.company()

#         w=Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]
#         ar=AcceessRecord.objects.get_or_create(name=w,date=fake_date)[0]

# if __name__=='__main__':    
#     print('populating script')
#     populate(20)
#     print('polulating complete!')