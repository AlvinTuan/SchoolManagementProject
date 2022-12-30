from flask import Markup, request, render_template, url_for, session, redirect
from app_school.xu_ly.Xu_ly_Form import *
from app_school.xu_ly.lop_hoc.XL_Lop_hoc import lay_nien_khoa_theo_lop, cap_nhat_si_so
from app_school.xu_ly.giao_vien.XL_Giao_vien import Profile_Giao_Vien
from app_school.xu_ly.bang_diem.XL_Bang_diem import tao_bang_diem_cho_hoc_sinh, doc_bang_diem_theo_hoc_sinh
from app_school.xu_ly.hoc_sinh.XL_Hoc_sinh import Profile_hoc_sinh
from app_school.xu_ly.lop_hoc.XL_Lop_hoc import doc_danh_sach_lop_hoc, doc_danh_sach_lop_hoc_theo_giao_vien
from app_school.xu_ly.Xu_ly_Model import HocSinh, Lop
from app_school.xu_ly.hoc_sinh.XL_Hoc_sinh import *
from app_school.xu_ly.quan_li.xu_ly_doc_lien_he import *
from app_school import app, db_session
from datetime import date
from flask_mail import Mail , Message
from app_school import bcrypt

@app.route("/quan-li" , methods = ['GET','POST'])
def trang_quan_li() :
    if session.get("quanli") == None:
        return redirect(url_for('login'))
    quanli = session['quanli']
    message = ''
    quan_li = Profile_Quan_li(quanli)
    if request.args.get('message'):
        message = request.args.get('message')
        print(message)
    return render_template('quan_ly/thong_tin_quan_li.html',quan_li=quan_li,message=message)

@app.route("/quan-li/doc-lien-he" , methods = ['GET','POST'])
def trang_doc_lien_he() :
    if session.get("quanli") == None:
        return redirect(url_for('login'))
    Danh_sach_lh = Doc_danh_sach_lh()
    form = Form_Feedback()
    return render_template("quan_ly/doc_lien_he.html" , Danh_sach_lh=Danh_sach_lh)

@app.route("/quan-li/doc-lien-he/<string:Chuoi_tra_cuu>/" , methods=['GET','POST'])
def trang_tra_loi_lien_he(Chuoi_tra_cuu) :
    if session.get("quanli") == None:
        return redirect(url_for('login'))
    danh_sach = Doc_danh_sach_lh()
    danh_sach_chon = Lay_info_theo_Email(Chuoi_tra_cuu , danh_sach)
    noi_dung = ""
    if request.form.get("Th_noi_dung") :

        app.config['MAIL_SERVER'] = "smtp.gmail.com"
        app.config['MAIL_PORT'] = 465
        app.config['MAIL_USERNAME'] = 'tuanle0715@gmail.com'
        app.config['MAIL_PASSWORD'] = 'kxmeufzyzkvhkigm'
        app.config['MAIL_USE_TLS'] = False  
        app.config['MAIL_USE_SSL'] = True

    return render_template("quan_ly/xem_lien_he.html" ,danh_sach_chon=danh_sach_chon)


@app.route("/quan-li/tao-tai-khoan" , methods=['GET','POST'])
def trang_tao_tai_khoan() :
    if session.get("quanli") == None:
        return redirect(url_for('login'))
    ten_dang_nhap = ""
    mat_khau = ""
    ho_ten = ""
    gioi_tinh = ""
    dia_chi = ""
    email = ""
    ngay_sinh= ""
    sdt= ""
    trinh_do = ""
    chuyen_mon = ""
    quyen = ""
    Danh_sach = []
    if request.form.get('Th_Ten_dang_nhap') :
        ten_dang_nhap = request.form.get('Th_Ten_dang_nhap')
        encryted_pw = bcrypt.generate_password_hash(request.form.get('Th_Mat_khau')).decode("utf-8")
        mat_khau = encryted_pw
        ho_ten = request.form.get('Th_Ho_va_ten')
        gioi_tinh = request.form.get('Th_Gioi_tinh')
        dia_chi = request.form.get('Th_Dia_chi')
        email = request.form.get('Th_email')
        ngay_sinh= request.form.get('Th_Ngay_sinh')
        sdt= request.form.get('Th_Sdt_gv')
        trinh_do = request.form.get('Th_Trinh_do')
        chuyen_mon = request.form.get('Th_Chuyen_mon')
        quyen = request.form.get('Th_Quyen')
        Danh_sach.append(ten_dang_nhap)
        Danh_sach.append(mat_khau)
        Danh_sach.append(ho_ten)
        Danh_sach.append(gioi_tinh)
        Danh_sach.append(dia_chi)
        Danh_sach.append(email)
        Danh_sach.append(ngay_sinh)
        Danh_sach.append(sdt)
        Danh_sach.append(trinh_do)
        Danh_sach.append(chuyen_mon)
        Danh_sach.append(quyen)
        Them_tai_khoan(Danh_sach)
    return render_template("quan_ly/tao_tai_khoan.html")

