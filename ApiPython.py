from flask import Flask, jsonify, request
from flask_cors import CORS

import psycopg2

#https://www.postgresqltutorial.com/postgresql-python/connect/

app = Flask(__name__)
CORS(app)

url="127.0.0.1"
db="geoapp"
us="postgres"
psw="postgres"

###############################################################################

@app.route("/")
def hello():
    return "I am running!!!"

@app.route("/get/circoscrizioni", methods=['GET'])
def getCircoscrizioni():
    conn = psycopg2.connect(host=url, database=db, user=us, password=psw)
    cur = conn.cursor()
    cur.execute("SELECT jsonb_build_object(    'type',     'FeatureCollection',    'features', jsonb_agg(features.feature))FROM (  SELECT jsonb_build_object(    'type',       'Feature',    'id',         gid,    'geometry',   ST_AsGeoJSON(geom)::jsonb,    'properties', to_jsonb(inputs) - 'gid' - 'geom'  ) AS feature  FROM (SELECT * FROM public.circoscrizioni) inputs) features;")
    righe = cur.fetchone()
    return righe[0]

@app.route("/get/farmacie", methods=['GET'])
def getFarmacie():
    conn = psycopg2.connect(host=url, database=db, user=us, password=psw)
    cur = conn.cursor()
    cur.execute("SELECT jsonb_build_object(    'type',     'FeatureCollection',    'features', jsonb_agg(features.feature))FROM (  SELECT jsonb_build_object(    'type',       'Feature',    'id',         gid,    'geometry',   ST_AsGeoJSON(geom)::jsonb,    'properties', to_jsonb(inputs) - 'gid' - 'geom'  ) AS feature  FROM (SELECT * FROM public.farmacie) inputs) features;")
    righe = cur.fetchone()
    return righe[0]

@app.route("/get/nuoveZone30", methods=['GET'])
def getNuoveZone30():
    conn = psycopg2.connect(host=url, database=db, user=us, password=psw)
    cur = conn.cursor()
    cur.execute("SELECT jsonb_build_object(    'type',     'FeatureCollection',    'features', jsonb_agg(features.feature))FROM (  SELECT jsonb_build_object(    'type',       'Feature',    'id',         gid,    'geometry',   ST_AsGeoJSON(geom)::jsonb,    'properties', to_jsonb(inputs) - 'gid' - 'geom'  ) AS feature  FROM (SELECT * FROM public.nuovazona30) inputs) features;")
    righe = cur.fetchone()
    return righe[0]

@app.route("/get/parcheggiDedicati", methods=['GET'])
def getParcheggiDedicati():
    conn = psycopg2.connect(host=url, database=db, user=us, password=psw)
    cur = conn.cursor()
    cur.execute("SELECT jsonb_build_object(    'type',     'FeatureCollection',    'features', jsonb_agg(features.feature))FROM (  SELECT jsonb_build_object(    'type',       'Feature',    'id',         gid,    'geometry',   ST_AsGeoJSON(geom)::jsonb,    'properties', to_jsonb(inputs) - 'gid' - 'geom'  ) AS feature  FROM (SELECT * FROM public.parcheggi) inputs) features;")
    righe = cur.fetchone()
    return righe[0]

#NOT WORKING per quantita'
@app.route("/get/parchiPoligoni", methods=['GET'])
def getParchiPoligoni():
    conn = psycopg2.connect(host=url, database=db, user=us, password=psw)
    cur = conn.cursor()
    cur.execute("SELECT jsonb_build_object(    'type',     'FeatureCollection',    'features', jsonb_agg(features.feature))FROM (  SELECT jsonb_build_object(    'type',       'Feature',    'id',         gid,    'geometry',   ST_AsGeoJSON(geom)::jsonb,    'properties', to_jsonb(inputs) - 'gid' - 'geom'  ) AS feature  FROM (SELECT * FROM public.parchipoligoni LIMIT 50) inputs) features;")
    righe = cur.fetchone()
    return righe[0]

@app.route("/get/parchiPunti", methods=['GET'])
def getParchiPunti():
    conn = psycopg2.connect(host=url, database=db, user=us, password=psw)
    cur = conn.cursor()
    cur.execute("SELECT jsonb_build_object(    'type',     'FeatureCollection',    'features', jsonb_agg(features.feature))FROM (  SELECT jsonb_build_object(    'type',       'Feature',    'id',         gid,    'geometry',   ST_AsGeoJSON(geom)::jsonb,    'properties', to_jsonb(inputs) - 'gid' - 'geom'  ) AS feature  FROM (SELECT * FROM public.parchipunti) inputs) features;")
    righe = cur.fetchone()
    return righe[0]

@app.route("/get/popolazioneResidente", methods=['GET'])
def getPopolazioneResidente():
    conn = psycopg2.connect(host=url, database=db, user=us, password=psw)
    cur = conn.cursor()
    cur.execute("SELECT jsonb_build_object(    'type',     'FeatureCollection',    'features', jsonb_agg(features.feature))FROM (  SELECT jsonb_build_object(    'type',       'Feature',    'id',         gid,    'geometry',   ST_AsGeoJSON(geom)::jsonb,    'properties', to_jsonb(inputs) - 'gid' - 'geom'  ) AS feature  FROM (SELECT * FROM public.popolazioneresidente LIMIT 50) inputs) features;")
    righe = cur.fetchone()
    return righe[0]

