# pylint: disable=E1120, C0103
from __future__ import absolute_import
from django.conf.urls import url
from django.views.generic import TemplateView
from games.views import pages as views


urlpatterns = [
    url(r'^$',
        views.GameList.as_view(),
        name='game_list'),
    url(r'^year/(\d+)/$',
        views.GameListByYear.as_view(),
        name='games_by_year'),
    url(r'^genre/([\w-]+)/$',
        views.GameListByGenre.as_view(),
        name='games_by_genre'),
    url(r'^by/([\w-]+)/$',
        views.GameListByCompany.as_view(),
        name='games_by_company'),
    url(r'^platform/(?P<slug>[\w\-]+)/$',
        views.GameListByPlatform.as_view(),
        name="games_by_plaform"),
    url(r'^publish/(?P<id>\d+)$',
        views.publish_game,
        name='game-publish'),
    url(r'^add-game/$',
        views.submit_game,
        name='game-submit'),
    url(r'^game-submitted',
        TemplateView.as_view(template_name='games/submitted.html'),
        name="game-submitted"),

    url('^game-issue',
        views.submit_issue,
        name='game-submit-issue'),
    url(r'banner/(?P<slug>[\w\-]+).jpg',
        views.get_banner,
        name='get_banner'),
    url(r'icon/(?P<slug>[\w\-]+).png',
        views.get_icon,
        name='get_icon'),
    url(r'install/(?P<id>[\d]+)/view$',
        views.view_installer,
        name='view_installer'),
    url(r'install/(?P<id>[\d]+)/fork$',
        views.fork_installer,
        name='fork_installer'),

    # Deprecated! Remove after 0.5.0 release!
    url(r'install/(?P<slug>[\w\-]+)/$',
        views.get_installers,
        name='get_installers'),

    url(r'(?P<slug>[\w\-]+)/installer/new/$',
        views.new_installer,
        name="new_installer"),
    url(r'(?P<slug>[\w\-]+)/installer/edit/$',
        views.edit_installer,
        name='edit_installer'),
    url(r'(?P<slug>[\w\-]+)/installer/delete$',
        views.delete_installer,
        name='delete_installer'),
    url(r'(?P<slug>[\w\-]+)/installer/publish/$',
        views.publish_installer,
        name='publish_installer'),
    url(r'(?P<slug>[\w\-]+)/installer/complete/$',
        views.installer_complete,
        name='installer_complete'),
    url(r'installer/feed/$',
        views.InstallerFeed(),
        name='installer_feed'),
    url(r'installer/submissions$',
        views.installer_submissions,
        name='installer_submissions'),
    url(r'installer/review/(?P<slug>[\w\-]+)$',
        views.installer_review,
        name='installer_review'
        ),
    url(r'([\w\-]+)/screenshot/add/',
        views.screenshot_add,
        name='screenshot_add'),
    url(r'screenshot/(?P<id>\d+)/publish/$',
        views.publish_screenshot,
        name='publish_screenshot'),

    url(r'game-for-installer/(?P<slug>[\w\-]+)/',
        views.game_for_installer,
        name='game_for_installer'),
    url(r'(?P<slug>[\w\-]+)/$',
        views.game_detail,
        name="game_detail"),
]
