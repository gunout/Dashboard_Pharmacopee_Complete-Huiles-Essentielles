import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page
st.set_page_config(
    page_title="Dashboard Pharmacopée Huiles Essentielles",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

class CompleteEssentialOilDashboard:
    def __init__(self):
        self.oils_config = self._get_complete_oils_config()
        self.colors = ['#8B4513', '#228B22', '#FFD700', '#8A2BE2', '#FF6B6B', 
                      '#4ECDC4', '#45B7D1', '#F9A602', '#6A0572', '#2A9D8F']
        
    def _get_complete_oils_config(self):
        """Configuration complète pour toutes les huiles essentielles (50 huiles)"""
        return {
            # === 20 huiles existantes ===
            "Lavande": {
                "production_base": 150, "price_base": 45, "type": "relaxante",
                "proprietes": ["calmante", "cicatrisante", "antiseptique", "analgésique"],
                "regions": ["France", "Bulgarie", "Chine"], "rendement": 0.015,
                "molecules_principales": ["Linalol", "Acétate de linalyle", "Cinéole"],
                "contre_indications": ["Femmes enceintes", "Enfants < 6 ans"],
                "prix_evolution": "++", "demande_evolution": "+++",
                "couleur": "#6A0572"
            },
            "Menthe Poivrée": {
                "production_base": 80, "price_base": 60, "type": "tonique",
                "proprietes": ["digestive", "rafraichissante", "antalgique", "decongestionnante"],
                "regions": ["USA", "France", "Inde"], "rendement": 0.012,
                "molecules_principales": ["Menthol", "Menthone", "Acétate de menthyle"],
                "contre_indications": ["Épilepsie", "Problèmes biliaires"],
                "prix_evolution": "++", "demande_evolution": "++",
                "couleur": "#228B22"
            },
            "Arbre à Thé": {
                "production_base": 120, "price_base": 35, "type": "antiseptique",
                "proprietes": ["antibacterienne", "antifongique", "antivirale", "immunostimulante"],
                "regions": ["Australie", "Chine", "Afrique du Sud"], "rendement": 0.020,
                "molecules_principales": ["Terpinène-4-ol", "γ-Terpinène", "α-Terpinène"],
                "contre_indications": ["Peau sensible"],
                "prix_evolution": "+", "demande_evolution": "+++",
                "couleur": "#2A9D8F"
            },
            "Eucalyptus": {
                "production_base": 200, "price_base": 25, "type": "respiratoire",
                "proprietes": ["expectorante", "decongestionnante", "antiseptique", "febrifuge"],
                "regions": ["Australie", "Chine", "Portugal"], "rendement": 0.018,
                "molecules_principales": ["Eucalyptol", "α-Pinène", "Limonène"],
                "contre_indications": ["Asthme sévère"],
                "prix_evolution": "+", "demande_evolution": "++",
                "couleur": "#45B7D1"
            },
            "Ravintsara": {
                "production_base": 40, "price_base": 55, "type": "immunitaire",
                "proprietes": ["antivirale", "immunostimulante", "expectorante", "neurotonique"],
                "regions": ["Madagascar", "Comores"], "rendement": 0.008,
                "molecules_principales": ["Cinéole", "Sabinène", "α-Terpinéol"],
                "contre_indications": ["Aucune connue"],
                "prix_evolution": "+++", "demande_evolution": "+++",
                "couleur": "#4ECDC4"
            },
            "Palmarosa": {
                "production_base": 25, "price_base": 70, "type": "cosmetique",
                "proprietes": ["regenerante", "hydratante", "antibacterienne", "equilibrante"],
                "regions": ["Inde", "Nepal", "Indonesie"], "rendement": 0.006,
                "molecules_principales": ["Géraniol", "Linalol", "Acétate de géranyle"],
                "contre_indications": ["Aucune connue"],
                "prix_evolution": "++", "demande_evolution": "++",
                "couleur": "#FFD700"
            },
            "Ylang-Ylang": {
                "production_base": 30, "price_base": 85, "type": "aphrodisiaque",
                "proprietes": ["aphrodisiaque", "sedative", "hypotensive", "regulatrice"],
                "regions": ["Madagascar", "Comores", "Mayotte"], "rendement": 0.005,
                "molecules_principales": ["Linalol", "Géraniol", "Para-crésyl méthyl éther"],
                "contre_indications": ["Hypotension"],
                "prix_evolution": "+++", "demande_evolution": "++",
                "couleur": "#8A2BE2"
            },
            "Girofle": {
                "production_base": 60, "price_base": 40, "type": "antiseptique",
                "proprietes": ["antiseptique", "antalgique", "antiparasitaire", "stimulante"],
                "regions": ["Madagascar", "Indonesie", "Sri Lanka"], "rendement": 0.015,
                "molecules_principales": ["Eugénol", "Acétate d'eugényle", "Caryophyllène"],
                "contre_indications": ["Ulcères gastriques"],
                "prix_evolution": "+", "demande_evolution": "++",
                "couleur": "#8B4513"
            },
            "Citron": {
                "production_base": 180, "price_base": 20, "type": "detoxifiante",
                "proprietes": ["antibacterienne", "detoxifiante", "tonique", "digestive"],
                "regions": ["Italie", "Espagne", "USA", "Argentine"], "rendement": 0.003,
                "molecules_principales": ["Limonène", "β-Pinène", "γ-Terpinène"],
                "contre_indications": ["Photosensibilisante"],
                "prix_evolution": "+", "demande_evolution": "+++",
                "couleur": "#FFD700"
            },
            "Romarin": {
                "production_base": 90, "price_base": 38, "type": "tonique",
                "proprietes": ["tonique", "hepatique", "neurotonique", "antioxydante"],
                "regions": ["France", "Espagne", "Maroc", "Tunisie"], "rendement": 0.010,
                "molecules_principales": ["Cinéole", "Camphre", "α-Pinène"],
                "contre_indications": ["Hypertension", "Épilepsie"],
                "prix_evolution": "++", "demande_evolution": "++",
                "couleur": "#228B22"
            },
            "Tea Tree": {
                "production_base": 110, "price_base": 32, "type": "antiseptique",
                "proprietes": ["antibacterienne", "antifongique", "antivirale", "immunostimulante"],
                "regions": ["Australie", "Chine"], "rendement": 0.019,
                "molecules_principales": ["Terpinène-4-ol", "γ-Terpinène", "α-Terpinène"],
                "contre_indications": ["Peau sensible"],
                "prix_evolution": "+", "demande_evolution": "+++",
                "couleur": "#2A9D8F"
            },
            "Géranium": {
                "production_base": 45, "price_base": 75, "type": "equilibrante",
                "proprietes": ["equilibrante", "hemostatique", "cicatrisante", "antiseptique"],
                "regions": ["Egypte", "Maroc", "Réunion"], "rendement": 0.007,
                "molecules_principales": ["Citronellol", "Géraniol", "Linalol"],
                "contre_indications": ["Aucune connue"],
                "prix_evolution": "++", "demande_evolution": "++",
                "couleur": "#FF6B6B"
            },
            "Camomille": {
                "production_base": 35, "price_base": 95, "type": "calmante",
                "proprietes": ["calmante", "anti-inflammatoire", "antispasmodique", "analgésique"],
                "regions": ["France", "Egypte", "Allemagne"], "rendement": 0.004,
                "molecules_principales": ["Chamazulène", "Bisabolol", "Farnésène"],
                "contre_indications": ["Allergie aux Astéracées"],
                "prix_evolution": "+++", "demande_evolution": "++",
                "couleur": "#FFD700"
            },
            "Sauge": {
                "production_base": 28, "price_base": 88, "type": "hormonale",
                "proprietes": ["equilibrante hormonale", "antiseptique", "digestive", "neurotonique"],
                "regions": ["France", "Espagne", "Croatie"], "rendement": 0.005,
                "molecules_principales": ["Thuyone", "Cinéole", "Camphre"],
                "contre_indications": ["Femmes enceintes", "Épilepsie"],
                "prix_evolution": "+++", "demande_evolution": "+",
                "couleur": "#6A0572"
            },
            "Niaouli": {
                "production_base": 55, "price_base": 42, "type": "immunitaire",
                "proprietes": ["immunostimulante", "antivirale", "expectorante", "decongestionnante"],
                "regions": ["Madagascar", "Nouvelle-Calédonie"], "rendement": 0.014,
                "molecules_principales": ["Cinéole", "α-Pinène", "Limonène"],
                "contre_indications": ["Aucune connue"],
                "prix_evolution": "++", "demande_evolution": "++",
                "couleur": "#45B7D1"
            },
            "Basilic": {
                "production_base": 65, "price_base": 48, "type": "digestive",
                "proprietes": ["digestive", "antispasmodique", "neurotonique", "antibacterienne"],
                "regions": ["France", "Egypte", "Comores"], "rendement": 0.009,
                "molecules_principales": ["Estragole", "Linalol", "Eugénol"],
                "contre_indications": ["Femmes enceintes"],
                "prix_evolution": "++", "demande_evolution": "++",
                "couleur": "#228B22"
            },
            "Cèdre": {
                "production_base": 40, "price_base": 65, "type": "grounding",
                "proprietes": ["grounding", "lymphotonique", "antiseptique", "repulsif"],
                "regions": ["Maroc", "USA", "Himalaya"], "rendement": 0.008,
                "molecules_principales": ["Cédrol", "α-Cédrène", "Thujopsène"],
                "contre_indications": ["Femmes enceintes"],
                "prix_evolution": "++", "demande_evolution": "+",
                "couleur": "#8B4513"
            },
            "Encens": {
                "production_base": 22, "price_base": 120, "type": "spirituelle",
                "proprietes": ["meditative", "anti-inflammatoire", "cicatrisante", "immunostimulante"],
                "regions": ["Oman", "Somalie", "Ethiopie"], "rendement": 0.003,
                "molecules_principales": ["α-Pinène", "Limonène", "Incensole"],
                "contre_indications": ["Aucune connue"],
                "prix_evolution": "+++", "demande_evolution": "++",
                "couleur": "#F9A602"
            },
            "Myrrhe": {
                "production_base": 18, "price_base": 110, "type": "spirituelle",
                "proprietes": ["anti-inflammatoire", "cicatrisante", "antiseptique", "expectorante"],
                "regions": ["Somalie", "Ethiopie", "Yémen"], "rendement": 0.002,
                "molecules_principales": ["Furanoeudesma-1,3-diène", "Curzerène", "Lindestrene"],
                "contre_indications": ["Femmes enceintes"],
                "prix_evolution": "+++", "demande_evolution": "+",
                "couleur": "#8B4513"
            },
            "Vetiver": {
                "production_base": 32, "price_base": 78, "type": "grounding",
                "proprietes": ["grounding", "tonique nerveux", "repulsif", "cicatrisante"],
                "regions": ["Haïti", "Réunion", "Indonésie"], "rendement": 0.006,
                "molecules_principales": ["Vetivone", "β-Vetivène", "Khusimol"],
                "contre_indications": ["Aucune connue"],
                "prix_evolution": "++", "demande_evolution": "++",
                "couleur": "#8B4513"
            },

            # === 12 nouvelles huiles (ajout précédent) ===
            "Citronnelle": {
                "production_base": 100, "price_base": 30, "type": "repulsif",
                "proprietes": ["repulsive", "antiseptique", "antifongique", "digestive"],
                "regions": ["Inde", "Chine", "Vietnam"], "rendement": 0.012,
                "molecules_principales": ["Citronellal", "Géranial", "Limonène"],
                "contre_indications": ["Peau sensible", "Femmes enceintes"],
                "prix_evolution": "++", "demande_evolution": "+++",
                "couleur": "#7CB342"
            },
            "Gingembre": {
                "production_base": 70, "price_base": 55, "type": "digestive",
                "proprietes": ["digestive", "tonique", "anti-inflammatoire", "stimulante"],
                "regions": ["Inde", "Chine", "Nigeria"], "rendement": 0.008,
                "molecules_principales": ["Zingibérène", "Gingérol", "Sesquiphellandrène"],
                "contre_indications": ["Calculs biliaires", "Ulcères"],
                "prix_evolution": "++", "demande_evolution": "++",
                "couleur": "#D84315"
            },
            "Cannelle": {
                "production_base": 40, "price_base": 80, "type": "stimulante",
                "proprietes": ["stimulante", "antiseptique", "antispasmodique", "digestive"],
                "regions": ["Sri Lanka", "Madagascar", "Inde"], "rendement": 0.006,
                "molecules_principales": ["Cinnamaldéhyde", "Eugénol", "Linalol"],
                "contre_indications": ["Femmes enceintes", "Peau sensible"],
                "prix_evolution": "+++", "demande_evolution": "++",
                "couleur": "#D2691E"
            },
            "Pamplemousse": {
                "production_base": 120, "price_base": 28, "type": "detoxifiante",
                "proprietes": ["detoxifiante", "tonique", "stimulante", "diurétique"],
                "regions": ["USA", "Israël", "Chine"], "rendement": 0.004,
                "molecules_principales": ["Limonène", "Pinène", "Myrcène"],
                "contre_indications": ["Photosensibilisante", "Interactions médicamenteuses"],
                "prix_evolution": "+", "demande_evolution": "+++",
                "couleur": "#FFB74D"
            },
            "Mandarine": {
                "production_base": 150, "price_base": 22, "type": "calmante",
                "proprietes": ["calmante", "sédative", "digestive", "spasmolytique"],
                "regions": ["Italie", "Espagne", "Maroc"], "rendement": 0.004,
                "molecules_principales": ["Limonène", "Myrcène", "α-Pinène"],
                "contre_indications": ["Aucune connue"],
                "prix_evolution": "+", "demande_evolution": "++",
                "couleur": "#FFA726"
            },
            "Orange douce": {
                "production_base": 200, "price_base": 18, "type": "relaxante",
                "proprietes": ["relaxante", "antiseptique", "digestive", "tonique"],
                "regions": ["Brésil", "USA", "Espagne"], "rendement": 0.004,
                "molecules_principales": ["Limonène", "Myrcène", "Pinène"],
                "contre_indications": ["Photosensibilisante"],
                "prix_evolution": "+", "demande_evolution": "+++",
                "couleur": "#FF9800"
            },
            "Bois de rose": {
                "production_base": 15, "price_base": 110, "type": "cosmetique",
                "proprietes": ["regenerante", "calmante", "antiseptique", "hydratante"],
                "regions": ["Brésil", "Guyane", "Pérou"], "rendement": 0.003,
                "molecules_principales": ["Linalol", "α-Terpinéol", "Géraniol"],
                "contre_indications": ["Aucune connue"],
                "prix_evolution": "+++", "demande_evolution": "++",
                "couleur": "#F48FB1"
            },
            "Patchouli": {
                "production_base": 35, "price_base": 85, "type": "grounding",
                "proprietes": ["grounding", "antiseptique", "antifongique", "aphrodisiaque"],
                "regions": ["Indonésie", "Chine", "Inde"], "rendement": 0.005,
                "molecules_principales": ["Patchoulol", "α-Patchoulène", "β-Caryophyllène"],
                "contre_indications": ["Aucune connue"],
                "prix_evolution": "+++", "demande_evolution": "++",
                "couleur": "#8D6E63"
            },
            "Santal": {
                "production_base": 12, "price_base": 150, "type": "spirituelle",
                "proprietes": ["meditative", "apaisante", "antiseptique", "anti-inflammatoire"],
                "regions": ["Inde", "Australie", "Nouvelle-Calédonie"], "rendement": 0.002,
                "molecules_principales": ["α-Santalol", "β-Santalol", "α-Bisabolol"],
                "contre_indications": ["Aucune connue"],
                "prix_evolution": "+++", "demande_evolution": "+",
                "couleur": "#A1887F"
            },
            "Jasmin": {
                "production_base": 10, "price_base": 200, "type": "aphrodisiaque",
                "proprietes": ["aphrodisiaque", "relaxante", "antispasmodique", "équilibrante"],
                "regions": ["Inde", "Egypte", "Maroc"], "rendement": 0.001,
                "molecules_principales": ["Benzyl acétate", "Linalol", "Phényléthyl alcool"],
                "contre_indications": ["Aucune connue"],
                "prix_evolution": "+++", "demande_evolution": "++",
                "couleur": "#F8BBD0"
            },
            "Rose": {
                "production_base": 8, "price_base": 250, "type": "cosmetique",
                "proprietes": ["équilibrante", "hydratante", "antiseptique", "tonique"],
                "regions": ["Bulgarie", "Turquie", "Maroc"], "rendement": 0.001,
                "molecules_principales": ["Citronellol", "Géraniol", "Phényléthyl alcool"],
                "contre_indications": ["Aucune connue"],
                "prix_evolution": "+++", "demande_evolution": "+++",
                "couleur": "#F06292"
            },
            "Cardamome": {
                "production_base": 25, "price_base": 95, "type": "digestive",
                "proprietes": ["digestive", "antispasmodique", "tonique", "expectorante"],
                "regions": ["Guatemala", "Inde", "Sri Lanka"], "rendement": 0.005,
                "molecules_principales": ["Cinéole", "α-Terpinéol", "Linalol"],
                "contre_indications": ["Calculs biliaires"],
                "prix_evolution": "+++", "demande_evolution": "++",
                "couleur": "#A5D6A7"
            },

            # === 10 nouvelles huiles (ajout précédent) ===
            "Thym": {
                "production_base": 50, "price_base": 45, "type": "antiseptique",
                "proprietes": ["antibactérienne", "antifongique", "immunostimulante", "expectorante"],
                "regions": ["France", "Espagne", "Maroc"], "rendement": 0.012,
                "molecules_principales": ["Thymol", "Carvacrol", "p-Cymène"],
                "contre_indications": ["Femmes enceintes", "Hypertension"],
                "prix_evolution": "++", "demande_evolution": "++",
                "couleur": "#7B1FA2"
            },
            "Origan": {
                "production_base": 30, "price_base": 55, "type": "antiseptique",
                "proprietes": ["antibactérienne", "antivirale", "antiparasitaire", "anti-inflammatoire"],
                "regions": ["Grèce", "Turquie", "Maroc"], "rendement": 0.010,
                "molecules_principales": ["Carvacrol", "Thymol", "p-Cymène"],
                "contre_indications": ["Femmes enceintes", "Allergie aux Lamiacées"],
                "prix_evolution": "++", "demande_evolution": "+++",
                "couleur": "#D32F2F"
            },
            "Marjolaine": {
                "production_base": 35, "price_base": 50, "type": "relaxante",
                "proprietes": ["sédative", "antispasmodique", "digestive", "régulatrice nerveuse"],
                "regions": ["France", "Egypte", "Tunisie"], "rendement": 0.008,
                "molecules_principales": ["Terpinène-4-ol", "Sabinène", "α-Terpinène"],
                "contre_indications": ["Aucune connue"],
                "prix_evolution": "++", "demande_evolution": "++",
                "couleur": "#8BC34A"
            },
            "Lavandin": {
                "production_base": 100, "price_base": 30, "type": "respiratoire",
                "proprietes": ["expectorante", "décongestionnante", "antiseptique", "calmante"],
                "regions": ["France", "Espagne", "Italie"], "rendement": 0.016,
                "molecules_principales": ["Linalol", "Acétate de linalyle", "Cinéole"],
                "contre_indications": ["Femmes enceintes", "Enfants < 6 ans"],
                "prix_evolution": "+", "demande_evolution": "++",
                "couleur": "#9575CD"
            },
            "Bergamote": {
                "production_base": 90, "price_base": 35, "type": "équilibrante",
                "proprietes": ["équilibrante", "antidépressive", "antiseptique", "digestive"],
                "regions": ["Italie", "Côte d'Ivoire", "Argentine"], "rendement": 0.004,
                "molecules_principales": ["Limonène", "Linalol", "Acétate de linalyle"],
                "contre_indications": ["Photosensibilisante"],
                "prix_evolution": "++", "demande_evolution": "+++",
                "couleur": "#F9A825"
            },
            "Citron vert": {
                "production_base": 100, "price_base": 25, "type": "tonique",
                "proprietes": ["tonique", "digestive", "antiseptique", "détoxifiante"],
                "regions": ["Mexique", "Inde", "Brésil"], "rendement": 0.004,
                "molecules_principales": ["Limonène", "β-Pinène", "γ-Terpinène"],
                "contre_indications": ["Photosensibilisante"],
                "prix_evolution": "+", "demande_evolution": "++",
                "couleur": "#CDDC39"
            },
            "Poivre noir": {
                "production_base": 45, "price_base": 65, "type": "digestive",
                "proprietes": ["digestive", "stimulante", "antiseptique", "antioxydante"],
                "regions": ["Inde", "Vietnam", "Brésil"], "rendement": 0.005,
                "molecules_principales": ["Caryophyllène", "Limonène", "Pinène"],
                "contre_indications": ["Ulcères gastriques", "Hypertension"],
                "prix_evolution": "++", "demande_evolution": "++",
                "couleur": "#424242"
            },
            "Fenouil": {
                "production_base": 60, "price_base": 40, "type": "digestive",
                "proprietes": ["digestive", "carminative", "détoxifiante", "expectorante"],
                "regions": ["France", "Inde", "Egypte"], "rendement": 0.007,
                "molecules_principales": ["Trans-anéthole", "Fenchone", "Estragole"],
                "contre_indications": ["Femmes enceintes", "Épilepsie"],
                "prix_evolution": "++", "demande_evolution": "++",
                "couleur": "#66BB6A"
            },
            "Anis étoilé": {
                "production_base": 20, "price_base": 70, "type": "digestive",
                "proprietes": ["digestive", "antispasmodique", "expectorante", "stimulante"],
                "regions": ["Chine", "Vietnam", "Inde"], "rendement": 0.004,
                "molecules_principales": ["Trans-anéthole", "Linalol", "Estragole"],
                "contre_indications": ["Femmes enceintes", "Allergie aux apiacées"],
                "prix_evolution": "+++", "demande_evolution": "+",
                "couleur": "#8D6E63"
            },
            "Carotte": {
                "production_base": 15, "price_base": 90, "type": "cosmetique",
                "proprietes": ["régénérante cutanée", "antioxydante", "équilibrante", "hydratante"],
                "regions": ["France", "Inde", "USA"], "rendement": 0.002,
                "molecules_principales": ["β-Caryophyllène", "Daucène", "α-Pinène"],
                "contre_indications": ["Aucune connue"],
                "prix_evolution": "+++", "demande_evolution": "++",
                "couleur": "#FF8A65"
            },

            # === 8 nouvelles huiles (ajout de cette version) ===
            "Néroli": {
                "production_base": 10, "price_base": 180, "type": "relaxante",
                "proprietes": ["anti-anxiété", "apaisante", "antispasmodique", "équilibrante nerveuse"],
                "regions": ["Tunisie", "Maroc", "Egypte"], "rendement": 0.001,
                "molecules_principales": ["Linalol", "Limonène", "β-Pinène"],
                "contre_indications": ["Photosensibilisante"],
                "prix_evolution": "+++", "demande_evolution": "+++",
                "couleur": "#FFF176"
            },
            "Petit Grain": {
                "production_base": 15, "price_base": 75, "type": "relaxante",
                "proprietes": ["sédative", "antispasmodique", "neurotonique", "équilibrante"],
                "regions": ["Paraguay", "Maroc", "Espagne"], "rendement": 0.002,
                "molecules_principales": ["Linalol", "Acétate de linalyle", "β-Pinène"],
                "contre_indications": ["Aucune connue"],
                "prix_evolution": "++", "demande_evolution": "++",
                "couleur": "#C8E6C9"
            },
            "Coriandre": {
                "production_base": 55, "price_base": 50, "type": "digestive",
                "proprietes": ["digestive", "antispasmodique", "carminative", "tonique"],
                "regions": ["Inde", "Maroc", "Russie"], "rendement": 0.008,
                "molecules_principales": ["Linalol", "α-Pinène", "Géraniol"],
                "contre_indications": ["Aucune connue"],
                "prix_evolution": "++", "demande_evolution": "++",
                "couleur": "#81C784"
            },
            "Laurier noble": {
                "production_base": 30, "price_base": 45, "type": "respiratoire",
                "proprietes": ["expectorante", "antiseptique", "stimulante", "tonique"],
                "regions": ["Turquie", "Espagne", "Maroc"], "rendement": 0.006,
                "molecules_principales": ["Cinéole", "α-Pinène", "Linalol"],
                "contre_indications": ["Aucune connue"],
                "prix_evolution": "++", "demande_evolution": "++",
                "couleur": "#558B2F"
            },
            "Immortelle": {
                "production_base": 8, "price_base": 200, "type": "cicatrisante",
                "proprietes": ["anti-inflammatoire", "cicatrisante", "hémostatique", "régénérante"],
                "regions": ["Corse", "Croatie", "Italie"], "rendement": 0.001,
                "molecules_principales": ["Néryl acétate", "Italidiones", "α-Pinène"],
                "contre_indications": ["Aucune connue"],
                "prix_evolution": "+++", "demande_evolution": "+++",
                "couleur": "#FFD54F"
            },
            "Ciste ladanifère": {
                "production_base": 12, "price_base": 110, "type": "cicatrisante",
                "proprietes": ["cicatrisante", "hémostatique", "astringente", "antiseptique"],
                "regions": ["Espagne", "France", "Grèce"], "rendement": 0.002,
                "molecules_principales": ["α-Pinène", "Cédrol", "Cistus diterpenes"],
                "contre_indications": ["Aucune connue"],
                "prix_evolution": "+++", "demande_evolution": "+",
                "couleur": "#D7CCC8"
            },
            "Myrte": {
                "production_base": 25, "price_base": 60, "type": "respiratoire",
                "proprietes": ["expectorante", "antiseptique", "décongestionnante", "tonique"],
                "regions": ["France", "Tunisie", "Maroc"], "rendement": 0.005,
                "molecules_principales": ["Cinéole", "α-Pinène", "Myrténol"],
                "contre_indications": ["Aucune connue"],
                "prix_evolution": "++", "demande_evolution": "++",
                "couleur": "#4CAF50"
            },
            "Genévrier": {
                "production_base": 30, "price_base": 55, "type": "détoxifiante",
                "proprietes": ["diurétique", "détoxifiante", "antiseptique", "tonique"],
                "regions": ["France", "Italie", "Pologne"], "rendement": 0.006,
                "molecules_principales": ["α-Pinène", "Cédrol", "Limonène"],
                "contre_indications": ["Insuffisance rénale", "Femmes enceintes"],
                "prix_evolution": "++", "demande_evolution": "++",
                "couleur": "#5D4037"
            }
        }
    
    def generate_comprehensive_data(self, oil_name, start_year=2000, end_year=2025):
        """Génère des données complètes pour le dashboard"""
        config = self.oils_config[oil_name]
        dates = pd.date_range(start=f'{start_year}-01-01', end=f'{end_year}-12-31', freq='YS')
        years = [date.year for date in dates]
        data = {
            'Annee': years,
            'Production_Mondiale': self._generate_trend_data(config["production_base"], years, trend=0.08),
            'Prix_Moyen': self._generate_trend_data(config["price_base"], years, trend=0.06),
            'Demande_Mondiale': self._generate_trend_data(config["production_base"] * 0.9, years, trend=0.12),
            'Valeur_Marche': self._generate_trend_data(config["production_base"] * config["price_base"] / 1000, years, trend=0.15),
            'Efficacite_Therapeutique': self._generate_quality_data(75, years, improvement=0.012),
            'Etudes_Scientifiques': self._generate_research_data(years),
            'Qualite_Bio': self._generate_quality_data(60, years, improvement=0.025),
            'Usage_Aromatherapie': self._generate_usage_data(70, years),
            'Usage_Cosmetique': self._generate_usage_data(65, years, growth=0.020),
            'Usage_Pharmaceutique': self._generate_usage_data(40, years, growth=0.025),
            'Impact_Environnemental': self._generate_impact_data(45, years),
            'Durabilite_Production': self._generate_quality_data(65, years, improvement=0.015),
            'Exportations': self._generate_trend_data(config["production_base"] * 0.7, years, trend=0.10),
            'Surface_Cultivee': self._generate_trend_data(config["production_base"] / config["rendement"] * 10, years, trend=0.09)
        }
        return pd.DataFrame(data)
    
    def _generate_trend_data(self, base, years, trend=0.1, volatility=0.1):
        data = []
        for i, year in enumerate(years):
            growth = 1 + trend * i
            noise = np.random.normal(1, volatility)
            if year == 2008:
                noise *= 0.9
            elif year == 2020:
                noise *= 1.2
            data.append(base * growth * noise)
        return data
    
    def _generate_quality_data(self, base, years, improvement=0.01):
        data = []
        for year in years:
            improvement_factor = 1 + improvement * (year - 2000)
            noise = np.random.normal(1, 0.05)
            value = min(100, base * improvement_factor * noise)
            data.append(value)
        return data
    
    def _generate_research_data(self, years):
        data = []
        for year in years:
            if year <= 2005:
                base = 5 + (year - 2000) * 2
            elif year <= 2015:
                base = 15 + (year - 2005) * 5
            else:
                base = 65 + (year - 2015) * 8
            noise = np.random.normal(1, 0.2)
            data.append(base * noise)
        return data
    
    def _generate_usage_data(self, base, years, growth=0.015):
        data = []
        for year in years:
            growth_factor = 1 + growth * (year - 2000)
            noise = np.random.normal(1, 0.08)
            value = min(100, base * growth_factor * noise)
            data.append(value)
        return data
    
    def _generate_impact_data(self, base, years):
        data = []
        for year in years:
            improvement = 1 - 0.01 * (year - 2000)
            noise = np.random.normal(1, 0.08)
            value = max(10, base * improvement * noise)
            data.append(value)
        return data

# --- Fonctions d'affichage (inchangées) ---
def create_kpi_metrics(df, oil_config):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        current_production = df['Production_Mondiale'].iloc[-1]
        st.metric(
            label="🌍 Production Mondiale Actuelle",
            value=f"{current_production:,.0f} tonnes",
            delta=f"{((df['Production_Mondiale'].iloc[-1] / df['Production_Mondiale'].iloc[0]) - 1) * 100:.1f}%"
        )
    with col2:
        current_price = df['Prix_Moyen'].iloc[-1]
        st.metric(
            label="💰 Prix Moyen Actuel",
            value=f"{current_price:.1f} €/kg",
            delta=f"{((df['Prix_Moyen'].iloc[-1] / df['Prix_Moyen'].iloc[0]) - 1) * 100:.1f}%"
        )
    with col3:
        market_value = df['Valeur_Marche'].iloc[-1]
        st.metric(
            label="📈 Valeur du Marché",
            value=f"{market_value:.1f} M€",
            delta=f"{((df['Valeur_Marche'].iloc[-1] / df['Valeur_Marche'].iloc[0]) - 1) * 100:.1f}%"
        )
    with col4:
        efficacy = df['Efficacite_Therapeutique'].iloc[-1]
        st.metric(
            label="💊 Efficacité Thérapeutique",
            value=f"{efficacy:.1f}/100",
            delta=f"{efficacy - df['Efficacite_Therapeutique'].iloc[0]:.1f}"
        )

def create_production_analysis(df, oil_name, oil_config):
    st.subheader("📊 Analyse Production & Marché")
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Production vs Demande', 'Évolution des Prix', 
                       'Valeur du Marché', 'Croissance Comparative'),
        specs=[[{"secondary_y": True}, {"secondary_y": False}],
               [{"secondary_y": False}, {"secondary_y": False}]]
    )
    fig.add_trace(
        go.Scatter(x=df['Annee'], y=df['Production_Mondiale'], 
                  name="Production", line=dict(color=oil_config["couleur"])),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=df['Annee'], y=df['Demande_Mondiale'], 
                  name="Demande", line=dict(color='#228B22')),
        row=1, col=1, secondary_y=True
    )
    fig.add_trace(
        go.Scatter(x=df['Annee'], y=df['Prix_Moyen'], 
                  name="Prix Moyen", line=dict(color='#FFD700')),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=df['Annee'], y=df['Valeur_Marche'], 
                  name="Valeur Marché", line=dict(color='#8A2BE2')),
        row=2, col=1
    )
    fig.add_trace(
        go.Scatter(x=df['Annee'], 
                  y=df['Production_Mondiale']/df['Production_Mondiale'].max(), 
                  name="Production (norm)", line=dict(color=oil_config["couleur"])),
        row=2, col=2
    )
    fig.add_trace(
        go.Scatter(x=df['Annee'], y=df['Prix_Moyen']/df['Prix_Moyen'].max(), 
                  name="Prix (norm)", line=dict(color='#FFD700')),
        row=2, col=2
    )
    fig.update_layout(height=600, title_text=f"Analyse Marché - {oil_name}")
    st.plotly_chart(fig, use_container_width=True)

