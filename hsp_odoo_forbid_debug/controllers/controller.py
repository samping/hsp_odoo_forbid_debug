# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import http
from odoo.addons.web.controllers.main import Home, ensure_db, redirect_with_hash
from odoo.http import request


class HSPHome(Home, http.Controller):

    @http.route('/web', type='http', auth="none")
    def web_client(self, s_action=None, **kw):
        ensure_db()
        if kw.get('debug') == "1" or kw.get('debug') == "assets" or kw.get('debug') == "assets,tests":
            if kw.get('hsp') == "123456":
                pass
            else :
                return redirect_with_hash('/web?debug=0')

        return super(HSPHome, self).web_client(s_action=s_action, **kw)