@app.route("/quan-li/tao-tai-khoan-hs" , methods=['GET','POST'])
def trang_tao_tai_khoan_hs() :
    if session.get("quanli") == None:
        return redirect(url_for('login'))

    id_hoc_sinh = ""
    mat_khau = ""
    ho_ten = ""
    gioi_tinh = ""
    dia_chi = ""
    email = ""
    ngay_sinh = ""
    sdt = ""
    sdt_ph = ""
    id_lop = ""
    id_nien_khoa = ""
    Danh_sach = []
    if request.form.get('Th_Id_hoc_sinh') :
        id_hoc_sinh = request.form.get('Th_Id_hoc_sinh')
        encryted_pw = bcrypt.generate_password_hash(request.form.get('Th_Mat_khau')).decode("utf-8")
        mat_khau = encryted_pw
        ho_ten = request.form.get('Th_Ho_va_ten')
        gioi_tinh = request.form.get('Th_Gioi_tinh')
        dia_chi = request.form.get('Th_Dia_chi')
        email = request.form.get('Th_email')
        ngay_sinh = request.form.get('Th_Ngay_sinh')
        sdt = request.form.get('Th_Sdt')
        sdt_ph = request.form.get('Th_Sdt_ph')
        id_lop = request.form.get('Th_Lop')
        id_nien_khoa = request.form.get('Th_Nien_khoa')
        Danh_sach.append(id_hoc_sinh)
        Danh_sach.append(mat_khau)
        Danh_sach.append(ho_ten)
        Danh_sach.append(gioi_tinh)
        Danh_sach.append(dia_chi)
        Danh_sach.append(email)
        Danh_sach.append(ngay_sinh)
        Danh_sach.append(sdt)
        Danh_sach.append(sdt_ph)
        Danh_sach.append(id_lop)
        Danh_sach.append(id_nien_khoa)
        Them_tai_khoan_HS(Danh_sach)
    return render_template("quan_ly/tao_tai_khoan_hs.html")

@app.route('/quan-li/doi-mat-khau', methods=['GET', 'POST'])
def doi_mat_khau_ql():
    if session.get("quanli") == None:
        return redirect(url_for('login'))
    quanli = session['quanli']
    
    ql = Profile_Quan_li(quanli)
    ThongBao = ""
    form = Form_Reset_pw()

    if form.validate_on_submit():
        MatkhauCu = request.form['Th_MatkhauCu']
        MatkhauMoi = request.form['Th_MatkhauMoi']
        ThongBao = ql_doi_mat_khau(quanli, MatkhauCu, MatkhauMoi)
        if ThongBao == "Đổi Mật Khẩu Thành Công":
            return redirect(url_for('trang_quan_li', message='Đổi mật khẩu thành công'))
    return render_template('quan_ly/doi_mat_khau.html', form=form, ThongBao=ThongBao)


@app.route('/quan-li/xem-tai-khoan-hs/<string:Chuoi_Tra_cuu>/khoi_phuc_mat_khau', methods=['GET', 'POST'])
def ql_khoi_phuc_mat_khau_HS(Chuoi_Tra_cuu):
    if session.get("quanli") == None:
        return redirect(url_for('login'))
    quanli = session['quanli']
    Danh_sach_hs = Doc_danh_sach_hs()
    Danh_sach_hs_chon = Lay_info_theo_ID(Chuoi_Tra_cuu,Danh_sach_hs)
    ql = Profile_Quan_li(quanli)
    ThongBao = ""
    form = Form_Recovery_pw()
    if form.validate_on_submit():
        MatKhauMacDinh = request.form['Th_KhoiphucMatkhau']
        ThongBao = ql_dat_mk_choHS(Danh_sach_hs_chon, MatKhauMacDinh)
        if ThongBao == "Khôi Phục Mật Khẩu Thành Công":
            return render_template("quan_ly/xem_tai_khoan_hs_chon.html", Danh_sach_hs_chon=Danh_sach_hs_chon)
    return render_template("quan_ly/khoi_phuc_mat_khau.html", Danh_sach_hs_chon=Danh_sach_hs_chon, form=form, ThongBao=ThongBao)

