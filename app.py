from flask import Flask, request, render_template
from math import sqrt
from datetime import datetime

def calculate_distance(point_a, point_b):
    return sqrt(
        (point_b[0] - point_a[0])**2 +
        (point_b[1] - point_a[1])**2
    )

app = Flask('my_distance')

distances = list()

@app.route('/', methods=['GET', 'POST'])
def html_calculate():
    if request.method == 'GET':
    # Si get, afficher la page vide
        return render_template('index.html', result=None)
    if request.method == 'POST':
    # Si post, calculer et afficher le résultat
        point_a = list(map(float, request.form['apoint'].split(',')[0:2]))
        point_b = list(map(float, request.form['bpoint'].split(',')[0:2]))

        result_tmp = calculate_distance(point_a, point_b)
        result =             {
                    'requested_at': datetime.now(),
                    'result_distance': result_tmp,
                    'start_point': point_a,
                    'end_point': point_b        
                }
        distances.append({
                    'requested_at': datetime.now(),
                    'result_distance': result_tmp,
                    'start_point': point_a,
                    'end_point': point_b
                })    
        return render_template('index.html', result=result)

@app.route('/api')
def index():
    return {}

@app.route('/api/distances')
def already_calculated():
    starttime = datetime.now()
    result = list(map(lambda x: {
                    'requested_at': x['requested_at'],
                    'result_distance': x['result_distance'],
                    'start_point': x['start_point'],
                    'end_point': x['end_point']        
    }, distances))
    end = datetime.now()
    return result
    print(f'result given in {end - starttime} secondes')

@app.route('/api/distance', methods=['POST', 'GET', 'PUT'])
def Calculate():
    point_a = list(map(float, request.json['point_a'].split(',')[0:2]))
    point_b = list(map(float, request.json['point_b'].split(',')[0:2]))

    result_tmp = calculate_distance(point_a, point_b)

    result = {
        'requested_at': datetime.now(),
        'result_distance': result_tmp,
        'start_point': point_a,
        'end_point': point_b
    }

    return result



if __name__ == '__main__':
    app.run(debug=True)