def create_therapeutic_analysis(df, oil_config):
    st.subheader("💊 Analyse Thérapeutique")
    col1, col2 = st.columns(2)
    with col1:
        fig = px.line(df, x='Annee', y='Efficacite_Therapeutique',
                     title='Évolution de l\'Efficacité Thérapeutique',
                     labels={'Efficacite_Therapeutique': 'Score d\'Efficacité'})
        fig.update_traces(line=dict(color=oil_config["couleur"], width=3))
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.bar(df, x='Annee', y='Etudes_Scientifiques',
                    title='Études Scientifiques Publiées',
                    labels={'Etudes_Scientifiques': 'Nombre d\'Études'})
        fig.update_traces(marker_color=oil_config["couleur"])
        st.plotly_chart(fig, use_container_width=True)
    usage_data = pd.DataFrame({
        'Année': df['Annee'],
        'Aromathérapie': df['Usage_Aromatherapie'],
        'Cosmétique': df['Usage_Cosmetique'],
        'Pharmaceutique': df['Usage_Pharmaceutique']
    })
    fig = px.area(usage_data, x='Année', 
                  y=['Aromathérapie', 'Cosmétique', 'Pharmaceutique'],
                  title='Évolution des Applications par Secteur',
                  labels={'value': 'Score d\'Utilisation', 'variable': 'Secteur'})
    st.plotly_chart(fig, use_container_width=True)

