import os.path
import sys

import pandas as pd
import pymysql
import sqlalchemy
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QFileDialog
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from mould import Ui_mainWindow

conn = create_engine('mysql+mysqlconnector://root:wasdjkl123@localhost:3306/casedb', pool_pre_ping=True)
base = declarative_base(conn)

class casedbimport(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.checkdbconn.clicked.connect(self.checkDBconn)
        #提示信息先隐藏
        self.ui.dbcheckinfolabel.hide()
        self.ui.filecheck.clicked.connect(self.checkflie)
        # 提示信息先隐藏
        self.ui.filecheckinfolabel.hide()
        self.ui.startinputing.clicked.connect(self.startInput)
        self.ui.progressBar.hide()
        # 提示信息先隐藏
        self.ui.startinputinginfolabel.hide()
        self.ui.fileaddr.hide()
    #检查数据库连接
    @Slot()
    def checkDBconn(self):
        self.ui.checkdbconn.setChecked(False)
        try:
            conn = pymysql.connect(host="localhost",port=3306,user="root",password="wasdjkl123",database="casedb",charset="utf8")
            conn.close()
            self.ui.dbcheckinfolabel.setText("数据库连接成功")
            self.ui.dbcheckbox.setCheckable(True)
            self.ui.dbcheckbox.setChecked(True)
        except:
            self.ui.dbcheckinfolabel.setText("数据库连接失败")
            self.ui.dbcheckbox.setChecked(False)
            self.ui.dbcheckbox.setCheckable(False)
        self.ui.dbcheckinfolabel.show()
    #检查要导入的文件格式是否正确
    def checkflie(self):
        self.ui.filecheck.setChecked(False)
        file = QFileDialog.getOpenFileName()[0]
        file_name, file_extension = os.path.splitext(file)
        correctlist =  ['统计日期', '归属地市', '归属县市', '归属区域', '客户经理编码', '客户经理名称',
                       '集团编码', '集团名称', '行业类型', '价值等级', '管会产品分类1', '管会产品分类2',
                       '产品名称', '明细账目项', '明细账目项名称', '是否通服收入', '本月总收入(元)', '去年同期总收入(元)',
                       '本月税后出账收入(元)', '去年同期税后出账收入(元)', '本月税后折扣收入(元)', '去年同期税后折扣收入(元)',
                       '本月税后调账收入(元)', '去年同期税后调账收入(元)', '本月包年分摊收入(元)', '去年同期包年分摊收入(元)',
                       '本月包年费用税后出账金额(元)', '去年包年费用税后出账金额(元)', '本月出账用户数', '去年同期出账用户数',
                       '跨期本期摊销金额(元)', '去年同期跨期本期摊销金额(元)', '跨期本期出账金额(元)', '去年同期跨期本期出账金额(元)',
                       '折前', '是否直管池收入']
        if file_extension == '.csv' :
            self.ui.fileaddr.setText(file)
            with open(file,encoding="gb18030",errors='ignore') as csvfile:
                reader = csv.reader(csvfile)
                for i,rows in enumerate(reader):
                    if i == 0:
                        row = rows
            if row == correctlist:
                self.ui.filecheckinfolabel.setText("文件以及内容格式正确")
                self.ui.filecheckbox.setCheckable(True)
                self.ui.filecheckbox.setChecked(True)
            else:
                # 缺失列的字符
                lostcolumnstr = ""
                if len(correctlist) != len(row):
                    self.ui.fileaddr.setText("")
                    self.ui.filecheckinfolabel.setText("行数错误")
                    self.ui.filecheckbox.setChecked(False)
                    self.ui.filecheckbox.setCheckable(False)
                else:
                    for i in range(0,len(correctlist)):
                        if row[i] != correctlist[i]:
                            lostcolumnstr += correctlist[i]
                            lostcolumnstr += ","
                    self.ui.fileaddr.setText("")
                    self.ui.filecheckinfolabel.setText("以下列缺失 %s " %(lostcolumnstr))
                    self.ui.filecheckbox.setChecked(False)
                    self.ui.filecheckbox.setCheckable(False)

        else:
            self.ui.fileaddr.setText("")
            self.ui.filecheckinfolabel.setText("文件格式错误，请转换成csv格式的文件")
            self.ui.filecheckbox.setChecked(False)
            self.ui.filecheckbox.setCheckable(False)
        self.ui.filecheckinfolabel.show()

    def startInput(self):
        if self.ui.dbcheckbox.isChecked() and self.ui.filecheckbox.isChecked():
            #开始导入
            self.ui.startinputinginfolabel.setText("正在导入")
            self.ui.startinputinginfolabel.show()
            print("----------------->正在导入")
            count = 0
            data = []
            with open(self.ui.fileaddr.text(), encoding="gb18030", errors='ignore') as csvfile:
                reader = csv.reader(csvfile)
                for i, rows in enumerate(reader):
                    if i != 0:
                        data.append(rows)
            print("----------------->表格一共%d条记录" %(len(data)))
            print("----------------->表格数据载入已经完成")
            #conn = pymysql.connect(host="localhost", port=3306, user="root", password="wasdjkl123", database="casedb",
            #                       charset="utf8")
            cursor = sessionmaker(bind=conn)
            session = cursor()
            create_date_sql = "select create_date from casedb_main group by create_date"
            row = session.query(casetable).group_by(casetable.create_date).all()
            old_date = []
            for eachrow in row:
                old_date.append(eachrow.create_date)
            #需要新增的
            addlist = []
            for eachdata in data :
                if eachdata[0] not in old_date:
                    addlist.append(eachdata)
            # 创建dataframe
            df = pd.DataFrame(data=addlist,columns=['create_date', 'city', 'country', 'region', 'manager_id', 'manager_name',
                       'company_id', 'company_name', 'profession', 'grade', 'committee_class', 'committee_subclass',
                       'Eproduct_name', 'account_detail_id', 'account_detail_name', 'is_common_income', 'monthly_total_income', 'monthly_total_income_lastyear',
                       'monthly_income_aftertex', 'monthly_income_aftertex_lastyear', 'monthly_income_aftertex_and_afterdiscount', 'monthly_income_aftertex_and_afterdiscount_lastyear',
                       'monthly_income_aftertex_and_afteradjust', 'monthly_income_aftertex_and_afteradjust_lastyear', 'monthly_yearpack_shared_income', 'monthly_yearpack_shared_income_lastyear',
                       'monthly_yearpack_aftertex_charge_off', 'monthly_yearpack_aftertex_charge_off_lastyear', 'monthly_charge_off_user', 'monthly_charge_off_user_lastyear',
                       'intertemporal_shared', 'intertemporal_shared_lastyear', 'intertemporal_shared_charge_off', 'intertemporal_shared_charge_off_lastyear',
                       'pre_discount', 'is_direct_income'])
            df.to_sql('casedb_main',con=conn,if_exists='append',index=False,chunksize=5000)
            session.close()
            print("----------------->同步成功，一共新增 %d 条数据" %(len(addlist)))
            self.ui.startinputinginfolabel.setText("同步成功，一共新增 %d 条数据" %(len(addlist)))
        else:
            self.ui.startinputinginfolabel.setText("还有通过的项目请检查")



class casetable(base):
    __tablename__ = "casedb_main"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    create_date = sqlalchemy.Column(sqlalchemy.String(50))
    city = sqlalchemy.Column(sqlalchemy.String(50))
    country = sqlalchemy.Column(sqlalchemy.String(50))
    region= sqlalchemy.Column(sqlalchemy.String(50))
    manager_id= sqlalchemy.Column(sqlalchemy.String(50))
    manager_name= sqlalchemy.Column(sqlalchemy.String(50))
    company_id= sqlalchemy.Column(sqlalchemy.String(50))
    company_name= sqlalchemy.Column(sqlalchemy.String(50))
    profession= sqlalchemy.Column(sqlalchemy.String(50))
    grade= sqlalchemy.Column(sqlalchemy.String(50))
    committee_class= sqlalchemy.Column(sqlalchemy.String(50))
    committee_subclass= sqlalchemy.Column(sqlalchemy.String(50))
    Eproduct_name= sqlalchemy.Column(sqlalchemy.String(50))
    account_detail_id= sqlalchemy.Column(sqlalchemy.String(50))
    account_detail_name= sqlalchemy.Column(sqlalchemy.String(50))
    is_common_income= sqlalchemy.Column(sqlalchemy.String(50))
    monthly_total_income = sqlalchemy.Column(sqlalchemy.FLOAT)
    monthly_total_income_lastyear = sqlalchemy.Column(sqlalchemy.FLOAT)
    monthly_income_aftertex = sqlalchemy.Column(sqlalchemy.FLOAT)
    monthly_income_aftertex_lastyear = sqlalchemy.Column(sqlalchemy.FLOAT)
    monthly_income_aftertex_and_afterdiscount = sqlalchemy.Column(sqlalchemy.FLOAT)
    monthly_income_aftertex_and_afterdiscount_lastyear = sqlalchemy.Column(sqlalchemy.FLOAT)
    monthly_income_aftertex_and_afteradjust = sqlalchemy.Column(sqlalchemy.FLOAT)
    monthly_income_aftertex_and_afteradjust_lastyear = sqlalchemy.Column(sqlalchemy.FLOAT)
    monthly_yearpack_shared_income = sqlalchemy.Column(sqlalchemy.FLOAT)
    monthly_yearpack_shared_income_lastyear = sqlalchemy.Column(sqlalchemy.FLOAT)
    monthly_yearpack_aftertex_charge_off = sqlalchemy.Column(sqlalchemy.FLOAT)
    monthly_yearpack_aftertex_charge_off_lastyear = sqlalchemy.Column(sqlalchemy.FLOAT)
    monthly_charge_off_user = sqlalchemy.Column(sqlalchemy.Integer)
    monthly_charge_off_user_lastyear = sqlalchemy.Column(sqlalchemy.Integer)
    intertemporal_shared = sqlalchemy.Column(sqlalchemy.FLOAT)
    intertemporal_shared_lastyear = sqlalchemy.Column(sqlalchemy.FLOAT)
    intertemporal_shared_charge_off = sqlalchemy.Column(sqlalchemy.FLOAT)
    intertemporal_shared_charge_off_lastyear = sqlalchemy.Column(sqlalchemy.FLOAT)
    pre_discount = sqlalchemy.Column(sqlalchemy.FLOAT)
    is_direct_income = sqlalchemy.Column(sqlalchemy.String(50))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    mainWindow = casedbimport()
    mainWindow.show()
    sys.exit(app.exec())
