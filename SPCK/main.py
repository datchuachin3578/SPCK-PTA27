import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsColorizeEffect, QMessageBox
from PyQt5.QtCore import QEvent, QTimer, QPoint
from PyQt5.QtGui import QColor
from hover_effect import addHoverEffect
from sidebar_ui import Ui_MainWindow
from PyQt5.QtCore import Qt



class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        #CAC BIEN GLOBAL
        self.store = True
        self.log = False
        self.res = False
        self.out = True
        self.Cart = False
        self.buyed = False
        self.register_users = {}
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.countitem = 0
        #BUTTON ADD IN PAGE_DETAIL

        #CHECK CAC PAGE PRODUCT (DEATAILPG)
        self.Kesach = False
        self.Den = False
        self.Giuong = False
        self.Cay = False
        # Ẩn widget con trước
        self.ui.sb_widget.hide()
        self.ui.sb_acc.hide()
        self.ui.sb_out.hide()
        self.ui.stacked_tong.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(0)
        # Button chuyển trang
        '''SIDE_BAR MAIN'''
        self.ui.bt_home.clicked.connect(self.all)
        self.ui.bt_all.clicked.connect(self.all)
        self.ui.bt_logo.clicked.connect(self.all)
        self.ui.bt_room.clicked.connect(self.room)
        self.ui.bt_table.clicked.connect(self.table)
        self.ui.bt_light.clicked.connect(self.light)
        self.ui.bt_noel.clicked.connect(self.noel)
        self.ui.bt_login.clicked.connect(self.login)
        self.ui.bt_res.clicked.connect(self.resg)
        self.ui.bt_cart.clicked.connect(self.cartft)
        '''LOGIN PAGE'''
        self.ui.bt_login1.clicked.connect(self.login)
        self.ui.bt_log.clicked.connect(self.CheckLogin)
        '''REGISTER PAGE'''
        self.ui.bt_res1.clicked.connect(self.resg)
        self.ui.bt_sup.clicked.connect(self.CheckRegister)
        '''CHECK ACCOUNT LOGIN/REGISTER'''
        self.ui.bt_account.clicked.connect(self.checkAcc)
        self.ui.bt_out.clicked.connect(self.Out)
        self.ui.le_retypePassword.returnPressed.connect(self.CheckRegister)
        self.ui.le_Lg_password.returnPressed.connect(self.CheckLogin)
        '''CART PAGE'''
        self.ui.pb_delete.clicked.connect(self.DeleteItem)
        self.ui.pb_add.clicked.connect(self.cartft)
        self.ui.pb_buy.clicked.connect(self.buy)
        #BUTTON PRODUCT
        '''KỆ SÁCH PAGE'''
        self.ui.bt_kesach.clicked.connect(self.kesach)
        self.ui.bt_preks.clicked.connect(self.preks)
        self.ui.bt_nextks.clicked.connect(self.nextks)
        self.ui.bt_addks.setCheckable(True)
        self.ui.bt_addks.clicked.connect(self.cartft)
        self.ui.bt_buyks.clicked.connect(self.buyindt)
        '''ĐÈN PAGE'''
        self.ui.bt_den.clicked.connect(self.den)
        self.ui.bt_preden.clicked.connect(self.preden)
        self.ui.bt_nextden.clicked.connect(self.nextden)
        self.ui.bt_addd.setCheckable(True)
        self.ui.bt_addd.clicked.connect(self.cartft)
        self.ui.bt_buyd.clicked.connect(self.buyindt)
        '''ĐỆM GIƯỜNG PAGE'''
        self.ui.bt_giuong.clicked.connect(self.giuong)
        self.ui.bt_preg.clicked.connect(self.preg)
        self.ui.bt_nextg.clicked.connect(self.nextg)
        self.ui.bt_addg.setCheckable(True)
        self.ui.bt_addg.clicked.connect(self.cartft)
        self.ui.bt_buyg.clicked.connect(self.buyindt)
        '''ĐÈN PAGE'''
        self.ui.bt_cay.clicked.connect(self.cay)
        self.ui.bt_prec.clicked.connect(self.prec)
        self.ui.bt_nextc.clicked.connect(self.nextc)
        self.ui.bt_addc.setCheckable(True)
        self.ui.bt_addc.clicked.connect(self.cartft)
        self.ui.bt_buyc.clicked.connect(self.buyindt)
        #ENTER INPUT ĐỂ CHUYỂN TỚI TRANG CHỨC NĂNG CART
        self.ui.le_input.returnPressed.connect(self.cartft)

        #ADD EFFECT_HOVER
        from hover_effect import addHoverEffect
        # gắn hover vào từng nút
        addHoverEffect(self.ui.bt_room) 
        addHoverEffect(self.ui.bt_table)
        addHoverEffect(self.ui.bt_light)
        addHoverEffect(self.ui.bt_noel)
        addHoverEffect(self.ui.bt_all)
        addHoverEffect(self.ui.bt_products)
        addHoverEffect(self.ui.bt_home)
        addHoverEffect(self.ui.bt_about)
        addHoverEffect(self.ui.bt_search)
        addHoverEffect(self.ui.bt_account)
        addHoverEffect(self.ui.bt_cart)
        addHoverEffect(self.ui.bt_contact)
        addHoverEffect(self.ui.bt_login)
        addHoverEffect(self.ui.bt_res)
        addHoverEffect(self.ui.bt_log)
        addHoverEffect(self.ui.bt_sup)
        addHoverEffect(self.ui.bt_out)
        addHoverEffect(self.ui.bt_info)
        #HOVER EFECT CART_PAGE
        addHoverEffect(self.ui.pb_showweb)
        addHoverEffect(self.ui.pb_edit)
        addHoverEffect(self.ui.pb_delete)
        addHoverEffect(self.ui.pb_add)
        addHoverEffect(self.ui.pb_buy)
        #HOVER EFFECT bt_buy PRODUCT
        addHoverEffect(self.ui.bt_kesach)
        addHoverEffect(self.ui.bt_den)
        addHoverEffect(self.ui.bt_cay)
        addHoverEffect(self.ui.bt_giuong)
        addHoverEffect(self.ui.bt_den)
        addHoverEffect(self.ui.bt_coc)
        addHoverEffect(self.ui.bt_tranh)
        addHoverEffect(self.ui.bt_ghe)
        addHoverEffect(self.ui.bt_tuong)

        #HOVER EFFECT DEATAIL_PAGE
        '''KE SACH PAGE'''
        addHoverEffect(self.ui.bt_buyks)
        addHoverEffect(self.ui.bt_addks)
        addHoverEffect(self.ui.bt_preks)
        addHoverEffect(self.ui.bt_nextks)
        '''DEN PAGE'''
        addHoverEffect(self.ui.bt_buyd)
        addHoverEffect(self.ui.bt_addd)
        addHoverEffect(self.ui.bt_preden)
        addHoverEffect(self.ui.bt_nextden)
        '''GIUONG PAGE'''
        addHoverEffect(self.ui.bt_buyg)
        addHoverEffect(self.ui.bt_addg)
        addHoverEffect(self.ui.bt_preg)
        addHoverEffect(self.ui.bt_nextg)
        '''CAY PAGE'''
        addHoverEffect(self.ui.bt_buyc)
        addHoverEffect(self.ui.bt_addc)
        addHoverEffect(self.ui.bt_prec)
        addHoverEffect(self.ui.bt_nextc)
        '''ROOM PAGE'''
        addHoverEffect(self.ui.bt_den)
        addHoverEffect(self.ui.bt_coc)
        addHoverEffect(self.ui.bt_tranh)
        addHoverEffect(self.ui.bt_ghe)
        addHoverEffect(self.ui.bt_tuong)
        '''GIUONG PAGE'''



        self.ui.bt_res1.setStyleSheet("""
            QPushButton {
                border: 0px;
                color: rgb(0, 0, 0);
                font: 75 20pt "8514oem";
                background: 0
            }
            QPushButton:hover {
                text-decoration: underline;
            }
            """)
        self.ui.bt_login1.setStyleSheet("""
            QPushButton {
                border: 0px;
                color: rgb(0, 0, 0);
                font: 75 20pt "8514oem";
                background: 0
            }
            QPushButton:hover {
                text-decoration: underline;
            }
            QPushButton:pressed {
                background-color: 0;     
            }
            """)

                # ============= TIMER CHO 2 MENU HOVER =============
        #Count thời gian cho sb_widget
        self.closetimer = QTimer(self)
        self.closetimer.setSingleShot(True)# Timer chỉ chạy 1 lần rồi tự dừng #Vì ta chỉ muốn ẩn menu 1 lần khi chuột rời đi, không cần lặp lại.
        self.closetimer.setInterval(50)# Đặt thời gian delay = 200 milliseconds (0.2 giây)
        self.closetimer.timeout.connect(self.ui.sb_widget.hide)
        #Count thời gian cho sb_acc
        self.close_timer = QTimer(self)        
        self.close_timer.setSingleShot(True)
        self.close_timer.setInterval(50)
        self.close_timer.timeout.connect(self.ui.sb_acc.hide)
        #Count thời gian cho sb_out
        self.close_timero = QTimer(self)        
        self.close_timero.setSingleShot(True)
        self.close_timero.setInterval(1000)
        self.close_timero.timeout.connect(self.ui.sb_out.hide)
        #Cai event cho cac widgets
        self.ui.bt_account.installEventFilter(self)
        self.ui.sb_acc.installEventFilter(self)
        self.ui.bt_products.installEventFilter(self)
        self.ui.sb_widget.installEventFilter(self)
        self.ui.bt_out.installEventFilter(self)
        self.ui.sb_out.installEventFilter(self)

    def eventFilter(self, obj, event): #eventFilter hàm trong Qtdes (bắt buộc đúng cú pháp), obj; loại widget đang xảy ra(di chuột vào bt_product => obj = bt_products), event: loại sự kiện xảy ra 
        if event.type() not in (QEvent.Enter, QEvent.Leave): #QEvent.Enter = chuột vừa vào vùng của widget, QEvent.Leave = chuột vừa rời khỏi vùng của widget
            return super().eventFilter(obj, event)

        # ============= MENU ACCOUNT =============
        if self.out == True:
            if obj in (self.ui.bt_account, self.ui.sb_acc): #obj xảy ra với bt_account hoặc là sb_acc
                if event.type() == QEvent.Enter: #thì loại event sẽ là chuột chạm vào bt_account hoặc sb_acc
                    self.close_timer.stop() #từ đó => KHÔNG count thời gian nhả chuột khỏi obj
                    if obj == self.ui.bt_account:   #Nếu obj chính bằng bt_account THÌ ---------#
                        self.ui.sb_acc.move(1130, 70)   # vị trí của widget                     #
                        self.ui.sb_acc.show()       #THÌ Hiện lên widget khi chuột trỏ tới obj<=#
                elif event.type() == QEvent.Leave: #Nếu loại event là chuột không trỏ tới obj
                    self.close_timer.start()    #THÌ Count thời gian sau khi nhả chuột khỏi obj
            else:
                self.checkAcc()
        #==========SB_OUT==============================
        if self.out == False:
            if obj in (self.ui.bt_out, self.ui.sb_out):
                if event.type() == QEvent.Enter:
                    self.close_timero.stop()
                    if obj == self.ui.bt_out:
                        self.ui.sb_out.move(1130, 70)   # vị trí của bạn
                        self.ui.sb_out.show()
                elif event.type() == QEvent.Leave:
                    self.close_timero.start()
        # ============= MENU PRODUCTS =============
        if obj in (self.ui.bt_products, self.ui.sb_widget):
            if event.type() == QEvent.Enter:
                self.closetimer.stop()
                if obj == self.ui.bt_products:
                    self.ui.sb_widget.move(540, -5)   # vị trí của bạn
                    self.ui.sb_widget.show()
            elif event.type() == QEvent.Leave:
                self.closetimer.start()

        return super().eventFilter(obj, event)
        
    #===========================================================================================#
    def Out(self):
        self.ui.stacked_tong.setCurrentWidget(self.ui.page_log)
        self.ui.sb_out.close()
        self.ui.list_item.clear()
        self.out = True
    def checkAcc(self):
        if self.out == True:
            next
        else:
            self.ui.sb_out.move(1130, 70)   # vị trí của bạn
            self.ui.sb_out.show()
            self.close_timero.start()
    def login(self):
        self.store = False
        self.res = False
        self.log = True
        self.ui.stacked_tong.setCurrentWidget(self.ui.page_log)
        self.checkpage()
    def resg(self):
        self.store = False
        self.log = False
        self.res = True
        self.ui.stacked_tong.setCurrentWidget(self.ui.page_res)
        self.checkpage()
    def room(self):
        self.store = True
        self.log = False
        self.res = False
        self.ui.stackedWidget.setCurrentWidget(self.ui.room)
        self.checkpage()
    def table(self):
        self.store = True
        self.log = False
        self.res = False
        self.ui.stackedWidget.setCurrentWidget(self.ui.table)
        self.checkpage()
    def light(self):
        self.store = True
        self.log = False
        self.res = False
        self.ui.stackedWidget.setCurrentWidget(self.ui.light)
        self.checkpage()
    def noel(self):
        self.store = True
        self.log = False
        self.res = False
        self.ui.stackedWidget.setCurrentWidget(self.ui.noel)
        self.checkpage()
    def all(self):
        self.store = True
        self.log = False
        self.res = False
        self.ui.stackedWidget.setCurrentWidget(self.ui.all)
        self.checkpage()
    
        
    def cart(self): #Set cho page_cart = True
        msgBox = QMessageBox()
        if self.out == True:
            msgBox.warning(self, "*_*", "Cần đăng nhập để vào giỏ hàng!")
            self.login()
    def cartft(self,sender):
        msgBox = QMessageBox()
        name = self.ui.le_input.text()
        c_len = len(name)
        sender = self.sender()  # ← DÒNG THẦN THÁNH: biết được nút nào bấm vào
        if self.out == False:
            if self.ui.bt_cart.clicked:
                self.Cart = True
                self.checkpage()
                if c_len >= 1:
                    self.ui.list_item.addItem(name)
                    self.ui.le_input.clear()
                    self.ui.le_input.setFocus()
                    self.countitem += 1
                    msgBox.information(self, "Thong bao", f'Da them {name} vao list thanh cong')
            # Nếu bấm nút "ADD Kệ sách"
            if sender == self.ui.bt_addks:
                self.ui.list_item.addItem("KỆ SÁCH TRANG TRÍ PHÒNG")
                msgBox.information(self, "!", "Đã thêm KỆ SÁCH vào giỏ hàng")
                self.ui.bt_addks.setChecked(False)  # bỏ check
                self.countitem += 1
            # Nếu bấm nút "ADD DEN NGU"
            elif sender == self.ui.bt_addd:
                self.ui.list_item.addItem("ĐÈN NGỦ (ÁNH SÁNG VÀNG NHẠT) TRANG TRÍ PHÒNG")
                msgBox.information(self, "!", "Đã thêm ĐÈN NGỦ vào giỏ hàng")
                self.ui.bt_addd.setChecked(False)  # bỏ check
                self.countitem += 1
            # Nếu bấm nút "ADD GIUONG"
            elif sender == self.ui.bt_addg:
                self.ui.list_item.addItem("ĐỆM GIƯỜNG")
                msgBox.information(self, "!", "Đã thêm ĐỆM GIƯỜNG vào giỏ hàng")
                self.ui.bt_addg.setChecked(False)  # bỏ check
                self.countitem += 1
            # Nếu bấm nút "ADD CAY"
            elif sender == self.ui.bt_addc:
                self.ui.list_item.addItem("ĐỆM GIƯỜNG")
                msgBox.information(self, "!", "Đã thêm CÂY GIẢ vào giỏ hàng")
                self.ui.bt_addc.setChecked(False)  # bỏ check
                self.countitem += 1
        else:
            self.cart()
    def DeleteItem(self):
        msgBox = QMessageBox()
        selected_item = self.ui.list_item.currentItem()
        if selected_item:
            # LẤY TÊN THẬT CỦA SẢN PHẨM Ở ĐÂY
            ten_san_pham = selected_item.text()        
            
            # Xóa khỏi listWidget
            self.ui.list_item.takeItem(self.ui.list_item.row(selected_item))
            
            # In tên thật, không in object nữa
            msgBox.information(self, "Thông báo", f'Bạn đã xóa sản phẩm "{ten_san_pham}" thành công')
            self.countitem - 1
        else:
            msgBox.warning(self, "Lỗi", "Chưa chọn sản phẩm mình muốn xóa")
        
        
    #TAO BIEN CHECK CAC STACKED_WIDGETS
    def checkpage(self):
        if not self.store and not self.log:
            self.ui.stacked_tong.setCurrentWidget(self.ui.page_res)
        if not self.store and not self.res:
            self.ui.stacked_tong.setCurrentWidget(self.ui.page_log)
        if not self.res and not self.log:
            self.ui.stacked_tong.setCurrentWidget(self.ui.page_store)
        if self.Cart == True:
            self.ui.stacked_tong.setCurrentWidget(self.ui.page_cart)
            self.Cart = False
    def CheckLogin(self):
        # Lấy dữ liệu từ line edit
        userName = self.ui.le_Lg_email.text()
        self.password = self.ui.le_Lg_password.text()
        msgBox = QMessageBox()
        self.ui.le_Lg_password.clear()
        # Kiểm tra đăng nhập
        if not userName or not self.password:
            msgBox.warning(self, "Lỗi", "Vui lòng nhập đầu đủ thông tin")
        elif userName in self.register_users and self.register_users[userName] == self.password:
            self.store = True
            self.log = False
            self.res = False
            self.out = False
            self.ui.stackedWidget.setCurrentWidget(self.ui.all)
            self.checkpage()
        elif userName not in self.register_users and userName != "1" and self.password != "1":
            msgBox.warning(self, "Lỗi", "Tài khoản không tồn tại")
            self.ui.le_Lg_email.clear()
            self.ui.le_Lg_password.clear()
        elif userName in self.register_users and self.register_users[userName] != self.password:
            msgBox.warning(self, "Lỗi", "Nhập sai mật khẩu!")
            self.ui.le_Lg_password.clear()
        # Sử dụng tài khoản có sẵn
        if userName == "1" and self.password == "1":
            self.store = True
            self.log = False
            self.res = False
            self.out = False
            self.ui.stackedWidget.setCurrentWidget(self.ui.all)
            self.checkpage()
    def CheckRegister(self):
        self.register_users
        # Lấy dữ liệu từ các line edit 
        userName = self.ui.le_email.text()
        self.password = self.ui.le_password.text()
        self.RetypePass = self.ui.le_retypePassword.text()
        self.lenPass = len(self.password) # Độ dài của mật khẩu
        msgBox = QMessageBox()
        
        # Kiểm tra các điều kiện 
        if not userName or not self.password or not self.RetypePass:
            msgBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin")
        elif self.password != self.RetypePass:
            msgBox.warning(self, "Lỗi", "Mật khẩu không trùng nhau")
        elif self.lenPass <6:
            msgBox.warning(self, "Lỗi", "Mật khẩu ít nhất 6 kí tự")
        else:
            self.register_users[userName] = self.password
            msgBox.information(self,"thông báo", "Đăng kí thành công")
            self.store = False
            self.log = True
            self.res = False
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_log)
            self.checkpage()
            userName = self.ui.le_email.clear()
            self.password = self.ui.le_password.clear()
            self.RetypePass = self.ui.le_retypePassword.clear()
    def stacked_tong(self):
        self.ui.stacked_tong.setCurrentWidget(self.ui.detailpg)
        self.stacked_detail()
    def stacked_detail(self):
        if self.Kesach == True:
            self.ui.stacked_detail.setCurrentWidget(self.ui.kesachpg)
            self.Kesach = False
        if self.Den == True:
            self.ui.stacked_detail.setCurrentWidget(self.ui.denpg)
            self.Den = False
        if self.Giuong == True:
            self.ui.stacked_detail.setCurrentWidget(self.ui.giuongpg)
            self.Giuong = False
        if self.Cay == True:
            self.ui.stacked_detail.setCurrentWidget(self.ui.caypg)
            self.Cay = False
    #PAGE KE SACH#
    def kesach(self):
        self.Kesach = True
        self.stacked_tong()  
    '''ĐỔI IMAGE PRODUCT'''
    def nextks(self):
        stacked = self.ui.stacked_kesach
        stacked.setCurrentIndex((stacked.currentIndex() + 1) % stacked.count())

    def preks(self):
        stacked = self.ui.stacked_kesach
        stacked.setCurrentIndex((stacked.currentIndex() - 1) % stacked.count())
    #PAGE DEN#
    def den(self):
        self.Den = True
        self.stacked_tong()

    '''ĐỔI IMAGE PRODUCT'''
    def nextden(self):
        stacked = self.ui.stacked_den 
        stacked.setCurrentIndex((stacked.currentIndex() + 1) % stacked.count())

    def preden(self):
        stacked = self.ui.stacked_den
        stacked.setCurrentIndex((stacked.currentIndex() - 1) % stacked.count() ) #stacked.count(): Đếm tổng số trang trong StackedWidget

    def preks(self):
        stacked = self.ui.stacked_kesach
        stacked.setCurrentIndex((stacked.currentIndex() - 1) % stacked.count())
        
    #PAGE GIUONG#
    def giuong(self):
        self.Giuong = True
        self.stacked_tong()

    '''ĐỔI IMAGE PRODUCT'''
    def nextg(self):
        stacked = self.ui.stacked_giuong
        stacked.setCurrentIndex((stacked.currentIndex() + 1) % stacked.count())

    def preg(self):
        stacked = self.ui.stacked_giuong
        stacked.setCurrentIndex((stacked.currentIndex() - 1) % stacked.count() ) #stacked.count(): Đếm tổng số trang trong StackedWidget

            
    #PAGE GIUONG#
    def cay(self):
        self.Cay = True
        self.stacked_tong()

    '''ĐỔI IMAGE PRODUCT'''
    def nextc(self):
        stacked = self.ui.stacked_cay
        stacked.setCurrentIndex((stacked.currentIndex() + 1) % stacked.count())

    def prec(self):
        stacked = self.ui.stacked_cay
        stacked.setCurrentIndex((stacked.currentIndex() - 1) % stacked.count() ) #stacked.count(): Đếm tổng số trang trong StackedWidget

    def buyindt(self):
        if self.out == False:
            self.countitem = 1
            if self.countitem >= 1:
                self.ui.stacked_tong.setCurrentWidget(self.ui.page_buyed)
                self.ui.list_item.clear()
                self.countitem = 0
        msgBox = QMessageBox()
        if self.out == True:
            msgBox.warning(self, "*_*", "Cần đăng nhập để mua hàng!")
            self.login()

    def buy(self):
        msgBox = QMessageBox()
        if self.out == False:
            if self.countitem >= 1:
                self.ui.stacked_tong.setCurrentWidget(self.ui.page_buyed)
                self.ui.list_item.clear()
                self.countitem = 0
            else:
                msgBox.warning(self, "*_*", "Chưa có sản phẩm trong giỏ hàng")
        else:
            self.cart()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

'''self.slider_timer = QTimer(self)
self.slider_timer.timeout.connect(self.next_image)
self.slider_timer.start(3000)  # 3 giây đổi ảnh
'''