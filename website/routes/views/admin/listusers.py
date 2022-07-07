from flask import render_template, request, url_for, flash
from website.const.init_roles import ADMIN_ROLE_ID
from website.utils.api import apiGet
from website.utils.role import role_required
from website.utils.jwt import token_required
from .route import admin


@admin.route("users")
@token_required()
@role_required(ADMIN_ROLE_ID)
def listusers(user):
    try:
        users_resp, users_respdata = apiGet(
            url_for('api.admin.listusers'),
            data={
                "auth": request.cookies.get('auth'),
            }
        )
    except Exception:
        flash("An unknown error occured.", category="error")
        return render_template('error.html')
    
    try:
        roles_resp, roles_respdata = apiGet(
            url_for('api.admin.listroles'),
            data={
                "auth": request.cookies.get('auth'),
            }
        )
    except Exception as e:
        flash("An unknown error occured.", category="error")
        return render_template('error.html')
    
    if not users_resp or not roles_resp:
        flash("An unknown error occured.", category="error")
        return render_template('error.html')
    
    users = users_respdata['result']
    roles = roles_respdata['result']
    return render_template("admin/listusers.html", users=users, roles=roles)