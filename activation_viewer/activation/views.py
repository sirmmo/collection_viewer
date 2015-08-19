from django.core.exceptions import PermissionDenied
from django.template import RequestContext
from django.shortcuts import render_to_response

from guardian.shortcuts import get_perms

from .models import Activation

_PERMISSION_MSG_VIEW = "You are not permitted to view this activation"

def _resolve_activation(request, activation_id, permission='activation.view_activation',
                   msg=_PERMISSION_MSG_VIEW):
    """
    Resolve the activation by the provided activation_id and check the optional permission.
    """
    activation = Activation.objects.get(activation_id=activation_id)
    if not request.user.has_perm(permission, activation):
        raise PermissionDenied(mesg)

    return activation


def activation_detail(request, activation_id, template="activation_detail.html"):
    activation = _resolve_activation(request, activation_id)
    context_dict = {
        'activation': activation,
        'perms_list': get_perms(request.user, activation),
    }
    return render_to_response(template, RequestContext(request, context_dict))