def test_homepage_loads(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Bug Tracker' in response.data


def test_submit_bug(client):
    response = client.post('/submit', data={
        'title': 'Sample Bug',
        'description': 'Bug description here',
        'priority': 'High'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Sample Bug' in response.data


def test_delete_bug(client):
    client.post('/submit', data={
        'title': 'Bug to Delete',
        'description': 'Delete me',
        'priority': 'Low'
    }, follow_redirects=True)

    response = client.get('/delete/1', follow_redirects=True)
    assert b'Bug to Delete' not in response.data


def test_resolve_bug(client):
    client.post('/submit', data={
        'title': 'Bug to Resolve',
        'description': 'Needs fixing',
        'priority': 'Medium'
    }, follow_redirects=True)

    # Resolve the bug
    response = client.get('/resolve/1', follow_redirects=True)
    assert response.status_code == 200
    assert b'Resolved' in response.data


def test_edit_bug(client):
    # Add a bug
    client.post('/submit', data={
        'title': 'Old Title',
        'description': 'Old Desc',
        'priority': 'Low'
    }, follow_redirects=True)

    # Edit the bug
    response = client.post('/edit/1', data={
        'title': 'New Title',
        'description': 'Updated Desc',
        'priority': 'High'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'New Title' in response.data
    assert b'Updated Desc' in response.data
    assert b'High' in response.data
