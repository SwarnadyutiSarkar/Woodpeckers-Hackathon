# app.py
from flask import Flask, request, jsonify
from db import Session, Client
import openai

app = Flask(__name__)

# Initialize OpenAI
openai.api_key = 'YOUR_OPENAI_API_KEY'

def query_database(query):
    session = Session()
    result = session.query(Client).filter(Client.name.ilike(f'%{query}%')).all()
    session.close()
    return result

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    user_query = data.get('query')
    
    # Use OpenAI GPT-3 to interpret the query
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Extract the client's name from this query: {user_query}",
        max_tokens=50
    )
    client_name = response.choices[0].text.strip()
    
    results = query_database(client_name)
    
    if results:
        response_data = [{
            'id': client.id,
            'name': client.name,
            'email': client.email,
            'phone': client.phone,
            'address': client.address,
            'created_at': client.created_at
        } for client in results]
        return jsonify(response_data)
    else:
        return jsonify({'message': 'No results found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