#NOT WORKING per Coordinate
@app.route("/get/puntiDiInteresse", methods=['GET'])
def getPuntiDiInteresse():
    conn = psycopg2.connect(host=url, database=db, user=us, password=psw)
    cur = conn.cursor()
    cur.execute("SELECT jsonb_build_object(    'type',     'FeatureCollection',    'features', jsonb_agg(features.feature))FROM (  SELECT jsonb_build_object(    'type',       'Feature',    'id',         gid,    'geometry',   ST_AsGeoJSON(geom)::jsonb,    'properties', to_jsonb(inputs) - 'gid' - 'geom'  ) AS feature  FROM (SELECT * FROM public.puntidiinteresse LIMIT 1) inputs) features;")
    righe = cur.fetchone()
    return righe[0]

@app.route("/get/quartieri", methods=['GET'])
def getQuartieri():
    conn = psycopg2.connect(host=url, database=db, user=us, password=psw)
    cur = conn.cursor()
    cur.execute("SELECT jsonb_build_object(    'type',     'FeatureCollection',    'features', jsonb_agg(features.feature))FROM (  SELECT jsonb_build_object(    'type',       'Feature',    'id',         gid,    'geometry',   ST_AsGeoJSON(geom)::jsonb,    'properties', to_jsonb(inputs) - 'gid' - 'geom'  ) AS feature  FROM (SELECT * FROM public.quartieri) inputs) features;")
    righe = cur.fetchone()
    return righe[0]

@app.route("/get/scuole", methods=['GET'])
def getScuole():
    conn = psycopg2.connect(host=url, database=db, user=us, password=psw)
    cur = conn.cursor()
    cur.execute("SELECT jsonb_build_object(    'type',     'FeatureCollection',    'features', jsonb_agg(features.feature))FROM (  SELECT jsonb_build_object(    'type',       'Feature',    'id',         gid,    'geometry',   ST_AsGeoJSON(geom)::jsonb,    'properties', to_jsonb(inputs) - 'gid' - 'geom'  ) AS feature  FROM (SELECT * FROM public.scuole) inputs) features;")
    righe = cur.fetchone()
    return righe[0]

@app.route("/get/sostaVietata", methods=['GET'])
def getSostaVietata():
    conn = psycopg2.connect(host=url, database=db, user=us, password=psw)
    cur = conn.cursor()
    cur.execute("SELECT jsonb_build_object(    'type',     'FeatureCollection',    'features', jsonb_agg(features.feature))FROM (  SELECT jsonb_build_object(    'type',       'Feature',    'id',         gid,    'geometry',   ST_AsGeoJSON(geom)::jsonb,    'properties', to_jsonb(inputs) - 'gid' - 'geom'  ) AS feature  FROM (SELECT * FROM public.sostavietata) inputs) features;")
    righe = cur.fetchone()
    return righe[0]

@app.route("/get/strade30", methods=['GET'])
def getStrade30():
    conn = psycopg2.connect(host=url, database=db, user=us, password=psw)
    cur = conn.cursor()
    cur.execute("SELECT jsonb_build_object(    'type',     'FeatureCollection',    'features', jsonb_agg(features.feature))FROM (  SELECT jsonb_build_object(    'type',       'Feature',    'id',         gid,    'geometry',   ST_AsGeoJSON(geom)::jsonb,    'properties', to_jsonb(inputs) - 'gid' - 'geom'  ) AS feature  FROM (SELECT * FROM public.strade30) inputs) features;")
    righe = cur.fetchone()
    return righe[0]

@app.route("/get/zone30", methods=['GET'])
def getZone30():
    conn = psycopg2.connect(host=url, database=db, user=us, password=psw)
    cur = conn.cursor()
    cur.execute("SELECT jsonb_build_object(    'type',     'FeatureCollection',    'features', jsonb_agg(features.feature))FROM (  SELECT jsonb_build_object(    'type',       'Feature',    'id',         gid,    'geometry',   ST_AsGeoJSON(geom)::jsonb,    'properties', to_jsonb(inputs) - 'gid' - 'geom'  ) AS feature  FROM (SELECT * FROM public.zone30) inputs) features;")
    righe = cur.fetchone()
    return righe[0]

@app.route("/get/ztl", methods=['GET'])
def getZtl():
    conn = psycopg2.connect(host=url, database=db, user=us, password=psw)
    cur = conn.cursor()
    cur.execute("SELECT jsonb_build_object(    'type',     'FeatureCollection',    'features', jsonb_agg(features.feature))FROM (  SELECT jsonb_build_object(    'type',       'Feature',    'id',         gid,    'geometry',   ST_AsGeoJSON(geom)::jsonb,    'properties', to_jsonb(inputs) - 'gid' - 'geom'  ) AS feature  FROM (SELECT * FROM public.ztl) inputs) features;")
    righe = cur.fetchone()
    return righe[0]

@app.route("/post")
def post():
    return "POST"

###################################################
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='7484', debug=True)
