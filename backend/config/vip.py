import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

ALLOWED_ORIGINS = {"http://localhost:5173", "http://127.0.0.1:5173"}

PROFILE = {
    "name": "Аркадий Бесполезный",
    "height": 182,
    "nationality": "Землянин",
    "city": "Атырау",
    "avatar": "",
    "services": [
        "Консультация по выбору шаурмы",
        "Подержу ваш телефон, пока вы фотографируетесь",
        "Скажу «да ладно, всё нормально» в любой ситуации",
        "Найду свободную розетку в аэропорту",
        "Сделаю вид, что понимаю вашу криптовалюту",
    ],
    "prices": [
        {"service": "Консультация по шаурме", "price": "500 ₸"},
        {"service": "Подержать телефон", "price": "1 000 ₸"},
        {"service": "Сказать «всё нормально»", "price": "2 000 ₸"},
        {"service": "Найти розетку", "price": "5 000 ₸"},
        {"service": "Понимающий вид", "price": "10 000 ₸"},
    ],
    "notes": [
        {"emoji": "🔥", "text": "Работаю без выходных, но с обеденным перерывом"},
        {"emoji": "💎", "text": "Скидка 10% при оплате смешной шуткой"},
        {"emoji": "🚗", "text": "Выезд по городу бесплатно, если по пути"},
        {"emoji": "📵", "text": "Не отвечаю на звонки, только на сообщения"},
    ],
}

BOOKINGS = []


@require_http_methods(["GET"])
def profile(request):
    return JsonResponse(PROFILE)


@csrf_exempt
@require_http_methods(["POST"])
def book(request):
    try:
        data = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"status": "error", "message": "Некорректный JSON"}, status=400)

    name = str(data.get("name", "")).strip()
    service = str(data.get("service", "")).strip()
    if not name or not service:
        return JsonResponse({"status": "error", "message": "Укажите имя и услугу"}, status=400)

    BOOKINGS.append({"name": name, "service": service})
    return JsonResponse({"status": "ok", "message": f"Заявка принята: {name}, {service}"})


class SimpleCorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "OPTIONS" and request.headers.get("Origin"):
            response = HttpResponse(status=204)
        else:
            response = self.get_response(request)

        origin = request.headers.get("Origin", "")
        if origin in ALLOWED_ORIGINS:
            response["Access-Control-Allow-Origin"] = origin
            response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
            response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
            response["Vary"] = "Origin"
        return response
