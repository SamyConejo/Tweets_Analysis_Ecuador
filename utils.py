stop_words = ['http', 'https','de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del', 'se', 'las', 'por', 'un', 'para', 'con', 'no', 'una', 'su', 'al', 'lo', 'como', 'más', 'pero', 'sus', 'le', 'ya', 'o', 'este', 'sí', 'porque', 'esta', 'entre', 'cuando', 'muy', 'sin', 'sobre', 'también', 'me', 'hasta', 'hay', 'donde', 'quien', 'desde', 'todo', 'nos', 'durante', 'todos', 'uno', 'les', 'ni', 'contra', 'otros', 'ese', 'eso', 'ante', 'ellos', 'e', 'esto', 'mí', 'antes', 'algunos', 'qué', 'unos', 'yo', 'otro', 'otras', 'otra', 'él', 'tanto', 'esa', 'estos', 'mucho', 'quienes', 'nada', 'muchos', 'cual', 'poco', 'ella', 'estar', 'estas', 'algunas', 'algo', 'nosotros', 'mi', 'mis', 'tú', 'te', 'ti', 'tu', 'tus', 'ellas', 'nosotras', 'vosotros', 'vosotras', 'os', 'mío', 'mía', 'míos', 'mías', 'tuyo', 'tuya', 'tuyos', 'tuyas', 'suyo', 'suya', 'suyos', 'suyas', 'nuestro', 'nuestra', 'nuestros', 'nuestras', 'vuestro', 'vuestra', 'vuestros', 'vuestras', 'esos', 'esas', 'estoy', 'estás', 'está', 'estamos', 'estáis', 'están', 'esté', 'estés', 'estemos', 'estéis', 'estén', 'estaré', 'estarás', 'estará', 'estaremos', 'estaréis', 'estarán', 'estaría', 'estarías', 'estaríamos', 'estaríais', 'estarían', 'estaba', 'estabas', 'estábamos', 'estabais', 'estaban', 'estuve', 'estuviste', 'estuvo', 'estuvimos', 'estuvisteis', 'estuvieron', 'estuviera', 'estuvieras', 'estuviéramos', 'estuvierais', 'estuvieran', 'estuviese', 'estuvieses', 'estuviésemos', 'estuvieseis', 'estuviesen', 'estando', 'estado', 'estada', 'estados', 'estadas', 'estad', 'he', 'has', 'ha', 'hemos', 'habéis', 'han', 'haya', 'hayas', 'hayamos', 'hayáis', 'hayan', 'habré', 'habrás', 'habrá', 'habremos', 'habréis', 'habrán', 'habría', 'habrías', 'habríamos', 'habríais', 'habrían', 'había', 'habías', 'habíamos', 'habíais', 'habían', 'hube', 'hubiste', 'hubo', 'hubimos', 'hubisteis', 'hubieron', 'hubiera', 'hubieras', 'hubiéramos', 'hubierais', 'hubieran', 'hubiese', 'hubieses', 'hubiésemos', 'hubieseis', 'hubiesen', 'habiendo', 'habido', 'habida', 'habidos', 'habidas', 'soy', 'eres', 'es', 'somos', 'sois', 'son', 'sea', 'seas', 'seamos', 'seáis', 'sean', 'seré', 'serás', 'será', 'seremos', 'seréis', 'serán', 'sería', 'serías', 'seríamos', 'seríais', 'serían', 'era', 'eras', 'éramos', 'erais', 'eran', 'fui', 'fuiste', 'fue', 'fuimos', 'fuisteis', 'fueron', 'fuera', 'fueras', 'fuéramos', 'fuerais', 'fueran', 'fuese', 'fueses', 'fuésemos', 'fueseis', 'fuesen', 'sintiendo', 'sentido', 'sentida', 'sentidos', 'sentidas', 'siente', 'sentid', 'tengo', 'tienes', 'tiene', 'tenemos', 'tenéis', 'tienen', 'tenga', 'tengas', 'tengamos', 'tengáis', 'tengan', 'tendré', 'tendrás', 'tendrá', 'tendremos', 'tendréis', 'tendrán', 'tendría', 'tendrías', 'tendríamos', 'tendríais', 'tendrían', 'tenía', 'tenías', 'teníamos', 'teníais', 'tenían', 'tuve', 'tuviste', 'tuvo', 'tuvimos', 'tuvisteis', 'tuvieron', 'tuviera', 'tuvieras', 'tuviéramos', 'tuvierais', 'tuvieran', 'tuviese', 'tuvieses', 'tuviésemos', 'tuvieseis', 'tuviesen', 'teniendo', 'tenido', 'tenida', 'tenidos', 'tenidas', 'tened']

dates = [
    ('2019-02-17','2019-02-24'),
    ('2019-02-25','2019-03-03'),
    ('2019-03-04','2019-03-10'),
    ('2019-03-11','2019-03-17'),
    ('2019-03-18','2019-03-24'),
    ('2019-03-25','2019-03-31'),
    ('2019-04-01','2019-04-07'),
    ('2019-04-08','2019-04-14'),
    ('2019-04-15','2019-04-21'),
    ('2019-04-22','2019-04-28'),
    ('2019-04-29','2019-05-05'),
    ('2019-05-06','2019-05-12'),
    ('2019-05-13','2019-05-19')
]
dates_aux = [
    str('2019-02-17/2019-02-24'),
    str('2019-02-25/2019-03-03'),
    str('2019-03-04/2019-03-10'),
    str('2019-03-11/2019-03-17'),
    str('2019-03-18/2019-03-24'),
    str('2019-03-25/2019-03-31'),
    str('2019-04-01/2019-04-07'),
    str('2019-04-08/2019-04-14'),
    str('2019-04-15/2019-04-21'),
    str('2019-04-22/2019-04-28'),
    str('2019-04-29/2019-05-05'),
    str('2019-05-06/2019-05-12'),
    str('2019-05-13/2019-05-19')
]
docs_aux = ['doc1','doc2','doc3','doc4','doc5','doc6','doc7','doc8','doc9','doc10','doc11','doc12','doc13']

username_candidatos = ['abenavidesgol1', 'mariasolcorral', 'PabloDavalos63', 'patobuendia23', 'victorhugoerazo',
                       'PatoGYE', 'juancaholguin', 'EdgarJacomeT', 'LuisaMaldonadoM', 'CesarMontufar51', 'PacoMoncayo',
                       'AndresPasquel', 'OlivioSarzosa', 'SevilaCarlos', 'PaolaVintimilla', 'LoroHomero','JoseVasquezC71']

paths_manifiestos = {'abenavidesgol1': 'benavides.pdf',
'LuisaMaldonadoM': 'maldonado.pdf',
'LoroHomero': 'yunda.pdf',
'PaolaVintimilla': 'vintimilla.pdf',
'mariasolcorral': 'corral.pdf',
'CesarMontufar51': 'montufar.pdf',
'PacoMoncayo': 'moncayo.pdf',
'EdgarJacomeT': 'jacome.pdf',
'juancaholguin': 'holguin.pdf',
'SevilaCarlos': 'sevilla.pdf'}

exclude = ['quito','plan','metropolitano','distrito','así','planes',
               'pichincha','ciudad','dmq','debe','municipio','proyectos',
               'numerator','mediante','fin','eje','propuesta','alcaldia']
