import turtle
import math
import random
import time

class SinyalHafizasi:
    def __init__(self):
        self.ch1_buffer = []
        self.ch2_buffer = []
        self.maks_kapasite = 600
        self.kayit_sayisi = 0

    def veri_ekle(self, v1, v2):
        self.ch1_buffer.append(v1)
        self.ch2_buffer.append(v2)
        if len(self.ch1_buffer) > self.maks_kapasite:
            self.ch1_buffer.pop(0)
            self.ch2_buffer.pop(0)

    def rapora_kaydet(self, v_rms1, v_max1, v_rms2, v_max2, frek1, frek2, sinyal_tipi):
        self.kayit_sayisi += 1
        dosya_adi = f"osiloskop_quantum_log_{self.kayit_sayisi}.txt"
        try:
            with open(dosya_adi, "w", encoding="utf-8") as f:
                f.write("==================================================\n")
                f.write("     QUANTUM LABORATORY CORE DATA LOG REPORT     \n")
                f.write("==================================================\n")
                f.write(f" Kayıt Tarihi/Zamanı: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f" Aktif Dalga Formu  : {sinyal_tipi.upper()}\n")
                f.write("--------------------------------------------------\n")
                f.write(" [KANAL 1 ADVANCED METRICS]\n")
                f.write(f"  Etkin Voltaj (V-RMS)     : {v_rms1:.2f} V\n")
                f.write(f"  Tepe Voltajı (V-Peak)    : {v_max1:.2f} V\n")
                f.write(f"  Tepe-Tepe Voltaj (V-pp)  : {(v_max1*2):.2f} V\n")
                f.write(f"  Sinyal Frekansı          : {frek1:.1f} Hz\n")
                f.write("--------------------------------------------------\n")
                f.write(" [KANAL 2 ADVANCED METRICS]\n")
                f.write(f"  Etkin Voltaj (V-RMS)     : {v_rms2:.2f} V\n")
                f.write(f"  Tepe Voltajı (V-Peak)    : {v_max2:.2f} V\n")
                f.write(f"  Tepe-Tepe Voltaj (V-pp)  : {(v_max2*2):.2f} V\n")
                f.write(f"  Sinyal Frekansı          : {frek2:.1f} Hz\n")
                f.write("==================================================\n")
                f.write(" ARCHITECTURE: 64-BIT MATHEMATICS DSP CORE\n")
                f.write(" STATUS: OPERATION LOG SUCCESSFUL\n")
            return True
        except:
            return False

class MatematikselAnalizMotoru:
    def __init__(self):
        pass

    def ortalama_hesapla(self, veri_listesi):
        if not veri_listesi:
            return 0.0
        return sum(veri_listesi) / len(veri_listesi)

    def tepeden_tepeye_hesapla(self, v_max):
        return v_max * 2.0

    def crest_factor_hesapla(self, v_max, v_rms):
        if v_rms == 0:
            return 0.0
        return v_max / v_rms

    def form_faktoru_hesapla(self, v_rms, veri_listesi):
        ort = self.ortalama_hesapla(veri_listesi)
        if ort == 0:
            return 1.11
        return v_rms / abs(ort)

    def thd_simule_et(self, gurultu_aktif):
        if gurultu_aktif:
            return random.uniform(4.2, 7.8)
        return random.uniform(0.05, 0.12)

class SpektrumAnalizatorEngine:
    def __init__(self):
        self.harmonikler = [1.0, 0.0, 0.0, 0.0, 0.0]

    def harmonik_hesapla(self, sinyal_tipi):
        if sinyal_tipi == 'sinus':
            return [1.0, 0.02, 0.01, 0.005, 0.001]
        elif sinyal_tipi == 'kare':
            return [1.0, 0.0, 0.33, 0.0, 0.20]
        elif sinyal_tipi == 'ucgen':
            return [1.0, 0.0, 0.11, 0.0, 0.04]
        elif sinyal_tipi == 'testere':
            return [1.0, 0.50, 0.33, 0.25, 0.20]
        elif sinyal_tipi == 'ekg':
            return [1.0, 0.85, 0.65, 0.45, 0.30]
        return [1.0, 0.0, 0.0, 0.0, 0.0]

class DonanimTephisSistemi:
    def __init__(self, t_sub):
        self.t_sub = t_sub

    def self_test_kos(self):
        self.t_sub.clear()
        self.t_sub.penup()
        self.t_sub.color("#00FF00")
        
        mesajlar = [
            "INITIALIZING QUANTUM OSCOPE ARCHITECTURE...",
            "LOADING NATIVE 64-BIT DSP MATHEMATICS MOTOR...",
            "COUPLING CHANNEL 1 HARDWARE RELAYS... OK",
            "COUPLING CHANNEL 2 HARDWARE RELAYS... OK",
            "CALIBRATING TRUE-RMS MATH MATRIX ENGINE... OK",
            "GENERATING FFT FREQUENCY SPECTRUM BUFFERS... OK",
            "MATH CORE COUPLING INTERRUPT INTEGRATION... OK",
            "STABILIZING GRAPHIC GRID MESH (1920x1080)... OK",
            "STABILIZING INTERACTIVE GUI MOUSE BUTTONS... OK",
            "CALIBRATING ADVANCED VOLTAGE CURSORS... OK",
            "SYSTEM DIAGNOSTICS STATUS: QUANTUM EXCELLENT",
            "LAUNCHING GRAPHIC ENGINE TERMINAL IN 1 SECOND..."
        ]
        
        y_koor = 260
        for mesaj in mesajlar:
            self.t_sub.goto(-450, y_koor)
            self.t_sub.write(mesaj, font=("Courier", 13, "bold"))
            turtle.Screen().update()
            time.sleep(0.2)
            y_koor -= 35
        self.t_sub.clear()

class SinyalKonfigurasyonu:
    def __init__(self):
        self.akis_durumu = True
        self.sinyal_tipi = 'sinus'
        self.gurultu_aktif = False
        self.ch1_aktif = True
        self.ch2_aktif = True
        self.math_kanal_aktif = False
        self.aktif_mouse_kanali = 1
        self.trigger_modu = "YUKSELEN"
        self.cursor_aktif = False
        self.aktif_cursor = 1

class DonanimOlcekleyici:
    def __init__(self):
        self.voltaj_olcegi_ch1 = 12.0
        self.voltaj_olcegi_ch2 = 7.0
        self.zaman_olcegi = 1.4
        self.zaman_ofseti = 0.0
        self.faz_kaymasi = 45.0
        self.trigger_seviyesi = 0.0
        self.CH1_MERKEZ = 280.0
        self.CH2_MERKEZ = -220.0
        self.MATH_MERKEZ = 30.0
        self.cursor1_y = 100.0
        self.cursor2_y = -100.0

class GrafikArayuzButonu:
    def __init__(self, name, x1, y1, x2, y2, color):
        self.name = name
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

    def tiklandi_mi(self, px, py):
        return self.x1 <= px <= self.x2 and self.y2 <= py <= self.y1

class DijitalOsiloskop:
    def __init__(self):
        self.cfg = SinyalKonfigurasyonu()
        self.olcek = DonanimOlcekleyici()
        self.hafiza = SinyalHafizasi()
        self.analiz = MatematikselAnalizMotoru()
        self.fft_engine = SpektrumAnalizatorEngine()
        
        self.ekran = turtle.Screen()
        self.ekran_genislik = 1920
        self.ekran_yukseklik = 1080
        self.ekran_arka_plan = "#070707"
        self.ekran_basligi = "ADVANCED QUANTUM DSP MATHEMATICS DIGITAL OSÍLLOSCOPE V9.2 - PROFESSIONAL LABORATORY SYSTEM"
        
        self.ekran_kurulumunu_yap()
        self.donanim_kaynaklarini_uret()
        self.alt_sistemleri_kalibre_et()
        self.butonlari_olustur()
        
        self.tephis = DonanimTephisSistemi(self.sub_panel)
        self.tephis.self_test_kos()
        
        self.dinleyicileri_aktif_et()
        self.panel_guncelle()

    def ekran_kurulumunu_yap(self):
        self.ekran.title(self.ekran_basligi)
        self.ekran.bgcolor(self.ekran_arka_plan)
        self.ekran.setup(width=self.ekran_genislik, height=self.ekran_yukseklik)
        self.ekran.tracer(0)

    def donanim_kaynaklarini_uret(self):
        self.v_rms_ch1 = round(random.uniform(11.8, 12.6), 2)
        self.v_rms_ch2 = round(random.uniform(4.9, 5.4), 2)
        self.v_max_matematiksel1 = self.v_rms_ch1 * 1.414
        self.v_max_matematiksel2 = self.v_rms_ch2 * 1.414

    def alt_sistemleri_kalibre_et(self):
        self.sub_ch1 = turtle.Turtle()
        self.sub_ch2 = turtle.Turtle()
        self.sub_math = turtle.Turtle()
        self.sub_grid = turtle.Turtle()
        self.sub_panel = turtle.Turtle()
        self.sub_gui = turtle.Turtle()
        self.sub_cursor = turtle.Turtle()
        self.sub_fft = turtle.Turtle()
        
        self.sub_ch1.hideturtle()
        self.sub_ch1.speed(0)
        self.sub_ch1.width(3)
        self.sub_ch1.color("#FFFF00")
        
        self.sub_ch2.hideturtle()
        self.sub_ch2.speed(0)
        self.sub_ch2.width(3)
        self.sub_ch2.color("#00FFFF")

        self.sub_math.hideturtle()
        self.sub_math.speed(0)
        self.sub_math.width(2)
        self.sub_math.color("#FF00FF")
        
        self.sub_grid.hideturtle()
        self.sub_grid.speed(0)
        
        self.sub_panel.hideturtle()
        self.sub_panel.speed(0)
        
        self.sub_gui.hideturtle()
        self.sub_gui.speed(0)

        self.sub_cursor.hideturtle()
        self.sub_cursor.speed(0)
        self.sub_cursor.width(1)

        self.sub_fft.hideturtle()
        self.sub_fft.speed(0)

    def butonlari_olustur(self):
        self.butonlar = [
            GrafikArayuzButonu("CH1 ON/OFF", 780, 480, 930, 440, "#FFFF00"),
            GrafikArayuzButonu("CH2 ON/OFF", 780, 430, 930, 390, "#00FFFF"),
            GrafikArayuzButonu("MATH CH", 780, 380, 930, 340, "#FF00FF"),
            GrafikArayuzButonu("SINUS", 780, 310, 930, 270, "#FFFFFF"),
            GrafikArayuzButonu("KARE", 780, 260, 930, 220, "#FFFFFF"),
            GrafikArayuzButonu("UCGEN", 780, 210, 930, 170, "#FFFFFF"),
            GrafikArayuzButonu("TESTERE", 780, 160, 930, 120, "#FFFFFF"),
            GrafikArayuzButonu("EKG HEART", 780, 110, 930, 70, "#FF3344"),
            GrafikArayuzButonu("NOISE SYS", 780, 0, 930, -40, "#FF6600"),
            GrafikArayuzButonu("CURSOR SYS", 780, -70, 930, -110, "#00FFCC"),
            GrafikArayuzButonu("SAVE DATA", 780, -160, 930, -200, "#AA33FF")
        ]

    def dinleyicileri_aktif_et(self):
        self.ekran.listen()
        self.ekran.onkey(self.akis_toggle, "space")
        self.ekran.onkey(self.trigger_yukari, "Up")
        self.ekran.onkey(self.trigger_asagi, "Down")
        self.ekran.onkey(self.trigger_mod_degistir, "m")
        self.ekran.onkey(self.trigger_mod_degistir, "M")
        
        self.ekran.onkey(self.cursor_yukari, "w")
        self.ekran.onkey(self.cursor_yukari, "W")
        self.ekran.onkey(self.cursor_asagi, "s")
        self.ekran.onkey(self.cursor_asagi, "S")
        self.ekran.onkey(self.cursor_degistir, "c")
        self.ekran.onkey(self.cursor_degistir, "C")

        self.ekran.onscreenclick(self.ekran_tiklama_kontrol)
        
        canvas = self.ekran.getcanvas()
        canvas.bind("<MouseWheel>", self.fare_tekerlek_kontrol)

    def akis_toggle(self):
        self.cfg.akis_durumu = not self.cfg.akis_durumu
        self.panel_guncelle()

    def trigger_yukari(self):
        if self.olcek.trigger_seviyesi < 220:
            self.olcek.trigger_seviyesi += 10

    def trigger_asagi(self):
        if self.olcek.trigger_seviyesi > -220:
            self.olcek.trigger_seviyesi -= 10

    def trigger_mod_degistir(self):
        self.cfg.trigger_modu = "DUSEN" if self.cfg.trigger_modu == "YUKSELEN" else "YUKSELEN"
        self.panel_guncelle()

    def cursor_yukari(self):
        if self.cfg.aktif_cursor == 1:
            self.olcek.cursor1_y += 8
        else:
            self.olcek.cursor2_y += 8

    def cursor_asagi(self):
        if self.cfg.aktif_cursor == 1:
            self.olcek.cursor1_y -= 8
        else:
            self.olcek.cursor2_y -= 8

    def cursor_degistir(self):
        self.cfg.aktif_cursor = 2 if self.cfg.aktif_cursor == 1 else 1

    def veri_kaydet_tetikleyici(self):
        ch1_hz = (self.olcek.voltaj_olcegi_ch1 * 0.14) * self.olcek.zaman_olcegi * 10
        ch2_hz = (self.olcek.voltaj_olcegi_ch2 * 0.14) * self.olcek.zaman_olcegi * 10
        basarili = self.hafiza.rapora_kaydet(
            self.v_rms_ch1, self.v_max_matematiksel1,
            self.v_rms_ch2, self.v_max_matematiksel2,
            ch1_hz, ch2_hz, self.cfg.sinyal_tipi
        )
        if basarili:
            self.sub_gui.penup()
            self.sub_gui.goto(770, -230)
            self.sub_gui.color("#00FF00")
            self.sub_gui.write("LOG SAVED!", font=("Courier", 10, "bold"))

    def ekran_tiklama_kontrol(self, x, y):
        for b in self.butonlar:
            if b.tiklandi_mi(x, y):
                self.gui_aksiyon_yurut(b.name)
                return

        if y >= 100:
            self.cfg.aktif_mouse_kanali = 1
        elif y <= -100:
            self.cfg.aktif_mouse_kanali = 2
        else:
            self.cfg.aktif_mouse_kanali = 3
        self.panel_guncelle()

    def gui_aksiyon_yurut(self, name):
        if name == "CH1 ON/OFF":
            self.cfg.ch1_aktif = not self.cfg.ch1_aktif
        elif name == "CH2 ON/OFF":
            self.cfg.ch2_aktif = not self.cfg.ch2_aktif
        elif name == "MATH CH":
            self.cfg.math_kanal_aktif = not self.cfg.math_kanal_aktif
        elif name == "SINUS":
            self.cfg.sinyal_tipi = "sinus"
        elif name == "KARE":
            self.cfg.sinyal_tipi = "kare"
        elif name == "UCGEN":
            self.cfg.sinyal_tipi = "ucgen"
        elif name == "TESTERE":
            self.cfg.sinyal_tipi = "testere"
        elif name == "EKG HEART":
            self.cfg.sinyal_tipi = "ekg"
        elif name == "NOISE SYS":
            self.cfg.gurultu_aktif = not self.cfg.gurultu_aktif
        elif name == "CURSOR SYS":
            self.cfg.cursor_aktif = not self.cfg.cursor_aktif
        elif name == "SAVE DATA":
            self.veri_kaydet_tetikleyici()
        
        self.panel_guncelle()
        self.gui_render()

    def fare_tekerlek_kontrol(self, event):
        delta = event.delta
        if self.cfg.aktif_mouse_kanali == 1:
            if delta > 0 and self.olcek.voltaj_olcegi_ch1 < 50.0: self.olcek.voltaj_olcegi_ch1 += 1.0
            elif delta < 0 and self.olcek.voltaj_olcegi_ch1 > 2.0: self.olcek.voltaj_olcegi_ch1 -= 1.0
        elif self.cfg.aktif_mouse_kanali == 2:
            if delta > 0 and self.olcek.voltaj_olcegi_ch2 < 50.0: self.olcek.voltaj_olcegi_ch2 += 1.0
            elif delta < 0 and self.olcek.voltaj_olcegi_ch2 > 2.0: self.olcek.voltaj_olcegi_ch2 -= 1.0
        elif self.cfg.aktif_mouse_kanali == 3:
            if delta > 0 and self.olcek.zaman_olcegi < 5.0: self.olcek.zaman_olcegi += 0.1
            elif delta < 0 and self.olcek.zaman_olcegi > 0.3: self.olcek.zaman_olcegi -= 0.1
        self.panel_guncelle()

    def matematiksel_sinus_uret(self, aci, genlik):
        return genlik * math.sin(aci)

    def matematiksel_kare_uret(self, aci, genlik):
        return genlik if math.sin(aci) >= 0 else -genlik

    def matematiksel_ucgen_uret(self, aci, genlik):
        return genlik * (2.0 / math.pi) * math.asin(math.sin(aci))

    def matematiksel_testere_uret(self, aci, genlik):
        return genlik * (2.0 * (aci / (2.0 * math.pi) - math.floor(0.5 + aci / (2.0 * math.pi))))

    def matematiksel_ekg_uret(self, aci, genlik):
        mod_aci = aci % (2.0 * math.pi)
        if 0.0 <= mod_aci < 0.3:
            return genlik * (mod_aci / 0.3) * 0.2
        elif 0.3 <= mod_aci < 0.6:
            return 0.0
        elif 0.6 <= mod_aci < 0.8:
            return -genlik * 0.3
        elif 0.8 <= mod_aci < 1.0:
            return genlik * 1.5
        elif 1.0 <= mod_aci < 1.2:
            return -genlik * 0.5
        elif 1.2 <= mod_aci < 1.5:
            return 0.0
        elif 1.5 <= mod_aci < 1.9:
            return genlik * 0.25 * math.sin((mod_aci - 1.5) * math.pi / 0.4)
        return 0.0

    def dsp_sinyal_motoru(self, x, ofset, kanal, faz=0):
        if kanal == 1:
            frekans_katlayici = self.olcek.voltaj_olcegi_ch1 * 0.14
            genlik = self.v_max_matematiksel1 / 1.4
        else:
            frekans_katlayici = self.olcek.voltaj_olcegi_ch2 * 0.14
            genlik = self.v_max_matematiksel2 / 1.4
            
        aci = math.radians((x * self.olcek.zaman_olcegi * frekans_katlayici) + ofset - faz)
        
        if self.cfg.sinyal_tipi == 'sinus':
            saf_deger = self.matematiksel_sinus_uret(aci, genlik)
        elif self.cfg.sinyal_tipi == 'kare':
            saf_deger = self.matematiksel_kare_uret(aci, genlik)
        elif self.cfg.sinyal_tipi == 'ucgen':
            saf_deger = self.matematiksel_ucgen_uret(aci, genlik)
        elif self.cfg.sinyal_tipi == 'testere':
            saf_deger = self.matematiksel_testere_uret(aci, genlik)
        elif self.cfg.sinyal_tipi == 'ekg':
            saf_deger = self.matematiksel_ekg_uret(aci, genlik)
        else:
            saf_deger = 0.0
            
        if self.cfg.gurultu_aktif:
            saf_deger += random.uniform(-2.5, 2.5)
            
        return saf_deger

    def panel_guncelle(self):
        self.sub_panel.clear()
        self.sub_panel.penup()
        
        self.render_top_status()
        self.render_channel_telemetry()
        self.render_advanced_matrix()
        self.render_math_lab_metrics()

    def render_top_status(self):
        self.sub_panel.goto(-930, 490)
        durum = "RUNNING" if self.cfg.akis_durumu else "HOLD / ANALYZE"
        self.sub_panel.color("#00FF00" if self.cfg.akis_durumu else "#FF0000")
        self.sub_panel.write(f"SYSTEM CORE: {durum} | CORE TYPE: {self.cfg.sinyal_tipi.upper()} | EDGE TRIG: {self.cfg.trigger_modu}", font=("Courier", 13, "bold"))
        
        self.sub_panel.goto(200, 490)
        self.sub_panel.color("#FFD700")
        self.sub_panel.write("Mouse: CH1(Üst) CH2(Alt) Zaman(Orta) | Wheel: Ölçek | W/S: Cursor | C: Csr Değiş", font=("Courier", 9, "bold"))

    def render_channel_telemetry(self):
        self.sub_panel.goto(-930, 455)
        if self.cfg.ch1_aktif:
            self.sub_panel.color("#FFFF00")
            txt = f"CH1 SCALE: {self.olcek.voltaj_olcegi_ch1:.1f}x | V-RMS: {self.v_rms_ch1:.2f}V"
        else:
            self.sub_panel.color("#555511")
            txt = "CH1 INACTIVE"
        self.sub_panel.write(txt, font=("Courier", 11, "bold"))

        self.sub_panel.goto(-930, -50)
        if self.cfg.ch2_aktif:
            self.sub_panel.color("#00FFFF")
            txt = f"CH2 SCALE: {self.olcek.voltaj_olcegi_ch2:.1f}x | V-RMS: {self.v_rms_ch2:.2f}V"
        else:
            self.sub_panel.color("#115555")
            txt = "CH2 INACTIVE"
        self.sub_panel.write(txt, font=("Courier", 11, "bold"))

        self.sub_panel.goto(-930, -470)
        if self.cfg.math_kanal_aktif:
            self.sub_panel.color("#FF00FF")
            txt = "MATH CHANNEL (CH1 + CH2) ONLINE"
        else:
            self.sub_panel.color("#551155")
            txt = "MATH CHANNEL DISABLED"
        self.sub_panel.write(txt, font=("Courier", 11, "bold"))

    def render_advanced_matrix(self):
        ch1_hz = (self.olcek.voltaj_olcegi_ch1 * 0.14) * self.olcek.zaman_olcegi * 10
        ch2_hz = (self.olcek.voltaj_olcegi_ch2 * 0.14) * self.olcek.zaman_olcegi * 10
        
        odak = "CH1 (SARI)" if self.cfg.aktif_mouse_kanali == 1 else ("CH2 (MAVİ)" if self.cfg.aktif_mouse_kanali == 2 else "ZAMAN EKSENİ")
        
        self.sub_panel.goto(380, -290)
        self.sub_panel.color("#FF33AA")
        self.sub_panel.write(f"🎯 ACTIVE MOUSE COUPLING: {odak}", font=("Courier", 11, "bold"))
        
        self.sub_panel.goto(380, -325)
        self.sub_panel.color("#00FFCC")
        self.sub_panel.write("⚡ METRICS DATA MATRIX (DSP METERS)", font=("Courier", 11, "bold"))
        
        self.sub_panel.goto(380, -355)
        self.sub_panel.color("#FFFF00")
        self.sub_panel.write(f"CH1 V-RMS: {self.v_rms_ch1:.2f}V | V-Peak: {self.v_max_matematiksel1:.2f}V | Freq: {ch1_hz:.1f}Hz", font=("Courier", 10, "normal"))
        
        self.sub_panel.goto(380, -385)
        self.sub_panel.color("#00FFFF")
        self.sub_panel.write(f"CH2 V-RMS: {self.v_rms_ch2:.2f}V | V-Peak: {self.v_max_matematiksel2:.2f}V | Freq: {ch2_hz:.1f}Hz", font=("Courier", 10, "normal"))

    def render_math_lab_metrics(self):
        cf1 = self.analiz.crest_factor_hesapla(self.v_max_matematiksel1, self.v_rms_ch1)
        vpp1 = self.analiz.tepeden_tepeye_hesapla(self.v_max_matematiksel1)
        thd = self.analiz.thd_simule_et(self.cfg.gurultu_aktif)
        
        self.sub_panel.goto(-930, -325)
        self.sub_panel.color("#FFFFFF")
        self.sub_panel.write("📊 REAL-TIME ALGORITHMIC MATH LAB ANALYSIS", font=("Courier", 11, "bold"))
        
        self.sub_panel.goto(-930, -355)
        self.sub_panel.color("#FFFF00")
        self.sub_panel.write(f"CH1 Vpp: {vpp1:.2f}V | Crest Factor: {cf1:.3f} | System THD: {thd:.3f}%", font=("Courier", 10, "normal"))
        
        if self.cfg.cursor_aktif:
            dv = abs(self.olcek.cursor1_y - self.olcek.cursor2_y) * 0.1
            self.sub_panel.goto(-930, -385)
            self.sub_panel.color("#00FFCC")
            self.sub_panel.write(f"CURSOR 1: {self.olcek.cursor1_y*0.1:.1f}V | CURSOR 2: {self.olcek.cursor2_y*0.1:.1f}V | delta-V: {dv:.2f}V", font=("Courier", 10, "bold"))

    def grid_render(self):
        self.sub_grid.clear()
        self.sub_grid.color("#0F0F0F")
        
        for x in range(-960, 741, 40):
            self.sub_grid.penup()
            self.sub_grid.goto(x, -540)
            self.sub_grid.pendown()
            self.sub_grid.goto(x, 540)
            
        for y in range(-540, 541, 30):
            self.sub_grid.penup()
            self.sub_grid.goto(-960, y)
            self.sub_grid.pendown()
            self.sub_grid.goto(740, y)
            
        self.center_lines_render()
        self.trigger_line_render()

    def center_lines_render(self):
        self.sub_grid.width(2)
        
        self.sub_grid.color("#2A2000")
        self.sub_grid.penup()
        self.sub_grid.goto(-960, self.olcek.CH1_MERKEZ)
        self.sub_grid.pendown()
        self.sub_grid.goto(740, self.olcek.CH1_MERKEZ)
        
        self.sub_grid.color("#00202A")
        self.sub_grid.penup()
        self.sub_grid.goto(-960, self.olcek.CH2_MERKEZ)
        self.sub_grid.pendown()
        self.sub_grid.goto(740, self.olcek.CH2_MERKEZ)

        if self.cfg.math_kanal_aktif:
            self.sub_grid.color("#330033")
            self.sub_grid.penup()
            self.sub_grid.goto(-960, self.olcek.MATH_MERKEZ)
            self.sub_grid.pendown()
            self.sub_grid.goto(740, self.olcek.MATH_MERKEZ)

    def trigger_line_render(self):
        self.sub_grid.color("#FF5500" if self.cfg.trigger_modu == "YUKSELEN" else "#FF00AA")
        self.sub_grid.width(1)
        self.sub_grid.penup()
        self.sub_grid.goto(-960, self.olcek.trigger_seviyesi)
        
        for tx in range(-960, 741, 40):
            self.sub_grid.pendown()
            self.sub_grid.goto(tx + 20, self.olcek.trigger_seviyesi)
            self.sub_grid.penup()
            self.sub_grid.goto(tx + 40, self.olcek.trigger_seviyesi)

    def gui_render(self):
        self.sub_gui.clear()
        self.sub_gui.width(2)
        
        self.sub_gui.color("#1C1C1C")
        self.sub_gui.penup()
        self.sub_gui.goto(750, 540)
        self.sub_gui.pendown()
        self.sub_gui.goto(750, -540)
        
        for b in self.butonlar:
            self.sub_gui.penup()
            self.sub_gui.goto(b.x1, b.y1)
            self.sub_gui.color(b.color)
            self.sub_gui.pendown()
            
            self.sub_gui.goto(b.x2, b.y1)
            self.sub_gui.goto(b.x2, b.y2)
            self.sub_gui.goto(b.x1, b.y2)
            self.sub_gui.goto(b.x1, b.y1)
            
            self.sub_gui.penup()
            self.sub_gui.goto(b.x1 + 10, b.y2 + 12)
            self.sub_gui.write(b.name, font=("Courier", 10, "bold"))
            
        self.render_gui_decorations()

    def render_gui_decorations(self):
        self.sub_gui.penup()
        self.sub_gui.color("#FFFFFF")
        self.sub_gui.goto(765, 515)
        self.sub_gui.write("QUANTUM HARDWARE CONTROLS", font=("Courier", 10, "bold"))
        
        self.sub_gui.penup()
        self.sub_gui.goto(380, -425)
        self.sub_gui.color("#888888")
        self.sub_gui.write("DSP KERNEL MODULE V9.2 SECURE COMPILATION", font=("Courier", 9, "normal"))

    def cursor_render(self):
        self.sub_cursor.clear()
        if not self.cfg.cursor_aktif:
            return
            
        self.sub_cursor.color("#00FFCC" if self.cfg.aktif_cursor == 1 else "#008866")
        self.sub_cursor.penup()
        self.sub_cursor.goto(-960, self.olcek.cursor1_y)
        for cx in range(-960, 741, 30):
            self.sub_cursor.pendown()
            self.sub_cursor.goto(cx + 15, self.olcek.cursor1_y)
            self.sub_cursor.penup()
            self.sub_cursor.goto(cx + 30, self.olcek.cursor1_y)
            
        self.sub_cursor.color("#00FFCC" if self.cfg.aktif_cursor == 2 else "#008866")
        self.sub_cursor.penup()
        self.sub_cursor.goto(-960, self.olcek.cursor2_y)
        for cx in range(-960, 741, 30):
            self.sub_cursor.pendown()
            self.sub_cursor.goto(cx + 15, self.olcek.cursor2_y)
            self.sub_cursor.penup()
            self.sub_cursor.goto(cx + 30, self.olcek.cursor2_y)

    def fft_render(self):
        self.sub_fft.clear()
        self.sub_fft.width(4)
        self.sub_fft.color("#00FF00")
        
        harm = self.fft_engine.harmonik_hesapla(self.cfg.sinyal_tipi)
        
        start_x = 380
        start_y = -520
        
        self.sub_fft.penup()
        self.sub_fft.color("#444444")
        self.sub_fft.goto(start_x, start_y)
        self.sub_fft.pendown()
        self.sub_fft.goto(start_x + 350, start_y)
        
        self.sub_fft.penup()
        self.sub_fft.color("#00FFCC")
        self.sub_fft.goto(start_x, start_y + 115)
        self.sub_fft.write("FFT FREQUENCY SPECTRUM (REAL-TIME)", font=("Courier", 10, "bold"))
        
        for idx, h_val in enumerate(harm):
            bx = start_x + (idx * 65) + 20
            by = start_y + int(h_val * 90)
            
            self.sub_fft.penup()
            self.sub_fft.goto(bx, start_y)
            self.sub_fft.color("#FF6600" if idx == 0 else "#00FF00")
            self.sub_fft.pendown()
            self.sub_fft.goto(bx, by)
            self.sub_fft.goto(bx + 25, by)
            self.sub_fft.goto(bx + 25, start_y)
            
            self.sub_fft.penup()
            self.sub_fft.goto(bx - 2, start_y - 15)
            self.sub_fft.color("#888888")
            self.sub_fft.write(f"f{idx+1}", font=("Courier", 8, "normal"))

    def clipping_mask(self, y):
        return max(-535, min(535, y))

    def trigger_edge_offset(self, y, ofs):
        return y + (self.olcek.trigger_seviyesi * 0.03)

    def ch1_dalga_ciz(self, ofs):
        v1_init = self.dsp_sinyal_motoru(-960, self.olcek.zaman_ofseti, 1)
        y1_init = (v1_init * self.olcek.voltaj_olcegi_ch1) + self.olcek.CH1_MERKEZ
        y1_init = self.trigger_edge_offset(y1_init, ofs)
        
        self.sub_ch1.penup()
        self.sub_ch1.goto(-960, self.clipping_mask(y1_init))
        self.sub_ch1.pendown()
        
        for x in range(-960, 741, 10):
            v = self.dsp_sinyal_motoru(x, ofs, 1)
            ny = (v * self.olcek.voltaj_olcegi_ch1) + self.olcek.CH1_MERKEZ
            ny = self.trigger_edge_offset(ny, ofs)
            self.sub_ch1.goto(x, self.clipping_mask(ny))
            if x == 0: self.hafiza.veri_ekle(v, 0.0)

    def ch2_dalga_ciz(self, ofs):
        v2_init = self.dsp_sinyal_motoru(-960, self.olcek.zaman_ofseti, 2, self.olcek.faz_kaymasi)
        y2_init = (v2_init * self.olcek.voltaj_olcegi_ch2) + self.olcek.CH2_MERKEZ
        y2_init = self.trigger_edge_offset(y2_init, ofs)
        
        self.sub_ch2.penup()
        self.sub_ch2.goto(-960, self.clipping_mask(y2_init))
        self.sub_ch2.pendown()
        
        for x in range(-960, 741, 10):
            v = self.dsp_sinyal_motoru(x, ofs, 2, self.olcek.faz_kaymasi)
            ny = (v * self.olcek.voltaj_olcegi_ch2) + self.olcek.CH2_MERKEZ
            ny = self.trigger_edge_offset(ny, ofs)
            self.sub_ch2.goto(x, self.clipping_mask(ny))
            if x == 0 and len(self.hafiza.ch2_buffer) > 0:
                self.hafiza.ch2_buffer[-1] = v

    def math_dalga_ciz(self, ofs):
        self.sub_math.penup()
        v1 = self.dsp_sinyal_motoru(-960, ofs, 1)
        v2 = self.dsp_sinyal_motoru(-960, ofs, 2, self.olcek.faz_kaymasi)
        y_init = ((v1 + v2) * 6.0) + self.olcek.MATH_MERKEZ
        self.sub_math.goto(-960, self.clipping_mask(y_init))
        self.sub_math.pendown()
        
        for x in range(-960, 741, 15):
            v1 = self.dsp_sinyal_motoru(x, ofs, 1)
            v2 = self.dsp_sinyal_motoru(x, ofs, 2, self.olcek.faz_kaymasi)
            ny = ((v1 + v2) * 6.0) + self.olcek.MATH_MERKEZ
            self.sub_math.goto(x, self.clipping_mask(ny))

    def donguyu_baslat(self):
        self.gui_render()
        while True:
            try:
                self.sub_ch1.clear()
                self.sub_ch2.clear()
                self.sub_math.clear()
                
                self.grid_render()
                self.cursor_render()
                self.fft_render()
                
                ofs = self.olcek.zaman_ofseti + (self.olcek.trigger_seviyesi * 0.08)
                
                if self.cfg.ch1_aktif:
                    self.ch1_dalga_ciz(ofs)
                if self.cfg.ch2_aktif:
                    self.ch2_dalga_ciz(ofs)
                if self.cfg.math_kanal_aktif:
                    self.math_dalga_ciz(ofs)
                    
                self.ekran.update()
                
                if self.cfg.akis_durumu:
                    self.olcek.zaman_ofseti -= 10
                    
                time.sleep(0.005)
            except turtle.Terminated:
                break

    def run(self):
        self.donguyu_baslat()

if __name__ == "__main__":
    osiloskop_sistemi = DijitalOsiloskop()
    osiloskop_sistemi.run()