from django.shortcuts import get_object_or_404
from rest_framework import response, status, permissions
from rest_framework.generics import GenericAPIView, ListAPIView
from licenses.models import License, Payment
from licenses.serializers import LicenseSerializer, PaymentSerializer
import os
from django.http import HttpResponse


def index(request):
    times = int(os.environ.get('TIMES', 3))
    return HttpResponse('Hello! ' * times)


class LicenseStatusAPIView(GenericAPIView):
    serializer_class = PaymentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        payments = Payment.objects.filter(user=self.request.user).order_by('-created_at')
        current_payments = []
        # get the payments that are not expired or are not paid
        for payment in payments:
            if not payment.verified_pay or not payment.has_expired():
                current_payments.append(payment)

        # check if the user doesn't have to buy a license
        if len(current_payments) > 0:
            # check if the user's older license is paid
            if current_payments[-1].verified_pay:
                # if it's paid then return all of the current user's payments
                return response.Response({'payments': self.serializer_class(current_payments, many=True).data},
                                         status=status.HTTP_200_OK)
            else:
                # if it isn't paid then return the only one license waiting for get paid
                # (due to the user only can have a not paid license)
                return response.Response({'payment': self.serializer_class(current_payments[0]).data})
        else:
            # user doesn't have a not expired license or never had one
            never_had_one = len(payments) == 0
            return response.Response({'message': 'No license', 'never_had_license': never_had_one},
                                     status=status.HTTP_200_OK)

    def post(self, request):
        user = self.request.user
        license_id = request.data.get('id')
        selected_license = get_object_or_404(License, id=license_id)
        payments = Payment.objects.filter(user=user, verified_pay=False).order_by('-created_at')
        if len(payments) > 0:
            last_payment = payments[-1]
            return response.Response({'message': 'User already has a not verified payment',
                                      'license': self.serializer_class(last_payment.license)},
                                     status=status.HTTP_208_ALREADY_REPORTED)
        payment = Payment(user=user, license=selected_license)
        payment.save()
        return response.Response({}, status=status.HTTP_200_OK)

    def delete(self, request):
        user = self.request.user
        payments = Payment.objects.filter(user=user).order_by('-created_at')
        current_payments = []
        # get the payments that are not paid
        for payment in payments:
            if not payment.verified_pay:
                current_payments.append(payment)

        if len(current_payments) > 0:
            current_payments[-1].delete()
            return response.Response(status=status.HTTP_200_OK)
        else:
            return response.Response(status=status.HTTP_204_NO_CONTENT)


class LicenseListAPIView(ListAPIView):
    serializer_class = LicenseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user)
        return License.objects.filter(is_active=True)
