from flask import Flask, request, render_template
from math import sqrt
from datetime import datetime

def calculate_distance(point_a, point_b):
    return sqrt(
        (point_b[0] - point_a[0])**2 +
        (point_b[1] - point_a[1])**2
    )

app = Flask('my_distance')

distances = []

@app.route('/', methods=['GET', 'POST'])
def html_calculate():
    if request.method == 'GET':
        return render_template('index.html', result=None, error=None)

    if request.method == 'POST':
        try:
            point_a = list(map(float, request.form['apoint'].split(',')))
            point_b = list(map(float, request.form['bpoint'].split(',')))

            if len(point_a) != 2 or len(point_b) != 2:
                return render_template(
                    'index.html',
                    result=None,
                    error="Chaque point doit contenir deux coordonnées (ex: 2,5)"
                )

            result_tmp = calculate_distance(point_a, point_b)

            result = {
                'requested_at': datetime.now(),
                'result_distance': result_tmp,
                'start_point': point_a,
                'end_point': point_b
            }

            distances.append(result)

            return render_template(
                'index.html',
                result=result,
                error=None
            )

        except ValueError:
            return render_template(
                'index.html',
                result=None,
                error="Les coordonnées doivent être numériques (ex: 2,5)"
            )
        return render_template('index.html',result=None,error=None)

@app.route('/api')
def index():
    return {}

@app.route('/api/distances')
def already_calculated():
    return [
        {
            'requested_at': x['requested_at'],
            'result_distance': x['result_distance'],
            'start_point': x['start_point'],
            'end_point': x['end_point']
        }
        for x in distances
    ]

@app.route('/api/distance', methods=['POST'])
def calculate():
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