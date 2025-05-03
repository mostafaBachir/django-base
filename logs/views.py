from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.conf import settings
import os
from rest_framework.pagination import PageNumberPagination

LOG_PATH = os.path.join(settings.BASE_DIR, 'logs/app.log')



class ClearLogsView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        try:
            open(LOG_PATH, 'w').close()
            return Response({'message': 'Log file cleared.'})
        except Exception as e:
            return Response({'error': str(e)}, status=500)



class LogPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 500


class LogListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        level_filter = request.query_params.get('level', '').upper()

        try:
            with open(LOG_PATH, 'r') as f:
                lines = f.readlines()

            # Filtrage par niveau si précisé
            if level_filter:
                lines = [line for line in lines if f'[{level_filter}]' in line]

            lines = list(reversed(lines))  # plus récents en haut

            paginator = LogPagination()
            result_page = paginator.paginate_queryset(lines, request)
            return paginator.get_paginated_response(result_page)

        except FileNotFoundError:
            return Response({'error': 'Log file not found'}, status=404)