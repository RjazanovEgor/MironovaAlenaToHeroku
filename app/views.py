from django.shortcuts import render

# Для показа файла
from .models import Articles, ShowArticle, AboutCompany, OurAdvantages,\
                    OurServices, ClientsAboutUs, MainInform, AboutCompanyPoints

# Отправка сообщения
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from vizitka.settings import DEFAULT_TO_EMAIL, DEFAULT_FROM_EMAIL


def index(request):
    articles = Articles.objects.all()
    show_articles = ShowArticle.objects.all()
    about_company = AboutCompany.objects.all()
    about_company_points = AboutCompanyPoints.objects.all()
    our_advantages = OurAdvantages.objects.all()
    our_services = OurServices.objects.all()
    clients_about_us = ClientsAboutUs.objects.all()
    main_inform = MainInform.objects.all()
    list0 = []
    for i in range(1, len(articles) + 1):
        list0.append(str(i))
    list1 = []
    for i in range(1, len(show_articles) + 1):
        list1.append([str(i), show_articles[i - 1]])
    print(list1)
    print(main_inform)
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            messages = name + '\n' + phone + '\n' + message
            try:
                send_mail(f'{"Заявка с сайта"} от {from_email}', messages,
                          DEFAULT_FROM_EMAIL, DEFAULT_TO_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return render(request, 'app/base.html', {
                'about_company': about_company,
                'about_company_points': about_company_points,
                'our_advantages': our_advantages,
                'our_services': our_services,
                'clients_about_us': clients_about_us,
                'main_inform': main_inform,
                'articles': articles,
                'show_articles': show_articles,
                'count_articles': len(articles),
                'list0': list0,
                'list1': list1,
                'form': ContactForm()

            })
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, 'app/base.html', {
                            'about_company': about_company,
                            'about_company_points': about_company_points,
                            'our_advantages': our_advantages,
                            'our_services': our_services,
                            'clients_about_us': clients_about_us,
                            'main_inform': main_inform,
                            'articles': articles,
                            'show_articles': show_articles,
                            'count_articles': len(articles),
                            'list0': list0,
                            'list1': list1,
                            'form': form
    })
