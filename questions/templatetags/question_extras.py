from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('scripts.html')
def load_scripts():
    if settings.DEBUG:
        scripts = (
            '/static/lib/angular/angular.min.js',
            '/static/lib/angular-route/angular-route.min.js',
            '/static/lib/angular-bootstrap/ui-bootstrap-tpls.min.js',
            '/static/lib/MathJax/MathJax.js?config=TeX-AMS-MML_HTMLorMML',
            '/static/lib/moment/moment.js',
        )
    else:
        scripts = {
            'https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.3/angular.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.3/angular-route.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/angular-ui-bootstrap/0.13.1/ui-bootstrap-tpls.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.10.3/moment.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.5.3/MathJax.js'
        }
    return {'scripts': scripts}
