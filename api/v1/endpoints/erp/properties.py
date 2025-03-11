ERROR_500_TEMPLATE = '500.html'
TEMPLATE_TITLE_KEY = "template_title"  # Key to be used to set the Template Tag to hold the title of Each Page
EMPLOYEE_CHOICES = "employee_choices"

LOGIN_URL = '/erp/'
LOGOUT_URL = '/erp/logout'
JSON_LOGIN_URL = '/erp/user/json/login_api/'
AUTH_REGISTER_ENTERPRISE = '/erp/auth/register_enterprise/'
VALIDATE_AND_REGISTER_ENTERPRISE = '/erp/auth/validate_and_register/'
SEND_SIGN_UP_MAIL = '/erp/auth/send_sign_up_mail/'
AUTH_CHANGE_PASSWORD = '/erp/auth/change_pwd/'
AUTH_FORGET_PASSWORD = '/erp/auth/forget_pwd/'
AUTH_CHANGE_PWD = '/erp/auth/json/change_password/'
AUTH_FORGET_PWD = '/erp/auth/json/forget_password/'
AUTH_VALIDATE_EMAIL = '/erp/auth/validate_email/'

LOGIN_TEMPLATE = 'auth/index.html'
SESSION_EXPIRY_TEMPLATE = "auth/session_expiry.html"
CHANGE_PASSWORD_TEMPLATE = 'auth/change_password.html'
FORGET_PASSWORD_TEMPLATE = 'auth/forget_password.html'

FILE_UPLOAD_PATH = "/site_media/upload/"

# DashBoard
DASH_BOARD_TEMPLATE = 'purchase/dashboard.html'

# ERP
ERP_HOME_TEMPLATE = 'dashboard/home.html'
HOME_URL = '/erp/home/'

# Catalogue related
MANAGE_MATERIAL_TEMPLATE = 'masters/material.html'
MANAGE_MATERIAL_SEARCH_URL = '/erp/masters/catalogues/#table_tab1'
MANAGE_SERVICE_MATERIAL_SEARCH_URL = '/erp/masters/services/#table_tab1'

# Indent related
MANAGE_INDENT_TEMPLATE = 'stores/indent.html'
MANAGE_INDENT_TEMPLATES = 'stores/indent_list.html'

MANAGE_MANUFACTURE_INDENT_TEMPLATES = 'production/manufacture_indent.html'
MANAGE_PRODUCTION_PLAN_TEMPLATES = 'production/production_plan.html'

MANAGE_INDENTS_URL = '/erp/stores/indent_list/'
EDIT_INDENT_URL = '/erp/stores/indent/'

# Masters related
MANAGE_MASTERS_TEMPLATE = 'masters/sidebar.html'

# Supplier related
MANAGE_SUPPLIER_TEMPLATE = 'masters/party_list.html'
MANAGE_SUPPLIER_URL = '/erp/masters/party_list'
EDIT_SUPPLIER_TEMPLATE = 'erp/add_supplier.html'

# Employee related
MANAGE_EMPLOYEE_TEMPLATE = 'hr/employee.html'

MANAGE_EMPLOYEE_URL = '/erp/hr/employee'
EDIT_EMPLOYEE_TEMPLATE = 'hr/employee.html'

# Tax related
MANAGE_TAX_TEMPLATE = 'masters/tax.html'
MANAGE_TAX_URL = '/erp/masters/tax'

# Ledger related
MANAGE_LEDGER_TEMPLATE = 'accounts/ledger.html'
MANAGE_LEDGER_URL = '/erp/accounts/ledger'

# Outstanding bill pdf related
OUTSTANDING_DOC_HEADER_PATH = '/site_media/tmp/out_standing_header_%s.html'
OUTSTANDING_DOC_FOOTER_PATH = '/site_media/tmp/out_standing_footer_%s.html'
OUTSTANDING_DOC_CONTENT_PATH = '/site_media/tmp/out_standing_content_%s.html'
OUTSTANDING_DOC_PATH = '/site_media/tmp/%s.pdf'

# Voucher related
MANAGE_VOUCHER_TEMPLATE = 'accounts/voucher.html'
MANAGE_VOUCHER_URL = '/erp/accounts/voucher'
MANAGE_VOUCHER_LIST_TEMPLATE = 'accounts/voucher_list.html'
MANAGE_VOUCHER_EDIT_URL = '/erp/accounts/voucher/edit/'

