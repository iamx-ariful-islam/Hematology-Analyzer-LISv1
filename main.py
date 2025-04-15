import webbrowser
import os,sys, time
import psutil, platform, threading

from PyQt5 import QtGui, uic, QtCore, QtWidgets


# main window class
class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        uic.loadUi('Components/ui/main_window.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.pb_admin.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pb_api.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pb_pathologists.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pb_doctors.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pb_reference.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pb_report.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pb_statement.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pb_settings.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pb_settings2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pb_login.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pb_help.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pb_minimize.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pb_maximize.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pb_exit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.lb_machine_info.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.lb_1.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.lb_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.lb_system_info.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.connect_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_5.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))
        self.lb_jonakisoft.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0))

        self.statusBar.setStyleSheet("font-family: Bookman Old Style; font-size: 10pt; border-radius: 0; background: white;")
        
        self.status_icon = QtWidgets.QLabel(u"\u2B24 Not ready! ")
        self.status_icon.setStyleSheet("border: none; background: none; color: red;")
        self.statusBar.addWidget(self.status_icon)

        self.status_text = QtWidgets.QLabel('Hematology Analyzer LIS v2023.x (Last Updated 17.02.2025) ')
        self.status_text.setStyleSheet("border: none; background: none;")
        self.statusBar.addWidget(self.status_text)
        
        self.companyInfo = QtWidgets.QLabel(u"\u00A9"+' 2021-'+time.strftime("%Y")+' All rights reserved | Jonaki Soft Network ')
        self.companyInfo.setStyleSheet("border: none; background: none;")
        self.statusBar.addPermanentWidget(self.companyInfo)
        
        self.show()
        threading.Thread(target = self.AnimateSymbol).start()

        self.lb_system.setText('OS: '+platform.system()+platform.release())
        self.lb_arch.setText('HD: '+platform.architecture()[0]+'/'+platform.machine())

        self.ShowHospitalInfo()
        self.ShowMachineInfo()
        
        IPath = 'Components/icons/excbio.ico'
        self.setWindowTitle('HE8300')
        self.setWindowIcon(QtGui.QIcon(IPath))
        self.lb_machine_img.setPixmap(QtGui.QPixmap(IPath))
        self.lb_machine_part.setText('3-Part')
        self.lb_model.setText('M: EH8300')
        self.lb_company_info.setText('ExcBio, China')

        self.lb_date.setText(time.strftime("%d.%m.%Y"))

        self.H, self.M, self.S = 0, 0, 0
        self.running = QtCore.QTimer()
        self.running.timeout.connect(self.TimerCount)
        self.running.start(1000)
        
        self.ctimer = QtCore.QTimer()
        self.ctimer.timeout.connect(self.ShowTime)
        self.ctimer.start(100)
        
        self.Animate = 1
        self.Tanimate = QtCore.QTimer()
        self.Tanimate.timeout.connect(self.Animation)
        self.Tanimate.start(500)

        self.CPUMemory()
        self.cpumtimer = QtCore.QTimer()
        self.cpumtimer.timeout.connect(self.CPUMemory)
        self.cpumtimer.start(60000)

        self.win_check = 0
        self.pb_help.clicked.connect(self.HelpWindow)
        self.pb_minimize.clicked.connect(self.MinimizeWindow)
        self.pb_maximize.clicked.connect(self.MaximizeWindow)
        self.pb_exit.clicked.connect(self.CloseWindow)

        self.lb_jonakisoft.mousePressEvent = self.ShowJonakisoftInfo
        
    def mousePressEvent(self, event):
        if self.win_check == 1:
            self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.win_check == 1:
            try:
                delta = QtCore.QPoint(event.globalPos() - self.oldPosition)
                self.move(self.x() + delta.x(), self.y() + delta.y())
                self.oldPosition = event.globalPos()
            except: QtCore.QPoint(event.globalPos())

    def MachineNetworkConnect(self, host, port):
        print(host, port)

    def ShowJonakisoftInfo(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            webbrowser.open('https://www.jonakisoft.net/')

    def AnimateSymbol(self):
        self.lb_dot1.setText(u"\u25CF"); self.lb_dot2.setText(u"\u25CF"); self.lb_dot3.setText(u"\u25CF"); self.lb_dot4.setText(u"\u25CF")
        i = 0
        while True:
            if i > 7: i = 0
            if i == 1 or i == 7:
                self.lb_dot1.show(); self.lb_dot2.hide(); self.lb_dot3.hide(); self.lb_dot4.hide()
            if i == 2 or i == 6:
                self.lb_dot1.show(); self.lb_dot2.show(); self.lb_dot3.hide(); self.lb_dot4.hide()
            if i == 3 or i == 5:
                self.lb_dot1.show(); self.lb_dot2.show(); self.lb_dot3.show(); self.lb_dot4.hide()
            if i == 4:
                self.lb_dot1.show(); self.lb_dot2.show(); self.lb_dot3.show(); self.lb_dot4.show()
            time.sleep(.25)
            i += 1
        
    def Animation(self):
        self.lb_red.hide()
        if self.lb_connect.text() != 'Connected....!':
            self.lb_green.hide()
            if self.Animate == 1:
                self.Animate = 0
                self.lb_red.hide()
            else:
                self.Animate = 1
                self.lb_red.show()
        else:
            self.status_icon.setText(u"\u2B24 Connected! ")
            self.status_icon.setStyleSheet("border: none; background: none; color: rgb(53, 201, 42);");
            if self.Animate == 1:
                self.Animate = 0
                self.lb_green.hide()
            else:
                self.Animate = 1
                self.lb_green.show()

    def ShowHospitalInfo(self):
        self.lb_hospital_name.setText("Jonaki Soft Network")
        self.lb_hospital_address.setText("Rajshahi Sadar, Rajshahi, Bangladesh")
        self.lb_hospital_mobile.setText("+880 1794899422 | +880 1714732878")

    def ShowMachineInfo(self):
        self.lb_ip_port.setText('127.0.0.1 : 5000')
    
    def HelpWindow(self):
        self.help = MyHelpWindow()

    def MinimizeWindow(self):
        self.showMinimized()

    def MaximizeWindow(self):
        if self.win_check == 0:
            self.showNormal()
            try: self.pb_maximize.setIcon(QtGui.QIcon(QtGui.QPixmap('Components/icons/maximize.png')))
            except: pass
            self.win_check = 1
        else:
            self.showMaximized()
            try: self.pb_maximize.setIcon(QtGui.QIcon(QtGui.QPixmap('Components/icons/restore.png')))
            except: pass
            self.win_check = 0
        
    def CloseWindow(self):
        self.close_window = MyCloseWindow()

    def get_size(self, bytes, suffix="B", factor=1024):
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    def CPUMemory(self):
        CPU  = 0.0
        MM   = 0.0
        FE   = 0.0
        sram = 0.0
        try:
            PID = os.getpid()
            PC  = psutil.Process(PID)
            CPU = PC.cpu_percent()/psutil.cpu_count()
            MM  = PC.memory_full_info().rss/(1024*1024)
            
            for partition in psutil.disk_partitions():
                try: partition_usage = psutil.disk_usage(partition.mountpoint)
                except PermissionError: continue
                FE += partition_usage.free
            
            sram = psutil.swap_memory().free
        except: pass
        self.lb_cpu_memory1.setText('CPU: '+str(CPU)+'%')
        self.lb_cpu_memory2.setText('RAM: '+'{:.2f}MB'.format(MM))
        self.lb_disk_size2.setText('RAM: '+self.get_size(sram))
        self.lb_disk_size1.setText('ROM: '+self.get_size(FE))
        
    def TimerCount(self):
        TF = '{:02d}:{:02d}:{:02d}'.format(self.H, self.M, self.S)
        self.lb_running_time.setText(TF)
        self.S += 1
        if self.S >= 60:
            self.M += 1
            self.S = 0
        if self.M >= 60:
            self.H += 1
            self.M = 0

    def ShowTime(self):
        self.time = QtCore.QDateTime.currentDateTime().toString("hh:mm:ssap")
        self.lb_time.setText(self.time)


# close window class
class MyCloseWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyCloseWindow, self).__init__(parent)
        uic.loadUi('Components/ui/close_window.ui', self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.main_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=10, xOffset=0, yOffset=0))
        self.show(); self.Center()

        self.pb_yes.setFocus()
        
        self.setTabOrder(self.pb_yes, self.pb_no)
        self.setTabOrder(self.pb_no, self.pb_close)
        
        self.pb_yes.clicked.connect(self.CloseProgram)
        self.pb_no.clicked.connect(self.CloseWindow)
        self.pb_close.clicked.connect(self.CloseWindow)
        
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()
        
    def CloseWindow(self):
        self.close()
        
    def CloseProgram(self):
        self.close()
        myID = os.getpid()
        for proc in psutil.process_iter():
            try:
                if proc.pid == myID:
                    proc.kill()
            except: pass
        
    def Center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


# help window class
class MyHelpWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MyHelpWindow, self).__init__(parent)
        uic.loadUi('Components/ui/help_window.ui', self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.main_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=10, xOffset=0, yOffset=0))
        self.show(); self.Center()
        
        self.pb_close.setToolTip('Close')
        self.pb_close.clicked.connect(self.CloseWindow)
        
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

    def CloseWindow(self):
        self.close()
        
    def Center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


# root
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    QtGui.QFontDatabase.addApplicationFont('Components/fonts/Bookman_Old_Style-B.TTF')
    QtGui.QFontDatabase.addApplicationFont('Components/fonts/Bookman_Old_Style-R.TTF')
    
    main_win = MyMainWindow()

    sys.exit(app.exec_())