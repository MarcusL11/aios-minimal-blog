from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from itertools import zip_longest
from .models import Post, Tag, TextAsset
from django.db.models import Prefetch


def post_list(request):
    posts = Post.objects.filter(is_index_post=False).order_by("-pub_date")
    tags = Tag.objects.all()
    search_query = request.GET.get("q", "")

    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) | Q(tag__name__icontains=search_query)
        )

    logo_asset = TextAsset.objects.filter(asset_type="logo").first()
    copyright_asset = TextAsset.objects.filter(asset_type="copyright").first()

    context = {
        "posts": posts,
        "tags": tags,
        "search_query": search_query,
        "logo_asset": logo_asset,
        "copyright_asset": copyright_asset,
    }

    return render(request, "post/post_list.html", context)


def post_detail(request, post_id):
    post = get_object_or_404(Post.objects.prefetch_related("category"), pk=post_id)
    tags = Tag.objects.all()

    # Fetch text assets
    logo_asset = TextAsset.objects.filter(asset_type="logo").first()
    copyright_asset = TextAsset.objects.filter(asset_type="copyright").first()

    context = {
        "post": post,
        "tags": tags,
        "logo_asset": logo_asset,
        "copyright_asset": copyright_asset,
    }

    return render(request, "post/post_detail.html", context)


def blog_index(request):
    latest_posts = (
        Post.objects.filter(is_index_post=False)
        .order_by("-pub_date")
        .prefetch_related("category")
    )[:3]

    try:
        special_post = Post.objects.get(is_index_post=True)
    except Post.DoesNotExist:
        special_post = None

    logo_asset = TextAsset.objects.filter(asset_type="logo").first()
    copyright_asset = TextAsset.objects.filter(asset_type="copyright").first()

    context = {
        "special_post": special_post,
        "logo_asset": logo_asset,
        "copyright_asset": copyright_asset,
        "latest_posts": latest_posts,
    }
    return render(request, "post/blog_index.html", context)


def about(request):
    latest_posts = (
        Post.objects.filter(is_index_post=False)
        .order_by("-pub_date")
        .prefetch_related("category")
    )[:3]

    try:
        special_post = Post.objects.get(is_index_post=True)
    except Post.DoesNotExist:
        special_post = None

    logo_asset = TextAsset.objects.filter(asset_type="logo").first()
    copyright_asset = TextAsset.objects.filter(asset_type="copyright").first()

    context = {
        "special_post": special_post,
        "logo_asset": logo_asset,
        "copyright_asset": copyright_asset,
        "latest_posts": latest_posts,
    }

    return render(request, "post/about.html", context)


def build_in_public(request):
    # Fetch the 'Build in Public' tag
    build_in_public_tag = Tag.objects.get(name="Build in Public")

    # Fetch posts with the 'Build in Public' tag and order by publication date
    build_in_public_posts = (
        Post.objects.filter(tag=build_in_public_tag)
        .order_by("-pub_date")
        .prefetch_related("category")
    )

    # Group the posts in pairs
    def pairwise(iterable):
        a = iter(iterable)
        return zip_longest(a, a)

    paired_posts = list(pairwise(build_in_public_posts))

    context = {"paired_posts": paired_posts}

    return render(request, "post/build_in_public.html", context)
