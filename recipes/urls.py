from django.urls import path
from .views import site
from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', site.RecipeListViewHome.as_view(), name="home"),  # Home
    path(
        'recipes/search/',
        site.RecipeListViewSearch.as_view(), name="search"
    ),
    path(
        'recipes/category/<int:category_id>/',
        site.RecipeListViewCategory.as_view(), name="category"
    ),

    path('recipes/<int:pk>/', site.RecipeDetail.as_view(), name="recipe"),

    path('recipes/api/v1/<int:pk>/', site.RecipeDetailAPI.as_view(),
         name="recipes_ap1_v1_detail"),

    path('recipes/api/v1/', site.RecipeListViewHomeApi.as_view(),
         name="recipes_api_v1"),

    path('recipes/theory/', site.theory, name='theory',),

    path(
        'recipes/tags/<slug:slug>/',
        site.RecipeListViewTag.as_view(),
        name="tag"
    ),
    path('recipes/api/v2/', views.recipe_api_list, name='recipes_api_v2'),
    path('recipes/api/v2/<int:pk>', views.recipe_api_detail, name='recipes_api_v2_detail'),  # noqa
    path('recipes/api/v2/tag/<int:pk>', views.tag_api_detail, name='recipes_api_v2_tag'),  # noqa




]
