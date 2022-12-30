from app_school import db_session, bcrypt
from app_school.xu_ly.Xu_ly_Model import QuanLi, HocSinh, GiaoVien
from datetime import datetime
from sqlalchemy import text

from app_school.xu_ly.Xu_ly_Model import engine

def Doc_danh_sach_lh_CSDL():
    with engine.connect() as conn:
        list_dslh = []
        cursor = conn.execute(text("SELECT * FROM lienhe"))
        for row in cursor:
            list_dslh.append(row)
        conn.commit()
        conn.close()
    return list_dslh

def Doc_danh_sach_lh():
    Danh_sach = []
    danh_sach_lh = Doc_danh_sach_lh_CSDL()
    for LienHe in danh_sach_lh:
        info_lh = {}
        info_lh["Người gửi"] = LienHe[0]
        info_lh["Email"] = LienHe[1]
        info_lh["Nội dung"] = LienHe[2]

        Danh_sach.append(info_lh)
    return Danh_sach

def Doc_danh_sach_lh_email():
    Danh_sach = []
    danh_sach_lh = Doc_danh_sach_lh_CSDL()
    for LienHe in danh_sach_lh:
        info_lh = {}
        info_lh["Email"] = LienHe[0]
        Danh_sach.append(info_lh)
    return Danh_sach

def Lay_info_theo_Email(Email, Danh_sach_LienHe):
    Danh_sach=list(filter(
        lambda LienHe: str(Email).strip() == str(LienHe["Email"]).strip() ,Danh_sach_LienHe))
    return Danh_sach[0]

def Doc_danh_sach_GV_CSDL():
    with engine.connect() as conn:
        list_dslh = []
        cursor = conn.execute(text("SELECT * FROM giaovien"))
        for row in cursor:
            list_dslh.append(row)
        conn.commit()
        conn.close()
    return list_dslh


def Them_tai_khoan(Danh_sach_info) :
    danh_sach = Doc_danh_sach_GV_CSDL()
    max_1 = max(danh_sach)
    Gtri_id = max_1[0] + 1
    with engine.connect() as conn:
        sql = f"INSERT INTO giaovien \
                VALUES ({Gtri_id},'{Danh_sach_info[0]}','{Danh_sach_info[1]}','{Danh_sach_info[2]}','{Danh_sach_info[3]}','{Danh_sach_info[4]}','{Danh_sach_info[5]}','{Danh_sach_info[6]}','{Danh_sach_info[7]}','{Danh_sach_info[8]}','{Danh_sach_info[9]}','{Danh_sach_info[10]}')"
        if conn.execute(text(sql)) :
            print("Đã thêm tài khoản thành công !")
        conn.commit()
        conn.close()

def Them_tai_khoan_HS(Danh_sach_info) :
    with engine.connect() as conn:
        sql = f"INSERT INTO hocsinh \
                VALUES ({Danh_sach_info[0]},'{Danh_sach_info[1]}','{Danh_sach_info[2]}','{Danh_sach_info[3]}','{Danh_sach_info[4]}','{Danh_sach_info[5]}','{Danh_sach_info[6]}','{Danh_sach_info[7]}','{Danh_sach_info[8]}',{Danh_sach_info[9]},{Danh_sach_info[10]}); \
                INSERT INTO bangdiem(IDHocSinh, IDMon) VALUES ({Danh_sach_info[0]}, 1); \
                INSERT INTO bangdiem(IDHocSinh, IDMon) VALUES ({Danh_sach_info[0]}, 2); \
                INSERT INTO bangdiem(IDHocSinh, IDMon) VALUES ({Danh_sach_info[0]}, 3); \
                INSERT INTO bangdiem(IDHocSinh, IDMon) VALUES ({Danh_sach_info[0]}, 4); \
                INSERT INTO bangdiem(IDHocSinh, IDMon) VALUES ({Danh_sach_info[0]}, 5); \
                UPDATE lop SET TongSoHS = TongSoHS + 1 WHERE IDLop = {Danh_sach_info[9]}"
        if conn.execute(text(sql)) :
            print("Đã thêm tài khoản thành công !")
        conn.commit()
        conn.close()



def Profile_Quan_li(TaiKhoan):
    ql1 = db_session.query(QuanLi).filter(QuanLi.TenDangNhap == TaiKhoan).first()
    ql = {"HoVaTen": ql1.HoVaTen, "GioiTinh": ql1.GioiTinh, "NgaySinh": datetime.strptime(ql1.NgaySinh,'%Y-%m-%d' ).date(), "Email": ql1.Email, "DiaChi" : ql1.DiaChi,
         "SoDienThoai": ql1.SoDienThoai, "ID_GV": ql1.IDQuanLi}
    return ql

def Doc_danh_sach_gv_CSDL():
    with engine.connect() as conn:
        list_dsgv = []
        cursor = conn.execute(text("SELECT * FROM giaovien"))
        for row in cursor:
            list_dsgv.append(row)
        conn.commit()
        conn.close()
    return list_dsgv

