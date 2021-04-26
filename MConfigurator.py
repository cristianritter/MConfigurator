import os
import parse_config
import wx.adv
import wx
import serial
from serial.tools import list_ports
from threading import Thread
import time

print('Carregando configurações...')
program_name = "MidiConfigurator"
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
configuration = parse_config.ConfPacket()
icon_file = os.path.join(ROOT_DIR, 'icon.png')
configs = configuration.load_config('FADER, AUX1, AUX2, AUX3, AUX4, AUX5, AUX6, AUX7, AUX8')
portascom_description = []
portascom_name = []
OUTPUTS = ['']
for items in configs:
    OUTPUTS.append(items)

def atualiza_portas_com():
    global portascom_description 
    global portascom_name 
    portascom = (list(list_ports.comports()))
    list_ports.comports
    portascom_description = []
    portascom_name = []
    for item in portascom:
        portascom_description.append(item.description)
        portascom_name.append(item.name)

atualiza_portas_com()
seriais = []

try:
    class MyFrame(wx.Frame):    
        def __init__(self):
            title_ = program_name +' - Configurador de Painel Remoto para 01V'
            super().__init__(parent=None, title=title_, pos=(0, 0), size=(800, 760))        
            self.panel = wx.Panel(self)
            self.Bind(wx.EVT_CLOSE, self.OnClose)
            
            coluna = wx.BoxSizer(wx.VERTICAL) 
            
            linha_titulo = wx.BoxSizer(wx.HORIZONTAL)
            texto_titulo = wx.StaticText(self.panel, label=program_name, style=wx.ALIGN_CENTRE_HORIZONTAL, size=(700,50))
            texto_titulo.ForegroundColour = 'White'
            #texto_titulo.BackgroundColour = 'Black'
            
            font = wx.Font(26, family = wx.FONTFAMILY_MODERN, style=0, weight=wx.BOLD, underline=False)
            texto_titulo.SetFont(font)
            linha_titulo.Add(texto_titulo, 0, flag=wx.CENTER, border=0)
            
            linha_labels = wx.BoxSizer(wx.HORIZONTAL)
            fn1txt = wx.StaticText(self.panel, label="FUNÇÃO 1", size=(190,15), style=wx.ALIGN_CENTRE_HORIZONTAL)
            fn1txt.ForegroundColour = 'White'
            fn1txt.BackgroundColour = 'Black'
            fn2txt = wx.StaticText(self.panel, label="FUNÇÃO 2", size=(290,15), style=wx.ALIGN_CENTRE_HORIZONTAL)
            fn2txt.ForegroundColour = 'White'
            fn2txt.BackgroundColour = 'Black'
            linha_labels.Add(fn1txt, flag=wx.CENTER)
            linha_labels.AddSpacer(10)
            linha_labels.Add(fn2txt, flag=wx.CENTER)
            linha_labels.AddSpacer(30)
            
            linha_bt0 = wx.BoxSizer(wx.HORIZONTAL)
            bt0txt = wx.StaticText(self.panel, label="Tecla 0: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt0.Add(bt0txt, 0, flag=wx.CENTER)
            combo00 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt0.Add(combo00, 0, flag=wx.CENTER)
            combo01 = wx.Choice(self.panel, size=(300,25))
            linha_bt0.Add(combo01)
            self.gravar_bt0 = wx.Button(self.panel, label='Gravar')
            linha_bt0.Add(self.gravar_bt0)
            self.gravar_bt0.Bind(wx.EVT_BUTTON, lambda event: self.on_record(0, combo00, combo01))            
            combo00.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo00, combo01))
       
            linha_bt1 = wx.BoxSizer(wx.HORIZONTAL)
            bt1txt = wx.StaticText(self.panel, label="Tecla 1: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt1.Add(bt1txt, 0, flag=wx.CENTER)
            combo10 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt1.Add(combo10)
            combo11 = wx.Choice(self.panel, size=(300,25))
            linha_bt1.Add(combo11)
            self.gravar_bt1 = wx.Button(self.panel, label='Gravar')
            linha_bt1.Add(self.gravar_bt1)
            self.gravar_bt1.Bind(wx.EVT_BUTTON, lambda event: self.on_record(1, combo10, combo11))            
            combo10.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo10, combo11))
            
            linha_bt2 = wx.BoxSizer(wx.HORIZONTAL)
            bt2txt = wx.StaticText(self.panel, label="Tecla 2: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt2.Add(bt2txt, 0, flag=wx.CENTER)
            combo20 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt2.Add(combo20)
            combo21 = wx.Choice(self.panel, size=(300,25))
            linha_bt2.Add(combo21)
            self.gravar_bt2 = wx.Button(self.panel, label='Gravar')
            linha_bt2.Add(self.gravar_bt2)
            self.gravar_bt2.Bind(wx.EVT_BUTTON, lambda event: self.on_record(2, combo20, combo21))            
            combo20.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo20, combo21))
       
            linha_bt3 = wx.BoxSizer(wx.HORIZONTAL)
            bt3txt = wx.StaticText(self.panel, label="Tecla 3: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt3.Add(bt3txt, 0, flag=wx.CENTER)
            combo30 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt3.Add(combo30)
            combo31 = wx.Choice(self.panel, size=(300,25))
            linha_bt3.Add(combo31)
            self.gravar_bt3 = wx.Button(self.panel, label='Gravar')
            linha_bt3.Add(self.gravar_bt3)
            self.gravar_bt3.Bind(wx.EVT_BUTTON, lambda event: self.on_record(3, combo30, combo31))            
            combo30.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo30, combo31))
       
            linha_bt4 = wx.BoxSizer(wx.HORIZONTAL)
            bt4txt = wx.StaticText(self.panel, label="Tecla 4: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt4.Add(bt4txt, 0, flag=wx.CENTER)
            combo40 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt4.Add(combo40)
            combo41 = wx.Choice(self.panel, size=(300,25))
            linha_bt4.Add(combo41)
            self.gravar_bt4 = wx.Button(self.panel, label='Gravar')
            linha_bt4.Add(self.gravar_bt4)
            self.gravar_bt4.Bind(wx.EVT_BUTTON, lambda event: self.on_record(4, combo40, combo41))            
            combo40.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo40, combo41))
       
            linha_bt5 = wx.BoxSizer(wx.HORIZONTAL)
            bt5txt = wx.StaticText(self.panel, label="Tecla 5: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt5.Add(bt5txt, 0, flag=wx.CENTER)
            combo50 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt5.Add(combo50)
            combo51 = wx.Choice(self.panel, size=(300,25))
            linha_bt5.Add(combo51)
            self.gravar_bt5 = wx.Button(self.panel, label='Gravar')
            linha_bt5.Add(self.gravar_bt5)
            self.gravar_bt5.Bind(wx.EVT_BUTTON, lambda event: self.on_record(5, combo50, combo51))            
            combo50.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo50, combo51))
       
            linha_bt6 = wx.BoxSizer(wx.HORIZONTAL)
            bt6txt = wx.StaticText(self.panel, label="Tecla 6: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt6.Add(bt6txt, 0, flag=wx.CENTER)
            combo60 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt6.Add(combo60)
            combo61 = wx.Choice(self.panel, size=(300,25))
            linha_bt6.Add(combo61)
            self.gravar_bt6 = wx.Button(self.panel, label='Gravar')
            linha_bt6.Add(self.gravar_bt6)
            self.gravar_bt6.Bind(wx.EVT_BUTTON, lambda event: self.on_record(6, combo60, combo61))            
            combo60.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo60, combo61))
       
            linha_bt7 = wx.BoxSizer(wx.HORIZONTAL)
            bt7txt = wx.StaticText(self.panel, label="Tecla 7: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt7.Add(bt7txt, 0, flag=wx.CENTER)
            combo70 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt7.Add(combo70)
            combo71 = wx.Choice(self.panel, size=(300,25))
            linha_bt7.Add(combo71)
            self.gravar_bt7 = wx.Button(self.panel, label='Gravar')
            linha_bt7.Add(self.gravar_bt7)
            self.gravar_bt7.Bind(wx.EVT_BUTTON, lambda event: self.on_record(7, combo70, combo71))            
            combo70.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo70, combo71))
       
            linha_bt8 = wx.BoxSizer(wx.HORIZONTAL)
            bt8txt = wx.StaticText(self.panel, label="Tecla 8: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt8.Add(bt8txt, 0, flag=wx.CENTER)
            combo80 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt8.Add(combo80)
            combo81 = wx.Choice(self.panel, size=(300,25))
            linha_bt8.Add(combo81)
            self.gravar_bt8 = wx.Button(self.panel, label='Gravar')
            linha_bt8.Add(self.gravar_bt8)
            self.gravar_bt8.Bind(wx.EVT_BUTTON, lambda event: self.on_record(8, combo80, combo81))            
            combo80.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo80, combo81))
       
            linha_bt9 = wx.BoxSizer(wx.HORIZONTAL)
            bt9txt = wx.StaticText(self.panel, label="Tecla 9: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt9.Add(bt9txt, 0, flag=wx.CENTER)
            combo90 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt9.Add(combo90)
            combo91 = wx.Choice(self.panel, size=(300,25))
            linha_bt9.Add(combo91)
            self.gravar_bt9 = wx.Button(self.panel, label='Gravar')
            linha_bt9.Add(self.gravar_bt9)
            self.gravar_bt9.Bind(wx.EVT_BUTTON, lambda event: self.on_record(9, combo90, combo91))            
            combo90.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo90, combo91))
       
            linha_bt10 = wx.BoxSizer(wx.HORIZONTAL)
            bt10txt = wx.StaticText(self.panel, label="Tecla 10: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt10.Add(bt10txt, 0, flag=wx.CENTER)
            combo100 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt10.Add(combo100)
            combo101 = wx.Choice(self.panel, size=(300,25))
            linha_bt10.Add(combo101)
            self.gravar_bt10 = wx.Button(self.panel, label='Gravar')
            linha_bt10.Add (self.gravar_bt10)
            self.gravar_bt10.Bind(wx.EVT_BUTTON, lambda event: self.on_record(10, combo100, combo101))            
            combo100.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo100, combo101))
       
            linha_bt11 = wx.BoxSizer(wx.HORIZONTAL)
            bt11txt = wx.StaticText(self.panel, label="Tecla 11: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt11.Add(bt11txt, 0, flag=wx.CENTER)
            combo110 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt11.Add(combo110)
            combo111 = wx.Choice(self.panel, size=(300,25))
            linha_bt11.Add(combo111)
            self.gravar_bt11 = wx.Button(self.panel, label='Gravar')
            linha_bt11.Add (self.gravar_bt11)
            self.gravar_bt11.Bind(wx.EVT_BUTTON, lambda event: self.on_record(11, combo110, combo111))            
            combo110.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo110, combo111))

            linha_bt12 = wx.BoxSizer(wx.HORIZONTAL)
            bt12txt = wx.StaticText(self.panel, label="Tecla 12: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt12.Add(bt12txt, 0, flag=wx.CENTER)
            combo120 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt12.Add(combo120)
            combo121 = wx.Choice(self.panel, size=(300,25))
            linha_bt12.Add(combo121)
            self.gravar_bt12 = wx.Button(self.panel, label='Gravar')
            linha_bt12.Add (self.gravar_bt12)
            self.gravar_bt12.Bind(wx.EVT_BUTTON, lambda event: self.on_record(12, combo120, combo121))            
            combo120.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo120, combo121))

            linha_bt13 = wx.BoxSizer(wx.HORIZONTAL)
            bt13txt = wx.StaticText(self.panel, label="Tecla 13: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt13.Add(bt13txt, 0, flag=wx.CENTER)
            combo130 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt13.Add(combo130)
            combo131 = wx.Choice(self.panel, size=(300,25))
            linha_bt13.Add(combo131)
            self.gravar_bt13 = wx.Button(self.panel, label='Gravar')
            linha_bt13.Add (self.gravar_bt13)
            self.gravar_bt13.Bind(wx.EVT_BUTTON, lambda event: self.on_record(13, combo130, combo131))            
            combo130.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo130, combo131))

            linha_bt14 = wx.BoxSizer(wx.HORIZONTAL)
            bt14txt = wx.StaticText(self.panel, label="Tecla 14: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt14.Add(bt14txt, 0, flag=wx.CENTER)
            combo140 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt14.Add(combo140)
            combo141 = wx.Choice(self.panel, size=(300,25))
            linha_bt14.Add(combo141)
            self.gravar_bt14 = wx.Button(self.panel, label='Gravar')
            linha_bt14.Add (self.gravar_bt14)
            self.gravar_bt14.Bind(wx.EVT_BUTTON, lambda event: self.on_record(14, combo140, combo141))            
            combo140.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo140, combo141))

            linha_bt15 = wx.BoxSizer(wx.HORIZONTAL)
            bt15txt = wx.StaticText(self.panel, label="Tecla 15: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt15.Add(bt15txt, 0, flag=wx.CENTER)
            combo150 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt15.Add(combo150)
            combo151 = wx.Choice(self.panel, size=(300,25))
            linha_bt15.Add(combo151)
            self.gravar_bt15 = wx.Button(self.panel, label='Gravar')
            linha_bt15.Add (self.gravar_bt15)
            self.gravar_bt15.Bind(wx.EVT_BUTTON, lambda event: self.on_record(15, combo150, combo151))            
            combo150.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo150, combo151))

            linha_bt16 = wx.BoxSizer(wx.HORIZONTAL)
            bt16txt = wx.StaticText(self.panel, label="Tecla 16: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt16.Add(bt16txt, 0, flag=wx.CENTER)
            combo160 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt16.Add(combo160)
            combo161 = wx.Choice(self.panel, size=(300,25))
            linha_bt16.Add(combo161)
            self.gravar_bt16 = wx.Button(self.panel, label='Gravar')
            linha_bt16.Add (self.gravar_bt16)
            self.gravar_bt16.Bind(wx.EVT_BUTTON, lambda event: self.on_record(16, combo160, combo161))            
            combo160.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo160, combo161))

            linha_bt17 = wx.BoxSizer(wx.HORIZONTAL)
            bt17txt = wx.StaticText(self.panel, label="Tecla 17: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt17.Add(bt17txt, 0, flag=wx.CENTER)
            combo170 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt17.Add(combo170)
            combo171 = wx.Choice(self.panel, size=(300,25))
            linha_bt17.Add(combo171)
            self.gravar_bt17 = wx.Button(self.panel, label='Gravar')
            linha_bt17.Add (self.gravar_bt17)
            self.gravar_bt17.Bind(wx.EVT_BUTTON, lambda event: self.on_record(17, combo170, combo171))            
            combo170.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo170, combo171))

            linha_bt18 = wx.BoxSizer(wx.HORIZONTAL)
            bt18txt = wx.StaticText(self.panel, label="Tecla 18: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt18.Add(bt18txt, 0, flag=wx.CENTER)
            combo180 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt18.Add(combo180)
            combo181 = wx.Choice(self.panel, size=(300,25))
            linha_bt18.Add(combo181)
            self.gravar_bt18 = wx.Button(self.panel, label='Gravar')
            linha_bt18.Add (self.gravar_bt18)
            self.gravar_bt18.Bind(wx.EVT_BUTTON, lambda event: self.on_record(18, combo180, combo181))            
            combo180.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo180, combo181))

            linha_bt19 = wx.BoxSizer(wx.HORIZONTAL)
            bt19txt = wx.StaticText(self.panel, label="Tecla 19: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt19.Add(bt19txt, 0, flag=wx.CENTER)
            combo190 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt19.Add(combo190)
            combo191 = wx.Choice(self.panel, size=(300,25))
            linha_bt19.Add(combo191)
            self.gravar_bt19 = wx.Button(self.panel, label='Gravar')
            linha_bt19.Add (self.gravar_bt19)
            self.gravar_bt19.Bind(wx.EVT_BUTTON, lambda event: self.on_record(19, combo190, combo191))            
            combo190.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo190, combo191))

            linha_bt20 = wx.BoxSizer(wx.HORIZONTAL)
            bt20txt = wx.StaticText(self.panel, label="Tecla 20: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt20.Add(bt20txt, 0, flag=wx.CENTER)
            combo200 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt20.Add(combo200)
            combo201 = wx.Choice(self.panel, size=(300,25))
            linha_bt20.Add(combo201)
            self.gravar_bt20 = wx.Button(self.panel, label='Gravar')
            linha_bt20.Add (self.gravar_bt20)
            self.gravar_bt20.Bind(wx.EVT_BUTTON, lambda event: self.on_record(20, combo200, combo201))            
            combo200.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo200, combo201))

            linha_bt21 = wx.BoxSizer(wx.HORIZONTAL)
            bt21txt = wx.StaticText(self.panel, label="Tecla 21: ", style=wx.ALIGN_CENTRE_HORIZONTAL, size=(45,18))
            linha_bt21.Add(bt21txt, 0, flag=wx.CENTER)
            combo210 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,25))
            linha_bt21.Add(combo210)
            combo211 = wx.Choice(self.panel, size=(300,25))
            linha_bt21.Add(combo211)
            self.gravar_bt21 = wx.Button(self.panel, label='Gravar')
            linha_bt21.Add (self.gravar_bt21)
            self.gravar_bt21.Bind(wx.EVT_BUTTON, lambda event: self.on_record(21, combo210, combo211))            
            combo210.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo210, combo211))
            
            self.led1 =  wx.StaticText(self.panel, wx.ID_ANY, label='', size=(20,15))
            ld1txt = wx.StaticText(self.panel, label='Status da Conexão')
            self.led1.SetBackgroundColour('gray')
            self.porta_com = wx.Choice(self.panel, size=(200,25), choices=portascom_description)            
            portacomtxt = wx.StaticText(self.panel, label='Porta: ')
            self.conectar_button = wx.Button(self.panel, label='Conectar')
            self.conectar_button.Bind(wx.EVT_BUTTON, self.conecta_serial)            
            self.desconectar_button = wx.Button(self.panel, label='Desconectar')
            self.desconectar_button.Bind(wx.EVT_BUTTON, self.desconecta_serial)            
            linha_led = wx.BoxSizer(wx.HORIZONTAL)
            linha_led.Add(portacomtxt, 0, wx.CENTER)
            linha_led.Add(self.porta_com, 0, wx.CENTER)
            linha_led.AddSpacer(10)
            linha_led.Add(self.conectar_button, 0, wx.CENTER, 0)
            linha_led.Add(self.desconectar_button, 0, wx.CENTER, 0)
            linha_led.AddSpacer(100)
            linha_led.Add(self.led1, 0, wx.CENTER, 5)
            linha_led.AddSpacer(10)
            linha_led.Add(ld1txt, 0, wx.CENTER, 5)
            
            coluna.AddSpacer(10)
            coluna.Add(linha_titulo, 0, wx.CENTER)
            coluna.AddSpacer(10)
            coluna.Add(linha_labels, 0, wx.CENTER)
            coluna.AddSpacer(10)
            coluna.Add(linha_bt0, 0, wx.CENTER)
            coluna.Add(linha_bt1, 0, wx.CENTER)
            coluna.Add(linha_bt2, 0, wx.CENTER)
            coluna.Add(linha_bt3, 0, wx.CENTER)
            coluna.Add(linha_bt4, 0, wx.CENTER)
            coluna.Add(linha_bt5, 0, wx.CENTER)
            coluna.Add(linha_bt6, 0, wx.CENTER)
            coluna.Add(linha_bt7, 0, wx.CENTER)
            coluna.Add(linha_bt8, 0, wx.CENTER)
            coluna.Add(linha_bt9, 0, wx.CENTER)
            coluna.Add(linha_bt10, 0, wx.CENTER)
            coluna.Add(linha_bt11, 0, wx.CENTER)
            coluna.Add(linha_bt12, 0, wx.CENTER)
            coluna.Add(linha_bt13, 0, wx.CENTER)
            coluna.Add(linha_bt14, 0, wx.CENTER)
            coluna.Add(linha_bt15, 0, wx.CENTER)
            coluna.Add(linha_bt16, 0, wx.CENTER)
            coluna.Add(linha_bt17, 0, wx.CENTER)
            coluna.Add(linha_bt18, 0, wx.CENTER)
            coluna.Add(linha_bt19, 0, wx.CENTER)
            coluna.Add(linha_bt20, 0, wx.CENTER)
            coluna.Add(linha_bt21, 0, wx.CENTER)
            coluna.AddSpacer(30)
            coluna.Add(linha_led, 0, wx.CENTER)
            self.panel.SetSizer(coluna)
            self.Show()
            self.desconectar_button.Hide()

        def conecta_serial(self, event):
            global portascom_name
            global portascom_description
            global seriais
            self.desconectar_button.Show()
            self.conectar_button.Hide()
            self.porta_com.Disable()
            try:
                idx = portascom_description.index(self.porta_com.GetStringSelection())
                ser = serial.Serial(portascom_name[idx] , baudrate=9600)  # open serial port
                if (not ser.is_open):
                    print('aqui')
                    self.desconecta_serial()
                    return
                seriais.append(ser)
                self.led1.SetBackgroundColour('green')
                self.panel.Refresh() 
                print('entrou') 
            except Exception as Err:
                print(Err)
                self.desconecta_serial()
            pass

        def desconecta_serial(self, event=0):
            self.desconectar_button.Hide()
            self.conectar_button.Show()
            self.porta_com.Enable()

            global seriais
            try:
                seriais[0].close()
            except:
                self.error_message()
            seriais.clear()
            self.led1.SetBackgroundColour('gray')
            self.panel.Refresh()
        
        def OnCombo(self, combo_output, combo_funcao):
            try:
                for items in configs[ combo_output.GetStringSelection() ]:
                    combo_funcao.Append(items)
            except:
                pass
        
        def on_record(self, bt_pos, combo_output, combo_funcao):
            try:
                global seriais
                comando = configs[combo_output.GetStringSelection()][combo_funcao.GetStringSelection()]
                lista = comando.split(', ')
                lista_int = []
                lista_int.append(bt_pos)
                for item in lista:
                    lista_int.append(int(item, 16))
                frase = 'REC {}'.format(lista_int)
                payload = bytearray(frase, "utf8")
                seriais[0].flush()
                seriais[0].write(payload)
                seriais[0].write(b'\n')
                print(payload)
                wx.MessageBox("Tecla gravada com sucesso.", "Informação!",
                              wx.ICON_INFORMATION | wx.OK)               
        
            except:
                wx.MessageBox("Selecione os campos de função corretamente antes de gravar.", "Atenção!",
                              wx.ICON_ERROR | wx.OK)               
        def OnClose(self, event):
            if event.CanVeto():
                if wx.MessageBox("Deseja realmente sair?",
                         "Confirmação",
                         wx.ICON_QUESTION | wx.YES_NO) != wx.YES:

                    event.Veto()
                    return
            global seriais
            if (len(seriais) > 0):
                self.desconecta_serial()
            self.Destroy()  # you may also do:  event.Skip()
                    # since the default event handler does call Destroy(), too

        def enable_rec_buttons(self):
            self.gravar_bt0.Enable()
            self.gravar_bt1.Enable()
            self.gravar_bt2.Enable()
            self.gravar_bt3.Enable()
            self.gravar_bt4.Enable()
            self.gravar_bt5.Enable()
            self.gravar_bt6.Enable()
            self.gravar_bt7.Enable()
            self.gravar_bt8.Enable()
            self.gravar_bt9.Enable()
            self.gravar_bt10.Enable()
            self.gravar_bt11.Enable()
            self.gravar_bt12.Enable()
            self.gravar_bt13.Enable()
            self.gravar_bt14.Enable()
            self.gravar_bt15.Enable()
            self.gravar_bt16.Enable()
            self.gravar_bt17.Enable()
            self.gravar_bt18.Enable()
            self.gravar_bt19.Enable()
            self.gravar_bt20.Enable()
            self.gravar_bt21.Enable()
        
        def disable_rec_buttons(self):
            self.gravar_bt0.Disable()
            self.gravar_bt1.Disable()
            self.gravar_bt2.Disable()
            self.gravar_bt3.Disable()
            self.gravar_bt4.Disable()
            self.gravar_bt5.Disable()
            self.gravar_bt6.Disable()
            self.gravar_bt7.Disable()
            self.gravar_bt8.Disable()
            self.gravar_bt9.Disable()
            self.gravar_bt10.Disable()
            self.gravar_bt11.Disable()
            self.gravar_bt12.Disable()
            self.gravar_bt13.Disable()
            self.gravar_bt14.Disable()
            self.gravar_bt15.Disable()
            self.gravar_bt16.Disable()
            self.gravar_bt17.Disable()
            self.gravar_bt18.Disable()
            self.gravar_bt19.Disable()
            self.gravar_bt20.Disable()
            self.gravar_bt21.Disable()

        def error_message(self):
            wx.MessageBox("Erro durante a conexão. Reconecte o dispositivo e tente novamente.", "Atenção!",
                              wx.ICON_ERROR | wx.OK)  

        def testa_serial(self):
            while 1:
                atualiza_portas_com()
                global portascom_name
                global seriais
                for ser in seriais:
                    if ( not (ser.name in portascom_name)):  
                        self.desconecta_serial()
                        self.error_message()
             
                if (len(seriais) > 0):
                    self.enable_rec_buttons()
                else:    
                    self.disable_rec_buttons()

                if (len(self.porta_com.GetStringSelection()) > 0):
                    self.conectar_button.Enable()
                else:
                    self.conectar_button.Disable()
                time.sleep(1)
                    


    if __name__ == "__main__":
        print('Iniciando janela wx...')  
        try:      
            app = wx.App()
            global frame
            frame = MyFrame()
            frame.SetIcon(wx.Icon(icon_file))
            t = Thread(target=frame.testa_serial, daemon=True)
            t.start()
            app.MainLoop()
          
        except Exception as Err:
            print(Err)
          
except Exception as ERR:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
    dire = os.path.join(ROOT_DIR, 'ERRO.TXT')
    f = open(dire, "a")
    f.write(str(ERR))
    f.close()
   