# Purchase Orders related
MANAGE_PO_URL = '/erp/purchase/po/'
MANAGE_PO_List_URL = '/erp/purchase/po_list/'
ADD_PO_URL = '/erp/purchase/po/add/'
PO_TEMPLATE = 'purchase/po.html'

MANAGE_JO_URL = '/erp/purchase/jo/'
MANAGE_JO_List_URL = '/erp/purchase/jo_list/'
MANAGE_WO_URL = '/erp/purchase/wo/'

# Grn related
GOODS_RECEIPT_EDIT_URL = '/erp/stores/grn/'
INTERNAL_RECEIPT_EDIT_URL = '/erp/stores/irn/'
SALES_RETURN_EDIt_URL = '/erp/sales/sr/'

GOODS_RECEIPT_LIST_URL = '/erp/stores/grn_list/'
INTERNAL_RECEIPT_LIST_URL = '/erp/stores/irn_list/'
SALES_RETURN_LIST_URL = '/erp/sales/sr_list/'

MANAGE_RECEIPTS_TEMPLATE = 'stores/grn_list.html'
EDIT_RECEIPT_TEMPLATE = 'stores/grn.html'

# User related
MANAGE_USER_URL = '/erp/admin/user/'
MANAGE_USER_SEARCH_URL = '/erp/admin/user/#table_tab2'
MANAGE_USER_TEMPLATE = 'admin/users.html'

# Invoice Related
INVOICE_LIST_URL = '/erp/sales/invoice_list/'
ISSUE_LIST_URL = '/erp/stores/issue_list/'
DC_LIST_URL = '/erp/stores/dc_list/'

INVOICE_EDIT_URL = '/erp/sales/invoice/'
ISSUE_EDIT_URL = '/erp/stores/issue/'
DC_EDIT_URL = '/erp/stores/dc/'

INVOICE_LIST_TEMPLATE = 'sales/invoice_list.html'
INVOICE_TEMPLATE = 'sales/invoice.html'

MANAGE_TEST_TEMPLATE = 'accounts/purchase.html'
MANAGE_TEST_URL = '/erp/accounts/purchase'

# Reports Page
PURCHASE_ORDER_MASTER_REPORT_TEMPLATE = 'purchase/reports.html'
PURCHASE_ORDER_MATERIAL_WISE_REPORT_TEMPLATE = 'purchase/materialwisereport.html'
PURCHASE_ORDER_MATERIAL_HISTORY_REPORT_TEMPLATE = 'stores/mat_history.html'
SHORTAGE_LIST_REPORT_TEMPLATE = 'stores/shortage.html'

SALES_REPORT_TEMPLATE = 'sales/reports.html'
MATERIAL_TAX_REPORT_TEMPLATE = 'sales/materialtaxreport.html'
INVOICE_TAX_REPORT_TEMPLATE = 'sales/invoicetaxreport.html'
OA_REPORT_TEMPLATE = 'sales/oa_report.html'

# Enterprise Details
MANAGE_ENTERPRISE_URL = '/erp/admin/enterprise/'
MANAGE_ENTERPRISE_TEMPLATE = 'admin/enterprise.html'

# Expenses Module
MANAGE_EXPENSES_TEMPLATE = 'auditing/expense.html'
MANAGE_EXPENSES_URL = '/erp/expenses/home/#tab1'

MANAGE_NOTE_URL = '/erp/auditing/icd/?is_credit_debit=True'
MANAGE_NOTE_TEMPLATE = 'auditing/note.html'
NOTE_CLIENT_APPROVAL_MAIL = '/templates/auditing/note_mail.html'
NOTE_STATUS_TEMPLATE = 'auditing/note_status.html'

# Pay related
MANAGE_PAY_TEMPLATE = 'hr/paystructure.html'
MANAGE_PAY_URL = '/erp/hr/pay/#tab1'

# HR Module
MANAGE_HR_TEMPLATE = 'hr/dashboard.html'
MANAGE_HR_URL = '/erp/hr/home'

MANAGE_HR_ATTENDANCE_TEMPLATE = 'hr/attendance.html'
MANAGE_HR_ATTENDANCE_URL = '/erp/hr/attendance'

