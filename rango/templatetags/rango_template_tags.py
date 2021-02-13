from django import template
from rango.models import Category 

register = template.Library()


# This method returns a list of categories - 
# but is mashed up with the template 'rango/cats.html'

#@register.inclusion_tag('rango/cats.html')
def get_category_list(max_result=0, starts_with=''):
    cat_list = []
    if starts_with:
        cat_list = Category.objects.filter(name__istartswith=starts_with)

        if max_results > 0:
            if len(cat_list) > max_results:
                cat_list = cat_list[:max_results]
        return cat_list

    #return {'cats': Category.objects.all(), 'act_cat': cat}

