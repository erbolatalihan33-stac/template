import random

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Profile


class HealthView(APIView):
    def get(self, request):
        return Response({"status": "ok", "service": "backend"})

DEFAULT_PROFILE = {
    "name": "Алмагуль",
    "age": 18,
    "status": "Индивидуально",
    "city": "Атырау",
    "params": {
        "height": "165 см",
        "nation": "Казахская красавица",
        "vibe": "99% вредности",
    },
    "services": [
        "Подержать за руку",
        "Поцелуй за кофе",
        "Массаж плеч",
        "Забрать толстовку",
        "Игнор в WhatsApp",
    ],
    "prices": [
        {"service": "Обычная прогулка", "price": "1 Кофе / Бабл-ти"},
        {"service": "Просмотр фильма", "price": "Выбор фильма + чипсы"},
        {"service": "Разговоры по телефону", "price": "Бесплатно (если не спит)"},
    ],
    "notes": [
        "💖 100% милая, когда не злится",
        "⚠️ Батя Али держит локацию под контролем",
        "👑 Забирает все внимание и твои толстовки",
    ],
}

BOOKING_RESPONSES = [
    {
        "status": "pending",
        "message": "Заявка отправлена Бате Али на согласование... Ожидайте SMS",
    },
    {"status": "rejected", "message": "Ошибка: сначала нужно купить Бабл-ти"},
    {"status": "approved", "message": "Бронь подтверждена! Не забудь взять толстовку"},
]


def get_profile_data():
    profile = Profile.objects.prefetch_related("services", "prices", "notes").first()
    if profile is None:
        return DEFAULT_PROFILE

    return {
        "name": profile.name,
        "age": profile.age,
        "status": profile.status,
        "city": profile.city,
        "params": {
            "height": profile.height,
            "nation": profile.nation,
            "vibe": profile.vibe,
        },
        "services": [item.title for item in profile.services.all()],
        "prices": [
            {"service": item.service, "price": item.price}
            for item in profile.prices.all()
        ],
        "notes": [item.text for item in profile.notes.all()],
    }


class ProfileView(APIView):
    def get(self, request):
        return Response(get_profile_data())


class BookView(APIView):
    def post(self, request):
        user_name = request.data.get("userName")
        service = request.data.get("service")

        if not user_name or not service:
            return Response(
                {"status": "error", "message": "Нужно указать userName и service"},
                status=400,
            )

        return Response(random.choice(BOOKING_RESPONSES))
