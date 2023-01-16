from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Tune


class TuneList(generic.ListView):
    model = Tune()
    queryset = Tune.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class TuneDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Tune.objects.filter(status=1)
        tune = get_object_or_404(queryset, slug=slug)
        comments = tune.comments.filter(approved=True).order_by('created_on')
        liked = False
        if tune.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "tune_detail.html",
            {
                "tune": tune,
                "comments": comments,
                "liked": liked
            },
        )
