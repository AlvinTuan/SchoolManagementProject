from flask import Markup, url_for
import json
import os
import sqlite3
from app_school.xu_ly.Xu_ly_Model import engine
from sqlalchemy import text

def Them_lien_he(Danh_sach_info) :
    with engine.connect() as conn:
        sql = f"INSERT INTO LienHe (Nguoi_Gui,Email,Noi_Dung) \
                VALUES ('{Danh_sach_info[0]}','{Danh_sach_info[1]}','{Danh_sach_info[2]}')"
        if conn.execute(text(sql)) :
            print("Đã thêm liên hệ thành công !")
        conn.commit()
        conn.close()