@app.route('/quan-li/xem-tai-khoan-gv/<string:Chuoi_Tra_cuu>/khoi_phuc_mat_khau', methods=['GET', 'POST'])
def ql_khoi_phuc_mat_khauGV(Chuoi_Tra_cuu):
    if session.get("quanli") == None:
        return redirect(url_for('login'))
    quanli = session['quanli']
    Danh_sach_gv = Doc_danh_sach_gv()
    Danh_sach_gv_chon = Lay_info_theo_IDgv(Chuoi_Tra_cuu,Danh_sach_gv)
    ThongBao = ""
    form = Form_Recovery_pw()
    if form.validate_on_submit():
        MatKhauMacDinh = request.form['Th_KhoiphucMatkhau']
        ThongBao = ql_dat_mk_choGV(Danh_sach_gv_chon, MatKhauMacDinh)
        if ThongBao == "Khôi Phục Mật Khẩu Thành Công":
            return render_template("quan_ly/xem_tai_khoan_gv_chon.html", Danh_sach_gv_chon=Danh_sach_gv_chon)
    return render_template("quan_ly/khoi_phuc_mat_khau.html", Danh_sach_gv_chon=Danh_sach_gv_chon, form=form, ThongBao=ThongBao)

@app.route('/quan-li/sua-quan-li', methods=['GET','POST'])
def cap_nhat_quan_li():
    if session.get("quanli") == None:
        return redirect(url_for('login'))
    error = ''
    quanli = session['quanli']
    quan_li = Profile_Quan_li(quanli)
    form = Form_Update_Ql()
    if form.validate_on_submit():
        HoVaTen = request.form['Th_Ho_ten']
        GioiTinh = request.form['Th_Gioi_tinh']
        NgaySinh = request.form['Th_Ngay_sinh']
        DiaChi = request.form['Th_Dia_chi']
        Email = request.form['Th_Email']
        SoDienThoai = request.form['Th_Sdt']

        ql = {"HoVaTen": HoVaTen, "GioiTinh": GioiTinh, "NgaySinh": NgaySinh, "Email": Email, "DiaChi": DiaChi,
              "SoDienThoai": SoDienThoai}

        value = db_session.query(QuanLi).filter(
            QuanLi.TenDangNhap == quanli).first()

        value.HoVaTen = ql['HoVaTen']
        value.GioiTinh = ql['GioiTinh']
        value.NgaySinh = datetime.strptime(ql['NgaySinh'], '%Y-%m-%d').date()
        value.Email = ql['Email']
        value.DiaChi = ql['DiaChi']
        value.SoDienThoai = ql['SoDienThoai']
        db_session.flush()
        db_session.commit()
        return redirect(url_for('trang_quan_li', message='Cập nhật thành công'))

    form.Th_Gioi_tinh.default = quan_li['GioiTinh']
    form.process()
    return render_template('quan_ly/cap_nhat_thong_tin.html', quan_li=quan_li, form=form, error=error)

@app.route("/quan-li/xem-tai-khoan-gv",methods=['GET','POST'])
def trang_xem_tai_khoan() :
    if session.get("quanli") == None:
        return redirect(url_for('login'))
    Danh_sach_gv = Doc_danh_sach_gv()
    return render_template("quan_ly/xem_tai_khoan_gv.html", Danh_sach_gv=Danh_sach_gv)

@app.route("/quan-li/xem-tai-khoan-gv/<string:Chuoi_Tra_cuu>/",methods=['GET','POST'])
def trang_xem_tai_khoan_chon(Chuoi_Tra_cuu) :
    if session.get("quanli") == None:
        return redirect(url_for('login'))
    Danh_sach_gv = Doc_danh_sach_gv()
    Danh_sach_gv_chon = Lay_info_theo_TK(Chuoi_Tra_cuu,Danh_sach_gv)
    return render_template("quan_ly/xem_tai_khoan_gv_chon.html", Danh_sach_gv_chon=Danh_sach_gv_chon)

@app.route("/quan-li/xem-tai-khoan-hs",methods=['GET','POST']) #
def trang_xem_tai_khoan_hs() :
    if session.get("quanli") == None:
        return redirect(url_for('login'))
    Danh_sach_hs = Doc_danh_sach_hs()
    return render_template("quan_ly/xem_tai_khoan_hs.html", Danh_sach_hs=Danh_sach_hs)

@app.route("/quan-li/xem-tai-khoan-hs/<string:Chuoi_Tra_cuu>/",methods=['GET','POST'])
def trang_xem_tai_khoan_hs_chon(Chuoi_Tra_cuu) :
    if session.get("quanli") == None:
        return redirect(url_for('login'))
    Danh_sach_hs = Doc_danh_sach_hs()
    Danh_sach_hs_chon = Lay_info_theo_ID(Chuoi_Tra_cuu,Danh_sach_hs)
    return render_template("quan_ly/xem_tai_khoan_hs_chon.html", Danh_sach_hs_chon=Danh_sach_hs_chon)

@app.route("/quan-li/xem-cac-lop" , methods = ['GET','POST'])
def trang_them_tkb() :
    danh_sach_lop = doc_danh_sach_lop_hoc()
    return render_template("quan_ly/xem_cac_lop.html",danh_sach_lop=danh_sach_lop)

@app.route('/quan-li/dang-xuat', methods=['GET', 'POST'])
def dang_xuat_ql():
    if session.get("quanli") != None:
        session.pop("quanli", None)
    return redirect('/')