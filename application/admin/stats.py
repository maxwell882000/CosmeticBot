from . import bp
from application.core.models import Stats
from flask import Blueprint, render_template
from flask_login import login_required
from .forms import DeliveryPriceForm, CafeLocationForm


@bp.route('/stats', methods=['GET'])
@login_required
def stats():
	dish_stat = Stats.query.all()
	return render_template('admin/stats.html', title='Статистика', area='stats', dish_stat=dish_stat)