from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/',methods=['get'])
def home():
	return "<h1>Distant reading api</h1><p>this site is prototype for distant reading api</p>"
books=[
 {
  'id':0,
  'val':12
 },
 {
 'id':1,
 'value':15
 }
]
@app.route('/ab',methods=['get'])
def random():
	#checking if any id is passed with the link
	#The id must be provided like this: linl/books?id=0
	#and if id is provided i am gonna assign it to a variable 
   if 'id' in request.args:
        id = int(request.args['id'])
   else:
        return "Error: No id field provided. Please specify an id."
   results=[]
   #empty list of results
   for book in books:
   	 if book['id']==id:
   		 results.append(book)
   return jsonify(results)

@app.route('newbooks', methods=['get'])
def new_books():
   id=int(request.args['id'])
   value=request.args['value']
   if id in books:
         return {"Id already there"}
   books.append({'id':id,'value':value})
         return {'status':'ok'}


app.run(debug = True)
