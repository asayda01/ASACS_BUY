from django.urls import path, include
from django.contrib import admin
from Users.views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('authentication/', include('Users.urls')),
    path('login/', LoginView.as_view()),
    path('users/', UserList, name='user-list'),
    #path('users/<pk>/', UserDetails),
    #path('view/', api_list_auctions),
    #path('auctions/', api_auction),
    path('bid/', api_bid, name='bid'),
    path('search/', api_search_items.as_view(), name='browse-items'),
    path('create/', api_create_auc, name='post-item'),
    path('detail/<str:somebody>', get_item_detail_of_somebody, name='detail-item'),
    path('wins/', get_wins_items, name='win-items'),
    path('sold/', get_sold_items, name='sold-items'),
    path('history/<str:item>', get_sold_item_history, name='sold-item-history'),
    path('task/', include('schedulejobs.urls')),
    ]
    