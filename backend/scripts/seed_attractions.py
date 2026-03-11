import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models.city import City
from app.models.attraction import Attraction

attractions_data = [
    # Brașov
    { "name": "attractions.brasov.cetatea_brasovului",   "category": "categories.historical",    "rating": 4.8, "duration_minutes": 150, "description": "attractions.brasov.cetatea_brasovului_description", "lat": 45.6427, "lng": 25.5887 },
    { "name": "attractions.brasov.centrul_vechi",        "category": "categories.culture",     "rating": 4.9, "duration_minutes": 210, "description": "attractions.brasov.centrul_vechi_description", "lat": 45.6430, "lng": 25.5889 },
    { "name": "attractions.brasov.tampa",               "category": "categories.nature",      "rating": 4.7, "duration_minutes": 120, "description": "attractions.brasov.tampa_description", "lat": 45.6369, "lng": 25.5952 },
    { "name": "attractions.brasov.biserica_neagra",     "category": "categories.historical",    "rating": 4.8, "duration_minutes": 60,  "description": "attractions.brasov.biserica_neagra_description",                    	"lat" :	45.6415,	"lng" :	25.5887 },
    { "name": "attractions.brasov.cheile_rasnoavei",   	"category":"categories.adventure",	"rating" :	4.6,	"duration_minutes" :	240,	"description" :	"attractions.brasov.cheile_rasnoavei_description",			"lat" :	45.5833,	"lng" :	25.5167 },
    { "name": "attractions.brasov.casa_banului",  	"category":"categories.gastronomy",	"rating" :	4.7,	"duration_minutes" :	90,	"description" :	"attractions.brasov.casa_banului_description",			"lat" :	45.6500,	"lng" :	25.6000 },
    # București
    { "name": "attractions.bucuresti.palatul_parlamentului",   "category": "categories.historical",    "rating": 4.7, "duration_minutes": 120, "description": "attractions.bucuresti.palatul_parlamentului_description", "lat": 44.4275, "lng": 26.0875 },
    { "name": "attractions.bucuresti.parcul_herastau",        "category": "categories.nature",      "rating": 4.8, "duration_minutes": 180, "description": "attractions.bucuresti.parcul_herastau_description", "lat": 44.4721, "lng": 26.0827 },
    { "name": "attractions.bucuresti.muzeul_national_de_arta", "category": "categories.culture",     "rating": 4.6, "duration_minutes": 150, "description": "attractions.bucuresti.muzeul_national_de_arta_description", "lat": 44.4394, "lng": 26.0963 },
    { "name": "attractions.bucuresti.cartierul_floreasca",     "category": "categories.gastronomy",    	"rating" :	4.7,	"duration_minutes" :	120,	"description" :	"attractions.bucuresti.cartierul_floreasca_description",			"lat" :	44.4697,	"lng" :	26.1036 },

    # Valea Prahovei
    { "name": "attractions.valea_prahovei.varful_omu",         "category": "categories.adventure", "rating": 4.9, "duration_minutes": 480, "description": "attractions.valea_prahovei.varful_omu_description", "lat": 45.4167, "lng": 25.4500 },
    { "name": "attractions.valea_prahovei.cascada_urlătoarea", "category": "categories.nature",   "rating": 4.7, "duration_minutes": 120, "description": "attractions.valea_prahovei.cascada_urlatoarea_description", "lat": 45.3833, "lng": 25.5333 },
    { "name": "attractions.valea_prahovei.babele_sfinxul",   "category": "categories.nature",   "rating": 4.8, "duration_minutes": 180, "description": "attractions.valea_prahovei.babele_sfinxul_description",                    	"lat" :	45.4097,	"lng" :	25.4639 },

    # Cluj
    { "name": "attractions.cluj.piata_unirii", "category": "categories.culture", "rating": 4.8, "duration_minutes": 120, "description": "attractions.cluj.piata_unirii_description", "lat": 46.7712, "lng": 23.5897 },
    { "name": "attractions.cluj.cetatuia",    "category": "categories.nature",  "rating": 4.7, "duration_minutes": 60,  "description": "attractions.cluj.cetatuia_description", "lat": 46.7644, "lng": 23.5811 },

    # Sibiu
    { "name": "attractions.sibiu.piata_mare",        "category": "categories.culture",  "rating": 4.9, "duration_minutes": 120, "description": "attractions.sibiu.piata_mare_description", "lat": 45.7983, "lng": 24.1522 },
    { "name": "attractions.sibiu.podul_minciunilor", "category": "categories.historical", "rating": 4.7, "duration_minutes": 30,  "description": "attractions.sibiu.podul_minciunilor_description", "lat": 45.7961, "lng": 24.1508 },

    # Sinaia
    { "name": "attractions.sinaia.castelul_peles",    "category": "categories.historical", "rating": 4.9, "duration_minutes": 120, "description": "attractions.sinaia.castelul_peleș_description", "lat": 45.3597, "lng": 25.5428 },
    { "name": "attractions.sinaia.manastirea_sinaia", "category": "categories.culture",  "rating": 4.8, "duration_minutes": 60,  "description": "attractions.sinaia.manastirea_sinaia_description", "lat": 45.3542, "lng": 25.5528 },
]

def seed_attractions():
    db = SessionLocal()

    try:
        print("Încarc orașele din DB...")
        
        # Facem map: translation_key -> obiect City
        cities = db.query(City).all()
        city_map = {city.name: city for city in cities}

        print("Inserez atracții...")

        for attr_data in attractions_data:
            city_key = attr_data["city_key"]

            if city_key not in city_map:
                raise Exception(f"Orașul {city_key} nu există în DB")

            attraction = Attraction(
                city=city_map[city_key],
                name=attr_data["name"],
                category=attr_data["category"],
                rating=attr_data["rating"],
                duration_minutes=attr_data["duration_minutes"],
                description=attr_data["description"],
                lat=attr_data["lat"],
                lng=attr_data["lng"],
            )

            db.add(attraction)

        db.commit()
        print("✅ Atracții inserate cu succes!")

    except Exception as e:
        db.rollback()
        print(f"❌ Eroare: {e}")

    finally:
        db.close()

if __name__ == "__main__":
    seed_attractions()