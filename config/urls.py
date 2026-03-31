from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Book.views import home, BookListView, BookCreateView, BookUpdateView, BookDeleteView
from config import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(

    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('list/', BookListView.as_view(), name='list'),
    path('create/', BookCreateView.as_view(), name='create'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='delete'),

    path('accounts/', include('accounts.urls')),
    path('file/', include('file.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('rosetta/', include('rosetta.urls'), ),
    # path('savollar/', include('savollar.urls')),

)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
