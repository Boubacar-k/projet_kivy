import pickle

from kivy.clock import Clock
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.material_resources import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker
from kivy.uix.popup import Popup
import mysql.connector


class SeConnecter(Screen):
    def __init__(self,**kwargs):
        super(SeConnecter,self).__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username
        pwd = self.ids.pwd
        username = user.text
        passw = pwd.text

        layout = GridLayout(cols=1, padding=10)
        layout2 = GridLayout(cols=1, padding=10)
        layout3 = GridLayout(cols=1, padding=10)
        layout4 = GridLayout(cols=1, padding=10)


        lbl = Label(text='Aucun champ ne doit être vide !',color="#000000")
        lbl2 = Label(text='Connecter avec succès', color="#000000")
        lbl3 = Label(text="Email ou mot de passe incorrect", color="#000000")
        lbl4 = Label(text='Problème de connexion', color="#000000")
        btn = Button(text='OK', size_hint=(.9, None), size=(200, 50),background_color="#5887FF")
        btn2 = Button(text='OK', size_hint=(.9, None), size=(200, 50), background_color="#5887FF")
        btn3 = Button(text='OK', size_hint=(.9, None), size=(200, 50), background_color="#5887FF")
        btn4 = Button(text='OK', size_hint=(.9, None), size=(200, 50), background_color="#5887FF")

        layout.add_widget(lbl)
        layout.add_widget(btn)
        layout2.add_widget(lbl2)
        layout2.add_widget(btn2)
        layout3.add_widget(lbl3)
        layout3.add_widget(btn3)
        layout4.add_widget(lbl4)
        layout4.add_widget(btn4)

        if (username == "" or passw == ""):

            popup = Popup(title='Erreur!', content=layout,
                          size_hint=(None, None), size=(300, 200),
                          auto_dismiss=False, background="#FFFFFF", title_color="#000000", separator_color="#163586")
            btn.bind(on_press=popup.dismiss)
            popup.open()
        else:
            try:
                sql = "SELECT * FROM personnel WHERE email =%s AND mot_de_passe =%s"
                valeur = (username, passw)
                con = mysql.connector.connect(host="localhost", user="root", password="", database='ParcAuto')
                curser = con.cursor()
                curser.execute(sql, valeur)
                resultat = curser.fetchone()
                if resultat:
                    popup = Popup(title='INFO!', content=layout2,
                                  size_hint=(None, None), size=(300, 200),
                                  auto_dismiss=False, background="#FFFFFF", title_color="#000000",
                                  separator_color="#163586")
                    btn2.bind(on_press=popup.dismiss)
                    popup.open()
                    res = resultat
                    with open("test.pickle", "wb") as outfile:
                        pickle.dump(res, outfile)
                    outfile.close()
                    self.parent.current = "accl"
                    con.close()
                else:
                    popup = Popup(title='Erreur!', content=layout3,
                                  size_hint=(None, None), size=(300, 200),
                                  auto_dismiss=False, background="#FFFFFF", title_color="#000000",
                                  separator_color="#163586")
                    btn3.bind(on_press=popup.dismiss)
                    popup.open()
            except:
                popup = Popup(title='Erreur!', content=layout4,
                              size_hint=(None, None), size=(300, 200),
                              auto_dismiss=False, background="#FFFFFF", title_color="#000000",
                              separator_color="#163586")
                btn4.bind(on_press=popup.dismiss)
                popup.open()


