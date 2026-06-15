from app import app


def test_page_accueil():
    client = app.test_client()

    response = client.get('/')

    assert response.status_code == 200


def test_calcul_distance():
    client = app.test_client()

    response = client.post(
        '/',
        data={
            'apoint': '2,5',
            'bpoint': '1,6'
        }
    )

    assert response.status_code == 200
    assert b'1.414' in response.data


def test_coordonnees_invalides():
    client = app.test_client()

    response = client.post(
        '/',
        data={
            'apoint': '2',
            'bpoint': '1,6'
        }
    )

    assert response.status_code == 200
    assert b"Chaque point doit contenir deux coordonn" in response.data


def test_valeurs_non_numeriques():
    client = app.test_client()

    response = client.post(
        '/',
        data={
            'apoint': 'abc,5',
            'bpoint': '1,6'
        }
    )

    assert response.status_code == 200
    assert b"Les coordonn" in response.data