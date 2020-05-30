from django.shortcuts import render, redirect

from django.views.generic.edit import FormView
from search.forms import PostSearchForm
from django.db.models import Q

# from BBB.model import ReadingRecord # 이따가 BBB 모델하고 연결할 때!
from .models import Post
import pdb
# pdb.set_trace()

def search(request):
    q = request.GET.get('q') or ""
    
    post_list = Post.objects.filter(
            Q(title__icontains=q) | Q(content__icontains=q)
        ).distinct()
    return render(request, 'searchPage.html', {"q": q})

# class SearchFormView(FormView):
#     form_class = PostSearchForm
#     template_name ='search/searchPage.html'

#     def form_valid(self, form):
#         schWord = '%s' % self.request.POST['search_word']
#         post_list = Post.objects.filter(
#             Q(title__icontains=schWord) | Q(content__icontains=schWord)
#         ).distinct()

#         context = {}
#         context['form'] = form
#         context['search_term'] = schWord
#         context['object_list'] = post_list

#         return render(self.request, self.template_name, context)