def Doc_danh_sach_gv():
    Danh_sach = []
    danh_sach_gv = Doc_danh_sach_gv_CSDL()
    for GiaoVien in danh_sach_gv:
        info_gv = {}
        info_gv["IDGiaoVien"] = GiaoVien[0]
        info_gv["TenDangNhap"] = GiaoVien[1]
        info_gv["HoVaTen"] = GiaoVien[3]
        info_gv["GioiTinh"] = GiaoVien[4]
        info_gv["DiaChi"] = GiaoVien[5]
        info_gv["Email"] = GiaoVien[6]
        info_gv["NgaySinh"] = GiaoVien[7]
        info_gv["SoDienThoai"] = GiaoVien[8]
        info_gv["TrinhDo"] = GiaoVien[9]
        info_gv["ChuyenMon"] = GiaoVien[10]
        Danh_sach.append(info_gv)
    return Danh_sach

def Lay_info_theo_IDgv(TaiKhoan, Danh_sach_GV):
    Danh_sach=list(filter(
        lambda GiaoVien : str(TaiKhoan).strip() == str(GiaoVien["IDGiaoVien"]).strip() ,Danh_sach_GV))
    return Danh_sach[0]

def Lay_info_theo_TK(TaiKhoan, Danh_sach_GV):
    Danh_sach=list(filter(
        lambda GiaoVien : str(TaiKhoan).strip() == str(GiaoVien["TenDangNhap"]).strip() ,Danh_sach_GV))
    return Danh_sach[0]

def Doc_danh_sach_hs_CSDL():
    with engine.connect() as conn:
        list_dshs = []
        cursor = conn.execute(text("SELECT * FROM hocsinh"))
        for row in cursor:
            list_dshs.append(row)
        conn.commit()
        conn.close()
    return list_dshs

def Doc_danh_sach_NK_CSDL():
    with engine.connect() as conn:
        list_dshs = []
        cursor = conn.execute(text("SELECT * FROM nienkhoa"))
        for row in cursor:
            list_dshs.append(row)
        conn.commit()
        conn.close()
    return list_dshs

def Doc_danh_sach_Lop_CSDL():
    with engine.connect() as conn:
        list_dshs = []
        cursor = conn.execute(text("SELECT * FROM lop"))
        for row in cursor:
            list_dshs.append(row)
        conn.commit()
        conn.close()
    return list_dshs

def Doc_danh_sach_hs():
    Danh_sach = []
    danh_sach_hs = Doc_danh_sach_hs_CSDL()
    danh_sach_nk = Doc_danh_sach_NK_CSDL()
    danh_sach_lop = Doc_danh_sach_Lop_CSDL()
    for HocSinh in danh_sach_hs:
        info_hs = {}
        info_hs["IDHocSinh"] = HocSinh[0]
        info_hs["HoVaTen"] = HocSinh[2]
        info_hs["GioiTinh"] = HocSinh[3]
        info_hs["DiaChi"] = HocSinh[4]
        info_hs["Email"] = HocSinh[5]
        info_hs["NgaySinh"] = HocSinh[6]
        info_hs["SoDienThoai"] = HocSinh[7]
        info_hs["SoDienThoaiPhuHuynh"] = HocSinh[8]
        info_hs["IDLop"] = HocSinh[9]
        i = 0
        while True :
            if HocSinh[9] == danh_sach_lop[i][0] :
                info_hs['Lop'] = danh_sach_lop[i][1]
                break
            i+=1

        info_hs["IDNienKhoa"] = HocSinh[10]
        i = 0
        while True :
            if HocSinh[10] == danh_sach_nk[i][0] :
                info_hs['NienKhoa'] = danh_sach_nk[i][1]
                break
            i += 1
        Danh_sach.append(info_hs)
    return Danh_sach

def Lay_info_theo_ID(ID, Danh_sach_HS):
    Danh_sach=list(filter(
        lambda HocSinh : str(ID).strip() == str(HocSinh["IDHocSinh"]).strip() ,Danh_sach_HS))
    return Danh_sach[0]

def ql_doi_mat_khau(TaiKhoan, MatkhauCu, MatkhauMoi):
    ThongBao = ""
    ql = db_session.query(QuanLi).filter(QuanLi.TenDangNhap == TaiKhoan).first()
    if MatkhauCu != ql.MatKhau:
        ThongBao = "Mật khẩu không khớp"
    else:
        ql.MatKhau = MatkhauMoi
        db_session.flush()
        db_session.commit()
        ThongBao = "Đổi Mật Khẩu Thành Công"
    return ThongBao

def ql_dat_mk_choHS(ds, MatKhauMacDinh):
    encrypt_pw = bcrypt.generate_password_hash(MatKhauMacDinh).decode("utf-8")
    with engine.connect() as conn:
        sql = f"UPDATE hocsinh set MatKhau = '{encrypt_pw}' WHERE IDHocSinh = {ds['IDHocSinh']}"
        if conn.execute(text(sql)):
            ThongBao = "Khôi Phục Mật Khẩu Thành Công"
        conn.commit()
        conn.close()
    return ThongBao

def ql_dat_mk_choGV(ds, MatKhauMacDinh):
    encrypt_pw = bcrypt.generate_password_hash(MatKhauMacDinh).decode("utf-8")
    with engine.connect() as conn:
        sql = f"UPDATE giaovien set MatKhau = '{encrypt_pw}' WHERE IDGiaoVien = {ds['IDGiaoVien']}"
        if conn.execute(text(sql)):
            ThongBao = "Khôi Phục Mật Khẩu Thành Công"
        conn.commit()
        conn.close()
    return ThongBao

