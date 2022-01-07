# API pytrends

* Implementación de api para ingesta de datos de Google trends utilizando [pytrends](https://pypi.org/project/pytrends/)

### Implementación

  * Para extraer los datos de Google Trends se utilizó la librería de Python [pytrends](https://pypi.org/project/pytrends/)

  * Procesado de los datos utilizando [pandas](https://pandas.pydata.org/docs)

  * Api creada utilizando [Flask](https://flask.palletsprojects.com/en/2.0.x/)

  * Docker image `docker pull guillermonar/urizen:1.00`

### Endpoints

1. Tendencias México
  * Regresa un json con las tendencias de búsqueda de Google México.
  * Endpoint: `/tendencias`
  * Parámetros:
2. Tendencias Generales
  * Regresa un json con las tendencias de Google México de los términos de
  búsqueda en el periodo dado.
  * Endpoint: `/tendenciasG`
  * Parámetros:
    * `single_q`: Término de búsqueda
    * `comparison_q`: Término para comparación (opcional)
    * `inicio`: Inicio del periodo a buscar, en formato (YYYY-MM-DD)
    * `fin`: Fin del periodo a buscar, en formato (YYYY-MM-DD)
3. Tendencias Regionales
  * Regresa un json con las tendencias de Google México de los términos dados
  con un enfoque estatal.
  * Endpoint: `/tendenciasR`
  * Parámetros:
    * `single_q`: Término de búsqueda
    * `comparison_q`: Término para comparación (opcional)
    * `inicio`: Inicio del periodo a buscar, en formato (YYYY-MM-DD)
    * `fin`: Fin del periodo a buscar, en formato (YYYY-MM-DD)
4. Sugerencias
  * Regresa json con sugerencias de búsqueda relacionados con los términos de
  búsqueda, las sugerencias no están acotadas a México.
  * Endpoint: `/sugerencias`
  * Parámetros:
    * `single_q`: Término de búsqueda
    * `comparison_q`: Término para comparación (opcional)
5. Relacionados
  * Regesa un json con las búsquedas "top" y "trending" de los términos dados.
  * Endpoint:`/relacionados`
  * Parámetros:
    * `single_q`: Término de búsqueda
    * `comparison_q`: Término para comparación (opcional)
6. Tendencias Totales
  * Regresa un json que contiene todos los json de los métodos mencionados anteriormente.
  * Endpoint:`/tendenciasTotales`
  * Parámetros:
    * `single_q`: Término de búsqueda
    * `comparison_q`: Término para comparación (opcional)
    * `inicio`: Inicio del periodo a buscar, en formato (YYYY-MM-DD)
    * `fin`: Fin del periodo a buscar, en formato (YYYY-MM-DD)


### Ejemplos

* Tendencias
  * Input: `http://127.0.0.1:5000/tendencias`

  * Output: `{"tendencias_mx":{"0":"Emma Coronel","1":"Salernitana Juventus","2":"Barbados","3":"Tecate Pal Norte 2022","4":"Copa del Rey","5":"Ingrid","6":"Marcelo Flores","7":"Pedro Caixinha","8":"Newcastle","9":"Lucha Villa","10":"Anabel hernandez","11":"Estreno de 'Spider-Man: No Way Home en mexico","12":"Shakira","13":"Quien es Androide en quien es la mascara","14":"Omicron sintomas","15":"Sebastian cordova","16":"La casa Gucci","17":"Aristegui Noticias","18":"Cyber Monday","19":"Sebastian boscan"}}`

* Tendencias Generales
  * Input: `http://127.0.0.1:5000/tendenciasG?inicio=2021-10-11&fin=2021-10-14&single_q=covid&comparison_q=vacuna`

  * Output: `{"1633910400000":{"covid":96,"vacuna":91},"1633996800000":{"covid":91,"vacuna":87},"1634083200000":{"covid":100,"vacuna":91},"1634169600000":{"covid":95,"vacuna":80}}`

* Tendencias Regionales
  * Input: `http://127.0.0.1:5000/tendenciasR?inicio=2021-10-11&fin=2021-10-14&single_q=covid&comparison_q=vacuna`

  * Output: `{"covid":{"Aguascalientes":59,"Baja California":68,"Baja California Sur":89,"Campeche":60,"Chiapas":56,"Chihuahua":54,"Coahuila":55,"Colima":64,"Durango":43,"Guanajuato":48,"Guerrero":63,"Hidalgo":51,"Jalisco":42,"Mexico City":58,"Michoac\u00e1n":61,"Morelos":43,"Nayarit":82,"Nuevo Leon":60,"Oaxaca":74,"Puebla":45,"Quer\u00e9taro":54,"Quintana Roo":59,"San Luis Potosi":66,"Sinaloa":69,"Sonora":64,"State of Mexico":47,"Tabasco":51,"Tamaulipas":60,"Tlaxcala":56,"Veracruz":53,"Yucatan":63,"Zacatecas":44},"vacuna":{"Aguascalientes":41,"Baja California":32,"Baja California Sur":11,"Campeche":40,"Chiapas":44,"Chihuahua":46,"Coahuila":45,"Colima":36,"Durango":57,"Guanajuato":52,"Guerrero":37,"Hidalgo":49,"Jalisco":58,"Mexico City":42,"Michoac\u00e1n":39,"Morelos":57,"Nayarit":18,"Nuevo Leon":40,"Oaxaca":26,"Puebla":55,"Quer\u00e9taro":46,"Quintana Roo":41,"San Luis Potosi":34,"Sinaloa":31,"Sonora":36,"State of Mexico":53,"Tabasco":49,"Tamaulipas":40,"Tlaxcala":44,"Veracruz":47,"Yucatan":37,"Zacatecas":56}}`

* Sugerencias
  * Input: `http://127.0.0.1:5000/sugerencias?single_q=covid&comparison_q=vacuna`
  * Output: `{
  "comparison_q_sugg": {
    "0": "Vaccine",
    "1": "COVID-19 vaccine",
    "2": "Vaccination",
    "3": "Influenza vaccine"
},
  "single_q_sugg": {
    "0": "Coronavirus disease 2019",
    "1": "COVID-19 vaccine",
    "2": "COVID-19 testing",
    "3": "Cubit",
    "4": "2019\u201320 coronavirus pandemic"}}`

  * Relacionados
    * Input: `http://127.0.0.1:5000/relacionados?single_q=covid`

    * Output: `{'temas_relacionados_single_query': {'top': '{"0":{"query":"covid 19","value":100},"1":{"query":"vacuna covid","value":78},"2":{"query":"vacuna","value":76},"3":{"query":"covid mexico","value":50},"4":{"query":"covid sintomas","value":35},"5":{"query":"vacuna de covid","value":28},"6":{"query":"prueba covid","value":26},"7":{"query":"vacunacion covid","value":24},"8":{"query":"sintomas de covid","value":23},"9":{"query":"semaforo covid","value":19},"10":{"query":"registro vacuna covid","value":19},"11":{"query":"covid 19 mexico","value":16},"12":{"query":"covid en mexico","value":16},"13":{"query":"vacunas covid","value":14},"14":{"query":"cdmx covid","value":13},"15":{"query":"prueba de covid","value":12},"16":{"query":"pruebas covid","value":12},"17":{"query":"sintomas covid 19","value":11},"18":{"query":"certificado covid","value":11},"19":{"query":"mi vacuna","value":10},"20":{"query":"mi vacuna covid","value":10},"21":{"query":"salud digna covid","value":9},"22":{"query":"sintomas del covid","value":9},"23":{"query":"certificado vacunacion covid","value":8},"24":{"query":"salud digna","value":8}}',
  'rising': '{"0":{"query":"covid 19","value":2215000},"1":{"query":"vacuna covid","value":1723750},"2":{"query":"vacuna","value":1679100},"3":{"query":"covid mexico","value":1100800},"4":{"query":"covid sintomas","value":785750},"5":{"query":"vacuna de covid","value":614350},"6":{"query":"prueba covid","value":573250},"7":{"query":"vacunacion covid","value":529650},"8":{"query":"sintomas de covid","value":512750},"9":{"query":"semaforo covid","value":429200},"10":{"query":"registro vacuna covid","value":410800},"11":{"query":"covid 19 mexico","value":358450},"12":{"query":"covid en mexico","value":343350},"13":{"query":"vacunas covid","value":303450},"14":{"query":"cdmx covid","value":295000},"15":{"query":"prueba de covid","value":273750},"16":{"query":"pruebas covid","value":254950},"17":{"query":"sintomas covid 19","value":249450},"18":{"query":"certificado covid","value":241200},"19":{"query":"mi vacuna","value":221650},"20":{"query":"mi vacuna covid","value":220750},"21":{"query":"salud digna covid","value":193550},"22":{"query":"sintomas del covid","value":190700},"23":{"query":"certificado vacunacion covid","value":185000},"24":{"query":"salud digna","value":185000}}'}}`