MANAGE_OA_URL = '/erp/sales/oa'
EDIT_OA_URL = '/erp/sales/oa/edit/'
MANAGE_OA_VIEW_URL = '/erp/sales/oa/view'

MANAGE_OA_TEMPLATE = 'sales/oa.html'
ADD_EDIT_OA_TEMPLATE = 'sales/oa.html'

MANAGE_OA_VIEW_TEMPLATE = 'sales/oaview.html'

# Payment related
MANAGE_PAYMENT_TEMPLATE = 'accounts/payment.html'
MANAGE_PAYMENT_URL = '/erp/accounts/payment'
MANAGE_PAYMENT_SUCCESS_MAIL_TEMPLATE = '/templates/pgi/payment_success_mail.html'

# BRS related
MANAGE_BRS_TEMPLATE = 'accounts/bank_reconciliation.html'
MANAGE_BRS_URL = '/erp/accounts/BRS'

MANAGE_INVOICE_TEMPLATE_NEW = 'admin/print_template/invoice/invoice_template_configuration.html'
INVOICE_TEMPLATE_URL = '/erp/admin/invoice_template/'

MANAGE_SALES_ESTIMATE_TEMPLATE_CONFIG = 'admin/print_template/se/se_template_configuration.html'
MANAGE_OA_TEMPLATE_CONFIG = 'admin/print_template/oa/oa_template_configuration.html'

MANAGE_PO_TEMPLATE = 'admin/print_template/po/po_template_configuration.html'
PO_TEMPLATE_URL = '/erp/admin/po_template/'

PASSWORD_CHANGED_MAIL = '/templates/auth/password_changed.html'
PASSWORD_RESET_MAIL = '/templates/auth/password_reset.html'
USER_INVITE_MAIL = '/templates/auth/user_invite_mail.html'
WELCOME_MAIL_MAIL = '/templates/auth/welcome_mail.html'
BROADCAST_URL = '/erp/commons/broadcast/'
VERSION_INFO = '/erp/commons/version_info/'

CONTACT_MAIL = '/templates/public/contact_mail.html'
FEEDBACK_MAIL = '/templates/public/feedback_mail.html'
USER_RESTRICT_CONTACT_MAIL = '/templates/admin/user_restrict_contact_mail.html'

SIGN_UP_INTIMATION_MAIL = '/templates/auth/sign_up_intimation_mail.html'
REGISTERED_INTIMATION_MAIL = '/templates/auth/registered_intimation_mail.html'
REQUEST_MAIL_TEMPLATE = '/templates/admin/request_mail_template.html'

MANAGE_SALES_ESTIMATE_URL = '/erp/sales/sales_estimate'
EDIT_SALES_ESTIMATE_URL = '/erp/sales/sales_estimate/edit/'
MANAGE_SALES_ESTIMATE_VIEW_URL = '/erp/sales/sales_estimate/view'

MANAGE_SALES_ESTIMATE_LIST_TEMPLATE = 'sales/sales_estimate_list.html'
MANAGE_SALES_ESTIMATE_TEMPLATE = 'sales/sales_estimate.html'
ADD_EDIT_SALES_ESTIMATE_TEMPLATE = 'sales/sales_estimate.html'
CLIENT_APPROVAL_MAIL = '/templates/admin/print_template/se/print/se_template_mail.html'
SALES_ESTIMATE_STATUS_TEMPLATE = 'sales/sales_estimate_status.html'

# Production Related
MANAGE_PP_List_URL = '/erp/production/production_plan/'

GSTIN_STATE_CODE = {
    '01': "Jammu and Kashmir",
    '02': "Himachal Pradesh",
    '03': "Punjab",
    '04': "Chandigarh",
    '05': "Uttarakhand",
    '06': "Haryana",
    '07': "Delhi",
    '08': "Rajasthan",
    '09': "Uttar Pradesh",
    '10': "Bihar",
    '11': "Sikkim",
    '12': "Arunachal Pradesh",
    '13': "Nagaland",
    '14': "Manipur",
    '15': "Mizoram",
    '16': "Tripura",
    '17': "Meghalaya",
    '18': "Assam",
    '19': "West Bengal",
    '20': "Jharkhand",
    '21': "Orissa",
    '22': "Chhattisgarh",
    '23': "Madhya Pradesh",
    '24': "Gujarat",
    '25': "Daman & Diu",
    '26': "Dadra & Nagar Haveli",
    '27': "Maharashtra",
    '28': "Andhra Pradesh",
    '29': "Karnataka",
    '30': "Goa",
    '31': "Lakshadweep",
    '32': "Kerala",
    '33': "Tamil Nadu",
    '34': "Puducherry",
    '35': "Andaman & Nicobar Islands",
    '36': "Telangana",
    '37': "Andhra Pradesh"

}

