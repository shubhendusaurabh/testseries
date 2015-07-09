from django.conf.urls import patterns, url

urlpatterns = patterns('questions.views',
    url(
        regex=r'(?P<pk>\d+)/$',
        view='question_detail',
        name='question_detail'
    ),
    url(
        regex=r'^$',
        view='question_list',
        name='question_list'
    ),
)