class CreerCompte(Screen):
    def __init__(self,**kwargs):
        super(CreerCompte,self).__init__(**kwargs)
        # Fonction
    def poste(self):
        item = ['PROPRIETAIRE', 'GERANT']
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.menu_fonction(x),
            } for i in item
        ]
        self.menuC = MDDropdownMenu(
            caller=self.ids.fonc,
            items=menu_items,
            width_mult=2.5,
        )
        self.menuC.open()
    def menu_fonction(self, text_item):
        self.ids.fonc.text = text_item
        self.menuC.dismiss()

    # SEXE
    def liste(self):
        item = ['HOMME', 'FEMME']
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.menu_callback(x),
            } for i in item
        ]
        self.menuSexe = MDDropdownMenu(
            caller=self.ids.sexe,
            items=menu_items,
            width_mult=2,
        )
        self.menuSexe.open()

    def menu_callback(self, text_item):
        self.ids.sexe.text = text_item
        self.menuSexe.dismiss()

    # Test
    def validate_user(self):
        prenom = self.ids.prenom.text
        nom = self.ids.nom.text
        dateNaissance = self.ids.age.text
        sexe = self.ids.sexe.text
        email = self.ids.email.text
        fonction = self.ids.fonc.text
        dateInsertion = self.ids.dateIns.text
        telephone = self.ids.tel.text
        nationalite = self.ids.nation.text
        adresse = self.ids.adresse.text
        motDePasse = self.ids.txtPass.text
        confirmer = self.ids.confirm.text
        layout = GridLayout(cols=1, padding=10)
        layout2 = GridLayout(cols=1, padding=10)
        layout3 = GridLayout(cols=1, padding=10)
        layout4 = GridLayout(cols=1, padding=10)

        lbl = Label(text='Aucun champ ne doit être vide !',color="#000000")
        lbl2 = Label(text='le mot de passe et la confirmation\ndoivent être les mêmes', color="#000000")
        lbl3 = Label(text="Votre mot de passe ne doit\npas être inferieur à 8 caractère", color="#000000")
        lbl4 = Label(text='compte créé avec succès ', color="#000000")
        btn = Button(text='OK', size_hint=(.9, None), size=(200, 50),background_color="#5887FF")
        btn2 = Button(text='OK', size_hint=(.9, None), size=(200, 50), background_color="#5887FF")
        btn3 = Button(text='OK', size_hint=(.9, None), size=(200, 50), background_color="#5887FF")
        btn4 = Button(text='OK', size_hint=(.9, None), size=(200, 50), background_color="#5887FF")

        layout.add_widget(lbl)
        layout.add_widget(btn)
        layout2.add_widget(lbl2)
        layout2.add_widget(btn2)
        layout3.add_widget(lbl3)
        layout3.add_widget(btn3)
        layout4.add_widget(lbl4)
        layout4.add_widget(btn4)

        if (prenom == "" or nom == "" or dateNaissance == "" or sexe == "" or email == "" or fonction == ""
                or dateInsertion == "" or telephone == "" or nationalite == "" or adresse == "" or motDePasse == "" or confirmer == ""):

            popup = Popup(title='Erreur!', content=layout,
                          size_hint=(None, None), size=(300, 200),
                          auto_dismiss=False, background="#FFFFFF", title_color="#000000", separator_color="#163586")
            btn.bind(on_press=popup.dismiss)
            popup.open()
        elif (motDePasse != confirmer):
            popup = Popup(title='Erreur!', content=layout2,
                          size_hint=(None, None), size=(300, 200),
                          auto_dismiss=False, background="#FFFFFF", title_color="#000000", separator_color="#163586")
            btn2.bind(on_press=popup.dismiss)
            popup.open()
        elif (len(motDePasse) < 8):
            popup = Popup(title='Erreur!', content=layout3,
                          size_hint=(None, None), size=(300, 200),
                          auto_dismiss=False, background="#FFFFFF", title_color="#000000", separator_color="#163586")
            btn3.bind(on_press=popup.dismiss)
            popup.open()
        else:
            sql = "INSERT INTO personnel(prenom,nom,dateNaissance,sexe,email,fonction,dateIns,telephone," \
                  "nationalite,adresse,mot_de_passe,Confirmer)" \
                  " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
            valeur = (prenom, nom, dateNaissance, sexe, email, fonction, dateInsertion, telephone, nationalite, adresse, motDePasse,confirmer)
            maBase = mysql.connector.connect(host="localhost", user="root", password="", database="ParcAuto")
            mConnect = maBase.cursor()
            mConnect.execute(sql, valeur)
            maBase.commit()
            popup = Popup(title='Succès !', content=layout4,
                          size_hint=(None, None), size=(300, 200),
                          auto_dismiss=False, background="#FFFFFF", title_color="#000000", separator_color="#163586")
            btn4.bind(on_press=popup.dismiss)
            popup.open()
            self.parent.current = "connect"
            maBase.close()

    # Date Insertion
    def on_save(self, instance, value, date_range):
        dte = value

        self.text = "{}-{}-{}".format(dte.year, dte.month, dte.day)
        self.focus = False
        self.ids.dateIns.text = self.text

    def on_cancel(self, instance, value):
        print("retour")

    # Date Naissance
    def save(self, instance, value, date_range):
        dte = value

        self.text = "{}-{}-{}".format(dte.year, dte.month, dte.day)
        self.focus = False
        self.ids.age.text = self.text

    def afficheDate(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def afficheDateN(self):
        date_dialog = MDDatePicker(year=2000, month=1, day=1)
        date_dialog.bind(on_save=self.save, on_cancel=self.on_cancel)
        date_dialog.open()

class Accueil(Screen):
    def __init__(self,**kwargs):
        super(Accueil,self).__init__(**kwargs)
        Clock.schedule_once(self.tab)
        i = list(self.listeVehicule())
        l = list(self.listeLocation())
        #VEHICULE TABLE
        self.data_tables = MDDataTable(
            pos_hint={'center_x': 0.50, 'center_y': 0.500},
            size_hint=(0.990 , 0.80),
            use_pagination=True,
            background_color_header="#5887FF",
            background_color_selected_cell="#D6D6D6",
            check = True,
            column_data=[
                ("Matricule", dp(35)),
                ("Moteur", dp(25)),
                ("Type", dp(13)),
                ("Etat", dp(12)),
                ("Date circulation", dp(20)),
                ("Marque", dp(30)),
                ("Porte", dp(16)),
                ("Place", dp(10)),
                ("Couleur", dp(20)),
                ("Date", dp(20)),
                ("Prix", dp(20)),
                ("Kilometrage", dp(25)),
            ],

            row_data=i,
        )
        #LOCATION TABLE

        self.table = MDDataTable(
            pos_hint={'center_x': 0.50, 'center_y': 0.500},
            size_hint=(0.990, 0.60),
            use_pagination=True,
            background_color_header="#5887FF",
            background_color_selected_cell="#D6D6D6",
            check=True,
            column_data=[
                ("Client", dp(30)),
                ("Lieu livraison", dp(30)),
                ("Vehicule", dp(35)),
                ("Date livraison", dp(30)),
                ("Date retour", dp(30)),
                ("Mode paiement", dp(30)),
                ("Somme", dp(30)),
                ("Date paiement", dp(30)),
                # ("Action", dp(10)),
            ],

            row_data=[
                (

                )
                for i in range(50)
            ],
        )

        # TABLE VENTE

        self.tableVente = MDDataTable(
            pos_hint={'center_x': 0.50, 'center_y': 0.500},
            size_hint=(0.990, 0.60),
            use_pagination=True,
            background_color_header="#5887FF",
            background_color_selected_cell="#D6D6D6",
            check=True,
            column_data=[
                ("id", dp(25)),
                ("Client", dp(40)),
                ("Vehicule", dp(40)),
                ("Date vente", dp(35)),
                ("Mode paiement", dp(35)),
                ("Somme", dp(35)),
                ("Date paiement", dp(35)),
                # ("Action", dp(10)),
            ],

            row_data=[
                (

                )
                for i in range(50)
            ],
        )

        # CLIENT TABLE

        self.tableClient = MDDataTable(
            pos_hint={'center_x': 0.50, 'center_y': 0.500},
            size_hint=(0.990, 0.60),
            use_pagination=True,
            background_color_header="#5887FF",
            background_color_selected_cell="#D6D6D6",
            check=True,
            column_data=[
                ("Id", dp(20)),
                ("Prenom", dp(25)),
                ("Nom", dp(25)),
                ("Sexe", dp(15)),
                ("Nationalité", dp(20)),
                ("Date naissance", dp(30)),
                ("Adresse", dp(20)),
                ("telephone", dp(20)),
                ("Email", dp(25)),
                ("N° permis", dp(20)),
                ("Date", dp(30)),
            ],

            row_data=[
                (

                )
                for i in range(50)
            ],
        )

        # PERSONNEL TABLE

        self.tablePerso = MDDataTable(
            pos_hint={'center_x': 0.50, 'center_y': 0.500},
            size_hint=(0.990, 0.60),
            use_pagination=True,
            background_color_header="#5887FF",
            background_color_selected_cell="#D6D6D6",
            check=True,
            column_data=[
                ("Id", dp(20)),
                ("Prenom", dp(25)),
                ("Nom", dp(25)),
                ("Sexe", dp(15)),
                ("Fonction", dp(20)),
                ("Date naissance", dp(30)),
                ("Adresse", dp(20)),
                ("telephone", dp(20)),
                ("Email", dp(25)),
                ("N° permis", dp(20)),
                ("Date d'embauche", dp(30)),
            ],

            row_data=[
                (

                )
                for i in range(50)
            ],
        )

        # ENTRETIEN TABLE

        self.tableEntre = MDDataTable(
            pos_hint={'center_x': 0.50, 'center_y': 0.500},
            size_hint=(0.700, 0.60),
            use_pagination=True,
            background_color_header="#5887FF",
            background_color_selected_cell="#D6D6D6",
            check=True,
            column_data=[
                ("Id", dp(20)),
                ("Vehicule", dp(25)),
                ("Type d'entretien", dp(25)),
                ("Debut", dp(30)),
                ("Fin", dp(20)),
                ("Somme", dp(20)),
                ("Date de paiement", dp(30)),
            ],

            row_data=[
                (

                )
                for i in range(50)
            ],
        )

        # FOURNISSEUR TABLE

        self.tableFour = MDDataTable(
            pos_hint={'center_x': 0.50, 'center_y': 0.500},
            size_hint=(0.700, 0.60),
            use_pagination=True,
            background_color_header="#5887FF",
            background_color_selected_cell="#D6D6D6",
            check=True,
            column_data=[
                ("Id", dp(20)),
                ("Nom", dp(25)),
                ("Email", dp(25)),
                ("Adresse", dp(30)),
                ("Numero", dp(20)),
                ("Pays", dp(20)),
                ("Date", dp(30)),
            ],

            row_data=[
                (

                )
                for i in range(50)
            ],
        )

        # APPROVISIONNEMENT TABLE

        self.tableAppro = MDDataTable(
            pos_hint={'center_x': 0.50, 'center_y': 0.500},
            size_hint=(0.700, 0.60),
            use_pagination=True,
            background_color_header="#5887FF",
            background_color_selected_cell="#D6D6D6",
            check=True,
            column_data=[
                ("Id", dp(20)),
                ("Fournisseur", dp(25)),
                ("Nombre", dp(25)),
                ("Date de commande", dp(30)),
                ("Date de livraison", dp(20)),
                ("Somme", dp(20)),
                ("Date de paiement", dp(30)),
            ],

            row_data=[
                (

                )
                for i in range(50)
            ],
        )

        self.data_tables.bind(on_check_press = self.checked)
        self.data_tables.bind(on_row_press = self.row_checked)
        self.table.bind(on_check_press = self.checked)
        self.table.bind(on_row_press=self.row_checked)
        self.tableVente.bind(on_check_press=self.checked)
        self.tableVente.bind(on_row_press=self.row_checked)
        self.tableClient.bind(on_check_press=self.checked)
        self.tableClient.bind(on_row_press=self.row_checked)
        self.tablePerso.bind(on_check_press=self.checked)
        self.tablePerso.bind(on_row_press=self.row_checked)
        self.tableEntre.bind(on_check_press=self.checked)
        self.tableEntre.bind(on_row_press=self.row_checked)
        self.tableFour.bind(on_check_press=self.checked)
        self.tableFour.bind(on_row_press=self.row_checked)
        self.tableAppro.bind(on_check_press=self.checked)
        self.tableAppro.bind(on_row_press=self.row_checked)

        #content = self.ids.accueil

    #liste des vehicules
    def listeVehicule(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="ParcAuto")
        cursor = con.cursor()
        cursor.execute( "SELECT immatriculation,moteur,typeVehicule,etat,dateCirculation,marque,porte,place,couleur,dateInsertion,prix,kilometrage FROM vehicule")
        element = cursor.fetchall()
        print(element)
        return element
        con.close()
    #liste des locations:

    def listeLocation(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="ParcAuto")
        cursor = con.cursor()
        cursor.execute( "SELECT v.typeVehicule,l.lieu,l.dateLivraison,l.dateRetour,l.modePaiement,l.somme,l.datePaiement FROM vehicule v,locations l where v.numVehicule = l.numVehicule")
        element = cursor.fetchall()
        print(element)
        return element
        con.close()

    # ECRAN ACCUEIL
    def change_screen(self, instance):
        self.ids.manager.current = "Vehicule"

    #ECRAN LISTE DES VEHICULES
    def accueil_screen(self,instance):
        self.ids.manager.current = "Accueil"

    #ECRAN AJOUTER UN VEHICULE
    def Ajouter_screen(self,instance):
        self.ids.manager.current = "Ajouter_Vehicule"
    #ECRAN AJOUTER LOCATION
    def Ajouter_Loca(self,instance):
        self.ids.manager.current = "Ajouter_Location"

    #ECRAN LOCATION
    def loca(self,instance):
        self.ids.manager.current = "location"

    # ECRAN AJOUTER VENTE
    def Ajouter_vente(self, instance):
        self.ids.manager.current = "Ajouter_Vente"

    # ECRAN VENTE
    def vente(self, instance):
        self.ids.manager.current = "vente"

    # ECRAN AJOUTER CLIENT
    def Ajouter_client(self, instance):
        self.ids.manager.current = "Ajouter_Client"

    # ECRAN CLIENT
    def client(self, instance):
        self.ids.manager.current = "client"

    # ECRAN AJOUTER PERSONNEL
    def Ajouter_personnel(self, instance):
        self.ids.manager.current = "Ajouter_Personnel"

    # ECRAN PERSONNEL
    def personnel(self, instance):
        self.ids.manager.current = "personnel"

    # ECRAN AJOUTER ENTRTIEN
    def Ajouter_entretien(self, instance):
        self.ids.manager.current = "Ajouter_Entretien"

    # ECRAN ENTRETIEN
    def entretien(self, instance):
        self.ids.manager.current = "entretien"

    # ECRAN AJOUTER FOURNISSEUR
    def Ajouter_fournisseur(self, instance):
        self.ids.manager.current = "Ajouter_Fournisseur"

    # ECRAN FOURNISSEUR
    def fournisseur(self, instance):
        self.ids.manager.current = "fournisseur"

    # ECRAN AJOUTER APPRO
    def Ajouter_appro(self, instance):
        self.ids.manager.current = "Ajouter_approvisionnement"

    # ECRAN APPRO
    def appro(self, instance):
        self.ids.manager.current = "approvisionnement"

    # DECONNECTER
    def deconnecter(self, instance):
        layoutDec = GridLayout(cols=1, padding=10)
        layoutDec2 = GridLayout(rows=1, padding=10)
        lblDec = Label(text='êtes vous sûr de vous deconnecter ?', color="#000000")
        btnOk = Button(text='Oui', size_hint=(.9, None), size=(200, 50), background_color="#5887FF")
        btnRetour = Button(text='Non', size_hint=(.9, None), size=(200, 50), background_color="#5887FF")
        layoutDec.add_widget(lblDec)
        layoutDec2.add_widget(btnOk)
        layoutDec2.add_widget(btnRetour)
        layoutDec.add_widget(layoutDec2)
        popup = Popup(title='Déconnection', content=layoutDec,
                      size_hint=(None, None), size=(300, 200),
                      auto_dismiss=False, background="#FFFFFF", title_color="#000000", separator_color="#163586")
        btnRetour.bind(on_press=popup.dismiss)
        if(btnOk.on_press()==True):
            self.parent.current = "connect"
        popup.open()
    #TABLEAUX
    def tab(self,d):
        self.ids.vehi.add_widget(self.data_tables)
        self.ids.loca.add_widget(self.table)
        self.ids.vnt.add_widget(self.tableVente)
        self.ids.clt.add_widget(self.tableClient)
        self.ids.person.add_widget(self.tablePerso)
        self.ids.entre.add_widget(self.tableEntre)
        self.ids.four.add_widget(self.tableFour)
        self.ids.appro.add_widget(self.tableAppro)

    def checked(self,instance_table,current_row):
        print(instance_table,current_row)

    def row_checked(self,instance_table,instance_row):
        print(instance_table,instance_row)
#--------------------------------------------------------------------------Les_dates-----------------------------------------------------
    def on_save(self, instance, value, date_range):
        dte = value

        self.text = "{}-{}-{}".format(dte.year, dte.month, dte.day)
        self.focus = False
        self.ids.dateIns.text = self.text

    def on_cancel(self, instance, value):
        print("retour")

        # Date Naissance

    def save(self, instance, value, date_range):
        dte = value

        self.text = "{}-{}-{}".format(dte.year, dte.month, dte.day)
        self.focus = False
        self.ids.dateCir.text = self.text

    def livLoca(self, instance, value, date_range):
        dte = value

        self.text = "{}-{}-{}".format(dte.year, dte.month, dte.day)
        self.focus = False
        self.ids.dateLivraison.text = self.text

    def retourLoca(self, instance, value, date_range):
        dte = value

        self.text = "{}-{}-{}".format(dte.year, dte.month, dte.day)
        self.focus = False
        self.ids.dateRetour.text = self.text

    def paieLoca(self, instance, value, date_range):
        dte = value

        self.text = "{}-{}-{}".format(dte.year, dte.month, dte.day)
        self.focus = False
        self.ids.datePaiement.text = self.text

    def venteVehi(self, instance, value, date_range):
        dte = value

        self.text = "{}-{}-{}".format(dte.year, dte.month, dte.day)
        self.focus = False
        self.ids.dateVente.text = self.text

    def paieVenteVehi(self, instance, value, date_range):
        dte = value

        self.text = "{}-{}-{}".format(dte.year, dte.month, dte.day)
        self.focus = False
        self.ids.datePaiement_vente.text = self.text

    def client_dateN(self, instance, value, date_range):
        dte = value

        self.text = "{}-{}-{}".format(dte.year, dte.month, dte.day)
        self.focus = False
        self.ids.clientDateNaissance.text = self.text

    def client_dateA(self, instance, value, date_range):
        dte = value

        self.text = "{}-{}-{}".format(dte.year, dte.month, dte.day)
        self.focus = False
        self.ids.clientDateAjout.text = self.text

    def person_dateN(self, instance, value, date_range):
        dte = value

        self.text = "{}-{}-{}".format(dte.year, dte.month, dte.day)
        self.focus = False
        self.ids.personnelDateNaissance.text = self.text

    def person_dateE(self, instance, value, date_range):
        dte = value

        self.text = "{}-{}-{}".format(dte.year, dte.month, dte.day)
        self.focus = False
        self.ids.dateEmbauche.text = self.text

    def debutEntretien(self, instance, value, date_range):
        dte = value

        self.text = "{}-{}-{}".format(dte.year, dte.month, dte.day)
        self.focus = False
        self.ids.debutEntretien.text = self.text

    def finEntretien(self, instance, value, date_range):
        dte = value

        self.text = "{}-{}-{}".format(dte.year, dte.month, dte.day)
        self.focus = False
        self.ids.finEntretien.text = self.text

    def dateFour(self, instance, value, date_range):
        dte = value

        self.text = "{}-{}-{}".format(dte.year, dte.month, dte.day)
        self.focus = False
        self.ids.dte.text = self.text

    def payeEntretien(self, instance, value, date_range):
        dte = value

        self.text = "{}-{}-{}".format(dte.year, dte.month, dte.day)
        self.focus = False
        self.ids.paiementEntretien.text = self.text

    def commande(self, instance, value, date_range):
        dte = value

        self.text = "{}-{}-{}".format(dte.year, dte.month, dte.day)
        self.focus = False
        self.ids.dateCommande.text = self.text

    def livraisonAppro(self, instance, value, date_range):
        dte = value

        self.text = "{}-{}-{}".format(dte.year, dte.month, dte.day)
        self.focus = False
        self.ids.dateLivraison.text = self.text

    def payementAppro(self, instance, value, date_range):
        dte = value

        self.text = "{}-{}-{}".format(dte.year, dte.month, dte.day)
        self.focus = False
        self.ids.date_payeAppro.text = self.text

    def afficheDate(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def afficheDateN(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.save, on_cancel=self.on_cancel)
        date_dialog.open()

    def dateLivraison(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.livLoca, on_cancel=self.on_cancel)
        date_dialog.open()

    def dateRetour(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.retourLoca, on_cancel=self.on_cancel)
        date_dialog.open()

    def datePaieLoca(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.paieLoca, on_cancel=self.on_cancel)
        date_dialog.open()

    def dateVenteVehi(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.venteVehi, on_cancel=self.on_cancel)
        date_dialog.open()

    def datePaieVehi(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.paieVenteVehi, on_cancel=self.on_cancel)
        date_dialog.open()

    def client_dateNaissance(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.client_dateN, on_cancel=self.on_cancel)
        date_dialog.open()

    def client_dateAjout(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.client_dateA, on_cancel=self.on_cancel)
        date_dialog.open()

    def personnel_dateNaissance(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.person_dateN, on_cancel=self.on_cancel)
        date_dialog.open()

    def personnel_dateEmbauche(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.person_dateE, on_cancel=self.on_cancel)
        date_dialog.open()

    def debut_entretien(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.finEntretien, on_cancel=self.on_cancel)
        date_dialog.open()

    def fin_entretien(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.debutEntretien, on_cancel=self.on_cancel)
        date_dialog.open()

    def payement_entretien(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.payeEntretien, on_cancel=self.on_cancel)
        date_dialog.open()

    def date_founisseur(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.dateFour, on_cancel=self.on_cancel)
        date_dialog.open()

    def date_commande(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.commande, on_cancel=self.on_cancel)
        date_dialog.open()

    def date_livraison(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.livraisonAppro, on_cancel=self.on_cancel)
        date_dialog.open()

    def date_paie(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.payementAppro, on_cancel=self.on_cancel)
        date_dialog.open()

#--------------------------------------------------------------------------fin_Les_dates-----------------------------------------------------

 #--------------------------------------------------------COMBOX--------------------------------------------------------
    def type_liste(self):
        item = ['LUXE', 'SPORT','FAMILIALE']
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.menu_callback(x),
            } for i in item
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.type,
            items=menu_items,
            width_mult=2,
        )
        self.menu.open()
    def etat_liste(self):
        item = ['PARC', 'LOCATION','ENTRETIEN']
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.etat_callback(x),
            } for i in item
        ]
        self.liste = MDDropdownMenu(
            caller=self.ids.etat,
            items=menu_items,
            width_mult=2,
        )
        self.liste.open()

    # SEXE
    def sex_client(self):
        item = ['HOMME', 'FEMME']
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.clientSexe(x),
            } for i in item
        ]
        self.sexe = MDDropdownMenu(
            caller=self.ids.sexeClient,
            items=menu_items,
            width_mult=2,
        )
        self.sexe.open()

    # SEXE PERSONNEL
    def sex_perso(self):
        item = ['HOMME', 'FEMME']
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.persoSexe(x),
            } for i in item
        ]
        self.sexeP = MDDropdownMenu(
            caller=self.ids.sexePersonnel,
            items=menu_items,
            width_mult=2,
        )
        self.sexeP.open()



    # SEXE PERSONNEL
    def fonc_perso(self):
        item = ['CHAUFFEUR', 'MECANICIEN']
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.persoFonc(x),
            } for i in item
        ]
        self.fonc = MDDropdownMenu(
            caller=self.ids.foncPersonnel,
            items=menu_items,
            width_mult=4,
        )
        self.fonc.open()

    # LISTE CLIENT
    def clientLoca(self):
        item = ['CHAUFFEUR', 'MECANICIEN']
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.cltLoca(x),
            } for i in item
        ]
        self.listeClientL = MDDropdownMenu(
            caller=self.ids.locaClient,
            items=menu_items,
            width_mult=4,
        )
        self.listeClientL.open()

    # LISTE VEHICULE
    def VehiculeLoca(self):
        item = ['V1', 'V2']
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.vehiLoca(x),
            } for i in item
        ]
        self.listeVehiL = MDDropdownMenu(
            caller=self.ids.vehiculeLoca,
            items=menu_items,
            width_mult=4,
        )
        self.listeVehiL.open()

    # LISTE CLIENT
    def clientVente(self):
        item = ['CHAUFFEUR', 'MECANICIEN']
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.cltVente(x),
            } for i in item
        ]
        self.listeClient = MDDropdownMenu(
            caller=self.ids.client_vente,
            items=menu_items,
            width_mult=4,
        )
        self.listeClient.open()

    # LISTE VEHICULE VENTE
    def VehiculeVente(self):
        item = ['V1', 'V2']
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.vehiVente(x),
            } for i in item
        ]
        self.listeVehiV = MDDropdownMenu(
            caller=self.ids.vehiculeVente,
            items=menu_items,
            width_mult=4,
        )
        self.listeVehiV.open()

    # LISTE VEHICULE ENTRETIEN
    def VehiculeEntre(self):
        item = ['V1', 'V2']
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.vehiEntre(x),
            } for i in item
        ]
        self.listeVehiE = MDDropdownMenu(
            caller=self.ids.vehiculeEntretien,
            items=menu_items,
            width_mult=4,
        )
        self.listeVehiE.open()

    # LISTE FOURNISSEUR
    def FournisseurAppro(self):
        item = ['V1', 'V2']
        menu_items = [
            {
                "text": f"{i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"{i}": self.fournisseursA(x),
            } for i in item
        ]
        self.listeFourA = MDDropdownMenu(
            caller=self.ids.fourAppro,
            items=menu_items,
            width_mult=4,
        )
        self.listeFourA.open()

    def cltVente(self, text_item):
        self.ids.client_vente.text = text_item
        self.listeClient.dismiss()

    def cltLoca(self, text_item):
        self.ids.locaClient.text = text_item
        self.listeClientL.dismiss()
    def vehiLoca(self, text_item):
        self.ids.vehiculeLoca.text = text_item
        self.listeVehiL.dismiss()
    def vehiVente(self, text_item):
        self.ids.vehiculeVente.text = text_item
        self.listeVehiV.dismiss()
    def vehiEntre(self, text_item):
        self.ids.vehiculeEntretien.text = text_item
        self.listeVehiE.dismiss()
    def fournisseursA(self, text_item):
        self.ids.fourAppro.text = text_item
        self.listeFourA.dismiss()
    def persoFonc(self, text_item):
        self.ids.foncPersonnel.text = text_item
        self.fonc.dismiss()
    def clientSexe(self, text_item):
        self.ids.sexeClient.text = text_item
        self.sexe.dismiss()
    def persoSexe(self, text_item):
        self.ids.sexePersonnel.text = text_item
        self.sexeP.dismiss()
    def menu_callback(self, text_item):
        self.ids.type.text = text_item
        self.menu.dismiss()

    def etat_callback(self, text_item):
        self.ids.etat.text = text_item
        self.liste.dismiss()