GSTIN_STATE_TITLE = {
    'JK': "Jammu & Kashmir",
    'HP': "Himachal Pradesh",
    'PB': "Punjab",
    'CH': "Chandigarh",
    'UK': "Uttarakhand",
    'HR': "Haryana",
    'DL': "Delhi",
    'RJ': "Rajasthan",
    'UP': "Uttar Pradesh",
    'BR': "Bihar",
    'SK': "Sikkim",
    'AR': "Arunachal Pradesh",
    'NL': "Nagaland",
    'MN': "Manipur",
    'MZ': "Mizoram",
    'TR': "Tripura",
    'ML': "Meghalaya",
    'AS': "Assam",
    'WB': "West Bengal",
    'JH': "Jharkhand",
    'OR': "Orissa",
    'CG': "Chhattisgarh",
    'MP': "Madhya Pradesh",
    'GJ': "Gujarat",
    'DD': "Daman & Diu",
    'DH': "Dadra & Nagar Haveli",
    'MH': "Maharashtra",
    'AP': "Andhra Pradesh",
    'KA': "Karnataka",
    'GA': "Goa",
    'LD': "Lakshadweep",
    'KL': "Kerala",
    'TN': "Tamil Nadu",
    'PY': "Puducherry",
    'AN': "Andaman & Nicobar Islands",
    'TS': "Telangana"
}

UNIT_NAME_MAPPING = {
    'BAGS': 'BAG-BAGS',
    'BALE': 'BAL-BALE',
    'BUNDLES': 'BDL-BUNDLES',
    'BUCKLES': 'BKL-BUCKLES',
    'BILLION OF UNITS': 'BOU-BILLION OF UNITS',
    'BOX': 'BOX-BOXES',
    'BOXES': 'BOX-BOXES',
    'BOTTLES': 'BTL-BOTTLES',
    'BUNCHES': 'BUN-BUNCHES',
    'CANS': 'CAN-CANS',
    'CUBIC METERS': 'CBM-CUBIC METERS',
    'CUBIC CENTIMETERS': 'CCM-CUBIC CENTIMETERS',
    'CENTIMETERS': 'CMS-CENTIMETERS',
    'CARTONS': 'CTN-CARTONS',
    'DOZENS': 'DOZ-DOZENS',
    'DRUMS': 'DRM-DRUMS',
    'GREAT GROSS': 'GGK-GREAT GROSS',
    'GRAMMES': 'GMS-GRAMMES',
    'GROSS': 'GRS-GROSS',
    'GROSS YARDS': 'GYD-GROSS YARDS',
    'KILOGRAMS': 'KGS-KILOGRAMS',
    'KILOLITRE': 'KLR-KILOLITRE',
    'KILOMETRE': 'KME-KILOMETRE',
    'MILILITRE': 'MLT-MILILITRE',
    'METERS': 'MTR-METERS',
    'METRIC TON': 'MTS-METRIC TON',
    'NUMBERS': 'NOS-NUMBERS',
    'PACKS': 'PAC-PACKS',
    'PIECES': 'PCS-PIECES',
    'PAIRS': 'PRS-PAIRS',
    'QUINTAL': 'QTL-QUINTAL',
    'ROLLS': 'ROL-ROLLS',
    'SETS': 'SET-SETS',
    'SQUARE FEET': 'SQF-SQUARE FEET',
    'SQUARE METERS': 'SQM-SQUARE METERS',
    'SQUARE YARDS': 'SQY-SQUARE YARDS',
    'TABLETS': 'TBS-TABLETS',
    'TEN GROSS': 'TGM-TEN GROSS',
    'THOUSANDS': 'THD-THOUSANDS',
    'TONNES': 'TON-TONNES',
    'TUBES': 'TUB-TUBES',
    'US GALLONS': 'UGS-US GALLONS',
    'UNITS': 'UNT-UNITS',
    'YARDS': 'YDS-YARDS'
}
