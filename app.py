import flask
from flask import request
from metodos_pytrends import _related_queries,tendencias_i, tendencias_mex,\
    tendencias_region,suggestions_word,all_trends


app = flask.Flask(__name__)

@app.route('/tendencias')
def tendencias():
    return tendencias_mex()

@app.route('/tendenciasG', methods=['GET'])
def tendencias_gen():
    inicio=request.args.get('inicio')
    fin=request.args.get('fin')
    single=request.args.get('single_q')
    comparison=request.args.get('comparison_q')
    return tendencias_i(inicio,fin,single,comparison)

@app.route('/tendenciasR')
def tendencias_reg():
    inicio=request.args.get('inicio')
    fin=request.args.get('fin')
    single_q=request.args.get('single_q')
    comparison_q=request.args.get('comparison_q')
    return tendencias_region(inicio,fin,single_q,comparison_q)

@app.route('/sugerencias')
def sugerencias():
    single_q=request.args.get('single_q')
    comparison_q=request.args.get('comparison_q')
    return suggestions_word(single_q,comparison_q)

@app.route('/relacionados')
def relacionados():
    single_q=request.args.get('single_q')
    comparison_q=request.args.get('comparison_q')
    return _related_queries(single_q,comparison_q)

@app.route('/tendenciasTotales')
def tendenciasTotales():
    inicio=request.args.get('inicio')
    fin=request.args.get('fin')
    single_q=request.args.get('single_q')
    comparison_q=request.args.get('comparison_q')
    return all_trends(inicio,fin,single_q,comparison_q)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