def create_sustainability_analysis(df, oil_config):
    st.subheader("🌱 Analyse Durabilité")
    col1, col2 = st.columns(2)
    with col1:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['Annee'], y=df['Durabilite_Production'], 
                               name='Durabilité Production', line=dict(color=oil_config["couleur"])))
        fig.add_trace(go.Scatter(x=df['Annee'], y=df['Impact_Environnemental'], 
                               name='Impact Environnemental', line=dict(color='#FF6B6B')))
        fig.update_layout(title='Durabilité vs Impact Environnemental',
                         xaxis_title='Année', yaxis_title='Score')
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        categories = ['Production', 'Qualité Bio', 'Durabilité', 'Impact Environ.']
        values = [
            df['Production_Mondiale'].iloc[-1] / df['Production_Mondiale'].max() * 100,
            df['Qualite_Bio'].iloc[-1],
            df['Durabilite_Production'].iloc[-1],
            100 - df['Impact_Environnemental'].iloc[-1]
        ]
        fig = go.Figure(data=go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            line=dict(color=oil_config["couleur"])
        ))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=False,
            title='Indicateurs de Durabilité (Actuels)'
        )
        st.plotly_chart(fig, use_container_width=True)

def create_comparative_analysis(dashboard, selected_oils):
    st.subheader("📈 Analyse Comparative")
    comparison_data = []
    for oil in selected_oils:
        df = dashboard.generate_comprehensive_data(oil)
        latest = df.iloc[-1]
        config = dashboard.oils_config[oil]
        comparison_data.append({
            'Huile': oil,
            'Production': latest['Production_Mondiale'],
            'Prix': latest['Prix_Moyen'],
            'Efficacité': latest['Efficacite_Therapeutique'],
            'Études': latest['Etudes_Scientifiques'],
            'Durabilité': latest['Durabilite_Production'],
            'Rendement': config['rendement'] * 100,
            'Type': config['type'],
            'Couleur': config['couleur']
        })
    comp_df = pd.DataFrame(comparison_data)
    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(comp_df, x='Huile', y='Production', color='Huile',
                    title='Production Mondiale Comparée',
                    labels={'Production': 'Tonnes'},
                    color_discrete_map={oil: dashboard.oils_config[oil]['couleur'] for oil in selected_oils})
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.bar(comp_df, x='Huile', y='Prix', color='Huile',
                    title='Prix Moyen Comparé',
                    labels={'Prix': '€/kg'},
                    color_discrete_map={oil: dashboard.oils_config[oil]['couleur'] for oil in selected_oils})
        st.plotly_chart(fig, use_container_width=True)
    fig = go.Figure()
    for oil in selected_oils:
        row = comp_df[comp_df['Huile'] == oil].iloc[0]
        fig.add_trace(go.Scatterpolar(
            r=[row['Production']/comp_df['Production'].max()*100,
               row['Prix']/comp_df['Prix'].max()*100,
               row['Efficacité'],
               row['Études']/comp_df['Études'].max()*100,
               row['Durabilité']],
            theta=['Production', 'Prix', 'Efficacité', 'Recherche', 'Durabilité'],
            name=oil,
            fill='toself',
            line=dict(color=dashboard.oils_config[oil]['couleur'])
        ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        title='Analyse Comparative Multi-Critères'
    )
    st.plotly_chart(fig, use_container_width=True)

def create_market_overview(dashboard):
    st.subheader("🏢 Vue d'Ensemble du Marché")
    market_data = []
    for oil_name, config in dashboard.oils_config.items():
        df = dashboard.generate_comprehensive_data(oil_name)
        latest = df.iloc[-1]
        market_data.append({
            'Huile': oil_name,
            'Production (t)': latest['Production_Mondiale'],
            'Prix (€/kg)': latest['Prix_Moyen'],
            'Valeur Marché (M€)': latest['Valeur_Marche'],
            'Type': config['type'],
            'Rendement (%)': config['rendement'] * 100,
            'Couleur': config['couleur']
        })
    market_df = pd.DataFrame(market_data)
    st.write("**Top 10 des Huiles par Valeur de Marché**")
    top_10 = market_df.nlargest(10, 'Valeur Marché (M€)')
    fig = px.bar(top_10, x='Huile', y='Valeur Marché (M€)', color='Huile',
                color_discrete_map={row['Huile']: row['Couleur'] for _, row in top_10.iterrows()})
    st.plotly_chart(fig, use_container_width=True)
    col1, col2 = st.columns(2)
    with col1:
        type_counts = market_df['Type'].value_counts()
        fig = px.pie(values=type_counts.values, names=type_counts.index,
                    title='Répartition par Type Thérapeutique')
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = px.scatter(market_df, x='Prix (€/kg)', y='Production (t)', 
                        size='Valeur Marché (M€)', color='Type',
                        hover_name='Huile', title='Prix vs Production')
        st.plotly_chart(fig, use_container_width=True)

def create_oil_info_card(oil_config):
    st.sidebar.subheader("📋 Informations Huile Essentielle")
    st.sidebar.write(f"**Type:** {oil_config['type']}")
    st.sidebar.write(f"**Rendement:** {oil_config['rendement']*100:.1f}%")
    st.sidebar.write("**Régions de production:**")
    for region in oil_config['regions']:
        st.sidebar.write(f"• {region}")
    st.sidebar.write("**Propriétés principales:**")
    for prop in oil_config['proprietes']:
        st.sidebar.write(f"• {prop.capitalize()}")
    st.sidebar.write("**Molécules principales:**")
    for molecule in oil_config.get('molecules_principales', []):
        st.sidebar.write(f"• {molecule}")
    st.sidebar.write("**Contre-indications:**")
    for ci in oil_config.get('contre_indications', []):
        st.sidebar.write(f"• {ci}")
    st.sidebar.write("**Évolution prix:**", oil_config['prix_evolution'])
    st.sidebar.write("**Évolution demande:**", oil_config['demande_evolution'])

# --- Main ---
def main():
    st.title("🌿 Dashboard Pharmacopée Complète - Huiles Essentielles")
    st.markdown("""
    **Analyse complète des données de production, marché, recherche et durabilité pour 50 huiles essentielles**
    """)
    
    dashboard = CompleteEssentialOilDashboard()
    available_oils = list(dashboard.oils_config.keys())
    selected_oil = st.sidebar.selectbox(
        "Sélectionnez une huile essentielle:",
        available_oils
    )
    
    df = dashboard.generate_comprehensive_data(selected_oil)
    oil_config = dashboard.oils_config[selected_oil]
    
    create_oil_info_card(oil_config)
    create_kpi_metrics(df, oil_config)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Marché & Production", 
        "💊 Applications", 
        "🌱 Durabilité", 
        "📈 Comparatif",
        "🏢 Vue Marché"
    ])
    
    with tab1:
        create_production_analysis(df, selected_oil, oil_config)
        with st.expander("📋 Voir les données détaillées"):
            st.dataframe(df.style.format({
                'Production_Mondiale': '{:,.0f}',
                'Prix_Moyen': '{:.1f}',
                'Valeur_Marche': '{:.1f}',
                'Efficacite_Therapeutique': '{:.1f}'
            }))
    
    with tab2:
        create_therapeutic_analysis(df, oil_config)
        st.subheader("💡 Insights Thérapeutiques")
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"""
            **Applications recommandées:**
            - {oil_config['proprietes'][0].capitalize()}
            - {oil_config['proprietes'][1].capitalize()}
            - {oil_config['proprietes'][2].capitalize()}
            """)
        with col2:
            st.success(f"""
            **Potentiel de développement:**
            - Efficacité actuelle: {df['Efficacite_Therapeutique'].iloc[-1]:.1f}/100
            - Recherche scientifique: {df['Etudes_Scientifiques'].iloc[-1]:.0f} études
            - Croissance: {((df['Usage_Pharmaceutique'].iloc[-1] / df['Usage_Pharmaceutique'].iloc[0]) - 1) * 100:.1f}%
            """)
    
    with tab3:
        create_sustainability_analysis(df, oil_config)
        st.subheader("♻️ Recommandations Durabilité")
        impact_score = df['Impact_Environnemental'].iloc[-1]
        durability_score = df['Durabilite_Production'].iloc[-1]
        if impact_score > 40:
            st.warning("""
            **Attention:** Impact environnemental élevé. Recommandations:
            - Optimiser les techniques de distillation
            - Développer l'agriculture régénérative
            - Réduire la consommation d'eau
            """)
        else:
            st.success("**Excellent:** Impact environnemental maîtrisé. Maintenir les bonnes pratiques.")
        if durability_score < 70:
            st.warning("""
            **Amélioration possible:** Durabilité de production modérée.
            - Investir dans des pratiques durables
            - Certifications environnementales
            - Optimisation de la chaîne d'approvisionnement
            """)
    
    with tab4:
        comparative_oils = st.multiselect(
            "Sélectionnez les huiles à comparer:",
            available_oils,
            default=[selected_oil, "Lavande", "Menthe Poivrée", "Arbre à Thé"]
        )
        if len(comparative_oils) >= 2:
            create_comparative_analysis(dashboard, comparative_oils)
        else:
            st.warning("Sélectionnez au moins 2 huiles pour la comparaison")
    
    with tab5:
        create_market_overview(dashboard)
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center'>
        <p>📅 Données simulées pour la période 2000-2025 | 🌿 Dashboard Pharmacopée Complète - 50 Huiles Essentielles</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
