from django.shortcuts import render
from usuario.models import Usuario
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from usuario.serializers import UsuarioSerializer
from rest_framework import status
import json
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


@api_view(["GET"])
#@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_users(request):
    usuarios = Usuario.getAll()
    serializer = UsuarioSerializer(usuarios, many=True)
    return JsonResponse({'data': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
#@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_user(request):
	payload = json.loads(request.body)
	try:
		user=payload
		user=Usuario.createUser(user)
		serializer = UsuarioSerializer(user)
		return JsonResponse({'data': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
	except ObjectDoesNotExist as e:
		return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
	except Exception as e:
		return JsonResponse({'error': 'Algo salió mal'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
#@csrf_exempt
#@permission_classes([IsAuthenticated])
def edit_user(request, id_usuario):
    payload = json.loads(request.body)
    try:
        user_item = payload
        user=Usuario.editUser(user_item,id_usuario)
        serializer = UsuarioSerializer(user)
        return JsonResponse({'data': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo salió mal'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
#@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_user(request,id_usuario):
    try:
        Usuario.deleteUser(id_usuario)
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Algo salió mal'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)