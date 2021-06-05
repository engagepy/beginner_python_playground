#IMPORTING THE NEEDS

from flask import Flask
from helper import pets

#instance of the flask variable
app = Flask(__name__)


#using decorators, setting .route to homepage with index function
@app.route('/')
def index():
  return '''
  <h1> Adopt a Pet!</h1> 
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
    <li> <a href = '/animals/dogs'>Dogs</a>
    <li> <a href = '/animals/cats'>Cats
    <li> <a href = '/animals/rabbits'>Rabbits
  </ul>
  '''


#got new here. Collecting variable paths, establish in previous index("/") page
@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f'<h1> List of {pet_type}: </h1>'
  html += '<ul>'

#enumerate functions returns tuples with counting. Default value to start count can be setup
  for idx, pet in enumerate(pets[pet_type]):
    html += '<li>{link}{namey}</li>'.format(link='<a href="/animals/{pet_type}/{idx}">'.format(pet_type=pet_type, idx=idx),namey='{n}'.format(n=pet['name']))
  html += '</a>'
  html += '</ul>'  
  return html


#setting up the deepest page, with new new pet_id. Comes from previous pet_type handling page.
@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]
    return f"""
  <h1>Name: {pet['name']}</h1>
  <img src={pet['url']} alt='alt text'>
  <p><h2>Description: </h2> <h4>{pet['description']}</h4></p>
  <ul>
  <li> <h3>Breed:</h3> {pet['breed']}</li>
  <li> <h3>Age: </h3> {pet['age']}</li>
  </ul>
  """