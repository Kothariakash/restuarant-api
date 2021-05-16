from django.urls import path
from .views import ViewMenu, take_order , book_table, TableDetails


urlpatterns = [
    path("api/v1.0/menu/", ViewMenu.as_view(), name ="get_menu" ),
    path("api/v1.0/orderfood/", take_order, name ='book-order'),
    path("api/v1.0/booktable/", book_table, name ="book-table"),
    path("api/v1.0/tabledetails/", TableDetails.as_view(),name = 'table-details'),
    # path("<str:audioFileType>/<int:pk>/", ListOneAudioFileAPIView.as_view(), name="list1"),
    # path("create/<str:audioFileType>/", CreateAudioFileAPIView.as_view(), name="create"),
    # path("update/<str:audioFileType>/<int:pk>/", UpdateAudioFileAPIView.as_view(), name="update"),
    # path("delete/<str:audioFileType>/<int:pk>/", DeleteAudioFileAPIView.as_view(), name="delete"),
]
