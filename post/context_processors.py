# myapp/context_processors.py
from .models import TextAsset


def global_site_data(request):
    copyright = TextAsset.objects.filter(asset_type="copyright").first()
    default_copyright = (
        '© 2024 Copyright - <a class="text-body">Marcus Lertkomolsuk</a>'
    )

    return {"copyright_text": copyright.content if copyright else default_copyright}
