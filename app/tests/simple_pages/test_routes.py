
# Test the routes of the simple pages

# Home page route test
def test_index_success(client):
  # Page loads
  response = client.get('/')
  assert response.status_code == 200

# About page route test
def test_about_success(client):
  # Page loads
  response = client.get('/about')
  assert response.status_code == 200

# Contact page route test
def test_contact_success(client):
    # Page loads
    response = client.get('/contact')
    assert response.status_code == 200

# Topics page route test
def test_topics_success(client):
    # Page loads
    response = client.get('/topics')
    assert response.status_code == 200
