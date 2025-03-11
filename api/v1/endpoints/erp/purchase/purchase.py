from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from schemas.user import UserCreate, UserResponse
from services.user_service import create_user, get_users

from api.v1.endpoints.erp import properties
import json
import datetime

from util.api_util import (
    success,
    delete,
    failure,
    unknown_failure,
    param_missing,
    session_timeout,
    internal_error,
    database_error,
    object_as_array_map,
    get_value,
    get_date_range,
    get_date_range_by_month
)

router = APIRouter()


@router.get("/po_list", response_model=dict)
def renderPurchaseHome(request, order_type="po", edit_link=properties.MANAGE_PO_List_URL):
    try:
        request_handler = RequestHandler(request)
        enterprise_id = request_handler.getSessionAttribute(USER_IN_SESSION_KEY).enterprise.id
        since, till = get_date_range(
            rh=request_handler, since_session_key="po.list.since", till_session_key="po.list.till")
        status = request_handler.getAndCacheData(key="status", session_key="po.list.status")
        if request.POST.get('po_fromdate'):
            since = datetime.strptime(request.POST.get('po_fromdate'), "%Y-%m-%d")
            project_id = "5"  # All
        else:
            project_id = request_handler.getAndCacheData(key="project_id", session_key="po.list.project_id")
        status = request.POST.get('po_status') if request.POST.get('po_status') else status
        pending_indents = loadIndentDetails(request)
        purchase_service = PurchaseService()

        po_type_choices = (('PO', 'PO'), ('JO', 'JO'), ('WO', 'WO'))
        enterprise = purchase_service.purchase_dao.db_session.query(Enterprise).filter(
            Enterprise.id == enterprise_id).first()
        indent_access = enterprise.setting_flags & enterprise_module_settings['indent_flag'] > 0
        query = "SELECT code, name FROM projects WHERE enterprise_id='%s' AND code<>'' ORDER BY name" % enterprise_id
        projects = executeQuery(query)
        return TemplateResponse(request=request, template='purchase/po_list.html', context={
            'indent_access': indent_access, 'pending_indents': pending_indents,
            TEMPLATE_TITLE_KEY: "Purchase Order" if order_type == "po" else (
                "Job Order" if order_type == "jo" else "Work Order"),
            'po_type': po_type_choices, 'projects': projects, 'status': status, 'project_id': project_id,
            'since': since.strftime("%Y-%m-%d"), 'till': till.strftime("%Y-%m-%d"), 'order_type': order_type,
            'edit_link': edit_link})
    except Exception as e:
        raise e
