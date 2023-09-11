"""
URL configuration for clickerAlentejo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clicker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.nova_pagina, name='nova_pagina'),
    path('configurations/', views.configurations, name='configurations'),
    path('addContador/', views.addContador, name='addContador'),
    path('add_periodo/', views.add_periodo, name='add_periodo'),
    path('add_pergunta/', views.add_pergunta, name='add_pergunta'),
    path('getCliques/', views.getCliques, name='getCliques'),
    path('elimina_ultimo_valor/', views.elimina_ultimo_valor, name='elimina_ultimo_valor'),
    path('getPerguntas/', views.getPerguntas, name='getPerguntas'),
    path('download_excel_all_final_dia/', views.download_excel_all_final_dia, name='download_excel_all_final_dia'),



    #rotas para pagina das compras
    path('home_registo_compras/', views.home_registo_compras, name='home_registo_compras'),
    path('add_compra/', views.add_compra, name='add_compra'),
    path('get_dados_fatura/', views.get_dados_fatura, name='get_dados_fatura'),
    path('fechar_contas1/', views.fechar_contas1, name='fechar_contas1'),
    path('fechar_contas/', views.fechar_contas, name='fechar_contas'),
    path('elimina_fatura/', views.elimina_fatura, name='elimina_fatura'),
    path('edita_fatura/', views.edita_fatura, name='edita_fatura'),
    path('fechar_contas/', views.fechar_contas, name='fechar_contas'),

]
