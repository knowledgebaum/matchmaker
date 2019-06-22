from matchmaker.regex_sub  import *
from pathlib import Path
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:')

Session = sessionmaker(bind=engine)
session = Session()


from datetime import datetime

from sqlalchemy import Table, Column, Integer, Numeric, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()




class Myco(Base):
    #32 items
    __tablename__ = 'mushrooms'

    id = Column(Integer(), primary_key=True)
    family = Column(Text())
    latin_names = Column(Text())
    english_names = Column(Text())
    notes = Column(Text())
    chemical_reactions = Column(Text())
    cap = Column(Text())
    nest = Column(Text())
    fruiting_body = Column(Text())
    upper_surface = Column(Text())
    flesh = Column(Text())
    outer_surface = Column(Text())
    habitat = Column(Text())
    gills = Column(Text())
    inner_layer = Column(Text())
    inner_surface = Column(Text())
    microscopic = Column(Text())
    underside = Column(Text())
    pores = Column(Text())
    stem = Column(Text())
    spore_mass = Column(Text())
    teeth = Column(Text())
    interior = Column(Text())
    eggs = Column(Text())
    name_origin = Column(Text())
    veil = Column(Text())
    odor = Column(Text())
    edibility = Column(Text())
    similar = Column(Text())
    taste = Column(Text())
    sources = Column(Text())
    spore_deposit = Column(Text())


Base.metadata.create_all(engine)

###################
###ORIGIN FILES ###
###################

#PATHS
base_path = Path("C:/webDev/pycharm/matchmaker/data/origin_data/")

cor_path=os.path.join(base_path, "cor_origin.txt")
cru_path=os.path.join(base_path, "cru_origin.txt")
cup_path=os.path.join(base_path, "cup_origin.txt")
gil_path=os.path.join(base_path, "gil_origin.txt")
jel_path=os.path.join(base_path, "jel_Origin.txt")
mor_path=os.path.join(base_path, "mor_origin.txt")
oth_path=os.path.join(base_path, "oth_Origin.txt")
pol_path=os.path.join(base_path, "pol_origin.txt")
puf_path=os.path.join(base_path, "puf_origin.txt")
too_path=os.path.join(base_path, "too_Origin.txt")
tru_path=os.path.join(base_path, "tru_origin.txt")
vei_path=os.path.join(base_path, "vei_origin.txt")
bir_path=os.path.join(base_path, "bir_origin.txt")
bol_path=os.path.join(base_path, "bol_Origin.txt")
clu_path=os.path.join(base_path, "clu_origin.txt")

#LIST OF FILE VARS
origin_file_list = [cor_path,
                    cru_path,
                    cup_path,
                    gil_path,
                    jel_path,
                    mor_path,
                    oth_path,
                    pol_path,
                    puf_path,
                    too_path,
                    tru_path,
                    vei_path,
                    bir_path,
                    bol_path,
                    clu_path
]

regex_string_list = []




mushroom_list = make_dic(cru_path)

####################





for item in mushroom_list:


    mushroom = Myco(
    family = item[1],
    latin_name = item[2],
    english_name=item[3],
    notes=item[4],
    chemical_reaction=item[5],
    upper_surface=item[6],
    flesh=item[7],
    underside=item[8],
    stem=item[9],
    odor=item[10],
    taste=item[11],
    edibility=item[12],
    habitat=item[13],
    spore_deposit=item[14],
    microscopic=item[15],
    name_origin=item[16],
    similar=item[17],
    sources=item[18],

    )


##SQL VERSION OF TABLE
# CREATE TABLE `mushroom_db` (
# 	`id` INT,
# 	`family` TEXT,
# 	`latin_names` TEXT,
# 	`english_names` TEXT,
# 	`notes` TEXT,
# 	`chemical_reactions` TEXT,
# 	`cap` TEXT,
# 	`nest` TEXT,
# 	`fruiting_body` TEXT,
# 	`upper_surface` TEXT,
# 	`flesh` TEXT,
# 	`outer_surface` TEXT,
# 	`habitat` TEXT,
# 	`gills` TEXT,
# 	`inner_layer` TEXT,
# 	`inner_surface` TEXT,
# 	`microscopic` TEXT,
# 	`underside` TEXT,
# 	`pores` TEXT,
# 	`stem` TEXT,
# 	`spore_mass` TEXT,
# 	`teeth` TEXT,
# 	`interior` TEXT,
# 	`eggs` TEXT,
# 	`name_origin` TEXT,
# 	`veil` TEXT,
# 	`odor` TEXT,
# 	`edibility` TEXT,
# 	`similar` TEXT,
# 	`taste` TEXT,
# 	`sources` TEXT,
# 	`spore_deposit` TEXT,
# 	PRIMARY KEY (`id`)
# );
