from flask import Markup, request, render_template, url_for, session, redirect
from app_school import app, db_session
from app_school.xu_ly.Xu_ly_Model import GiaoVien
from app_school.xu_ly.Xu_ly_Form import Form_Register, Form_Login
from app_school.xu_ly.tra_cuu.tra_cuu import *
from app_school.xu_ly.lien_he.xu_ly_lien_he import *


@app.route('/trang-chu/thong-tin', methods=['GET','POST'])
def trang_thong_tin():
    return render_template('index/thong_tin.html')

@app.route('/trang-chu/lien-he', methods=['GET','POST'])
def trang_lien_he():
    Ho_va_ten = ""
    Email = ""
    Noi_dung = ""
    message_hoatdong = ""
    if request.form.get("Th_Ho_va_ten") :
        Ho_va_ten = request.form.get("Th_Ho_va_ten")
        Email = request.form.get("Th_email")
        Noi_dung = request.form.get("Th_noi_dung")
        Danh_sach = [Ho_va_ten,Email,Noi_dung]
        Them_lien_he(Danh_sach)
        message_hoatdong='Đã gửi thông tin liên hệ'
    return render_template('index/lien_he.html', message_hoatdong=message_hoatdong)