#fonctions ajouter et afficher__________________________________________________________________
    def ajouterVehicule(self):
        matricule = self.ids.matricule.text
        moteur = self.ids.moteur.text
        type = self.ids.type.text
        etat = self.ids.etat.text
        dateCir = self.ids.dateCir.text
        marque = self.ids.marque.text
        porte = self.ids.porte.text
        place = self.ids.place.text
        couleur = self.ids.couleur.text
        dateIns = self.ids.dateIns.text
        prix = self.ids.prix.text
        km = self.ids.km.text

        layout = GridLayout(cols=1, padding=10)
        layout2 = GridLayout(cols=1, padding=10)
        layout3 = GridLayout(cols=1, padding=10)

        lbl = Label(text='Aucun champ ne doit être vide !',color="#000000")
        btn = Button(text='OK', size_hint=(.9, None), size=(200, 50),background_color="#5887FF")
        lbl2 = Label(text='Ajouter avec succès !', color="#000000")
        btn2 = Button(text='OK', size_hint=(.9, None), size=(200, 50), background_color="#5887FF")
        lbl3 = Label(text='Problême de connexion !', color="#000000")
        btn3 = Button(text='OK', size_hint=(.9, None), size=(200, 50), background_color="#5887FF")

        layout.add_widget(lbl)
        layout.add_widget(btn)
        layout2.add_widget(lbl2)
        layout2.add_widget(btn2)
        layout3.add_widget(lbl3)
        layout3.add_widget(btn3)
        if (matricule == "" or moteur == "" or type == "" or etat == "" or dateCir == "" or marque == ""
                or porte == "" or place == "" or couleur == "" or dateIns == "" or prix == "" or km == ""):
            popup = Popup(title='Erreur!', content=layout,
                          size_hint=(None, None), size=(300, 200),
                          auto_dismiss=False, background="#FFFFFF", title_color="#000000", separator_color="#163586")
            btn.bind(on_press=popup.dismiss)
            popup.open()
        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="", database="ParcAuto")
                cursor = con.cursor(buffered=True)
                """cursor.execute("SELECT * FROM secretaire")
                resultat = cursor.fetchone()
                res = resultat[0]
                id = str(res)"""
                cursor.execute(
                    "INSERT INTO vehicule (immatriculation,moteur,typeVehicule,etat,"
                    "dateCirculation,marque,porte,place,couleur,dateInsertion,prix,kilometrage) VALUES ('" + matricule + "','" +moteur + "','" + type + "','" + etat+ "','" +dateCir + "','" + marque + "','" + porte + "','" + place + "','" + couleur + "','" + dateIns + "',"+prix+",'"+km+"')")
                cursor.execute("commit")
                popup = Popup(title='INFO!', content=layout2,
                              size_hint=(None, None), size=(300, 200),
                              auto_dismiss=False, background="#FFFFFF", title_color="#000000",
                              separator_color="#163586")
                btn2.bind(on_press=popup.dismiss)
                popup.open()
                self.ids.manager.current = "Accueil"
                i = list(self.listeVehicule())
                self.data_tables.row_data=i
                con.close()
            except:
                popup = Popup(title='Erreur!', content=layout3,
                              size_hint=(None, None), size=(300, 200),
                              auto_dismiss=False, background="#FFFFFF", title_color="#000000",
                              separator_color="#163586")
                btn3.bind(on_press=popup.dismiss)
                popup.open()

    def ajouterLocation(self):
        client = self.ids.locaClient.text
        livraison = self.ids.livraison.text
        vehiculeLoca = self.ids.vehiculeLoca.text
        dateLivraison = self.ids.dateLivr.text
        dateRetour = self.ids.dateRetour.text
        modePaiement = self.ids.modePaiement.text
        somme = self.ids.somme.text
        datePaiement = self.ids.datePaiement.text

        layout = GridLayout(cols=1, padding=10)
        layout2 = GridLayout(cols=1, padding=10)
        layout3 = GridLayout(cols=1, padding=10)

        lbl = Label(text='Aucun champ ne doit être vide !',color="#000000")
        btn = Button(text='OK', size_hint=(.9, None), size=(200, 50),background_color="#5887FF")
        lbl2 = Label(text='Ajouter avec succès !', color="#000000")
        btn2 = Button(text='OK', size_hint=(.9, None), size=(200, 50), background_color="#5887FF")
        lbl3 = Label(text='Problême de connexion !', color="#000000")
        btn3 = Button(text='OK', size_hint=(.9, None), size=(200, 50), background_color="#5887FF")

        layout.add_widget(lbl)
        layout.add_widget(btn)
        layout2.add_widget(lbl2)
        layout2.add_widget(btn2)
        layout3.add_widget(lbl3)
        layout3.add_widget(btn3)
        if (client=="" or livraison==""or vehiculeLoca==""or dateLivraison==""or dateRetour=="" or modePaiement==""
        or somme=="" or datePaiement==""):
            from kivy.uix.popup import Popup
            popup = Popup(title='Erreur!', content=layout,
                          size_hint=(None, None), size=(300, 200),
                          auto_dismiss=False, background="#FFFFFF", title_color="#000000", separator_color="#163586")
            btn.bind(on_press=popup.dismiss)
            popup.open()
        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="", database="ParcAuto")
                cursor = con.cursor(buffered=True)
                """cursor.execute("SELECT * FROM secretaire")
                resultat = cursor.fetchone()
                res = resultat[0]
                id = str(res)"""
                cursor.execute(
                    "INSERT INTO vehicule (numVehicule,numClient,lieu,dateLivraison,"
                    "dateRetour,modePaiement,somme,datePaiement) VALUES ('" + vehiculeLoca + "','" +client + "','" + livraison + "','" + dateLivraison+ "','" +dateRetour + "','" + modePaiement + "','" + somme + "','" + datePaiement + "')")
                cursor.execute("commit")
                popup = Popup(title='INFO!', content=layout2,
                              size_hint=(None, None), size=(300, 200),
                              auto_dismiss=False, background="#FFFFFF", title_color="#000000",
                              separator_color="#163586")
                btn2.bind(on_press=popup.dismiss)
                popup.open()
                self.ids.manager.current = "Accueil"
                i = list(self.listeVehicule())
                self.data_tables.row_data=i
                con.close()
            except:
                popup = Popup(title='Erreur!', content=layout3,
                              size_hint=(None, None), size=(300, 200),
                              auto_dismiss=False, background="#FFFFFF", title_color="#000000",
                              separator_color="#163586")
                btn3.bind(on_press=popup.dismiss)
                popup.open()

    def ajouterVente(self):
        client_vente = self.ids.client_vente.text
        vehiculeVente = self.ids.vehiculeVente.text
        dateVente = self.ids.dateVente.text
        modePaiementV = self.ids.modePaiementV.text
        sommeV = self.ids.sommeV.text
        datePaiement_vente = self.ids.datePaiement_vente.text

        layout = GridLayout(cols=1, padding=10)

        lbl = Label(text='Aucun champ ne doit être vide !',color='#000000')
        btn = Button(text='OK', size_hint=(.9, None), size=(200, 50),background_color="#5887FF")

        layout.add_widget(lbl)
        layout.add_widget(btn)
        if (client_vente=="" or vehiculeVente==""or dateVente==""or modePaiementV==""or sommeV=="" or datePaiement_vente==""):
            from kivy.uix.popup import Popup
            popup = Popup(title='Erreur!', content=layout,
                          size_hint=(None, None), size=(300, 200),
                          auto_dismiss=False, background="#FFFFFF", title_color="#000000", separator_color="#163586")
            btn.bind(on_press=popup.dismiss)
            popup.open()
    def ajouterClient(self):
        prenomClient = self.ids.prenomClient.text
        nomClient = self.ids.nomClient.text
        sexeClient = self.ids.sexeClient.text
        nationClient = self.ids.nationClient.text
        clientDateNaissance = self.ids.clientDateNaissance.text
        clientAdresse = self.ids.clientAdresse.text
        clientTel = self.ids.clientTel.text
        clientEmail = self.ids.clientEmail.text
        clientPermis = self.ids.clientPermis.text
        clientDateAjout = self.ids.clientDateAjout.text

        layout = GridLayout(cols=1, padding=10)

        lbl = Label(text='Aucun champ ne doit être vide !',color='#000000')
        btn = Button(text='OK', size_hint=(.9, None), size=(200, 50),background_color="#5887FF")

        layout.add_widget(lbl)
        layout.add_widget(btn)
        if (prenomClient=="" or nomClient==""or sexeClient==""or nationClient==""or clientDateNaissance=="" or clientAdresse==""
        or clientTel=="" or clientEmail=="" or clientPermis=="" or clientDateAjout==""):
            from kivy.uix.popup import Popup
            popup = Popup(title='Erreur!', content=layout,
                          size_hint=(None, None), size=(300, 200),
                          auto_dismiss=False,background="#FFFFFF",title_color="#000000",separator_color="#163586")
            btn.bind(on_press=popup.dismiss)
            popup.open()

    def ajouterPerso(self):
        prenomPersonnel = self.ids.prenomPersonnel.text
        nomPersonnel = self.ids.nomPersonnel.text
        sexePersonnel = self.ids.sexePersonnel.text
        foncPersonnel = self.ids.foncPersonnel.text
        personnelDateNaissance = self.ids.personnelDateNaissance.text
        personnelAdresse = self.ids.personnelAdresse.text
        personnelTel = self.ids.personnelTel.text
        personnelEmail = self.ids.personnelEmail.text
        personnelPermis = self.ids.personnelPermis.text
        dateEmbauche = self.ids.dateEmbauche.text

        layout = GridLayout(cols=1, padding=10)

        lbl = Label(text='Aucun champ ne doit être vide !',color='#000000')
        btn = Button(text='OK', size_hint=(.9, None), size=(200, 50),background_color="#5887FF")

        layout.add_widget(lbl)
        layout.add_widget(btn)
        if (prenomPersonnel=="" or nomPersonnel==""or sexePersonnel==""or foncPersonnel==""or personnelDateNaissance=="" or personnelAdresse==""
        or personnelTel=="" or personnelEmail=="" or personnelPermis=="" or dateEmbauche==""):
            from kivy.uix.popup import Popup
            popup = Popup(title='Erreur!', content=layout,
                          size_hint=(None, None), size=(300, 200),
                          auto_dismiss=False,background="#FFFFFF",title_color="#000000",separator_color="#163586")
            btn.bind(on_press=popup.dismiss)
            popup.open()

    def ajouterEntretien(self):
        vehiculeEntretien = self.ids.vehiculeEntretien.text
        type_entretien = self.ids.type_entretien.text
        debutEntretien = self.ids.debutEntretien.text
        finEntretien = self.ids.finEntretien.text
        sommeEntretien = self.ids.sommeEntretien.text
        paiementEntretien = self.ids.paiementEntretien.text

        layout = GridLayout(cols=1, padding=10)

        lbl = Label(text='Aucun champ ne doit être vide !',color='#000000')
        btn = Button(text='OK', size_hint=(.9, None), size=(200, 50),background_color="#5887FF")

        layout.add_widget(lbl)
        layout.add_widget(btn)
        if (vehiculeEntretien=="" or type_entretien==""or debutEntretien==""or finEntretien==""or sommeEntretien=="" or paiementEntretien==""):
            from kivy.uix.popup import Popup
            popup = Popup(title='Erreur!', content=layout,
                          size_hint=(None, None), size=(300, 200),
                          auto_dismiss=False,background="#FFFFFF",title_color="#000000",separator_color="#163586")
            btn.bind(on_press=popup.dismiss)
            popup.open()

    def ajouterFournisseur(self):
        nomEntreprise = self.ids.nomEntreprise.text
        entrepriseEmail = self.ids.entrepriseEmail.text
        adresseEntreprise = self.ids.adresseEntreprise.text
        numEntreprise = self.ids.numEntreprise.text
        pays = self.ids.pays.text
        dte = self.ids.dte.text

        layout = GridLayout(cols=1, padding=10)

        lbl = Label(text='Aucun champ ne doit être vide !',color='#000000')
        btn = Button(text='OK', size_hint=(.9, None), size=(200, 50),background_color="#5887FF")

        layout.add_widget(lbl)
        layout.add_widget(btn)
        if (nomEntreprise=="" or entrepriseEmail==""or adresseEntreprise==""or numEntreprise==""or pays=="" or dte==""):
            from kivy.uix.popup import Popup
            popup = Popup(title='Erreur!', content=layout,
                          size_hint=(None, None), size=(300, 200),
                          auto_dismiss=False,background="#FFFFFF",title_color="#000000",separator_color="#163586")
            btn.bind(on_press=popup.dismiss)
            popup.open()

    def ajouterAppro(self):
        fourAppro = self.ids.fourAppro.text
        nbrVehicule = self.ids.nbrVehicule.text
        dateCommande = self.ids.dateCommande.text
        dateLivraison = self.ids.dateLivraison.text
        sommeAppro = self.ids.sommeAppro.text
        date_payeAppro = self.ids.date_payeAppro.text

        layout = GridLayout(cols=1, padding=10)

        lbl = Label(text='Aucun champ ne doit être vide !',color='#000000')
        btn = Button(text='OK', size_hint=(.9, None), size=(200, 50),background_color="#5887FF")

        layout.add_widget(lbl)
        layout.add_widget(btn)
        if (fourAppro=="" or nbrVehicule==""or dateCommande==""or dateLivraison==""or sommeAppro=="" or date_payeAppro==""):
            from kivy.uix.popup import Popup
            popup = Popup(title='Erreur!', content=layout,
                          size_hint=(None, None), size=(300, 200),
                          auto_dismiss=False,background="#FFFFFF",title_color="#000000",separator_color="#163586")
            btn.bind(on_press=popup.dismiss)
            popup.open()

class Principal(ScreenManager):
    pass



class PrincipalApp(MDApp):
    def build(self):

        return Builder.load_file('principal.kv')

if __name__ =='__main__':
    PrincipalApp().run()