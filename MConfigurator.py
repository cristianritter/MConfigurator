import os
import parse_config
import wx.adv
import wx
import serial
print('Carregando configurações...')
program_name = "MConfigurator"
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
configuration = parse_config.ConfPacket()
icon_file = os.path.join(ROOT_DIR, 'icon.png')
configs = configuration.load_config('FADERS, AUX2')
print(configs)
ser = serial.Serial('COM44', baudrate=9600)  # open serial port
OUTPUTS = []
for items in configs:
    OUTPUTS.append(items)
try:
    class MyFrame(wx.Frame):    
        def __init__(self):
            title_ = program_name +' - Configurador de Painel Remoto para 01V'
            super().__init__(parent=None, title=title_, style=wx.CAPTION, pos=(5, 5), size=(1080, 600))        
            self.panel = wx.Panel(self)
            
            coluna = wx.BoxSizer(wx.VERTICAL) 
            
            linha_titulo = wx.BoxSizer(wx.HORIZONTAL)
            linha_titulo.Add(wx.StaticText(self.panel, label=program_name), 0, wx.TOP, 20)
            
            linha_labels = wx.BoxSizer(wx.HORIZONTAL)
            linha_labels.Add(wx.StaticText(self.panel, label="Teclas                             OUTPUT                                                                      FUNCAO                                                                 "))

            linha_bt0 = wx.BoxSizer(wx.HORIZONTAL)
            linha_bt0.Add(wx.StaticText(self.panel, label="Tecla 0: "))
            combo00 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,30))
            linha_bt0.Add(combo00)
            combo01 = wx.Choice(self.panel, size=(300,30))
            linha_bt0.Add(combo01)
            gravar_bt0 = wx.Button(self.panel, label='Gravar')
            linha_bt0.Add(gravar_bt0)
            gravar_bt0.Bind(wx.EVT_BUTTON, lambda event: self.on_record(0, combo00, combo01))            
            combo00.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo00, combo01))
       
            linha_bt1 = wx.BoxSizer(wx.HORIZONTAL)
            linha_bt1.Add(wx.StaticText(self.panel, label="Tecla 1: "))
            combo10 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,30))
            linha_bt1.Add(combo10)
            combo11 = wx.Choice(self.panel, size=(300,30))
            linha_bt1.Add(combo11)
            gravar_bt1 = wx.Button(self.panel, label='Gravar')
            linha_bt1.Add(gravar_bt1)
            gravar_bt1.Bind(wx.EVT_BUTTON, lambda event: self.on_record(1, combo10, combo11))            
            combo10.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo10, combo11))
            
            linha_bt2 = wx.BoxSizer(wx.HORIZONTAL)
            linha_bt2.Add(wx.StaticText(self.panel, label="Tecla 2: "))
            combo20 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,30))
            linha_bt2.Add(combo20)
            combo21 = wx.Choice(self.panel, size=(300,30))
            linha_bt2.Add(combo21)
            gravar_bt2 = wx.Button(self.panel, label='Gravar')
            linha_bt2.Add(gravar_bt2)
            gravar_bt2.Bind(wx.EVT_BUTTON, lambda event: self.on_record(2, combo20, combo21))            
            combo20.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo20, combo21))
       
            linha_bt3 = wx.BoxSizer(wx.HORIZONTAL)
            linha_bt3.Add(wx.StaticText(self.panel, label="Tecla 3: "))
            combo30 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,30))
            linha_bt3.Add(combo30)
            combo31 = wx.Choice(self.panel, size=(300,30))
            linha_bt3.Add(combo31)
            gravar_bt3 = wx.Button(self.panel, label='Gravar')
            linha_bt3.Add(gravar_bt3)
            gravar_bt3.Bind(wx.EVT_BUTTON, lambda event: self.on_record(3, combo30, combo31))            
            combo30.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo30, combo31))
       
            linha_bt4 = wx.BoxSizer(wx.HORIZONTAL)
            linha_bt4.Add(wx.StaticText(self.panel, label="Tecla 4: "))
            combo40 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,30))
            linha_bt4.Add(combo40)
            combo41 = wx.Choice(self.panel, size=(300,30))
            linha_bt4.Add(combo41)
            gravar_bt4 = wx.Button(self.panel, label='Gravar')
            linha_bt4.Add(gravar_bt4)
            gravar_bt4.Bind(wx.EVT_BUTTON, lambda event: self.on_record(4, combo40, combo41))            
            combo40.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo40, combo41))
       
            linha_bt5 = wx.BoxSizer(wx.HORIZONTAL)
            linha_bt5.Add(wx.StaticText(self.panel, label="Tecla 5: "))
            combo50 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,30))
            linha_bt5.Add(combo50)
            combo51 = wx.Choice(self.panel, size=(300,30))
            linha_bt5.Add(combo51)
            gravar_bt5 = wx.Button(self.panel, label='Gravar')
            linha_bt5.Add(gravar_bt5)
            gravar_bt5.Bind(wx.EVT_BUTTON, lambda event: self.on_record(5, combo50, combo51))            
            combo50.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo50, combo51))
       
            linha_bt6 = wx.BoxSizer(wx.HORIZONTAL)
            linha_bt6.Add(wx.StaticText(self.panel, label="Tecla 6: "))
            combo60 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,30))
            linha_bt6.Add(combo60)
            combo61 = wx.Choice(self.panel, size=(300,30))
            linha_bt6.Add(combo61)
            gravar_bt6 = wx.Button(self.panel, label='Gravar')
            linha_bt6.Add(gravar_bt6)
            gravar_bt6.Bind(wx.EVT_BUTTON, lambda event: self.on_record(6, combo60, combo61))            
            combo60.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo60, combo61))
       
            linha_bt7 = wx.BoxSizer(wx.HORIZONTAL)
            linha_bt7.Add(wx.StaticText(self.panel, label="Tecla 7: "))
            combo70 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,30))
            linha_bt7.Add(combo70)
            combo71 = wx.Choice(self.panel, size=(300,30))
            linha_bt7.Add(combo71)
            gravar_bt7 = wx.Button(self.panel, label='Gravar')
            linha_bt7.Add(gravar_bt7)
            gravar_bt7.Bind(wx.EVT_BUTTON, lambda event: self.on_record(7, combo70, combo71))            
            combo70.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo70, combo71))
       
            linha_bt8 = wx.BoxSizer(wx.HORIZONTAL)
            linha_bt8.Add(wx.StaticText(self.panel, label="Tecla 8: "))
            combo80 = wx.Choice(self.panel, choices=OUTPUTS, size=(200,30))
            linha_bt8.Add(combo80)
            combo81 = wx.Choice(self.panel, size=(300,30))
            linha_bt8.Add(combo81)
            gravar_bt8 = wx.Button(self.panel, label='Gravar')
            linha_bt8.Add(gravar_bt8)
            gravar_bt8.Bind(wx.EVT_BUTTON, lambda event: self.on_record(8, combo80, combo81))            
            combo80.Bind(wx.EVT_CHOICE, lambda event: self.OnCombo(combo80, combo81))
       
            fechar_button = wx.Button(self.panel, label='Fechar')
            fechar_button.Bind(wx.EVT_BUTTON, self.on_exit)            
            linha_buttons = wx.BoxSizer(wx.HORIZONTAL)
            linha_buttons.Add(fechar_button)
            
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
            coluna.Add(linha_buttons, 0, wx.CENTER)
            
            
            self.panel.SetSizer(coluna)
            self.Show()
        
        def OnCombo(self, combo_output, combo_funcao):
            try:
                for items in configs[ combo_output.GetStringSelection() ]:
                    combo_funcao.Append(items)
            except:
                pass
        
        def on_record(self, bt_pos, combo_output, combo_funcao):
            comando = configs[combo_output.GetStringSelection()][combo_funcao.GetStringSelection()]
            lista = comando.split(', ')
            lista_int = []
            lista_int.append(bt_pos)
            for item in lista:
                lista_int.append(int(item, 16))
            frase = 'REC {}'.format(lista_int)
            payload = bytearray(frase, "utf8")
            ser.write(payload)
            print(payload)

        def on_exit(self, event):
            wx.CallAfter(self.Destroy)
            self.Close()

       
    if __name__ == "__main__":
        print('Iniciando janela wx...')  
        try:      
            app = wx.App()
            frame = MyFrame()
            frame.SetIcon(wx.Icon(icon_file))
            app.MainLoop()

        except Exception as Err:
            print(Err)
            pass

except Exception as ERR:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
    dire = os.path.join(ROOT_DIR, 'ERRO.TXT')
    f = open(dire, "a")
    f.write(str(ERR))
    f.close()
   

